import json
import os

notebook_path = "d:/code/Uni/On_thi_cuoi_ky/Giải tích số/scripts/CHƯƠNG 5 GIÁ TRỊ RIÊNG VÀ VECTOR RIÊNG CỦA MA TRẬN/Giá trị kỳ dị SVD (Lớn nhất).ipynb"

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

new_source = r"""import numpy as np
from IPython.display import display, Math, HTML

def SVD_Reduced(A_input):
    def matrix_to_latex(M, precision=4):
        if not isinstance(M, np.ndarray):
            return str(M)
        elif M.ndim == 1:
            inner = " & ".join([f"{x:.{precision}f}" for x in M])
            return f"\\begin{{bmatrix}} {inner} \\end{{bmatrix}}^T"
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
    
    print("="*60)
    print("PHÂN TÍCH SVD RÚT GỌN BẰNG LŨY THỪA VÀ XUỐNG THANG")
    print("="*60)
    
    display(Math(f"A_1 = {matrix_to_latex(A, precision=4)}"))

    A_k = A.copy()
    rank = min(n, m)
    
    U_cols = []
    S_vals = []
    V_cols = []
    
    for k in range(1, rank + 1):
        print(f"\n--- BƯỚC {k} ---")
        B_k = A_k.T @ A_k
        
        lam, v = power_method(B_k)
        
        if lam < 1e-10:
            print(f"⚠️ DỪNG THUẬT TOÁN: Giá trị riêng cực đại của A_k^T A_k xấp xỉ 0 (ma trận thặng dư đã triệt tiêu).")
            break
            
        sigma = np.sqrt(lam)
        
        # Đồng bộ dấu vector v
        idx = np.argmax(np.abs(v))
        if v[idx] < 0:
            v = -v
            
        u = (A_k @ v) / sigma
        
        U_cols.append(u)
        S_vals.append(sigma)
        V_cols.append(v)
        
        print(f"- Trị riêng lớn nhất: λ_{k} ≈ {lam:.4f}")
        print(f"- Giá trị kỳ dị: σ_{k} ≈ {sigma:.4f}")
        display(Math(f"v_{k} = {matrix_to_latex(v, precision=4)}"))
        display(Math(f"u_{k} = \\frac{{A_{k} v_{k}}}{{\\sigma_{k}}} = {matrix_to_latex(u, precision=4)}"))
        
        # Deflation
        A_next = A_k - sigma * np.outer(u, v)
        print(f"\n👉 Xuống thang: Cập nhật ma trận thặng dư A_{k+1}")
        display(Math(f"A_{{{k+1}}} = {matrix_to_latex(A_next, precision=4)}"))
        
        A_k = A_next
        
    print("\n" + "="*60)
    print("KẾT LUẬN: PHÂN TÍCH SVD RÚT GỌN A = U * Σ * V^T")
    print("="*60)
    
    U = np.column_stack(U_cols)
    S = np.diag(S_vals)
    V = np.column_stack(V_cols)
    
    display(Math(f"U = {matrix_to_latex(U, precision=4)}"))
    display(Math(f"\\Sigma = {matrix_to_latex(S, precision=4)}"))
    display(Math(f"V^T = {matrix_to_latex(V.T, precision=4)}"))
    
    A_reconstructed = U @ S @ V.T
    err = np.linalg.norm(A - A_reconstructed)
    print(f"\nKiểm tra lại sai số ||A - U Σ V^T||_F = {err:.2e}")

A = np.array([
    [3,  3,  8],
    [3,  9,  4],
    [7, 10,  6],
    [0,  4, -2]
], dtype=float)

SVD_Reduced(A)
"""

source_lines = [line + '\n' for line in new_source.split('\n')]
source_lines[-1] = source_lines[-1][:-1]

nb['cells'][1]['source'] = source_lines
nb['cells'][1]['outputs'] = []

with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print("Đã đổi sang display(Math) thành công!")
