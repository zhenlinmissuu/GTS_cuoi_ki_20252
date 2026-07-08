import os
import json
import numpy as np

base_dir = "d:/code/Uni/On_thi_cuoi_ky/Giải tích số/scripts/CHƯƠNG 5 GIÁ TRỊ RIÊNG VÀ VECTOR RIÊNG CỦA MA TRẬN"

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
# 1. Khoảng cách ly nghiệm đa thức
# ==============================================================================
code_khoang_cach_ly = r"""import numpy as np
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

def Polynomial_Root_Isolation(coeffs_input):
    # coeffs_input là mảng hệ số đa thức, từ bậc cao nhất đến bậc 0
    # Ví dụ: x^3 - 2x + 1 => [1, 0, -2, 1]
    P = np.array(coeffs_input, dtype=float)
    n = len(P) - 1
    
    display(Markdown("## ❖ TÌM KHOẢNG CÁCH LY NGHIỆM CỦA ĐA THỨC"))
    display(Markdown("Sử dụng **Định lý Sturm** để đếm số nghiệm thực phân biệt trong khoảng [a, b]."))
    
    poly_str = format_poly(P)
    display(Math(f"P(x) = {poly_str}"))
    
    # Chuỗi Sturm
    sturm_seq = [np.poly1d(P)]
    P_deriv = np.polyder(sturm_seq[0])
    sturm_seq.append(P_deriv)
    
    md = ["### 1. Xây dựng chuỗi Sturm"]
    md.append(f"- $P_0(x) = P(x) = {format_poly(sturm_seq[0].coeffs)}$")
    md.append(f"- $P_1(x) = P'(x) = {format_poly(sturm_seq[1].coeffs)}$")
    
    while True:
        P_prev = sturm_seq[-2]
        P_curr = sturm_seq[-1]
        
        if P_curr.order == 0 and abs(P_curr.coeffs[0]) < 1e-10:
            sturm_seq.pop() # Loại bỏ đa thức 0
            break
            
        # Chia đa thức
        quot, rem = np.polydiv(P_prev, P_curr)
        # P_{i+1} = - phần dư
        P_next = np.poly1d(-rem.coeffs)
        
        if P_next.order == 0 and abs(P_next.coeffs[0]) < 1e-10:
            break
            
        sturm_seq.append(P_next)
        idx = len(sturm_seq) - 1
        md.append(f"- $P_{idx}(x) = - \\text{{dư}}(P_{idx-2}, P_{idx-1}) = {format_poly(P_next.coeffs)}$")
        
    display(Markdown('\n'.join(md)))
    
    def count_sign_changes(x_val):
        signs = []
        for p in sturm_seq:
            val = p(x_val)
            if abs(val) > 1e-10:
                signs.append(np.sign(val))
        changes = 0
        for i in range(len(signs)-1):
            if signs[i] * signs[i+1] < 0:
                changes += 1
        return changes

    # Giới hạn nghiệm theo tiêu chuẩn Cauchy
    a_n = P[0]
    A_max = np.max(np.abs(P[1:]))
    R = 1 + A_max / abs(a_n)
    
    display(Markdown("### 2. Đánh giá giới hạn nghiệm và quét tìm khoảng"))
    display(Math(f"R = 1 + \\frac{{\\max |a_k|}}{{|a_n|}} = 1 + \\frac{{{A_max:.4f}}}{{{abs(a_n):.4f}}} = {R:.4f}"))
    display(Markdown(f"Tất cả các nghiệm thực đều nằm trong khoảng $[-R, R] = [{-R:.4f}, {R:.4f}]$.\n"))
    
    intervals = []
    # Quét từ -R đến R với bước 1.0 (có thể tinh chỉnh bước quét nếu cần)
    step = 1.0
    start = -np.ceil(R)
    end = np.ceil(R)
    
    curr = start
    while curr < end:
        a = curr
        b = curr + step
        
        V_a = count_sign_changes(a)
        V_b = count_sign_changes(b)
        
        num_roots = V_a - V_b
        if num_roots == 1:
            intervals.append((a, b))
        elif num_roots > 1:
            # Nếu có >1 nghiệm trong khoảng này, chia nhỏ ra để tìm chính xác khoảng cách ly 1 nghiệm
            mid = (a + b) / 2.0
            V_mid = count_sign_changes(mid)
            if V_a - V_mid == 1: intervals.append((a, mid))
            if V_mid - V_b == 1: intervals.append((mid, b))
            
        curr += step
        
    display(Markdown("**Kết luận các khoảng cách ly nghiệm:**"))
    for i, (a, b) in enumerate(intervals):
        display(Markdown(f"- Khoảng cách ly nghiệm thứ {i+1}: $x_{i+1} \in [{a:.4f}, {b:.4f}]$"))

# DỮ LIỆU ĐỀ BÀI (Câu 3)
# Đặc trưng đa thức của A^T A (bạn có thể lấy kết quả từ hàm Danielevski đưa vào đây)
# Ví dụ: P(lambda) = lambda^3 - 5*lambda^2 + 6*lambda
coeffs = [1.0, -5.0, 6.0, 0.0]
Polynomial_Root_Isolation(coeffs)
"""

