import os
import json
import numpy as np

base_dir = "d:/code/Uni/On_thi_cuoi_ky/Giải tích số/scripts/CHƯƠNG 4 GIẢI HỆ ĐẠI SỐ TUYẾN TÍNH & TÌM MA TRẬN NGHỊCH ĐẢO"
folder_name = "Lặp Jacobi - Lặp Đơn"
target_dir = os.path.join(base_dir, folder_name)

os.makedirs(target_dir, exist_ok=True)

# Helper for notebook creation
def create_notebook(filepath, title, source_code):
    nb = {
     "cells": [
      {
       "cell_type": "markdown",
       "metadata": {},
       "source": [f"### {title}\n"]
      },
      {
       "cell_type": "code",
       "execution_count": None,
       "metadata": {},
       "outputs": [],
       "source": [line + '\n' for line in source_code.split('\n')]
      }
     ],
     "metadata": {
      "kernelspec": {
       "display_name": "Python 3",
       "language": "python",
       "name": "python3"
      },
      "language_info": {
       "name": "python",
       "version": "3.13.7"
      }
     },
     "nbformat": 4,
     "nbformat_minor": 4
    }
    nb['cells'][1]['source'][-1] = nb['cells'][1]['source'][-1].rstrip('\n')
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)

# ==============================================================================
# 1. Lặp Đơn (x = Bx + d)
# ==============================================================================
code_lap_don = r"""import numpy as np
from IPython.display import display, Math, Markdown

def matrix_to_latex(M, precision=4):
    if not isinstance(M, np.ndarray): return str(M)
    elif M.ndim == 1:
        inner = " \\\\ ".join([f"{x:.{precision}f}" for x in M])
        return f"\\begin{{bmatrix}} {inner} \\end{{bmatrix}}^T"
    else:
        rows = " \\\\ ".join([" & ".join([f"{x:.{precision}f}" for x in row]) for row in M])
        return f"\\begin{{bmatrix}} {rows} \\end{{bmatrix}}"

def Lap_Don_x_Bx_d(B_input, d_input, x0_input=None, num_iters=None, epsilon=None, p_norm=np.inf):
    B = np.array(B_input, dtype=float)
    d = np.array(d_input, dtype=float).flatten()
    n = len(d)
    
    if x0_input is None: x_k = np.zeros(n)
    else: x_k = np.array(x0_input, dtype=float).flatten()
    
    md = []
    md.append("## ❖ PHƯƠNG PHÁP LẶP ĐƠN (Giải hệ $x = Bx + d$)")
    md.append("---\n")
    
    md.append("### I. ĐẦU VÀO VÀ ĐIỀU KIỆN HỘI TỤ")
    md.append(f"$$ B = {matrix_to_latex(B)} $$")
    md.append(f"$$ d = {matrix_to_latex(d)} $$\n")
    
    q = np.linalg.norm(B, p_norm)
    norm_name = "Chuẩn vô cùng" if p_norm == np.inf else f"Chuẩn {p_norm}"
    md.append(f"- **{norm_name} của B:** $q = ||B|| = {q:.5f}$")
    
    if q < 1:
        md.append("- **Kết luận:** Vì $q < 1$, thuật toán lặp đơn **chắc chắn hội tụ**.")
    else:
        md.append("- **Cảnh báo:** Vì $q \ge 1$, thuật toán **chưa chắc chắn hội tụ** (Cần kiểm tra chuẩn khác hoặc giá trị riêng).")
        
    md.append("\n---\n### II. BẢNG QUÁ TRÌNH LẶP")
    
    table = ["| $k$ | " + " | ".join([f"$x_{i+1}$" for i in range(n)]) + " | Sai số $||x^{(k)} - x^{(k-1)}||$ |",
             "|---|" + "|".join(["---"] * n) + "|---|"]
             
    history = [x_k.copy()]
    k = 0
    while True:
        if k == 0:
            row_str = " | ".join([f"{v:.5f}" for v in x_k])
            table.append(f"| {k} | {row_str} | - |")
        else:
            diff = np.linalg.norm(history[k] - history[k-1], p_norm)
            row_str = " | ".join([f"{v:.5f}" for v in x_k])
            table.append(f"| {k} | {row_str} | {diff:.5f} |")
            
            stop_eps = (epsilon is not None) and (diff <= epsilon or (q/(1-q))*diff <= epsilon if q < 1 else False)
            stop_iter = (num_iters is not None) and (k >= num_iters)
            if stop_eps or stop_iter:
                break
                
        x_next = B @ x_k + d
        history.append(x_next.copy())
        x_k = x_next
        k += 1
        
    md.extend(table)
    
    md.append("\n---\n### III. KẾT LUẬN")
    md.append(f"Hệ dừng lại tại bước lặp $k = {k}$. Nghiệm gần đúng là:")
    md.append(f"$$ X^{{({k})}} \\approx {matrix_to_latex(x_k, precision=5)} $$")
    
    diff_final = np.linalg.norm(history[-1] - history[-2], p_norm)
    if q < 1:
        sai_so_hau_nghiem = (q / (1 - q)) * diff_final
        md.append(f"**Sai số hậu nghiệm:** $\\frac{{q}}{{1-q}} ||x^{{({k})}} - x^{{({k-1})}}|| = {sai_so_hau_nghiem:.5e}$")
    else:
        md.append(f"**Sai số thực tế (khoảng cách 2 bước cuối):** $||x^{{({k})}} - x^{{({k-1})}}|| = {diff_final:.5e}$")
        
    display(Markdown('\n'.join(md)))

# NHẬP LIỆU
B = np.array([
    [0.0, 0.1, 0.2],
    [0.1, 0.0, 0.3],
    [0.2, 0.3, 0.0]
], dtype=float)

d = np.array([1, 2, 3], dtype=float)
x0 = np.array([0, 0, 0], dtype=float)

Lap_Don_x_Bx_d(B, d, x0, num_iters=5, epsilon=None)
"""

