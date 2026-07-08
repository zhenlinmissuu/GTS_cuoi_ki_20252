import os
import json

gs_dir = "d:/code/Uni/On_thi_cuoi_ky/Giải tích số/scripts/CHƯƠNG 4 GIẢI HỆ ĐẠI SỐ TUYẾN TÍNH & TÌM MA TRẬN NGHỊCH ĐẢO/Lặp Gauss-Seidel"

def fix_gs_file(filename, is_ax_b=False, is_permute=False):
    filepath = os.path.join(gs_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        nb = json.load(f)
        
    source = "".join(nb['cells'][1]['source'])
    
    # We need to replace the function definition and loop logic
    if not is_ax_b and not is_permute:
        new_source = r"""import numpy as np
from IPython.display import Markdown, display

def Gauss_Seidel_Bd(B_input, d_input, max_iter=None, epsilon=None, x0=None):
    def matrix_to_latex(M, precision=4):
        if not isinstance(M, np.ndarray): return str(M)
        elif M.ndim == 1:
            inner = " \\\\ ".join([f"{x:.{precision}f}" for x in M])
            return f"\\begin{{bmatrix}} {inner} \\end{{bmatrix}}"
        else:
            rows = " \\\\ ".join([" & ".join([f"{x:.{precision}f}" for x in row]) for row in M])
            return f"\\begin{{bmatrix}} {rows} \\end{{bmatrix}}"

    B = np.array(B_input, dtype=float)
    d = np.array(d_input, dtype=float).flatten()
    n = len(d)
    
    if x0 is None:
        X_k = np.zeros(n)
    else:
        X_k = np.array(x0, dtype=float)
        
    md = []
    md.append("## ❖ PHƯƠNG PHÁP LẶP GAUSS-SEIDEL (DẠNG $x = Bx + d$)")
    md.append("---\n")
    md.append("> **📝 HƯỚNG DẪN TRÌNH BÀY BÀI THI:**")
    md.append("> - **Bước 1:** Kiểm tra điều kiện hội tụ $||B||_\\infty < 1$.")
    md.append("> - **Bước 2:** Viết công thức lặp Gauss-Seidel dạng khai triển.")
    md.append("> - **Bước 3:** Kẻ bảng quá trình lặp và ghi số liệu.")
    md.append("> - **Bước 4:** Kết luận nghiệm và sai số nếu được yêu cầu.")
    
    norm_B = np.linalg.norm(B, np.inf)
    md.append("\n### I. ĐIỀU KIỆN HỘI TỤ")
    md.append(f"Chuẩn vô cùng của ma trận $B$: $||B||_\\infty = {norm_B:.4f}$")
    if norm_B < 1:
        md.append(f"Vì $||B||_\\infty < 1$, phương pháp lặp chắc chắn hội tụ.")
    else:
        md.append(f"**Cảnh báo:** $||B||_\\infty \\ge 1$, phương pháp chưa chắc hội tụ.")

    md.append("\n### II. CÔNG THỨC LẶP GAUSS-SEIDEL (KHAI TRIỂN)")
    
    for i in range(n):
        terms = []
        for j in range(n):
            val = B[i, j]
            if abs(val) < 1e-10: continue
            
            sign = " + " if val > 0 else " - "
            if j < i:
                terms.append(f"{sign}{abs(val):.4f} x_{{{j+1}}}^{{(k+1)}}")
            else:
                terms.append(f"{sign}{abs(val):.4f} x_{{{j+1}}}^{{(k)}}")
        
        formula = "".join(terms).lstrip(" + ")
        d_sign = f" + {d[i]:.4f}" if d[i] >= 0 else f" - {abs(d[i]):.4f}"
        md.append(f"- $x_{{{i+1}}}^{{(k+1)}} = {formula}{d_sign}$")
        
    md.append("\n---\n### III. BẢNG QUÁ TRÌNH LẶP")
    
    header = "| $k$ | " + " | ".join([f"$x_{{{i+1}}}$" for i in range(n)]) + " | Sai số $||x^{(k)} - x^{(k-1)}||_\\infty$ |"
    md.append(header)
    md.append("|---" * (n + 2) + "|")
    
    row0 = f"| 0 | " + " | ".join([f"{x:.5f}" for x in X_k]) + " | - |"
    md.append(row0)
    
    k = 1
    # Vòng lặp an toàn chống lặp vô hạn
    max_safe_iters = max_iter if max_iter is not None else 100
    
    while True:
        X_new = np.copy(X_k)
        for i in range(n):
            s1 = sum(B[i][j] * X_new[j] for j in range(i))
            s2 = sum(B[i][j] * X_k[j] for j in range(i, n))
            X_new[i] = s1 + s2 + d[i]
            
        sai_so = np.linalg.norm(X_new - X_k, np.inf)
        row = f"| {k} | " + " | ".join([f"{x:.5f}" for x in X_new]) + f" | {sai_so:.5f} |"
        md.append(row)
        X_k = X_new
        
        # Điều kiện dừng
        stop_eps = (epsilon is not None) and (sai_so <= epsilon)
        stop_iter = (max_iter is not None) and (k >= max_iter)
        
        if stop_eps or stop_iter or k >= max_safe_iters:
            break
        k += 1
        
    md.append("\n---\n### IV. KẾT LUẬN")
    md.append(f"Hệ dừng lại tại bước lặp $k = {k}$. Nghiệm gần đúng là:")
    md.append(f"$$ x^{{({k})}} = {matrix_to_latex(X_k, precision=5)} $$")
    
    display(Markdown('\n'.join(md)))

# Ma trận hệ số B (Kích thước 5x5)
B = np.array([
    [-0.0900,  0.0100,  0.0600, -0.0500, -0.0900],
    [ 0.0100, -0.0100, -0.0400,  0.0300, -0.0600],
    [ 0.0600, -0.1000,  0.0100,  0.0400,  0.0900],
    [ 0.0900, -0.0300, -0.0700,  0.0500, -0.0700],
    [-0.0800, -0.0700,  0.0200, -0.0100,  0.0700]
], dtype=float)

# Vectơ hệ số tự do d (Kích thước 5x1)
d = np.array([
    [6],
    [10],
    [1],
    [5],
    [2]
], dtype=float)

# Điền max_iter nếu muốn lặp số lần cố định, HOẶC điền epsilon nếu muốn lặp đến khi đạt sai số (VD: epsilon=1e-3)
Gauss_Seidel_Bd(B, d, max_iter=6, epsilon=None)
"""
    elif is_ax_b and not is_permute:
        new_source = r"""import numpy as np
from IPython.display import Markdown, display

def Gauss_Seidel_Ax_B(A_input, b_input, max_iter=None, epsilon=None, x0=None):
    def matrix_to_latex(M, precision=4):
        if not isinstance(M, np.ndarray): return str(M)
        elif M.ndim == 1:
            inner = " \\\\ ".join([f"{x:.{precision}f}" for x in M])
            return f"\\begin{{bmatrix}} {inner} \\end{{bmatrix}}"
        else:
            rows = " \\\\ ".join([" & ".join([f"{x:.{precision}f}" for x in row]) for row in M])
            return f"\\begin{{bmatrix}} {rows} \\end{{bmatrix}}"

    A = np.array(A_input, dtype=float)
    b = np.array(b_input, dtype=float).flatten()
    n = len(b)
    
    if x0 is None:
        X_k = np.zeros(n)
    else:
        X_k = np.array(x0, dtype=float)
        
    md = []
    md.append("## ❖ PHƯƠNG PHÁP LẶP GAUSS-SEIDEL (DẠNG $Ax = b$)")
    md.append("---\n")
    md.append("> **📝 HƯỚNG DẪN TRÌNH BÀY BÀI THI:**")
    md.append("> - **Bước 1:** Đưa hệ về dạng $x = Bx + d$ bằng cách rút $x_i$ từ phương trình thứ $i$. Tính $||B||_\\infty$.")
    md.append("> - **Bước 2:** Viết công thức lặp Gauss-Seidel dạng khai triển.")
    md.append("> - **Bước 3:** Kẻ bảng quá trình lặp và ghi số liệu.")
    md.append("> - **Bước 4:** Kết luận nghiệm và sai số nếu được yêu cầu.")
    
    # Biến đổi Ax=b thành x=Bx+d
    D = np.diag(np.diag(A))
    L = np.tril(A, -1)
    U = np.triu(A, 1)
    
    # B = -D^-1 (L + U)
    D_inv = np.linalg.inv(D)
    B = -D_inv @ (L + U)
    d = D_inv @ b
    
    md.append("\n### I. RÚT X VÀ KIỂM TRA ĐIỀU KIỆN HỘI TỤ")
    md.append(f"Hệ tương đương với dạng $x = Bx + d$, với:")
    md.append(f"$$ B = {matrix_to_latex(B, precision=4)} $$")
    md.append(f"$$ d = {matrix_to_latex(d, precision=4)} $$")
    
    norm_B = np.linalg.norm(B, np.inf)
    md.append(f"Chuẩn vô cùng của ma trận $B$: $||B||_\\infty = {norm_B:.4f}$")
    if norm_B < 1:
        md.append(f"Vì $||B||_\\infty < 1$, phương pháp lặp chắc chắn hội tụ.")
    else:
        md.append(f"**Cảnh báo:** $||B||_\\infty \\ge 1$, phương pháp chưa chắc hội tụ.")

    md.append("\n### II. CÔNG THỨC LẶP GAUSS-SEIDEL (KHAI TRIỂN)")
    
    for i in range(n):
        terms = []
        for j in range(n):
            val = B[i, j]
            if abs(val) < 1e-10: continue
            
            sign = " + " if val > 0 else " - "
            if j < i:
                terms.append(f"{sign}{abs(val):.4f} x_{{{j+1}}}^{{(k+1)}}")
            else:
                terms.append(f"{sign}{abs(val):.4f} x_{{{j+1}}}^{{(k)}}")
        
        formula = "".join(terms).lstrip(" + ")
        d_sign = f" + {d[i]:.4f}" if d[i] >= 0 else f" - {abs(d[i]):.4f}"
        md.append(f"- $x_{{{i+1}}}^{{(k+1)}} = {formula}{d_sign}$")
        
    md.append("\n---\n### III. BẢNG QUÁ TRÌNH LẶP")
    
    header = "| $k$ | " + " | ".join([f"$x_{{{i+1}}}$" for i in range(n)]) + " | Sai số $||x^{(k)} - x^{(k-1)}||_\\infty$ |"
    md.append(header)
    md.append("|---" * (n + 2) + "|")
    
    row0 = f"| 0 | " + " | ".join([f"{x:.5f}" for x in X_k]) + " | - |"
    md.append(row0)
    
    k = 1
    max_safe_iters = max_iter if max_iter is not None else 100
    
    while True:
        X_new = np.copy(X_k)
        for i in range(n):
            s1 = sum(B[i][j] * X_new[j] for j in range(i))
            s2 = sum(B[i][j] * X_k[j] for j in range(i, n))
            X_new[i] = s1 + s2 + d[i]
            
        sai_so = np.linalg.norm(X_new - X_k, np.inf)
        row = f"| {k} | " + " | ".join([f"{x:.5f}" for x in X_new]) + f" | {sai_so:.5f} |"
        md.append(row)
        X_k = X_new
        
        stop_eps = (epsilon is not None) and (sai_so <= epsilon)
        stop_iter = (max_iter is not None) and (k >= max_iter)
        if stop_eps or stop_iter or k >= max_safe_iters:
            break
        k += 1
        
    md.append("\n---\n### IV. KẾT LUẬN")
    md.append(f"Hệ dừng lại tại bước lặp $k = {k}$. Nghiệm gần đúng là:")
    md.append(f"$$ x^{{({k})}} = {matrix_to_latex(X_k, precision=5)} $$")
    
    display(Markdown('\n'.join(md)))

# Ma trận hệ số A
A = np.array([
    [ 10.0, -1.0,  2.0,  0.0],
    [ -1.0, 11.0, -1.0,  3.0],
    [  2.0, -1.0, 10.0, -1.0],
    [  0.0,  3.0, -1.0,  8.0]
], dtype=float)

# Vectơ vế phải B
B = np.array([6.0, 25.0, -11.0, 15.0], dtype=float)

# Điền max_iter nếu muốn lặp số lần cố định, HOẶC điền epsilon nếu muốn lặp đến khi đạt sai số
Gauss_Seidel_Ax_B(A, B, max_iter=5, epsilon=None)
"""
    else:
        new_source = r"""import numpy as np
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
    md.append(f"$$ A_{{ban\_dau}} = {matrix_to_latex(A_origin, 2)} \\quad b_{{ban\_dau}} = {matrix_to_latex(b_origin, 2)} $$\n")
    
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
    
    header = "| $k$ | " + " | ".join([f"$x_{{{i+1}}}$" for i in range(n)]) + " | Sai số $||x^{(k)} - x^{(k-1)}||_\\infty$ |"
    md.append(header)
    md.append("|---" * (n + 2) + "|")
    
    row0 = f"| 0 | " + " | ".join([f"{x:.5f}" for x in X_k]) + " | - |"
    md.append(row0)
    
    k = 1
    max_safe_iters = max_iter if max_iter is not None else 100
    
    while True:
        X_new = np.copy(X_k)
        for i in range(n):
            s1 = sum(B[i][j] * X_new[j] for j in range(i))
            s2 = sum(B[i][j] * X_k[j] for j in range(i, n))
            X_new[i] = s1 + s2 + d[i]
            
        sai_so = np.linalg.norm(X_new - X_k, np.inf)
        row = f"| {k} | " + " | ".join([f"{x:.5f}" for x in X_new]) + f" | {sai_so:.5f} |"
        md.append(row)
        X_k = X_new
        
        stop_eps = (epsilon is not None) and (sai_so <= epsilon)
        stop_iter = (max_iter is not None) and (k >= max_iter)
        if stop_eps or stop_iter or k >= max_safe_iters:
            break
        k += 1
        
    md.append("\n---\n### IV. KẾT LUẬN")
    md.append(f"Hệ dừng lại tại bước lặp $k = {k}$. Nghiệm gần đúng là:")
    md.append(f"$$ x^{{({k})}} = {matrix_to_latex(X_k, precision=5)} $$")
    
    display(Markdown('\n'.join(md)))

# Ma trận hệ số A (Cố tình để lộn xộn để test tự động đổi dòng)
A = np.array([
    [1, 1, 10],
    [10, 2, 1],
    [1, 10, 2]
], dtype=float)

# Vectơ vế phải b
b = np.array([12, 13, 13], dtype=float)

Gauss_Seidel_Ax_B_Permute(A, b, max_iter=5, epsilon=None)
"""

    source_lines = [line + '\n' for line in new_source.split('\n')]
    source_lines[-1] = source_lines[-1][:-1]
    
    nb['cells'][1]['source'] = source_lines
    nb['cells'][1]['outputs'] = []
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)

fix_gs_file("Lặp Gauss-Seidel (x=Bx+d).ipynb", is_ax_b=False, is_permute=False)
fix_gs_file("Lặp Gauss-Seidel (Ax=B).ipynb", is_ax_b=True, is_permute=False)
fix_gs_file("Lặp Gauss-Seidel (Đổi dòng tạo chéo trội).ipynb", is_ax_b=True, is_permute=True)

print("Đã cập nhật lại epsilon cho cả 3 file Gauss-Seidel thành công!")
