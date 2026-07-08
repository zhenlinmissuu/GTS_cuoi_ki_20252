import json

notebook_path = "d:/code/Uni/On_thi_cuoi_ky/Giải tích số/scripts/CHƯƠNG 5 GIÁ TRỊ RIÊNG VÀ VECTOR RIÊNG CỦA MA TRẬN/Giá trị kỳ dị SVD (Lớn nhất).ipynb"

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

new_source = r"""import numpy as np
from IPython.display import Markdown, display

def SVD_Reduced(A_input):
    def matrix_to_latex(M, precision=4):
        if not isinstance(M, np.ndarray):
            return str(M)
        elif M.ndim == 1:
            inner = " & ".join([f"{x:.{precision}f}" for x in M])
            return f"\\begin{{bmatrix}} {inner} \\end{{bmatrix}}"
        else:
            rows = " \\\\ ".join([" & ".join([f"{x:.{precision}f}" for x in row]) for row in M])
            return f"\\begin{{bmatrix}} {rows} \\end{{bmatrix}}"

    def power_method(B, num_iters=1000, tol=1e-10):
        n = B.shape[0]
        v = np.ones(n)
        v = v / np.linalg.norm(v)
        lam_prev = 0
        for i in range(num_iters):
            v_new = B @ v
            lam = np.linalg.norm(v_new)
            if lam == 0:
                return 0, v
            v_new = v_new / lam
            lam_rayleigh = v_new.T @ B @ v_new
            if np.abs(lam_rayleigh - lam_prev) < tol:
                v = v_new
                break
            v = v_new
            lam_prev = lam_rayleigh
        return lam_rayleigh, v

    A = np.array(A_input, dtype=float)
    n, m = A.shape
    
    md = []
    md.append("## ❖ TÌM PHÂN TÍCH SVD RÚT GỌN BẰNG LŨY THỪA VÀ XUỐNG THANG")
    md.append("---\n")
    md.append(f"### I. MA TRẬN BAN ĐẦU\n")
    md.append(f"$$ A_1 = A = {matrix_to_latex(A, precision=4)} $$\n")

    A_k = A.copy()
    rank = min(n, m)
    
    U_cols = []
    S_vals = []
    V_cols = []
    
    md.append(f"---\n### II. QUÁ TRÌNH LẶP VÀ XUỐNG THANG\n")

    for k in range(1, rank + 1):
        md.append(f"#### 🔹 Bước {k}:\n")
        B_k = A_k.T @ A_k
        
        lam, v = power_method(B_k)
        
        if lam < 1e-10:
            md.append(f"> **⚠️ DỪNG THUẬT TOÁN:** Giá trị riêng cực đại của $A_{k}^T A_{k}$ xấp xỉ 0 (ma trận thặng dư đã triệt tiêu).\n")
            break
            
        sigma = np.sqrt(lam)
        
        # Đồng bộ dấu vector v để kết quả luôn cố định (chuẩn hóa phần tử lớn nhất mang dấu dương)
        idx = np.argmax(np.abs(v))
        if v[idx] < 0:
            v = -v
            
        u = (A_k @ v) / sigma
        
        U_cols.append(u)
        S_vals.append(sigma)
        V_cols.append(v)
        
        md.append(f"- Tính $B_{k} = A_{k}^T A_{k}$. Áp dụng PP Lũy thừa trên $B_{k}$:")
        md.append(f"  - Trị riêng lớn nhất $\\lambda_{k} \\approx {lam:.4f}$")
        md.append(f"  - Giá trị kỳ dị $\\sigma_{k} = \\sqrt{{\\lambda_{k}}} \\approx {sigma:.4f}$")
        md.append(f"  - Véctơ kỳ dị phải $v_{k} \\approx {matrix_to_latex(v, precision=4)}$")
        md.append(f"  - Véctơ kỳ dị trái $u_{k} = \\frac{{A_{k} v_{k}}}{{\\sigma_{k}}} \\approx {matrix_to_latex(u, precision=4)}$\n")
        
        # Deflation
        A_next = A_k - sigma * np.outer(u, v)
        md.append(f"👉 **Xuống thang:** Cập nhật ma trận thặng dư $A_{{{k+1}}} = A_{k} - \\sigma_{k} u_{k} v_{k}^T$")
        md.append(f"$$ A_{{{k+1}}} = {matrix_to_latex(A_next, precision=4)} $$\n")
        
        A_k = A_next
        
    md.append(f"---\n### III. KẾT LUẬN\n")
    md.append(f"Ta thu được phân tích SVD rút gọn $A = U \\Sigma V^T$ với:\n")
    
    U = np.column_stack(U_cols)
    S = np.diag(S_vals)
    V = np.column_stack(V_cols)
    
    md.append(f"$$ U = {matrix_to_latex(U, precision=4)} $$")
    md.append(f"$$ \\Sigma = {matrix_to_latex(S, precision=4)} $$")
    md.append(f"$$ V^T = {matrix_to_latex(V.T, precision=4)} $$")
    
    # Verify
    A_reconstructed = U @ S @ V.T
    err = np.linalg.norm(A - A_reconstructed)
    check_symbol = '✅' if err < 1e-6 else '⚠️'
    md.append(f"\n> **KIỂM TRA LẠI:** $||A - U \\Sigma V^T||_F = {err:.2e}$ {check_symbol}")

    display(Markdown('\n'.join(md)))

A = np.array([
    [3, 3, 7],
    [3, 9, 10],
    [8, 4, 6],
    [2, 10, 9]
])

SVD_Reduced(A)
"""

source_lines = [line + '\n' for line in new_source.split('\n')]
source_lines[-1] = source_lines[-1][:-1] # remove last newline

# Modify cells: keep markdown title, replace first code cell, remove the rest
nb['cells'][1]['source'] = source_lines
nb['cells'][1]['outputs'] = []

# Truncate any other cells
nb['cells'] = nb['cells'][:2]

with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print("Updated SVD notebook successfully!")
