import os
import json
import numpy as np

base_dir = "d:/code/Uni/On_thi_cuoi_ky/Giải tích số/scripts"
chuong7_dir = os.path.join(base_dir, "CHƯƠNG 7 GIẢI PHƯƠNG TRÌNH VI PHÂN")
os.makedirs(chuong7_dir, exist_ok=True)

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
      "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
      "language_info": {"name": "python", "version": "3.13.7"}
     },
     "nbformat": 4, "nbformat_minor": 4
    }
    nb['cells'][1]['source'][-1] = nb['cells'][1]['source'][-1].rstrip('\n')
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)

# ==============================================================================
# 1. Hệ PTVP - Hình thang
# ==============================================================================
code_hinh_thang = r"""import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display, Math, Markdown

def Trapezoidal_ODE_System(F, t0, Y0, h, t_end, epsilon=1e-5, max_iter=20):
    Y0 = np.array(Y0, dtype=float)
    n_vars = len(Y0)
    
    # Tính số bước
    N = int(np.round((t_end - t0) / h))
    
    t_vals = [t0]
    Y_vals = [Y0]
    
    display(Markdown("## ❖ GIẢI HỆ PTVP BẰNG CÔNG THỨC HÌNH THANG ẨN"))
    display(Markdown("Sử dụng phương pháp Lặp Dự đoán - Hiệu chỉnh (Predictor-Corrector):"))
    display(Markdown("- **Dự đoán (Euler):** $Y_{k+1}^{(0)} = Y_k + h F(t_k, Y_k)$"))
    display(Markdown("- **Hiệu chỉnh:** $Y_{k+1}^{(j+1)} = Y_k + \\frac{h}{2} [F(t_k, Y_k) + F(t_{k+1}, Y_{k+1}^{(j)})]$"))
    
    md = ["\n### Bảng kết quả"]
    header = "| $k$ | $t_k$ | " + " | ".join([f"$y_{i+1}(t_k)$" for i in range(n_vars)]) + " |"
    md.append(header)
    md.append("|---" * (n_vars + 2) + "|")
    
    row0 = f"| 0 | {t0:.4f} | " + " | ".join([f"{val:.5f}" for val in Y0]) + " |"
    md.append(row0)
    
    Y_k = Y0
    t_k = t0
    
    for k in range(1, N + 1):
        t_next = t_k + h
        F_k = np.array(F(t_k, Y_k))
        
        # Bước dự đoán (Predictor)
        Y_next_pred = Y_k + h * F_k
        
        # Bước lặp hiệu chỉnh (Corrector)
        for j in range(max_iter):
            F_next = np.array(F(t_next, Y_next_pred))
            Y_next_corr = Y_k + (h / 2.0) * (F_k + F_next)
            
            err = np.linalg.norm(Y_next_corr - Y_next_pred, np.inf)
            Y_next_pred = Y_next_corr
            
            if err < epsilon:
                break
                
        t_vals.append(t_next)
        Y_vals.append(Y_next_corr)
        
        t_k = t_next
        Y_k = Y_next_corr
        
        row = f"| {k} | {t_k:.4f} | " + " | ".join([f"{val:.5f}" for val in Y_k]) + " |"
        md.append(row)
        
    display(Markdown('\n'.join(md)))
    
    # Vẽ đồ thị quỹ đạo
    plt.figure(figsize=(10, 5))
    
    # Đồ thị theo thời gian
    plt.subplot(1, 2, 1)
    Y_array = np.array(Y_vals)
    for i in range(n_vars):
        plt.plot(t_vals, Y_array[:, i], marker='o', label=f'$y_{i+1}(t)$')
    plt.xlabel('t')
    plt.ylabel('Giá trị')
    plt.title('Hàm nghiệm theo t')
    plt.legend()
    plt.grid(True)
    
    # Nếu hệ 2 biến thì vẽ quỹ đạo pha
    if n_vars == 2:
        plt.subplot(1, 2, 2)
        plt.plot(Y_array[:, 0], Y_array[:, 1], marker='s', color='purple')
        plt.xlabel('$x(t)$')
        plt.ylabel('$y(t)$')
        plt.title('Quỹ đạo pha (x, y)')
        plt.grid(True)
        
    plt.tight_layout()
    plt.show()

# DỮ LIỆU ĐỀ BÀI (Câu 2.1)
# Hệ phương trình:
# x' = -2x + y
# y' = x - 2y
def F_system(t, Y):
    x, y = Y
    dx_dt = -2*x + y
    dy_dt = x - 2*y
    return [dx_dt, dy_dt]

# Điều kiện đầu: x(3)=1, y(3)=-0.5. Đoạn [3, 6], bước h=0.1
t0 = 3.0
Y0 = [1.0, -0.5]
h = 0.1
t_end = 6.0

Trapezoidal_ODE_System(F_system, t0, Y0, h, t_end, epsilon=1e-5)
"""

create_notebook(os.path.join(chuong7_dir, "Hệ PTVP - Công thức Hình thang.ipynb"), "Hệ Phương Trình Vi Phân - Công thức Hình thang (Predictor-Corrector)", code_hinh_thang)

print("Đã tạo CHƯƠNG 7 thành công!")
