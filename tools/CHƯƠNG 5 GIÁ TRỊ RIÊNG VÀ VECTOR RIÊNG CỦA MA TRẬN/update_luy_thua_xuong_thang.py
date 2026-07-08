import json
import os

dir_path = "d:/code/Uni/On_thi_cuoi_ky/Giải tích số/scripts/CHƯƠNG 5 GIÁ TRỊ RIÊNG VÀ VECTOR RIÊNG CỦA MA TRẬN"

# ==========================================
# 1. PHƯƠNG PHÁP LŨY THỪA
# ==========================================
code_luy_thua = r"""import numpy as np
from IPython.display import display, Math

def Power_Method_L2(A_input, x0_input=None, tol=1e-5, max_iter=20):
    def matrix_to_latex(M, precision=4):
        if not isinstance(M, np.ndarray): return str(M)
        elif M.ndim == 1:
            inner = " \\\\ ".join([f"{x:.{precision}f}" for x in M])
            return f"\\begin{{bmatrix}} {inner} \\end{{bmatrix}}"
        else:
            rows = " \\\\ ".join([" & ".join([f"{x:.{precision}f}" for x in row]) for row in M])
            return f"\\begin{{bmatrix}} {rows} \\end{{bmatrix}}"

    A = np.array(A_input, dtype=float)
    n = A.shape[0]
    
    if x0_input is None:
        x_k = np.ones(n)
    else:
        x_k = np.array(x0_input, dtype=float).flatten()
        
    # Chuẩn hóa x0 về chuẩn 2 bằng 1
    x_k = x_k / np.linalg.norm(x_k, 2)
        
    print("="*60)
    print("PHƯƠNG PHÁP LŨY THỪA TÌM TRỊ RIÊNG TRỘI (CHUẨN 2 = 1)")
    print("="*60)
    
    lam_prev = 0
    
    for k in range(1, max_iter + 1):
        print(f"\n--- BƯỚC {k} ---")
        
        # Tính y_k = A * x_{k-1}
        y_k = A @ x_k
        
        # Trị riêng xấp xỉ theo tỉ số Rayleigh: lambda = x^T * y (vì x^T * x = 1)
        lam_k = x_k.T @ y_k
        
        # Chuẩn hóa L2
        norm_y = np.linalg.norm(y_k, 2)
        x_new = y_k / norm_y
        
        # Đồng bộ dấu để vector không bị lật dấu liên tục nếu trị riêng âm
        idx = np.argmax(np.abs(x_new))
        if x_new[idx] < 0:
            x_new = -x_new
            norm_y = -norm_y
        
        display(Math(f"y_{{{k}}} = A x_{{{k-1}}} = {matrix_to_latex(y_k, precision=5)}"))
        display(Math(f"\\lambda_{{{k}}} = x_{{{k-1}}}^T y_{{{k}}} \\approx {lam_k:.5f}"))
        display(Math(f"x_{{{k}}} = \\frac{{y_{{{k}}}}}{{\\|y_{{{k}}}\\|_2}} = {matrix_to_latex(x_new, precision=5)}"))
        
        sai_so = np.abs(lam_k - lam_prev)
        print(f"> Sai số trị riêng: |λ_k - λ_prev| = {sai_so:.5e}")
        
        if sai_so < tol:
            print(f"\n✅ HỘI TỤ SAU {k} BƯỚC LẶP!")
            break
            
        x_k = x_new
        lam_prev = lam_k
        
    print("\n" + "="*60)
    print("KẾT LUẬN CÂU A:")
    display(Math(f"\\lambda_{{max}} \\approx {lam_k:.5f}"))
    display(Math(f"v_{{max}} \\approx {matrix_to_latex(x_k, precision=5)}"))

# Ma trận đề bài Câu 2
A = np.array([
    [4.0327, 2.6090, 2.3283, 4.8132, 2.8724],
    [2.6090, 3.6586, 4.6534, 3.5740, 3.9131],
    [2.3283, 4.6534, 6.7322, 3.4631, 5.0275],
    [4.8132, 3.5740, 3.4631, 6.8665, 3.1182],
    [2.8724, 3.9131, 5.0275, 3.1182, 4.8099]
], dtype=float)

# Véctơ xấp xỉ ban đầu (thường chọn vector [1,1,1,1,1] rồi tự động chuẩn hóa trong hàm)
x0 = np.ones(5)

Power_Method_L2(A, x0, tol=1e-4, max_iter=20)
"""