# ==============================================================================
# 2. Lặp Jacobi (Ax = b)
# ==============================================================================
code_jacobi = r"""import numpy as np
from IPython.display import display, Math, Markdown

def matrix_to_latex(M, precision=4):
    if not isinstance(M, np.ndarray): return str(M)
    elif M.ndim == 1:
        inner = " \\\\ ".join([f"{x:.{precision}f}" for x in M])
        return f"\\begin{{bmatrix}} {inner} \\end{{bmatrix}}^T"
    else:
        rows = " \\\\ ".join([" & ".join([f"{x:.{precision}f}" for x in row]) for row in M])
        return f"\\begin{{bmatrix}} {rows} \\end{{bmatrix}}"

def Jacobi_Ax_b(A_input, b_input, x0_input=None, num_iters=None, epsilon=None):
    A = np.array(A_input, dtype=float)
    b = np.array(b_input, dtype=float).flatten()
    n = len(b)
    
    if x0_input is None: x_k = np.zeros(n)
    else: x_k = np.array(x0_input, dtype=float).flatten()
    
    md = []
    md.append("## ❖ PHƯƠNG PHÁP LẶP JACOBI (Giải hệ $Ax = b$)")
    md.append("---\n")
    
    md.append("### I. CHÉO TRỘI VÀ BIẾN ĐỔI")
    md.append(f"$$ A = {matrix_to_latex(A)} $$")
    
    # Kiểm tra chéo trội hàng
    is_diagonally_dominant = True
    for i in range(n):
        if np.abs(A[i, i]) <= np.sum(np.abs(A[i])) - np.abs(A[i, i]):
            is_diagonally_dominant = False
            break
            
    if is_diagonally_dominant:
        md.append("- **Đánh giá:** Ma trận A là ma trận **chéo trội hàng ngặt**. Thuật toán Jacobi **chắc chắn hội tụ**!")
    else:
        md.append("- **Cảnh báo:** Ma trận A **KHÔNG** chéo trội hàng ngặt. Thuật toán có thể phân kỳ.")

    # Biến đổi
    D = np.diag(np.diag(A))
    L_plus_U = A - D
    D_inv = np.linalg.inv(D)
    B = -D_inv @ L_plus_U
    d = D_inv @ b
    
    md.append("Chuyển hệ phương trình về dạng $x = Bx + d$ với $B = -D^{-1}(L+U)$ và $d = D^{-1}b$:")
    md.append(f"$$ B = {matrix_to_latex(B)} $$")
    md.append(f"$$ d = {matrix_to_latex(d)} $$\n")
    
    q = np.linalg.norm(B, np.inf)
    md.append(f"- **Chuẩn vô cùng của B:** $q = ||B||_\\infty = {q:.5f}$")
    
    md.append("\n---\n### II. BẢNG QUÁ TRÌNH LẶP")
    
    table = ["| $k$ | " + " | ".join([f"$x_{i+1}$" for i in range(n)]) + " | Sai số $||x^{(k)} - x^{(k-1)}||_\\infty$ |",
             "|---|" + "|".join(["---"] * n) + "|---|"]
             
    history = [x_k.copy()]
    k = 0
    while True:
        if k == 0:
            row_str = " | ".join([f"{v:.5f}" for v in x_k])
            table.append(f"| {k} | {row_str} | - |")
        else:
            diff = np.linalg.norm(history[k] - history[k-1], np.inf)
            row_str = " | ".join([f"{v:.5f}" for v in x_k])
            table.append(f"| {k} | {row_str} | {diff:.5f} |")
            
            stop_eps = (epsilon is not None) and (diff <= epsilon or (q/(1-q))*diff <= epsilon if q < 1 else False)
            stop_iter = (num_iters is not None) and (k >= num_iters)
            if stop_eps or stop_iter:
                break
                
        # Lặp Jacobi thực chất là lặp đơn trên dạng x = Bx+d
        x_next = B @ x_k + d
        history.append(x_next.copy())
        x_k = x_next
        k += 1
        
    md.extend(table)
    
    md.append("\n---\n### III. KẾT LUẬN")
    md.append(f"Hệ dừng lại tại bước lặp $k = {k}$. Nghiệm gần đúng là:")
    md.append(f"$$ X^{{({k})}} \\approx {matrix_to_latex(x_k, precision=5)} $$")
    
    diff_final = np.linalg.norm(history[-1] - history[-2], np.inf)
    if q < 1:
        sai_so_hau_nghiem = (q / (1 - q)) * diff_final
        md.append(f"**Sai số hậu nghiệm:** $\\frac{{q}}{{1-q}} ||x^{{({k})}} - x^{{({k-1})}}||_\\infty = {sai_so_hau_nghiem:.5e}$")
    else:
        md.append(f"**Sai số thực tế (khoảng cách 2 bước cuối):** $||x^{{({k})}} - x^{{({k-1})}}||_\\infty = {diff_final:.5e}$")
        
    display(Markdown('\n'.join(md)))

# Dữ liệu từ Đề bài
A = np.array([
    [10.5, 1, 0.4, 0.7, -0.5, 0.9, -0.9],
    [-0.5, 10.7, 0.8, -0.5, 0.2, -0.4, 0.1],
    [0.4, 0.2, 13, 0.7, -0.1, 0.5, 0.6],
    [0.3, -0.6, 0.1, 12.5, -0.3, 0.5, 0.9],
    [-0.7, 0.5, -0.8, 0.9, 14.7, -0.3, -0.8],
    [-0.8, -0.5, -0.7, -0.3, 0.2, 15.1, 0.1],
    [0, 0, -0.5, -0.6, 0.1, -0.9, 15.9]
], dtype=float)

b = np.array([-10, -3, -7, 6, -4, 1, -7], dtype=float)
x0 = np.zeros(7) # Theo đề X^0 = 0

Jacobi_Ax_b(A, b, x0, num_iters=4, epsilon=None)
"""

