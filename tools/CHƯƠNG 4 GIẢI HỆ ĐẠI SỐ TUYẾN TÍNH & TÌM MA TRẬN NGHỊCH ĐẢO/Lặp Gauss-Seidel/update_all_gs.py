import json
import os

dir_path = "d:/code/Uni/On_thi_cuoi_ky/Giải tích số/scripts/CHƯƠNG 4 GIẢI HỆ ĐẠI SỐ TUYẾN TÍNH & TÌM MA TRẬN NGHỊCH ĐẢO/Lặp Gauss-Seidel"

def update_notebook(filename, new_code):
    filepath = os.path.join(dir_path, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        nb = json.load(f)
        
    source_lines = [line + '\n' for line in new_code.split('\n')]
    source_lines[-1] = source_lines[-1][:-1]
    
    nb['cells'][1]['source'] = source_lines
    nb['cells'][1]['outputs'] = []
    
    # Keep only the first two cells (Markdown header + Code)
    nb['cells'] = nb['cells'][:2]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
        
# -------------------------------------------------------------
# 1. Lặp Gauss-Seidel (x = Bx + d)
# -------------------------------------------------------------
code_Bd = r"""import numpy as np
from IPython.display import Markdown, display

def Gauss_Seidel_Bd(B_input, d_input, max_iter=6, x0=None):
    def matrix_to_latex(M, precision=4):
        if not isinstance(M, np.ndarray): return str(M)
        elif M.ndim == 1:
            inner = " \\\\ ".join([f"{x:.{precision}f}" for x in M])
            return f"\\begin{{bmatrix}} {inner} \\end{{bmatrix}}"
        else:
            rows = " \\\\ ".join([" & ".join([f"{x:.{precision}f}" for x in row]) for row in M])
            return f"\\begin{{bmatrix}} {rows} \\end{{bmatrix}}"

    B = np.array(B_input, dtype=float)
    d = np.array(d_input, dtype=float)
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
    
    header = "| $k$ | " + " | ".join([f"$x_{{{i+1}}}$" for i in range(n)]) + " | Sai số $\\|x^{(k)} - x^{(k-1)}\\|_\\infty$ |"
    md.append(header)
    md.append("|---" * (n + 2) + "|")
    
    row0 = f"| 0 | " + " | ".join([f"{x:.5f}" for x in X_k]) + " | - |"
    md.append(row0)
    
    for k in range(1, max_iter + 1):
        X_new = np.copy(X_k)
        for i in range(n):
            s1 = sum(B[i][j] * X_new[j] for j in range(i))
            s2 = sum(B[i][j] * X_k[j] for j in range(i, n))
            X_new[i] = s1 + s2 + d[i]
            
        sai_so = np.linalg.norm(X_new - X_k, np.inf)
        row = f"| {k} | " + " | ".join([f"{x:.5f}" for x in X_new]) + f" | {sai_so:.5f} |"
        md.append(row)
        X_k = X_new
        
    md.append("\n---\n### IV. KẾT LUẬN")
    md.append(f"Sau {max_iter} lần lặp, ta thu được nghiệm gần đúng:")
    md.append(f"$$ x^{{({max_iter})}} = {matrix_to_latex(X_k, precision=5)} $$")
    
    display(Markdown('\n'.join(md)))

B = np.array([
    [-0.09,  0.01,  0.06, -0.05, -0.09],
    [ 0.01, -0.01, -0.04,  0.03, -0.06],
    [ 0.06, -0.10,  0.01,  0.04,  0.09],
    [ 0.09, -0.03, -0.07,  0.05, -0.07],
    [-0.08, -0.07,  0.02, -0.01,  0.07]
], dtype=float)

d = np.array([6, 10, 1, 5, 2], dtype=float)

Gauss_Seidel_Bd(B, d, max_iter=6)
"""

update_notebook("Lặp Gauss-Seidel (x=Bx+d).ipynb", code_Bd)

# -------------------------------------------------------------
# 2. Lặp Gauss-Seidel (Ax = b)
# -------------------------------------------------------------
code_AxB = r"""import numpy as np
from IPython.display import Markdown, display

def Gauss_Seidel_AxB(A_input, b_input, max_iter=6, x0=None):
    def matrix_to_latex(M, precision=4):
        if not isinstance(M, np.ndarray): return str(M)
        elif M.ndim == 1:
            inner = " \\\\ ".join([f"{x:.{precision}f}" for x in M])
            return f"\\begin{{bmatrix}} {inner} \\end{{bmatrix}}"
        else:
            rows = " \\\\ ".join([" & ".join([f"{x:.{precision}f}" for x in row]) for row in M])
            return f"\\begin{{bmatrix}} {rows} \\end{{bmatrix}}"

    A = np.array(A_input, dtype=float)
    b = np.array(b_input, dtype=float)
    n = len(b)
    
    if x0 is None:
        X_k = np.zeros(n)
    else:
        X_k = np.array(x0, dtype=float)
        
    md = []
    md.append("## ❖ PHƯƠNG PHÁP LẶP GAUSS-SEIDEL (DẠNG $Ax = b$)")
    md.append("---\n")
    md.append("> **📝 HƯỚNG DẪN TRÌNH BÀY BÀI THI:**")
    md.append("> - **Bước 1:** Kiểm tra tính chéo trội của ma trận hệ số $A$.")
    md.append("> - **Bước 2:** Viết công thức lặp Gauss-Seidel dạng rút ra $x_i^{(k+1)}$.")
    md.append("> - **Bước 3:** Kẻ bảng quá trình lặp và ghi số liệu.")
    md.append("> - **Bước 4:** Kết luận nghiệm và sai số nếu được yêu cầu.")
    
    md.append("\n### I. ĐIỀU KIỆN HỘI TỤ (TÍNH CHÉO TRỘI)")
    is_dominant = True
    for i in range(n):
        sum_row = sum(abs(A[i, j]) for j in range(n) if j != i)
        if sum_row >= abs(A[i, i]):
            is_dominant = False
            break
            
    if is_dominant:
        md.append(f"Ma trận $A$ chéo trội hàng ngặt, phương pháp lặp chắc chắn hội tụ.")
    else:
        md.append(f"**Cảnh báo:** Ma trận $A$ KHÔNG chéo trội hàng ngặt, phương pháp chưa chắc hội tụ.")

    md.append("\n### II. CÔNG THỨC LẶP GAUSS-SEIDEL")
    
    for i in range(n):
        terms = []
        for j in range(n):
            if j == i: continue
            val = A[i, j]
            if abs(val) < 1e-10: continue
            
            # Đổi dấu vì chuyển vế
            val = -val
            sign = " + " if val > 0 else " - "
            if j < i:
                terms.append(f"{sign}{abs(val):.4f} x_{{{j+1}}}^{{(k+1)}}")
            else:
                terms.append(f"{sign}{abs(val):.4f} x_{{{j+1}}}^{{(k)}}")
        
        formula = "".join(terms).lstrip(" + ")
        b_sign = f" + {b[i]:.4f}" if b[i] >= 0 and formula else f"{b[i]:.4f}"
        if not formula: b_sign = f"{b[i]:.4f}"
        
        md.append(f"- $x_{{{i+1}}}^{{(k+1)}} = \\frac{{1}}{{{A[i,i]:.4f}}} \\left( {b_sign} {formula} \\right)$")
        
    md.append("\n---\n### III. BẢNG QUÁ TRÌNH LẶP")
    
    header = "| $k$ | " + " | ".join([f"$x_{{{i+1}}}$" for i in range(n)]) + " | Sai số $\\|x^{(k)} - x^{(k-1)}\\|_\\infty$ |"
    md.append(header)
    md.append("|---" * (n + 2) + "|")
    
    row0 = f"| 0 | " + " | ".join([f"{x:.5f}" for x in X_k]) + " | - |"
    md.append(row0)
    
    for k in range(1, max_iter + 1):
        X_new = np.copy(X_k)
        for i in range(n):
            s1 = sum(A[i][j] * X_new[j] for j in range(i))
            s2 = sum(A[i][j] * X_k[j] for j in range(i+1, n))
            X_new[i] = (b[i] - s1 - s2) / A[i, i]
            
        sai_so = np.linalg.norm(X_new - X_k, np.inf)
        row = f"| {k} | " + " | ".join([f"{x:.5f}" for x in X_new]) + f" | {sai_so:.5f} |"
        md.append(row)
        X_k = X_new
        
    md.append("\n---\n### IV. KẾT LUẬN")
    md.append(f"Sau {max_iter} lần lặp, ta thu được nghiệm gần đúng:")
    md.append(f"$$ x^{{({max_iter})}} = {matrix_to_latex(X_k, precision=5)} $$")
    
    display(Markdown('\n'.join(md)))

A = np.array([
    [5.0, -1.0, -1.0],
    [-1.0, 5.0, -1.0],
    [-1.0, -1.0, 5.0]
], dtype=float)
b = np.array([0.0, 6.0, 12.0], dtype=float)

Gauss_Seidel_AxB(A, b, max_iter=6)
"""

update_notebook("Lặp Gauss-Seidel (Ax=B).ipynb", code_AxB)

# -------------------------------------------------------------
# 3. Lặp Gauss-Seidel (Đổi dòng tạo chéo trội)
# -------------------------------------------------------------
code_AxB_Swap = r"""import numpy as np
from IPython.display import Markdown, display

def Gauss_Seidel_AxB_Swap(A_input, b_input, max_iter=6, x0=None):
    def matrix_to_latex(M, precision=4):
        if not isinstance(M, np.ndarray): return str(M)
        elif M.ndim == 1:
            inner = " \\\\ ".join([f"{x:.{precision}f}" for x in M])
            return f"\\begin{{bmatrix}} {inner} \\end{{bmatrix}}"
        else:
            rows = " \\\\ ".join([" & ".join([f"{x:.{precision}f}" for x in row]) for row in M])
            return f"\\begin{{bmatrix}} {rows} \\end{{bmatrix}}"

    A = np.array(A_input, dtype=float)
    b = np.array(b_input, dtype=float)
    n = len(b)
    
    md = []
    md.append("## ❖ PHƯƠNG PHÁP LẶP GAUSS-SEIDEL (KÈM HOÁN VỊ TẠO CHÉO TRỘI)")
    md.append("---\n")
    
    md.append("### I. TẠO MA TRẬN CHÉO TRỘI HÀNG")
    
    A_new = np.zeros_like(A)
    b_new = np.zeros_like(b)
    swaps = []
    
    for i in range(n):
        # Tìm dòng j có |A[j,i]| > sum(còn lại)
        found = False
        for j in range(n):
            sum_row = sum(abs(A[j, k]) for k in range(n) if k != i)
            if abs(A[j, i]) > sum_row:
                A_new[i] = A[j]
                b_new[i] = b[j]
                swaps.append((j, i))
                found = True
                break
        if not found:
            md.append(f"**❌ LỖI:** Không thể tìm được phương trình nào thoả mãn chéo trội cho biến $x_{{{i+1}}}$. Thuật toán dừng.")
            display(Markdown('\n'.join(md)))
            return
            
    md.append(f"Hệ phương trình mới (đã hoán vị dòng) đảm bảo chéo trội:")
    md.append(f"$$ A' = {matrix_to_latex(A_new, precision=4)} , \\quad b' = {matrix_to_latex(b_new, precision=4)} $$")
    
    if x0 is None:
        X_k = np.zeros(n)
    else:
        X_k = np.array(x0, dtype=float)
        
    md.append("\n### II. CÔNG THỨC LẶP GAUSS-SEIDEL")
    
    for i in range(n):
        terms = []
        for j in range(n):
            if j == i: continue
            val = A_new[i, j]
            if abs(val) < 1e-10: continue
            
            # Đổi dấu vì chuyển vế
            val = -val
            sign = " + " if val > 0 else " - "
            if j < i:
                terms.append(f"{sign}{abs(val):.4f} x_{{{j+1}}}^{{(k+1)}}")
            else:
                terms.append(f"{sign}{abs(val):.4f} x_{{{j+1}}}^{{(k)}}")
        
        formula = "".join(terms).lstrip(" + ")
        b_sign = f" + {b_new[i]:.4f}" if b_new[i] >= 0 and formula else f"{b_new[i]:.4f}"
        if not formula: b_sign = f"{b_new[i]:.4f}"
        
        md.append(f"- $x_{{{i+1}}}^{{(k+1)}} = \\frac{{1}}{{{A_new[i,i]:.4f}}} \\left( {b_sign} {formula} \\right)$")
        
    md.append("\n---\n### III. BẢNG QUÁ TRÌNH LẶP")
    
    header = "| $k$ | " + " | ".join([f"$x_{{{i+1}}}$" for i in range(n)]) + " | Sai số $\\|x^{(k)} - x^{(k-1)}\\|_\\infty$ |"
    md.append(header)
    md.append("|---" * (n + 2) + "|")
    
    row0 = f"| 0 | " + " | ".join([f"{x:.5f}" for x in X_k]) + " | - |"
    md.append(row0)
    
    for k in range(1, max_iter + 1):
        X_new = np.copy(X_k)
        for i in range(n):
            s1 = sum(A_new[i][j] * X_new[j] for j in range(i))
            s2 = sum(A_new[i][j] * X_k[j] for j in range(i+1, n))
            X_new[i] = (b_new[i] - s1 - s2) / A_new[i, i]
            
        sai_so = np.linalg.norm(X_new - X_k, np.inf)
        row = f"| {k} | " + " | ".join([f"{x:.5f}" for x in X_new]) + f" | {sai_so:.5f} |"
        md.append(row)
        X_k = X_new
        
    md.append("\n---\n### IV. KẾT LUẬN")
    md.append(f"Sau {max_iter} lần lặp, ta thu được nghiệm gần đúng:")
    md.append(f"$$ x^{{({max_iter})}} = {matrix_to_latex(X_k, precision=5)} $$")
    
    display(Markdown('\n'.join(md)))

# Ví dụ
A = np.array([
    [1, 1, 10],
    [10, 1, 1],
    [1, 10, 1]
], dtype=float)
b = np.array([12, 12, 12], dtype=float)

Gauss_Seidel_AxB_Swap(A, b, max_iter=6)
"""

update_notebook("Lặp Gauss-Seidel (Đổi dòng tạo chéo trội).ipynb", code_AxB_Swap)

print("Đã cập nhật đồng bộ cả 3 file Gauss-Seidel thành công!")
