import os
import json
import numpy as np

base_dir = "d:/code/Uni/On_thi_cuoi_ky/Giải tích số/scripts"

def update_notebook(filepath, title, source_code):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            nb = json.load(f)
        nb['cells'][0]['source'] = [f"### {title}\n"]
        nb['cells'][1]['source'] = [line + '\n' for line in source_code.split('\n')]
        if nb['cells'][1]['source']:
            nb['cells'][1]['source'][-1] = nb['cells'][1]['source'][-1].rstrip('\n')
        nb['cells'][1]['outputs'] = []
    else:
        nb = {
         "cells": [
          {"cell_type": "markdown", "metadata": {}, "source": [f"### {title}\n"]},
          {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": [line + '\n' for line in source_code.split('\n')]}
         ],
         "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"}, "language_info": {"name": "python", "version": "3.13.7"}},
         "nbformat": 4, "nbformat_minor": 4
        }
        if nb['cells'][1]['source']:
            nb['cells'][1]['source'][-1] = nb['cells'][1]['source'][-1].rstrip('\n')
            
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)

# ==============================================================================
# 1. Giải Đa Thức Toàn Tập
# ==============================================================================
dt_path = os.path.join(base_dir, "CHƯƠNG 2 GIẢI PHƯƠNG TRÌNH PHI TUYẾN 1 CHIỀU/Giải Đa Thức Toàn Tập.ipynb")
code_dt = r"""import numpy as np
from IPython.display import display, Math, Markdown

def format_poly(coeffs):
    n = len(coeffs) - 1
    terms = []
    for i, c in enumerate(coeffs):
        if abs(c) < 1e-10: continue
        deg = n - i
        sign = " + " if c > 0 else " - "
        c_abs = abs(c)
        c_str = f"{c_abs:.4f}" if abs(c_abs - 1.0) > 1e-10 or deg == 0 else ""
        if deg == 0: terms.append(f"{sign}{c_abs:.4f}")
        elif deg == 1: terms.append(f"{sign}{c_str}x")
        else: terms.append(f"{sign}{c_str}x^{deg}")
    res = "".join(terms).lstrip(" + ")
    if res.startswith("- "): res = "-" + res[2:]
    return res if res else "0"

def Polynomial_Solver_Full(coeffs_input, epsilon=1e-4):
    P = np.array(coeffs_input, dtype=float)
    display(Markdown("## ❖ TÌM TẤT CẢ NGHIỆM ĐA THỨC (CÁCH LY + NEWTON)"))
    display(Math(f"P(x) = {format_poly(P)} = 0"))
    
    # 1. TÌM KHOẢNG CÁCH LY (Sturm)
    display(Markdown("### 1. Phân tách khoảng cách ly nghiệm bằng định lý Sturm"))
    sturm_seq = [np.poly1d(P), np.polyder(np.poly1d(P))]
    while True:
        P_prev, P_curr = sturm_seq[-2], sturm_seq[-1]
        if P_curr.order == 0 and abs(P_curr.coeffs[0]) < 1e-10:
            sturm_seq.pop()
            break
        quot, rem = np.polydiv(P_prev, P_curr)
        P_next = np.poly1d(-rem.coeffs)
        if P_next.order == 0 and abs(P_next.coeffs[0]) < 1e-10: break
        sturm_seq.append(P_next)
        
    def count_sign_changes(x_val):
        signs = [np.sign(p(x_val)) for p in sturm_seq if abs(p(x_val)) > 1e-10]
        return sum(1 for i in range(len(signs)-1) if signs[i]*signs[i+1] < 0)

    R = 1 + np.max(np.abs(P[1:])) / abs(P[0])
    step, start, end = 1.0, -np.ceil(R), np.ceil(R)
    
    intervals = []
    curr = start
    while curr <= end:
        a, b = curr, curr + step
        num_roots = count_sign_changes(a) - count_sign_changes(b)
        if num_roots == 1: intervals.append((a, b))
        elif num_roots > 1: # Chia nhỏ khoảng
            mid = (a + b) / 2.0
            if count_sign_changes(a) - count_sign_changes(mid) == 1: intervals.append((a, mid))
            if count_sign_changes(mid) - count_sign_changes(b) == 1: intervals.append((mid, b))
        curr += step
        
    for i, (a, b) in enumerate(intervals):
        display(Markdown(f"- Khoảng nghiệm thứ {i+1}: $x \in [{a:.4f}, {b:.4f}]$"))
        
    # 2. PHƯƠNG PHÁP NEWTON
    f = np.poly1d(P)
    df = np.polyder(f)
    d2f = np.polyder(df)
    
    for i, (a, b) in enumerate(intervals):
        display(Markdown(f"\n### 2.{i+1}. Giải nghiệm trong khoảng $[{a:.4f}, {b:.4f}]$ bằng Tiếp tuyến (Newton)"))
        x0 = a if f(a)*d2f(a) > 0 else b
        
        history = [x0]
        x_k = x0
        k = 0
        while True:
            k += 1
            x_new = x_k - f(x_k)/df(x_k)
            err = abs(x_new - x_k)
            history.append(x_new)
            if err < epsilon:
                break
            if k > 50:
                display(Markdown("Chưa hội tụ!"))
                break
            x_k = x_new
            
        display(Markdown(f"- **Tổng số lần lặp:** {k}"))
        display(Markdown(f"- **Sai số cuối cùng:** $\Delta = {err:.6e} \le \epsilon = {epsilon}$"))
        
        display(Markdown("- **Chi tiết các xấp xỉ:**"))
        if len(history) <= 5:
            for idx, val in enumerate(history):
                display(Math(f"x_{{{idx}}} = {val:.6f}"))
        else:
            display(Math(f"x_{{0}} = {history[0]:.6f} \\quad \\text{{(Xấp xỉ đầu)}}"))
            display(Math(f"x_{{1}} = {history[1]:.6f}"))
            display(Math(f"x_{{2}} = {history[2]:.6f}"))
            display(Markdown("$\\dots$"))
            display(Math(f"x_{{{k-2}}} = {history[-3]:.6f}"))
            display(Math(f"x_{{{k-1}}} = {history[-2]:.6f}"))
            display(Math(f"x_{{{k}}} = {history[-1]:.6f} \\quad \\text{{(Xấp xỉ cuối)}}"))
            
        # Kiểm tra lại nghiệm
        val_check = f(history[-1])
        display(Markdown("- **Kiểm tra nghiệm:**"))
        display(Math(f"P(x_{{{k}}}) = {val_check:.6e} \\approx 0 \\quad \\Rightarrow \\text{{Nghiệm hợp lệ!}}"))

# ========================================================
# NHẬP HỆ SỐ ĐA THỨC CỦA BẠN VÀO ĐÂY
# P(x) = a_n * x^n + a_{n-1} * x^{n-1} + ... + a_0
# Ví dụ: P(x) = 1*x^5 - 3*x^4 + 2*x^3 + 5*x^2 - x - 7
P_coeffs = [1.0, -3.0, 2.0, 5.0, -1.0, -7.0]
# ========================================================

Polynomial_Solver_Full(P_coeffs, epsilon=1e-4)
"""
update_notebook(dt_path, "Giải Đa Thức (Cách ly & Newton)", code_dt)


