import os
import json
import numpy as np

base_dir = "d:/code/Uni/On_thi_cuoi_ky/Giải tích số/scripts"
chuong6_dir = os.path.join(base_dir, "CHƯƠNG 6 NỘI SUY VÀ ĐẠO HÀM SỐ")
os.makedirs(chuong6_dir, exist_ok=True)

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
# 1. Newton
# ==============================================================================
code_newton = r"""import numpy as np
import pandas as pd
from IPython.display import display, Math, Markdown
import math

def Newton_Interpolation(X_in, Y_in, t_val, degree=None):
    X = np.array(X_in, dtype=float)
    Y = np.array(Y_in, dtype=float)
    n = len(X) - 1
    if degree is None: degree = n
    else: degree = min(degree, n)
    
    h = X[1] - X[0]
    
    # Bảng sai phân
    diff_table = np.zeros((n + 1, n + 1))
    diff_table[:, 0] = Y
    for j in range(1, n + 1):
        for i in range(n - j + 1):
            diff_table[i][j] = diff_table[i+1][j-1] - diff_table[i][j-1]
            
    # Hiển thị bảng sai phân
    md = ["## ❖ BẢNG SAI PHÂN TỶ ĐỐI CÁCH ĐỀU"]
    header = "| $i$ | $x_i$ | $y_i$ | " + " | ".join([f"$\\Delta^{j} y$" for j in range(1, n+1)]) + " |"
    md.append(header)
    md.append("|---" * (n + 3) + "|")
    
    for i in range(n + 1):
        row = f"| {i} | {X[i]:.5f} | {Y[i]:.6f} | "
        for j in range(1, n + 1 - i):
            row += f"{diff_table[i][j]:.6f} | "
        for j in range(n + 1 - i, n + 1):
            row += " | "
        md.append(row)
    
    display(Markdown('\n'.join(md)))
    
    # Quyết định dùng Newton Tiến hay Lùi
    mid_point = (X[0] + X[-1]) / 2
    
    if t_val <= mid_point:
        method = "Tiến (Forward)"
        # Tìm x_0 gần t_val nhất mà t_val > x_0
        idx = 0
        for i in range(len(X)-degree):
            if X[i] <= t_val < X[i+1]:
                idx = i
                break
        
        x0 = X[idx]
        y0 = Y[idx]
        s = (t_val - x0) / h
        
        display(Markdown(f"\n### ❖ NỘI SUY NEWTON TIẾN"))
        display(Markdown(f"Điểm cần tính $t = {t_val}$ nằm ở nửa đầu bảng. Chọn mốc $x_0 = x_{{{idx}}} = {x0}$."))
        display(Math(f"h = {h:.5f}, \\quad s = \\frac{{t - x_0}}{{h}} = \\frac{{{t_val} - {x0}}}{{{h}}} = {s:.5f}"))
        
        # Giá trị nội suy
        val = y0
        term_s = 1.0
        
        eq_str = f"P_{{{degree}}}({t_val}) = {y0:.6f}"
        
        # Đạo hàm
        deriv = 0.0
        
        for i in range(1, degree + 1):
            delta_y = diff_table[idx][i]
            
            # Tính s(s-1)...(s-i+1)
            term_s *= (s - i + 1)
            val += (term_s * delta_y) / math.factorial(i)
            
            eq_str += f" + \\frac{{s(s-1)...(s-{i-1})}}{{{i}!}} ({delta_y:.6f})"
            
            # Đạo hàm dP/ds (cách đơn giản nhất là xấp xỉ số hoặc tính giải tích các hệ số đầu tiên)
            # Vì đề thi yêu cầu tính, ta có công thức đạo hàm tại x = x0 + sh:
            # P'(x) = 1/h * [ d y0 + (2s-1)/2 d2 y0 + (3s^2-6s+2)/6 d3 y0 + ... ]
        
        # Tính chính xác đạo hàm bằng sai phân tiến tới bậc 5
        dP_ds = 0
        if degree >= 1: dP_ds += diff_table[idx][1]
        if degree >= 2: dP_ds += diff_table[idx][2] * (2*s - 1) / 2.0
        if degree >= 3: dP_ds += diff_table[idx][3] * (3*s**2 - 6*s + 2) / 6.0
        if degree >= 4: dP_ds += diff_table[idx][4] * (4*s**3 - 18*s**2 + 22*s - 6) / 24.0
        if degree >= 5: dP_ds += diff_table[idx][5] * (5*s**4 - 40*s**3 + 105*s**2 - 100*s + 24) / 120.0
        
        deriv = dP_ds / h
        
        display(Math(eq_str))
        display(Math(f"\\Rightarrow P_{{{degree}}}({t_val}) \\approx {val:.6f}"))
        
        display(Markdown(f"**Đạo hàm tại $t = {t_val}$:**"))
        display(Math(f"P'_{{{degree}}}({t_val}) = \\frac{{1}}{{h}} \\frac{{dP}}{{ds}} \\approx {deriv:.6f}"))
        
    else:
        method = "Lùi (Backward)"
        # Tìm x_n
        idx = len(X) - 1
        for i in range(degree, len(X)):
            if X[i-1] < t_val <= X[i]:
                idx = i
                break
                
        xn = X[idx]
        yn = Y[idx]
        s = (t_val - xn) / h
        
        display(Markdown(f"\n### ❖ NỘI SUY NEWTON LÙI"))
        display(Markdown(f"Điểm cần tính $t = {t_val}$ nằm ở nửa sau bảng. Chọn mốc $x_n = x_{{{idx}}} = {xn}$."))
        display(Math(f"h = {h:.5f}, \\quad s = \\frac{{t - x_n}}{{h}} = \\frac{{{t_val} - {xn}}}{{{h}}} = {s:.5f}"))
        
        val = yn
        term_s = 1.0
        eq_str = f"P_{{{degree}}}({t_val}) = {yn:.6f}"
        
        for i in range(1, degree + 1):
            nabla_y = diff_table[idx-i][i] # nabla^i y_n = delta^i y_{n-i}
            term_s *= (s + i - 1)
            val += (term_s * nabla_y) / math.factorial(i)
            eq_str += f" + \\frac{{s(s+1)...(s+{i-1})}}{{{i}!}} ({nabla_y:.6f})"
            
        # Đạo hàm
        dP_ds = 0
        if degree >= 1: dP_ds += diff_table[idx-1][1]
        if degree >= 2: dP_ds += diff_table[idx-2][2] * (2*s + 1) / 2.0
        if degree >= 3: dP_ds += diff_table[idx-3][3] * (3*s**2 + 6*s + 2) / 6.0
        if degree >= 4: dP_ds += diff_table[idx-4][4] * (4*s**3 + 18*s**2 + 22*s + 6) / 24.0
        if degree >= 5: dP_ds += diff_table[idx-5][5] * (5*s**4 + 40*s**3 + 105*s**2 + 100*s + 24) / 120.0
        
        deriv = dP_ds / h
        
        display(Math(eq_str))
        display(Math(f"\\Rightarrow P_{{{degree}}}({t_val}) \\approx {val:.6f}"))
        
        display(Markdown(f"**Đạo hàm tại $t = {t_val}$:**"))
        display(Math(f"P'_{{{degree}}}({t_val}) = \\frac{{1}}{{h}} \\frac{{dP}}{{ds}} \\approx {deriv:.6f}"))

# DỮ LIỆU ĐỀ BÀI (Câu 1.1)
# Bảng giá trị Gamma trên [1; 2] với h = 0.05
X_data = np.arange(1.0, 2.01, 0.05)
Y_data = [1.00000, 0.97350, 0.95135, 0.93304, 0.91817, 0.90640, 0.89747, 0.89115, 
          0.88726, 0.88565, 0.88623, 0.88887, 0.89352, 0.90012, 0.90864, 0.91906, 
          0.93138, 0.94561, 0.96177, 0.97988, 1.00000]

# Nội suy bậc 5 tại t = 1.57
Newton_Interpolation(X_data, Y_data, t_val=1.57, degree=5)
"""