# ==============================================================================
# 3. Lặp Jacobi (Đổi dòng tạo chéo trội)
# ==============================================================================
code_jacobi_doi_dong = r"""import numpy as np
import itertools
from IPython.display import display, Math, Markdown

def matrix_to_latex(M, precision=4):
    if not isinstance(M, np.ndarray): return str(M)
    elif M.ndim == 1:
        inner = " \\\\ ".join([f"{x:.{precision}f}" for x in M])
        return f"\\begin{{bmatrix}} {inner} \\end{{bmatrix}}^T"
    else:
        rows = " \\\\ ".join([" & ".join([f"{x:.{precision}f}" for x in row]) for row in M])
        return f"\\begin{{bmatrix}} {rows} \\end{{bmatrix}}"

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

def Jacobi_Ax_b_Permute(A_input, b_input, x0_input=None, num_iters=None, epsilon=None):
    A_origin = np.array(A_input, dtype=float)
    b_origin = np.array(b_input, dtype=float).flatten()
    n = len(b_origin)
    
    if x0_input is None: x_k = np.zeros(n)
    else: x_k = np.array(x0_input, dtype=float).flatten()
    
    md = []
    md.append("## ❖ LẶP JACOBI (CÓ TỰ ĐỘNG ĐỔI DÒNG TẠO CHÉO TRỘI)")
    md.append("---\n")
    
    md.append("### I. TỰ ĐỘNG KIỂM TRA VÀ ĐỔI DÒNG")
    md.append("Hệ ban đầu:")
    md.append(f"$$ A_{{ban\_dau}} = {matrix_to_latex(A_origin)} \\quad b_{{ban\_dau}} = {matrix_to_latex(b_origin)} $$\n")
    
    is_dom, A, b, perm = Check_And_Permute_Dominant(A_origin, b_origin)
    
    if is_dom and perm != tuple(range(n)):
        md.append(f"**✅ ĐÃ ĐỔI DÒNG THÀNH CÔNG!** Thứ tự các hàng mới: {perm}")
        md.append(f"$$ A = {matrix_to_latex(A)} \\quad b = {matrix_to_latex(b)} $$\n")
        md.append("Ma trận A mới đã **chéo trội hàng ngặt**, đảm bảo Jacobi hội tụ.")
    elif is_dom:
        md.append("**✅ Hợp lệ:** Ma trận ban đầu đã chéo trội hàng ngặt sẵn, không cần đổi dòng.")
        A, b = A_origin, b_origin
    else:
        md.append("**⚠️ Cảnh báo:** Đã thử mọi hoán vị nhưng không thể tạo ra ma trận chéo trội hàng ngặt. Thuật toán có thể phân kỳ.")
        A, b = A_origin, b_origin

    # Biến đổi
    D = np.diag(np.diag(A))
    L_plus_U = A - D
    D_inv = np.linalg.inv(D)
    B = -D_inv @ L_plus_U
    d = D_inv @ b
    
    md.append("\n---\n### II. BIẾN ĐỔI x = Bx + d")
    md.append(f"$$ B = -D^{{-1}}(L+U) = {matrix_to_latex(B)} $$")
    md.append(f"$$ d = D^{{-1}}b = {matrix_to_latex(d)} $$\n")
    
    q = np.linalg.norm(B, np.inf)
    md.append(f"- **Chuẩn vô cùng của B:** $q = ||B||_\\infty = {q:.5f}$")
    
    md.append("\n---\n### III. BẢNG QUÁ TRÌNH LẶP JACOBI")
    
    table = ["| $k$ | " + " | ".join([f"$x_{i+1}$" for i in range(n)]) + " | Sai số $||x^{(k)} - x^{(k-1)}||_\\infty$ |",
             "|---|" + "|".join(["---"] * n) + "|---|"]
             
    history = [x_k.copy()]
    k = 0
    while True:
        if k == 0:
            row_str = " | ".join([f"{v:.5f}" for v in x_k])
            table.append(f"| {k} | {row_str} | - |")
        else:
            diff = np.linalg.norm(history[k] - history[k-1], np.inf)
            row_str = " | ".join([f"{v:.5f}" for v in x_k])
            table.append(f"| {k} | {row_str} | {diff:.5f} |")
            
            stop_eps = (epsilon is not None) and (diff <= epsilon or (q/(1-q))*diff <= epsilon if q < 1 else False)
            stop_iter = (num_iters is not None) and (k >= num_iters)
            if stop_eps or stop_iter:
                break
                
        x_next = B @ x_k + d
        history.append(x_next.copy())
        x_k = x_next
        k += 1
        
    md.extend(table)
    
    md.append("\n---\n### IV. KẾT LUẬN")
    md.append(f"Hệ dừng lại tại bước lặp $k = {k}$. Nghiệm gần đúng là:")
    md.append(f"$$ X^{{({k})}} \\approx {matrix_to_latex(x_k, precision=5)} $$")
    
    diff_final = np.linalg.norm(history[-1] - history[-2], np.inf)
    if q < 1:
        sai_so_hau_nghiem = (q / (1 - q)) * diff_final
        md.append(f"**Sai số hậu nghiệm:** $\\frac{{q}}{{1-q}} ||x^{{({k})}} - x^{{({k-1})}}||_\\infty = {sai_so_hau_nghiem:.5e}$")
    else:
        md.append(f"**Sai số thực tế:** $||x^{{({k})}} - x^{{({k-1})}}||_\\infty = {diff_final:.5e}$")
        
    display(Markdown('\n'.join(md)))

# Dữ liệu mẫu (cố tình để lộn xộn để test tự động đổi dòng)
A = np.array([
    [1, 1, 10],
    [10, 2, 1],
    [1, 10, 2]
], dtype=float)

b = np.array([12, 13, 13], dtype=float)
x0 = np.zeros(3)

Jacobi_Ax_b_Permute(A, b, x0, num_iters=5)
"""

create_notebook(os.path.join(target_dir, "Lặp Đơn (x=Bx+d).ipynb"), "Phương pháp Lặp Đơn (Hệ phương trình x=Bx+d)", code_lap_don)
create_notebook(os.path.join(target_dir, "Lặp Jacobi (Ax=b).ipynb"), "Phương pháp Lặp Jacobi (Hệ phương trình Ax=b)", code_jacobi)
create_notebook(os.path.join(target_dir, "Lặp Jacobi (Đổi dòng tạo chéo trội).ipynb"), "Lặp Jacobi (Có đổi dòng tự động)", code_jacobi_doi_dong)

print("Đã tạo thư mục Lặp Jacobi - Lặp Đơn và 3 biến thể notebook thành công!")
