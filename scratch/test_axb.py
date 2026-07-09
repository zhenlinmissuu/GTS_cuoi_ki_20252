import numpy as np
from IPython.display import display, Math, Markdown

def _mat(M, p=5):
    if hasattr(M[0], "__len__"):
        rows = " \\\\ ".join([" & ".join([f"{x:.{p}f}" for x in row]) for row in M])
        return f"\\begin{{bmatrix}} {rows} \\end{{bmatrix}}"
    inner = " \\\\ ".join([f"{x:.{p}f}" for x in M])
    return f"\\begin{{bmatrix}} {inner} \\end{{bmatrix}}"

def Gauss_Seidel_Ax_B(A_input, b_input, max_iter=200, epsilon=1e-5, x0=None):
    A = np.array(A_input, dtype=float)
    b = np.array(b_input, dtype=float).flatten()
    n = len(b)
    
    if x0 is None:
        X_k = np.zeros(n)
    else:
        X_k = np.array(x0, dtype=float).flatten()
        
    display(Markdown("## ❖ PHƯƠNG PHÁP LẶP GAUSS-SEIDEL (HỆ $Ax = b$)"))
    
    D = np.diag(np.diag(A))
    L = np.tril(A, -1)
    U = np.triu(A, 1)
    
    D_inv = np.linalg.inv(D)
    B = -D_inv @ (L + U)
    d = D_inv @ b
    
    display(Markdown("### 1. Kiểm tra điều kiện hội tụ"))
    
    # Tính s, q theo chuẩn vô cùng
    s = 0.0
    q = 0.0
    for i in range(n):
        sum_l = sum(abs(A[i, j]) for j in range(i))
        sum_u = sum(abs(A[i, j]) for j in range(i+1, n))
        s_i = sum_u / abs(A[i,i]) if abs(A[i,i]) != 0 else float('inf')
        q_i = sum_l / (abs(A[i,i]) - sum_u) if (abs(A[i,i]) - sum_u) > 0 else float('inf')
        s = max(s, s_i)
        q = max(q, q_i)
        
    display(Math(f"s = {s:.5f}, \\quad q \\approx {q:.5f}"))
    
    eps0 = epsilon * (1 - s) * (1 - q) / q if q < 1 else epsilon
    display(Math(f"\\varepsilon_0 = \\frac{{\\varepsilon(1-s)(1-q)}}{{q}} = {eps0:.5e}"))
    
    display(Markdown("### 2. Quá trình lặp"))
    
    history = []
    diffs = []
    k = 1
    
    while True:
        X_new = np.copy(X_k)
        for i in range(n):
            s1 = sum(B[i, j] * X_new[j] for j in range(i))
            s2 = sum(B[i, j] * X_k[j] for j in range(i, n))
            X_new[i] = s1 + s2 + d[i]
            
        diff = np.linalg.norm(X_new - X_k, np.inf)
        history.append(X_new.copy())
        diffs.append(diff)
        
        if diff < eps0 or (max_iter is not None and k >= max_iter) or k > 200:
            break
            
        X_k = np.copy(X_new)
        k += 1
        
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
    
    display(Markdown("\n".join(lines)))
    
    display(Markdown("### 3. Kết luận"))
    display(Markdown(f"Nghiệm xấp xỉ sau {N} lần lặp:"))
    display(Math(f"X \\approx {_mat(history[-1], 5)}"))

# ═══════════════════════════════════════════════════════════════════
# NHẬP DỮ LIỆU CỦA BẠN VÀO ĐÂY
# ═══════════════════════════════════════════════════════════════════

# ═══════════════════════════════════════════════════════════════════
# NHẬP DỮ LIỆU CỦA BẠN VÀO ĐÂY
# ═══════════════════════════════════════════════════════════════════

# ═══════════════════════════════════════════════════════════════════
# NHẬP DỮ LIỆU CỦA BẠN VÀO ĐÂY
# ═══════════════════════════════════════════════════════════════════
A = np.array([
    [10.0, 1.0,  2.0],
    [ 1.0, 10.0, 3.0],
    [ 2.0,  3.0, 10.0]
], dtype=float)

b = np.array([7.0, 8.0, 9.0], dtype=float)
# ═══════════════════════════════════════════════════════════════════

Gauss_Seidel_Ax_B(A, b, max_iter=None, epsilon=1e-6)