# ==========================================
# 2. PHƯƠNG PHÁP XUỐNG THANG
# ==========================================
code_xuong_thang = r"""import numpy as np
from IPython.display import display, Math

def Power_Method_L2_Silent(A_input, x0_input=None, tol=1e-5, max_iter=50):
    A = np.array(A_input, dtype=float)
    n = A.shape[0]
    if x0_input is None: x_k = np.ones(n)
    else: x_k = np.array(x0_input, dtype=float).flatten()
    x_k = x_k / np.linalg.norm(x_k, 2)
    lam_prev = 0
    for k in range(1, max_iter + 1):
        y_k = A @ x_k
        lam_k = x_k.T @ y_k
        norm_y = np.linalg.norm(y_k, 2)
        x_new = y_k / norm_y
        idx = np.argmax(np.abs(x_new))
        if x_new[idx] < 0: x_new = -x_new
        sai_so = np.abs(lam_k - lam_prev)
        if sai_so < tol: break
        x_k = x_new
        lam_prev = lam_k
    return lam_k, x_k

def Deflation_L2(A_input, x0_input=None, tol=1e-4, max_iter=50):
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
    
    if x0_input is None: x0 = np.ones(n)
    else: x0 = np.array(x0_input, dtype=float).flatten()
        
    print("="*60)
    print("PHƯƠNG PHÁP XUỐNG THANG (GIẢI CÂU B)")
    print("="*60)
    
    print("\nBước 1: Tìm trị riêng và véctơ riêng trội nhất của A (Dùng kết quả câu a)")
    lam1, v1 = Power_Method_L2_Silent(A, x0, tol, max_iter)
    display(Math(f"\\lambda_1 \\approx {lam1:.5f}"))
    display(Math(f"v_1 \\approx {matrix_to_latex(v1, precision=5)}"))
    
    print("\nBước 2: Chọn véctơ phụ x và xây dựng ma trận xuống thang A_1")
    print("Do v_1 đã có chuẩn 2 bằng 1 (||v_1||_2 = 1), ta chọn luôn véctơ phụ x = v_1")
    
    x = v1
    display(Math(f"x = v_1 = {matrix_to_latex(x, precision=5)}"))
    
    print("Công thức xuống thang Hotelling:")
    A1 = A - lam1 * np.outer(v1, x)
    display(Math(f"A_1 = A - \\lambda_1 v_1 x^T = {matrix_to_latex(A1, precision=4)}"))
    
    print("\n" + "="*60)
    print("KẾT LUẬN CÂU B:")
    print("Ma trận A_1 chứa tất cả các trị riêng của A (trừ trị riêng trội nhất) là:")
    display(Math(f"A_1 = {matrix_to_latex(A1, precision=4)}"))
    print("="*60)

# Ma trận đề bài Câu 2
A = np.array([
    [4.0327, 2.6090, 2.3283, 4.8132, 2.8724],
    [2.6090, 3.6586, 4.6534, 3.5740, 3.9131],
    [2.3283, 4.6534, 6.7322, 3.4631, 5.0275],
    [4.8132, 3.5740, 3.4631, 6.8665, 3.1182],
    [2.8724, 3.9131, 5.0275, 3.1182, 4.8099]
], dtype=float)

# Gọi hàm
Deflation_L2(A, tol=1e-4, max_iter=50)
"""

def update_notebook(filename, new_code):
    filepath = os.path.join(dir_path, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        nb = json.load(f)
        
    source_lines = [line + '\n' for line in new_code.split('\n')]
    source_lines[-1] = source_lines[-1][:-1]
    
    nb['cells'][1]['source'] = source_lines
    nb['cells'][1]['outputs'] = []
    
    nb['cells'] = nb['cells'][:2]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)

update_notebook("Phương pháp Lũy thừa.ipynb", code_luy_thua)
update_notebook("Phương pháp Xuống thang.ipynb", code_xuong_thang)

print("Đã cập nhật xong Lũy thừa và Xuống thang cho bài thi!")
