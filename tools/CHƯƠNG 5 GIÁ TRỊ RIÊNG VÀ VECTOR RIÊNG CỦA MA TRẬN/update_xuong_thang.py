import json
import os

notebook_path = "d:/code/Uni/On_thi_cuoi_ky/Giải tích số/scripts/CHƯƠNG 5 GIÁ TRỊ RIÊNG VÀ VECTOR RIÊNG CỦA MA TRẬN/Phương pháp Xuống thang.ipynb"

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

new_source = r"""import numpy as np
from IPython.display import display, Math

def Power_Method(A_input, x0_input=None, tol=1e-5, max_iter=20, print_steps=False):
    def matrix_to_latex(M, precision=4):
        if not isinstance(M, np.ndarray): return str(M)
        elif M.ndim == 1:
            inner = " \\\\ ".join([f"{x:.{precision}f}" for x in M])
            return f"\\begin{{bmatrix}} {inner} \\end{{bmatrix}}^T"
        else:
            rows = " \\\\ ".join([" & ".join([f"{x:.{precision}f}" for x in row]) for row in M])
            return f"\\begin{{bmatrix}} {rows} \\end{{bmatrix}}"

    A = np.array(A_input, dtype=float)
    n = A.shape[0]
    
    if x0_input is None:
        x_k = np.ones(n)
    else:
        x_k = np.array(x0_input, dtype=float).flatten()
        
    lam_prev = 0
    
    for k in range(1, max_iter + 1):
        y_k = A @ x_k
        idx = np.argmax(np.abs(y_k))
        lam_k = y_k[idx] / x_k[idx] if x_k[idx] != 0 else np.linalg.norm(y_k)
        c = y_k[idx]
        x_new = y_k / c
        
        if print_steps:
            display(Math(f"y_{{{k}}} = A x_{{{k-1}}} = {matrix_to_latex(y_k, precision=5)}"))
            display(Math(f"\\lambda_{{{k}}} \\approx {lam_k:.5f}"))
            display(Math(f"x_{{{k}}} = \\frac{{1}}{{{c:.5f}}} y_{{{k}}} = {matrix_to_latex(x_new, precision=5)}"))
        
        sai_so = np.abs(lam_k - lam_prev)
        if sai_so < tol:
            break
            
        x_k = x_new
        lam_prev = lam_k
        
    return lam_k, x_k

def Deflation(A_input, x0_input=None, tol=1e-5, max_iter=20):
    def matrix_to_latex(M, precision=4):
        if not isinstance(M, np.ndarray): return str(M)
        elif M.ndim == 1:
            inner = " \\\\ ".join([f"{x:.{precision}f}" for x in M])
            return f"\\begin{{bmatrix}} {inner} \\end{{bmatrix}}^T"
        else:
            rows = " \\\\ ".join([" & ".join([f"{x:.{precision}f}" for x in row]) for row in M])
            return f"\\begin{{bmatrix}} {rows} \\end{{bmatrix}}"

    A = np.array(A_input, dtype=float)
    n = A.shape[0]
    
    if x0_input is None:
        x0 = np.ones(n)
    else:
        x0 = np.array(x0_input, dtype=float).flatten()
        
    print("="*60)
    print("PHƯƠNG PHÁP XUỐNG THANG (TÌM TRỊ RIÊNG THỨ 2)")
    print("="*60)
    
    print("\nBước 1: Tìm trị riêng và véctơ riêng trội nhất của A (Dùng pp lũy thừa)")
    lam1, v1 = Power_Method(A, x0, tol, max_iter)
    display(Math(f"\\lambda_1 \\approx {lam1:.5f}"))
    display(Math(f"v_1 \\approx {matrix_to_latex(v1, precision=5)}"))
    
    print("\nBước 2: Chọn véctơ phụ x và xây dựng ma trận xuống thang B")
    # Chọn x sao cho v1^T x = 1. Thông thường x = v1 / ||v1||^2
    x = v1 / (v1.T @ v1)
    display(Math(f"x = \\frac{{v_1}}{{\\|v_1\\|^2}} = {matrix_to_latex(x, precision=5)}"))
    
    B = A - lam1 * np.outer(v1, x)
    display(Math(f"B = A - \\lambda_1 v_1 x^T = {matrix_to_latex(B, precision=5)}"))
    
    print("\nBước 3: Tìm trị riêng trội của B (Dùng pp lũy thừa)")
    lam2, u2 = Power_Method(B, x0, tol, max_iter)
    display(Math(f"\\lambda_2 \\approx {lam2:.5f}"))
    display(Math(f"u_2 \\approx {matrix_to_latex(u2, precision=5)}"))
    
    print("\nBước 4: Khôi phục véctơ riêng v_2 của A")
    # v2 = (lam2 - lam1)u2 + lam1(x^T u2)v1
    v2 = (lam2 - lam1) * u2 + lam1 * (x.T @ u2) * v1
    # Chuẩn hóa v2 giống v1 (chia cho phần tử lớn nhất)
    v2 = v2 / v2[np.argmax(np.abs(v2))]
    
    display(Math(f"v_2 = (\\lambda_2 - \\lambda_1) u_2 + \\lambda_1 (x^T u_2) v_1"))
    
    print("\n" + "="*60)
    print("KẾT LUẬN:")
    display(Math(f"\\lambda_2 \\approx {lam2:.5f}"))
    display(Math(f"v_2 \\approx {matrix_to_latex(v2, precision=5)}"))
    print("="*60)

A = np.array([
    [4.0327, 2.6090, 2.3283, 4.8132, 2.8724],
    [2.6090, 3.6586, 4.6534, 3.5740, 3.9131],
    [2.3283, 4.6534, 6.7322, 3.4631, 5.0275],
    [4.8132, 3.5740, 3.4631, 6.8665, 3.1182],
    [2.8724, 3.9131, 5.0275, 3.1182, 4.8099]
], dtype=float)

# Dùng vector khởi tạo np.ones() tự động
Deflation(A, tol=1e-4, max_iter=50)
"""

source_lines = [line + '\n' for line in new_source.split('\n')]
source_lines[-1] = source_lines[-1][:-1]

nb['cells'][1]['source'] = source_lines
nb['cells'][1]['outputs'] = []

# Truncate any old additional cells
nb['cells'] = nb['cells'][:2]

with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)