# ==============================================================================
# 2. Nghịch đảo ma trận Lặp Gauss-Seidel
# ==============================================================================
inv_path = os.path.join(base_dir, "CHƯƠNG 4 GIẢI HỆ ĐẠI SỐ TUYẾN TÍNH & TÌM MA TRẬN NGHỊCH ĐẢO/Nghịch đảo bằng Lặp Jacobi  Gauss-Seidel.ipynb")
code_inv = r"""import numpy as np
from IPython.display import Markdown, display, Math

def Inverse_Gauss_Seidel(A_input, epsilon=None, max_iter=50):
    def matrix_to_latex(M, precision=4):
        rows = " \\\\ ".join([" & ".join([f"{x:.{precision}f}" for x in row]) for row in M])
        return f"\\begin{{bmatrix}} {rows} \\end{{bmatrix}}"

    A = np.array(A_input, dtype=float)
    n = A.shape[0]
    I = np.eye(n)
    
    display(Markdown("## ❖ TÌM MA TRẬN NGHỊCH ĐẢO BẰNG PHƯƠNG PHÁP LẶP GAUSS-SEIDEL"))
    display(Math(f"A = {matrix_to_latex(A)}"))
    
    # Check chéo trội
    dom = True
    for i in range(n):
        if abs(A[i, i]) <= sum(abs(A[i, j]) for j in range(n) if j != i):
            dom = False
    if not dom:
        display(Markdown("⚠️ **Lưu ý:** Ma trận $A$ không có tính chéo trội hàng chặt ngặt. Hãy đảm bảo bạn đã biến đổi nó (nhân $A^T$) trước khi đưa vào hàm hoặc chấp nhận rủi ro thuật toán có thể phân kỳ!"))
    
    # Khởi tạo ma trận X
    X_k = np.zeros((n, n))
    history = [X_k.copy()]
    
    k = 0
    while True:
        k += 1
        X_new = X_k.copy()
        
        # Cập nhật Gauss-Seidel cột theo cột
        for col in range(n):
            for i in range(n):
                sum_val = I[i, col]
                for j in range(n):
                    if j != i:
                        sum_val -= A[i, j] * X_new[j, col]
                X_new[i, col] = sum_val / A[i, i]
                
        err = np.linalg.norm(X_new - X_k, np.inf)
        history.append(X_new.copy())
        
        if epsilon is not None and err < epsilon:
            break
        if max_iter is not None and k >= max_iter:
            break
        X_k = X_new

    display(Markdown(f"### Kết quả tính toán (Tổng số vòng lặp: {k})"))
    if epsilon is not None:
        display(Markdown(f"- **Đánh giá sai số:** $\\Delta = {err:.6e} \\le \\epsilon = {epsilon}$"))
        
    # In giá trị trung gian
    mid_idx = k // 2
    display(Markdown(f"- **Giá trị trung gian tại bước lặp {mid_idx}:**"))
    display(Math(f"A^{{-1}}_{{({mid_idx})}} = {matrix_to_latex(history[mid_idx], 5)}"))
    
    # In kết quả cuối
    display(Markdown(f"- **Kết quả xấp xỉ cuối cùng (bước {k}):**"))
    display(Math(f"A^{{-1}}_{{({k})}} = {matrix_to_latex(history[-1], 5)}"))
    
    # Kiểm tra nghiệm
    check_matrix = A @ history[-1]
    display(Markdown(f"### Kiểm tra nghiệm"))
    display(Markdown(f"Tính tích $A \\times A^{{-1}}_{{({k})}}$ để kiểm tra độ chính xác (kỳ vọng xấp xỉ ma trận đơn vị $I$):"))
    display(Math(f"A \\cdot A^{{-1}} \\approx {matrix_to_latex(check_matrix, 4)}"))
    
    err_I = np.linalg.norm(check_matrix - I, np.inf)
    if err_I < 1e-2:
        display(Markdown(f"**Nhận xét:** Tích $A \cdot A^{{-1}}$ rất sát với ma trận đơn vị $I$ (sai số cực đại: {err_I:.4e}). Thuật toán hoạt động chính xác!"))
    else:
        display(Markdown(f"**Nhận xét:** Sai số còn lớn (sai số cực đại: {err_I:.4e}). Nghịch đảo chưa đạt độ chính xác cao."))

# ========================================================
# NHẬP MA TRẬN A CẦN TÌM NGHỊCH ĐẢO VÀO ĐÂY
# Lưu ý: Nếu ma trận không chéo trội, thuật toán có thể phân kỳ
A = np.array([
    [10.0, 1.0, 2.0],
    [2.0, 15.0, 3.0],
    [1.0, 2.0, 20.0]
], dtype=float)
# ========================================================

Inverse_Gauss_Seidel(A, epsilon=1e-4)
"""
update_notebook(inv_path, "Nghịch đảo Ma Trận (Lặp Gauss-Seidel)", code_inv)