create_notebook(os.path.join(base_dir, "Khoảng cách ly nghiệm đa thức.ipynb"), "Định lý Sturm - Tìm khoảng cách ly nghiệm", code_khoang_cach_ly)


# ==============================================================================
# 2. Update SVD (thêm A_plus)
# ==============================================================================
notebook_svd_path = os.path.join(base_dir, "Giá trị kỳ dị SVD (Lớn nhất).ipynb")

with open(notebook_svd_path, 'r', encoding='utf-8') as f:
    nb_svd = json.load(f)

# The new source that appends Pseudoinverse computation
svd_source = r"""import numpy as np
from IPython.display import display, Math

def SVD_Reduced(A_input, v0_input=None, num_iters=1000, tol=1e-10):
    def matrix_to_latex(M, precision=4):
        if not isinstance(M, np.ndarray):
            return str(M)
        elif M.ndim == 1:
            inner = " \\\\ ".join([f"{x:.{precision}f}" for x in M])
            return f"\\begin{{bmatrix}} {inner} \\end{{bmatrix}}^T"
        else:
            rows = " \\\\ ".join([" & ".join([f"{x:.{precision}f}" for x in row]) for row in M])
            return f"\\begin{{bmatrix}} {rows} \\end{{bmatrix}}"

    def power_method_L2(B, v0, num_iters, tol):
        v = v0.copy()
        lam_prev = 0
        for i in range(num_iters):
            y_new = B @ v
            lam_rayleigh = v.T @ y_new
            norm_y = np.linalg.norm(y_new, 2)
            if norm_y == 0: return 0, v
            v_new = y_new / norm_y
            
            idx = np.argmax(np.abs(v_new))
            if v_new[idx] < 0: v_new = -v_new
                
            if np.abs(lam_rayleigh - lam_prev) < tol:
                v = v_new
                lam_prev = lam_rayleigh
                break
            v = v_new
            lam_prev = lam_rayleigh
        return lam_prev, v

    A = np.array(A_input, dtype=float)
    n, m = A.shape
    
    print("="*60)
    print("PHÂN TÍCH SVD VÀ TÍNH MA TRẬN NGHỊCH ĐẢO SUY RỘNG A^+")
    print("="*60)
    
    display(Math(f"A = {matrix_to_latex(A, precision=4)}"))

    A_k = A.copy()
    rank = min(n, m)
    
    if v0_input is None: v0_base = np.ones(m)
    else: v0_base = np.array(v0_input, dtype=float).flatten()
        
    v0_base = v0_base / np.linalg.norm(v0_base, 2)
    
    U_cols = []
    S_vals = []
    V_cols = []
    
    for k in range(1, rank + 1):
        print(f"\n--- BƯỚC {k} ---")
        B_k = A_k.T @ A_k
        lam, v = power_method_L2(B_k, v0_base, num_iters, tol)
        
        if lam < 1e-10:
            print(f"⚠️ DỪNG THUẬT TOÁN: Giá trị riêng cực đại xấp xỉ 0.")
            break
            
        sigma = np.sqrt(lam)
        u = (A_k @ v) / sigma
        
        U_cols.append(u)
        S_vals.append(sigma)
        V_cols.append(v)
        
        print(f"- Trị riêng lớn nhất: λ_{k} ≈ {lam:.4f}")
        print(f"- Giá trị kỳ dị: σ_{k} ≈ {sigma:.4f}")
        display(Math(f"v_{k} = {matrix_to_latex(v, precision=4)}"))
        display(Math(f"u_{k} = \\frac{{A_{k} v_{k}}}{{\\sigma_{k}}} = {matrix_to_latex(u, precision=4)}"))
        
        A_next = A_k - sigma * np.outer(u, v)
        display(Math(f"A_{{{k+1}}} = {matrix_to_latex(A_next, precision=4)}"))
        A_k = A_next
        
    print("\n" + "="*60)
    print("KẾT QUẢ SVD VÀ MA TRẬN NGHỊCH ĐẢO SUY RỘNG")
    print("="*60)
    
    U = np.column_stack(U_cols)
    S = np.diag(S_vals)
    V = np.column_stack(V_cols)
    
    display(Math(f"U = {matrix_to_latex(U, precision=4)}"))
    display(Math(f"\\Sigma = {matrix_to_latex(S, precision=4)}"))
    display(Math(f"V^T = {matrix_to_latex(V.T, precision=4)}"))
    
    A_reconstructed = U @ S @ V.T
    err = np.linalg.norm(A - A_reconstructed)
    print(f"\nKiểm tra sai số ||A - U Σ V^T||_F = {err:.2e}")

    # ================= NGHỊCH ĐẢO SUY RỘNG =================
    print("\n--- TÍNH MA TRẬN NGHỊCH ĐẢO SUY RỘNG A^+ ---")
    print("Công thức: A^+ = V * Σ^+ * U^T")
    
    S_plus_vals = [1.0/s if s > 1e-10 else 0.0 for s in S_vals]
    S_plus = np.zeros((m, n))
    for i in range(len(S_plus_vals)):
        S_plus[i, i] = S_plus_vals[i]
        
    display(Math(f"\\Sigma^+ = {matrix_to_latex(S_plus, precision=4)}"))
    
    A_plus = V @ np.diag(S_plus_vals) @ U.T
    display(Math(f"A^+ = {matrix_to_latex(A_plus, precision=5)}"))


# Ma trận đề bài Câu 3
A = np.array([
    [8,  6, 10, 10, 44,  6],
    [9,  1, 10,  5, 21,  9],
    [1,  3,  1,  8, 26, -8],
    [10, 6, 10,  1, 30, 30],
    [32, 10, 37, 2, 61, 75],
    [-6, 18, -7, 20, 89, -15]
], dtype=float)

# Áp dụng cho A^T A (Theo ý 4 yêu cầu khai triển kỳ dị của A)
SVD_Reduced(A)
"""

nb_svd['cells'][1]['source'] = [line + '\n' for line in svd_source.split('\n')]
nb_svd['cells'][1]['source'][-1] = nb_svd['cells'][1]['source'][-1].rstrip('\n')
nb_svd['cells'][1]['outputs'] = []

with open(notebook_svd_path, 'w', encoding='utf-8') as f:
    json.dump(nb_svd, f, indent=1, ensure_ascii=False)

print("Đã tạo file Khoảng cách ly và cập nhật SVD thành công!")