# ==============================================================================
# 2. Nội Suy Ngược
# ==============================================================================
code_inverse = r"""import numpy as np
from IPython.display import display, Math, Markdown
import math

def Inverse_Interpolation(X_in, Y_in, y_val, degree=3, max_iter=20, epsilon=1e-6):
    X = np.array(X_in, dtype=float)
    Y = np.array(Y_in, dtype=float)
    n = len(X) - 1
    h = X[1] - X[0]
    
    display(Markdown(f"## ❖ NỘI SUY NGƯỢC TÌM $t$ SAO CHO $f(t) = {y_val}$"))
    
    # Tìm khoảng chứa nghiệm
    idx = -1
    for i in range(len(Y)-1):
        if min(Y[i], Y[i+1]) <= y_val <= max(Y[i], Y[i+1]):
            idx = i
            break
            
    if idx == -1:
        print("Giá trị cần tìm không nằm trong bảng số liệu!")
        return
        
    x0 = X[idx]
    y0 = Y[idx]
    
    display(Markdown(f"Dựa vào bảng, $y^* = {y_val}$ nằm giữa $y_{{{idx}}} = {y0:.5f}$ và $y_{{{idx+1}}} = {Y[idx+1]:.5f}$."))
    display(Markdown(f"Chọn mốc nội suy tiến $x_0 = x_{{{idx}}} = {x0}$."))
    
    # Bảng sai phân
    diff = np.zeros((n + 1, n + 1))
    diff[:, 0] = Y
    for j in range(1, degree + 1):
        for i in range(n - j + 1):
            diff[i][j] = diff[i+1][j-1] - diff[i][j-1]
            
    delta_y0 = diff[idx][1]
    
    display(Markdown("Sử dụng công thức lặp Newton:"))
    display(Math(r"s^{(k+1)} = \frac{1}{\Delta y_0} \left[ y^* - y_0 - \frac{s^{(k)}(s^{(k)}-1)}{2!} \Delta^2 y_0 - \dots \right]"))
    
    s_k = (y_val - y0) / delta_y0
    
    md = ["| Bước $k$ | $s^{(k)}$ | Sai số $|s^{(k)} - s^{(k-1)}|$ |",
          "|---|---|---|",
          f"| 0 | {s_k:.6f} | - |"]
          
    history_s = [s_k]
    
    for k in range(1, max_iter + 1):
        s_old = s_k
        
        sum_correction = 0
        term = s_old
        for i in range(2, degree + 1):
            term = term * (s_old - i + 1)
            sum_correction += (term * diff[idx][i]) / math.factorial(i)
            
        s_new = (y_val - y0 - sum_correction) / delta_y0
        
        err = abs(s_new - s_old)
        md.append(f"| {k} | {s_new:.6f} | {err:.6e} |")
        
        s_k = s_new
        history_s.append(s_k)
        
        if err < epsilon:
            break
            
    display(Markdown('\n'.join(md)))
    
    t_res = x0 + s_k * h
    display(Markdown("### Kết luận"))
    display(Math(f"s \\approx {s_k:.6f} \\implies t = x_0 + s \\cdot h = {x0} + {s_k:.6f} \\times {h} = {t_res:.6f}"))

# DỮ LIỆU ĐỀ BÀI (Câu 1.2)
X_data = np.arange(1.0, 2.01, 0.05)
Y_data = [1.00000, 0.97350, 0.95135, 0.93304, 0.91817, 0.90640, 0.89747, 0.89115, 
          0.88726, 0.88565, 0.88623, 0.88887, 0.89352, 0.90012, 0.90864, 0.91906, 
          0.93138, 0.94561, 0.96177, 0.97988, 1.00000]

Inverse_Interpolation(X_data, Y_data, y_val=0.8915, degree=3)
"""

