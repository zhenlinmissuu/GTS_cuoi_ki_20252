import json
import os

dir_path = "d:/code/Uni/On_thi_cuoi_ky/Giải tích số/scripts/CHƯƠNG 4 GIẢI HỆ ĐẠI SỐ TUYẾN TÍNH & TÌM MA TRẬN NGHỊCH ĐẢO"
filepath = os.path.join(dir_path, "Lặp Jacobi (Ax=b).ipynb")

new_source = r"""import numpy as np
from IPython.display import display, Math, Markdown

def Jacobi_Method(A_input, b_input, x0_input=None, num_iters=4):
    def matrix_to_latex(M, precision=4):
        if not isinstance(M, np.ndarray): return str(M)
        elif M.ndim == 1:
            inner = " \\\\ ".join([f"{x:.{precision}f}" for x in M])
            return f"\\begin{{bmatrix}} {inner} \\end{{bmatrix}}^T"
        else:
            rows = " \\\\ ".join([" & ".join([f"{x:.{precision}f}" for x in row]) for row in M])
            return f"\\begin{{bmatrix}} {rows} \\end{{bmatrix}}"

    A = np.array(A_input, dtype=float)
    b = np.array(b_input, dtype=float).flatten()
    n = len(b)
    
    if x0_input is None:
        x_k = np.zeros(n)
    else:
        x_k = np.array(x0_input, dtype=float).flatten()
        
    print("="*60)
    print("PHƯƠNG PHÁP LẶP JACOBI GIẢI HỆ Ax = b")
    print("="*60)
    
    # Kiểm tra chéo trội hàng
    is_diagonally_dominant = True
    for i in range(n):
        sum_off_diag = np.sum(np.abs(A[i])) - np.abs(A[i, i])
        if np.abs(A[i, i]) <= sum_off_diag:
            is_diagonally_dominant = False
            break
            
    if is_diagonally_dominant:
        print("\n✅ Ma trận A là ma trận chéo trội hàng ngặt. Thuật toán chắc chắn hội tụ!")
    else:
        print("\n⚠️ Ma trận A KHÔNG chéo trội hàng ngặt. Thuật toán có thể không hội tụ.")

    # Biến đổi A x = b thành x = B x + d
    D = np.diag(np.diag(A))
    L_plus_U = A - D
    
    D_inv = np.linalg.inv(D)
    B = -D_inv @ L_plus_U
    d = D_inv @ b
    
    print("\nBước 1: Chuyển hệ Ax = b về dạng x = Bx + d")
    display(Math(f"B = -D^{{-1}}(L+U) = {matrix_to_latex(B, precision=4)}"))
    display(Math(f"d = D^{{-1}}b = {matrix_to_latex(d, precision=4)}"))
    
    q = np.linalg.norm(B, np.inf)
    display(Math(f"\\text{{Chuẩn vô cùng của B: }} q = ||B||_\\infty = {q:.4f}"))
    
    print(f"\nBước 2: Quá trình lặp (tính đến bước k = {num_iters})")
    
    # Lưu lịch sử để hiển thị
    history = [x_k.copy()]
    
    for k in range(1, num_iters + 1):
        # Công thức Jacobi: x^{(k)} = B * x^{(k-1)} + d
        x_next = B @ x_k + d
        history.append(x_next.copy())
        x_k = x_next
        
    # In bảng kết quả bằng Markdown
    md = ["| $k$ | " + " | ".join([f"$x_{i+1}$" for i in range(n)]) + " | Sai số $||x^{(k)} - x^{(k-1)}||_\\infty$ |",
          "|---|" + "|".join(["---"] * n) + "|---|"]
          
    for k in range(len(history)):
        row_vals = history[k]
        val_str = " | ".join([f"{v:.7f}" for v in row_vals])
        if k == 0:
            md.append(f"| {k} | {val_str} | - |")
        else:
            diff = np.linalg.norm(history[k] - history[k-1], np.inf)
            md.append(f"| {k} | {val_str} | {diff:.7f} |")
            
    display(Markdown('\n'.join(md)))
    
    print("\nBước 3: Kết luận")
    display(Math(f"X^{{({num_iters})}} = {matrix_to_latex(x_k, precision=7)}"))
    diff_final = np.linalg.norm(history[-1] - history[-2], np.inf)
    sai_so_hau_nghiem = (q / (1 - q)) * diff_final if q < 1 else diff_final
    print(f"Sai số hậu nghiệm tại bước {num_iters}: {sai_so_hau_nghiem:.7e}")

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

Jacobi_Method(A, b, x0, num_iters=4)
"""

nb = {
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Phương pháp Lặp Jacobi giải hệ Ax = b\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [line + '\n' for line in new_source.split('\n')]
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

# Remove trailing newline from last line of source
nb['cells'][1]['source'][-1] = nb['cells'][1]['source'][-1].rstrip('\n')

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)
    
print("Tạo file thành công!")