# ==============================================================================
# 3. Phương pháp Lũy thừa (Trị riêng)
# ==============================================================================
pow_path = os.path.join(base_dir, "CHƯƠNG 5 GIÁ TRỊ RIÊNG VÀ VECTOR RIÊNG CỦA MA TRẬN/Phương pháp Lũy thừa.ipynb")
code_pow = r"""import numpy as np
from IPython.display import display, Math, Markdown

def Power_Method_L2(A_input, x0_input=None, tol=1e-5, max_iter=100):
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
        
    x_k = x_k / np.linalg.norm(x_k, 2)
    
    display(Markdown("## ❖ TÌM TRỊ RIÊNG TRỘI BẰNG PHƯƠNG PHÁP LŨY THỪA"))
    display(Math(f"A = {matrix_to_latex(A)}"))
    
    lam_prev = 0
    history_lam = []
    history_v = [x_k.copy()]
    
    k = 0
    while True:
        k += 1
        y_new = A @ x_k
        lam_rayleigh = x_k.T @ y_new
        
        norm_y = np.linalg.norm(y_new, 2)
        if norm_y == 0:
            break
            
        v_new = y_new / norm_y
        idx = np.argmax(np.abs(v_new))
        if v_new[idx] < 0:
            v_new = -v_new
            
        err = np.abs(lam_rayleigh - lam_prev)
        history_lam.append(lam_rayleigh)
        history_v.append(v_new.copy())
        
        if err < tol:
            break
        if k >= max_iter:
            display(Markdown(f"**Cảnh báo:** Thuật toán chưa hội tụ sau {k} vòng lặp."))
            break
            
        x_k = v_new
        lam_prev = lam_rayleigh
        
    display(Markdown(f"### Kết quả tính toán (Tổng số vòng lặp: {k})"))
    display(Markdown(f"- **Đánh giá sai số:** $\\Delta = |\\lambda_{{{k}}} - \\lambda_{{{k-1}}}| = {err:.6e} \\le \\epsilon = {tol}$"))
    
    # In 3 xấp xỉ đầu và 3 xấp xỉ cuối
    display(Markdown("### Chi tiết các xấp xỉ Trị riêng $\\lambda$ và Véctơ riêng $v$:"))
    
    if len(history_lam) <= 5:
        for idx in range(len(history_lam)):
            display(Math(f"\\lambda_{{{idx+1}}} = {history_lam[idx]:.5f}, \\quad v_{{{idx+1}}} = {matrix_to_latex(history_v[idx+1])}"))
    else:
        display(Math(f"\\lambda_1 = {history_lam[0]:.5f}, \\quad v_1 = {matrix_to_latex(history_v[1])} \\quad \\text{{(Đầu)}}"))
        display(Math(f"\\lambda_2 = {history_lam[1]:.5f}, \\quad v_2 = {matrix_to_latex(history_v[2])}"))
        display(Math(f"\\lambda_3 = {history_lam[2]:.5f}, \\quad v_3 = {matrix_to_latex(history_v[3])}"))
        display(Markdown("$\\dots$"))
        display(Math(f"\\lambda_{{{k-2}}} = {history_lam[-3]:.5f}, \\quad v_{{{k-2}}} = {matrix_to_latex(history_v[-3])}"))
        display(Math(f"\\lambda_{{{k-1}}} = {history_lam[-2]:.5f}, \\quad v_{{{k-1}}} = {matrix_to_latex(history_v[-2])}"))
        display(Math(f"\\lambda_{{{k}}} = {history_lam[-1]:.5f}, \\quad v_{{{k}}} = {matrix_to_latex(history_v[-1])} \\quad \\text{{(Cuối)}}"))

    # Kiểm tra
    check_v = A @ history_v[-1]
    lam_v = history_lam[-1] * history_v[-1]
    display(Markdown("### Kiểm tra nghiệm"))
    display(Markdown(f"Kiểm tra định nghĩa $A \\cdot v \\approx \\lambda \\cdot v$:"))
    display(Math(f"A \\cdot v_k = {matrix_to_latex(check_v)}"))
    display(Math(f"\\lambda_k \\cdot v_k = {matrix_to_latex(lam_v)}"))
    
# ========================================================
# NHẬP MA TRẬN A CỦA BẠN VÀO ĐÂY
A = np.array([
    [4.0, 1.0, 1.0],
    [1.0, 5.0, 1.0],
    [1.0, 1.0, 6.0]
], dtype=float)
# ========================================================

# Tìm 1 trị riêng trội
Power_Method_L2(A, tol=1e-4)
"""
update_notebook(pow_path, "Phương pháp Lũy thừa (Tìm Trị Riêng)", code_pow)

print("Hoan tat sua thanh tong quat")