# ==============================================================================
# 3. Spline bậc 3
# ==============================================================================
code_spline = r"""import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display, Math, Markdown

def Cubic_Spline_Interpolation(X_in, Y_in, t_eval=None):
    X = np.array(X_in, dtype=float)
    Y = np.array(Y_in, dtype=float)
    n = len(X) - 1
    
    h = np.diff(X)
    
    display(Markdown("## ❖ NỘI SUY SPLINE BẬC 3 (ĐIỀU KIỆN BIÊN TỰ NHIÊN)"))
    
    # Lập hệ phương trình cho M (đạo hàm bậc 2)
    A = np.zeros((n+1, n+1))
    d = np.zeros(n+1)
    
    # Biên tự nhiên: M_0 = 0, M_n = 0
    A[0, 0] = 1
    A[n, n] = 1
    
    for i in range(1, n):
        A[i, i-1] = h[i-1] / 6.0
        A[i, i] = (h[i-1] + h[i]) / 3.0
        A[i, i+1] = h[i] / 6.0
        d[i] = (Y[i+1] - Y[i]) / h[i] - (Y[i] - Y[i-1]) / h[i-1]
        
    M = np.linalg.solve(A, d)
    
    md = ["### 1. Giải hệ phương trình tìm đạo hàm bậc hai $M_i$"]
    md.append("Từ hệ phương trình Spline, ta giải ra các giá trị $M_i$:")
    for i in range(n+1):
        md.append(f"- $M_{{{i}}} = {M[i]:.6f}$")
        
    md.append("\n### 2. Các hàm Spline thành phần $S_i(x)$")
    md.append("Trên mỗi đoạn $[x_i, x_{i+1}]$, ta có Spline:")
    
    coefs = []
    for i in range(n):
        a = (M[i+1] - M[i]) / (6 * h[i])
        b = M[i] / 2.0
        c = (Y[i+1] - Y[i]) / h[i] - h[i] * (M[i+1] + 2 * M[i]) / 6.0
        d_coef = Y[i]
        coefs.append((a, b, c, d_coef))
        
        md.append(f"**Đoạn $i={i}$ (trên khoảng [{X[i]}, {X[i+1]}]):**")
        md.append(f"$$ S_{{{i}}}(x) = {a:.4f}(x - {X[i]})^3 + {b:.4f}(x - {X[i]})^2 + {c:.4f}(x - {X[i]}) + {d_coef:.4f} $$")
        
    display(Markdown('\n'.join(md)))
    
    if t_eval is not None:
        display(Markdown("### 3. Tính giá trị nội suy"))
        for t in t_eval:
            # Tìm đoạn
            idx = 0
            for i in range(n):
                if X[i] <= t <= X[i+1]:
                    idx = i
                    break
            a, b, c, d_coef = coefs[idx]
            val = a*(t - X[idx])**3 + b*(t - X[idx])**2 + c*(t - X[idx]) + d_coef
            display(Math(f"S({t}) = S_{{{idx}}}({t}) \\approx {val:.6f}"))

# DỮ LIỆU ĐỀ BÀI (Câu 2.3)
# t_2k (k=0..4) từ bảng t = [3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6]
# x(t), y(t) ta lấy ngẫu nhiên 1 tập nghiệm để minh họa, đi thi bạn nhập số thực từ bước 2.1 vào
t_data = [3.0, 3.2, 3.4, 3.6, 3.8]
x_data = [1.000, 0.812, 0.650, 0.510, 0.390]

Cubic_Spline_Interpolation(t_data, x_data, t_eval=[3.1, 3.3, 3.5])
"""

create_notebook(os.path.join(chuong6_dir, "Nội suy Newton (Tiến - Lùi).ipynb"), "Nội Suy Newton Tiến Lùi (Tính Đạo Hàm)", code_newton)
create_notebook(os.path.join(chuong6_dir, "Nội suy ngược.ipynb"), "Nội Suy Ngược (Lặp Newton)", code_inverse)
create_notebook(os.path.join(chuong6_dir, "Nội suy Spline bậc 3.ipynb"), "Nội Suy Spline Bậc 3", code_spline)

print("Đã tạo CHƯƠNG 6 thành công!")
