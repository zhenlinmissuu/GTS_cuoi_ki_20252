import numpy as np
import itertools
from IPython.display import Markdown, display

def Check_And_Permute_Dominant(A, b):
    n = A.shape[0]
    for perm in itertools.permutations(range(n)):
        A_perm = A[list(perm), :]
        b_perm = b[list(perm)]
        
        is_dominant = True
        for i in range(n):
            if np.abs(A_perm[i, i]) <= np.sum(np.abs(A_perm[i])) - np.abs(A_perm[i, i]):
                is_dominant = False
                break
        if is_dominant:
            return True, A_perm, b_perm, perm
    return False, A, b, None

def Gauss_Seidel_Ax_B_Permute(A_input, b_input, max_iter=None, epsilon=None, x0=None):
    def matrix_to_latex(M, precision=4):
        if not isinstance(M, np.ndarray): return str(M)
        elif M.ndim == 1:
            inner = " \\\\ ".join([f"{x:.{precision}f}" for x in M])
            return f"\\begin{{bmatrix}} {inner} \\end{{bmatrix}}"
        else:
            rows = " \\\\ ".join([" & ".join([f"{x:.{precision}f}" for x in row]) for row in M])
            return f"\\begin{{bmatrix}} {rows} \\end{{bmatrix}}"

    A_origin = np.array(A_input, dtype=float)
    b_origin = np.array(b_input, dtype=float).flatten()
    n = len(b_origin)
    
    if x0 is None: X_k = np.zeros(n)
    else: X_k = np.array(x0, dtype=float)
        
    md = []
    md.append("## ❖ GAUSS-SEIDEL (CÓ TỰ ĐỘNG ĐỔI DÒNG TẠO CHÉO TRỘI)")
    md.append("---\n")
    
    md.append("### I. TỰ ĐỘNG KIỂM TRA VÀ ĐỔI DÒNG")
    md.append("Hệ ban đầu:")
    md.append(f"$$ A_{{ban\\_dau}} = {matrix_to_latex(A_origin, 2)} \\quad b_{{ban\\_dau}} = {matrix_to_latex(b_origin, 2)} $$\n")
    
    is_dom, A, b, perm = Check_And_Permute_Dominant(A_origin, b_origin)
    
    if is_dom and perm != tuple(range(n)):
        md.append(f"**✅ ĐÃ ĐỔI DÒNG THÀNH CÔNG!** Thứ tự các hàng mới: {perm}")
        md.append(f"$$ A = {matrix_to_latex(A, 2)} \\quad b = {matrix_to_latex(b, 2)} $$\n")
        md.append("Ma trận A mới đã **chéo trội hàng ngặt**, đảm bảo Gauss-Seidel hội tụ.")
    elif is_dom:
        md.append("**✅ Hợp lệ:** Ma trận ban đầu đã chéo trội hàng ngặt sẵn, không cần đổi dòng.")
        A, b = A_origin, b_origin
    else:
        md.append("**⚠️ Cảnh báo:** Đã thử mọi hoán vị nhưng không thể tạo ra ma trận chéo trội hàng ngặt.")
        A, b = A_origin, b_origin

    # Biến đổi Ax=b thành x=Bx+d
    D = np.diag(np.diag(A))
    L = np.tril(A, -1)
    U = np.triu(A, 1)
    D_inv = np.linalg.inv(D)
    B = -D_inv @ (L + U)
    d = D_inv @ b
    
    md.append("\n### II. RÚT X VÀ BIẾN ĐỔI THÀNH DẠNG x = Bx + d")
    md.append(f"$$ B = {matrix_to_latex(B, precision=4)} \\quad d = {matrix_to_latex(d, precision=4)} $$")
    
    norm_B = np.linalg.norm(B, np.inf)
    md.append(f"- **Chuẩn vô cùng của B:** $q = ||B||_\\infty = {norm_B:.4f}$")
    
    md.append("\n---\n### III. BẢNG QUÁ TRÌNH LẶP")
    
    history = []
    diffs = []
    k = 1
    max_safe_iters = max_iter if max_iter is not None else 100
    eps0 = epsilon if epsilon is not None else 1e-5
    
    while True:
        X_new = np.copy(X_k)
        for i in range(n):
            s1 = sum(B[i, j] * X_new[j] for j in range(i))
            s2 = sum(B[i, j] * X_k[j] for j in range(i, n))
            X_new[i] = s1 + s2 + d[i]
            
        diff = np.linalg.norm(X_new - X_k, np.inf)
        history.append(X_new.copy())
        diffs.append(diff)
        
        if diff < eps0 or k >= max_safe_iters:
            break
        k += 1
        X_k = np.copy(X_new)
        
    N = len(history)
    if N <= 5:
        cols = list(range(1, N+1))
    else:
        cols = [1, 2, -1, N-1, N]
        
    header = "| | " + " | ".join([f"Lần {c}" if c != -1 else "..." for c in cols]) + " |"
    sep = "|---|" + "|".join(["---" for c in cols]) + "|"
    lines = [header, sep]
    
    for i in range(n):
        row = [f"$x_{{{i+1}}}$"]
        for c in cols:
            if c == -1:
                row.append("...")
            else:
                row.append(f"{history[c-1][i]:.5f}")
        lines.append("| " + " | ".join(row) + " |")
        
    row = [f"$|| x_k - x_{{k-1}} ||$"]
    for c in cols:
        if c == -1:
            row.append("...")
        else:
            val_str = f"{diffs[c-1]:.5f}"
            if c == N:
                val_str += f" < \\varepsilon_0"
            elif c == N-1:
                val_str += f" > \\varepsilon_0"
            row.append(val_str)
    lines.append("| " + " | ".join(row) + " |")
    
    md.extend(lines)
    
    md.append("\n---\n### IV. KẾT LUẬN")
    md.append(f"Hệ dừng lại tại bước lặp $k = {N}$. Nghiệm gần đúng là:")
    md.append(f"$$ X \\approx {{matrix_to_latex(history[-1], precision=5)}} $$")
    
    display(Markdown('\n'.join(md)))

# Ma trận hệ số A (Cố tình để lộn xộn để test tự động đổi dòng)

# ═══════════════════════════════════════════════════════════════════
# NHẬP DỮ LIỆU CỦA BẠN VÀO ĐÂY
# ═══════════════════════════════════════════════════════════════════
A = np.array([
    [ 2.0, 10.0,  1.0],
    [10.0,  1.0,  2.0],
    [ 1.0,  2.0, 10.0]
], dtype=float)

b = np.array([13.0, 13.0, 13.0], dtype=float)
# ═══════════════════════════════════════════════════════════════════

Gauss_Seidel_Ax_B_Permute(A, b, max_iter=None, epsilon=1e-6)
