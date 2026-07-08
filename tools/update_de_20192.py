import os
import json
import numpy as np

base_dir = "d:/code/Uni/On_thi_cuoi_ky/Giải tích số/scripts"

def update_notebook(filepath, title, source_code):
    if not os.path.exists(filepath):
        print(f"Khong tim thay file {filepath}")
        return
        
    with open(filepath, 'r', encoding='utf-8') as f:
        nb = json.load(f)
        
    nb['cells'][0]['source'] = [f"### {title}\n"]
    nb['cells'][1]['source'] = [line + '\n' for line in source_code.split('\n')]
    if nb['cells'][1]['source']:
        nb['cells'][1]['source'][-1] = nb['cells'][1]['source'][-1].rstrip('\n')
        
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)

# ==============================================================================
# 1. Gauss-Seidel x=Bx+d
# ==============================================================================
gs_path = os.path.join(base_dir, "CHƯƠNG 4 GIẢI HỆ ĐẠI SỐ TUYẾN TÍNH & TÌM MA TRẬN NGHỊCH ĐẢO/Lặp Gauss-Seidel/Lặp Gauss-Seidel (x=Bx+d).ipynb")
code_gs = r"""import numpy as np
from IPython.display import Markdown, display, Math

def Gauss_Seidel_Bd(B_input, d_input, max_iter=None, epsilon=None, x0=None):
    def matrix_to_latex(M, precision=4):
        if not isinstance(M, np.ndarray): return str(M)
        elif M.ndim == 1:
            inner = " \\\\ ".join([f"{x:.{precision}f}" for x in M])
            return f"\\begin{{bmatrix}} {inner} \\end{{bmatrix}}^T"
        else:
            rows = " \\\\ ".join([" & ".join([f"{x:.{precision}f}" for x in row]) for row in M])
            return f"\\begin{{bmatrix}} {rows} \\end{{bmatrix}}"

    B = np.array(B_input, dtype=float)
    d = np.array(d_input, dtype=float).flatten()
    n = len(d)
    
    if x0 is None:
        x_k = np.zeros(n)
    else:
        x_k = np.array(x0, dtype=float).flatten()
        
    display(Markdown("## ❖ PHƯƠNG PHÁP LẶP GAUSS-SEIDEL CHO HỆ $x = Bx + d$"))
    display(Math(f"B = {matrix_to_latex(B)}, \\quad d = {matrix_to_latex(d)}"))
    
    history = [x_k.copy()]
    
    k = 0
    while True:
        k += 1
        x_new = x_k.copy()
        for i in range(n):
            sum_val = d[i]
            for j in range(n):
                sum_val += B[i][j] * x_new[j]
            x_new[i] = sum_val
            
        err = np.linalg.norm(x_new - x_k, np.inf)
        history.append(x_new.copy())
        
        if max_iter is not None and k >= max_iter:
            break
        if epsilon is not None and err < epsilon:
            break
        if k >= 100:
            display(Markdown(f"**Cảnh báo:** Thuật toán chưa hội tụ sau {k} vòng lặp."))
            break
            
        x_k = x_new
        
    # IN KẾT QUẢ ĐÃ ĐƯỢC TỐI ƯU TRÌNH BÀY
    display(Markdown(f"### Kết quả tính toán (Tổng số vòng lặp: {k})"))
    
    if len(history) <= 5:
        # Nếu số vòng lặp ít, in tất cả
        for idx, val in enumerate(history):
            display(Math(f"x^{{({idx})}} = {matrix_to_latex(val)}"))
    else:
        # Nếu số vòng lặp nhiều, chỉ in khởi đầu và 3 bước cuối
        display(Markdown("*(Do số vòng lặp lớn, chỉ hiển thị xấp xỉ đầu và 3 xấp xỉ cuối)*"))
        display(Math(f"x^{{(0)}} = {matrix_to_latex(history[0])}"))
        display(Markdown("$\\dots$"))
        display(Math(f"x^{{({k-2})}} = {matrix_to_latex(history[-3])}"))
        display(Math(f"x^{{({k-1})}} = {matrix_to_latex(history[-2])}"))
        display(Math(f"x^{{({k})}} = {matrix_to_latex(history[-1])}"))
        
    if epsilon is not None:
        display(Math(f"\\|x^{{({k})}} - x^{{({k-1})}}\\|_\\infty = {err:.6e} < \\epsilon = {epsilon}"))

# DỮ LIỆU ĐỀ BÀI
C = np.array([
    [0.1588, 0.0064, 0.0025, 0.0304, 0.0014, 0.0083, 0.1594],
    [0.0057, 0.2645, 0.0436, 0.0099, 0.0083, 0.0201, 0.3413],
    [0.0264, 0.1506, 0.3557, 0.0139, 0.0142, 0.0070, 0.0236],
    [0.3299, 0.0565, 0.0495, 0.3636, 0.0204, 0.0483, 0.0649],
    [0.0089, 0.0081, 0.0333, 0.0295, 0.3412, 0.0237, 0.0020],
    [0.1190, 0.0901, 0.0996, 0.1260, 0.1722, 0.2368, 0.3369],
    [0.0063, 0.0126, 0.0196, 0.0098, 0.0064, 0.0132, 0.0012]
], dtype=float)

d = np.array([74000, 56000, 10500, 25000, 17500, 196000, 5000], dtype=float)

# Lặp Gauss-Seidel tìm lượng sản phẩm cần thiết
Gauss_Seidel_Bd(C, d, max_iter=None, epsilon=1e-4)
"""
update_notebook(gs_path, "Lặp Gauss-Seidel (Hệ x = Bx + d)", code_gs)

# ==============================================================================
# 2. Lặp Đơn x=Bx+d
# ==============================================================================
ld_path = os.path.join(base_dir, "CHƯƠNG 4 GIẢI HỆ ĐẠI SỐ TUYẾN TÍNH & TÌM MA TRẬN NGHỊCH ĐẢO/Lặp Jacobi - Lặp Đơn/Lặp Đơn (x=Bx+d).ipynb")
code_ld = r"""import numpy as np
from IPython.display import display, Math, Markdown

def Lap_Don_x_Bx_d(B_input, d_input, x0_input=None, num_iters=None, epsilon=None):
    def matrix_to_latex(M, precision=4):
        if not isinstance(M, np.ndarray): return str(M)
        elif M.ndim == 1:
            inner = " \\\\ ".join([f"{x:.{precision}f}" for x in M])
            return f"\\begin{{bmatrix}} {inner} \\end{{bmatrix}}^T"
        else:
            rows = " \\\\ ".join([" & ".join([f"{x:.{precision}f}" for x in row]) for row in M])
            return f"\\begin{{bmatrix}} {rows} \\end{{bmatrix}}"

    B = np.array(B_input, dtype=float)
    d = np.array(d_input, dtype=float).flatten()
    n = len(d)
    
    if x0_input is None:
        X_k = np.zeros(n)
    else:
        X_k = np.array(x0_input, dtype=float).flatten()
        
    display(Markdown("## ❖ PHƯƠNG PHÁP LẶP ĐƠN CHO HỆ $x = Bx + d$"))
    display(Math(f"B = {matrix_to_latex(B)}, \\quad d = {matrix_to_latex(d)}"))
    
    history = [X_k.copy()]
    
    k = 0
    while True:
        k += 1
        X_new = B @ X_k + d
        err = np.linalg.norm(X_new - X_k, np.inf)
        history.append(X_new.copy())
        
        if num_iters is not None and k >= num_iters:
            break
        if epsilon is not None and err < epsilon:
            break
        if k >= 100:
            display(Markdown(f"**Cảnh báo:** Thuật toán chưa hội tụ sau {k} vòng lặp."))
            break
            
        X_k = X_new
        
    # IN KẾT QUẢ ĐÃ ĐƯỢC TỐI ƯU TRÌNH BÀY
    display(Markdown(f"### Kết quả tính toán (Tổng số vòng lặp: {k})"))
    
    if len(history) <= 5:
        # Nếu số vòng lặp ít, in tất cả
        for idx, val in enumerate(history):
            display(Math(f"x^{{({idx})}} = {matrix_to_latex(val)}"))
    else:
        # Nếu số vòng lặp nhiều, chỉ in khởi đầu và 3 bước cuối
        display(Markdown("*(Do số vòng lặp lớn, chỉ hiển thị xấp xỉ đầu và 3 xấp xỉ cuối)*"))
        display(Math(f"x^{{(0)}} = {matrix_to_latex(history[0])}"))
        display(Markdown("$\\dots$"))
        display(Math(f"x^{{({k-2})}} = {matrix_to_latex(history[-3])}"))
        display(Math(f"x^{{({k-1})}} = {matrix_to_latex(history[-2])}"))
        display(Math(f"x^{{({k})}} = {matrix_to_latex(history[-1])}"))
        
    if epsilon is not None:
        display(Math(f"\\|x^{{({k})}} - x^{{({k-1})}}\\|_\\infty = {err:.6e} < \\epsilon = {epsilon}"))

# DỮ LIỆU ĐỀ BÀI
C = np.array([
    [0.1588, 0.0064, 0.0025, 0.0304, 0.0014, 0.0083, 0.1594],
    [0.0057, 0.2645, 0.0436, 0.0099, 0.0083, 0.0201, 0.3413],
    [0.0264, 0.1506, 0.3557, 0.0139, 0.0142, 0.0070, 0.0236],
    [0.3299, 0.0565, 0.0495, 0.3636, 0.0204, 0.0483, 0.0649],
    [0.0089, 0.0081, 0.0333, 0.0295, 0.3412, 0.0237, 0.0020],
    [0.1190, 0.0901, 0.0996, 0.1260, 0.1722, 0.2368, 0.3369],
    [0.0063, 0.0126, 0.0196, 0.0098, 0.0064, 0.0132, 0.0012]
], dtype=float)

d = np.array([74000, 56000, 10500, 25000, 17500, 196000, 5000], dtype=float)

# Lặp Đơn tìm lượng sản phẩm cần thiết
Lap_Don_x_Bx_d(C, d, num_iters=None, epsilon=1e-4)
"""
update_notebook(ld_path, "Lặp Đơn (Hệ x = Bx + d)", code_ld)

# ==============================================================================
# 3. SVD
# ==============================================================================
svd_path = os.path.join(base_dir, "CHƯƠNG 5 GIÁ TRỊ RIÊNG VÀ VECTOR RIÊNG CỦA MA TRẬN/Giá trị kỳ dị SVD (Lớn nhất).ipynb")
code_svd = r"""import numpy as np
from IPython.display import display, Math, Markdown

def SVD_Reduced(A_input, num_components=None, v0_input=None, num_iters=1000, tol=1e-10):
    def matrix_to_latex(M, precision=4):
        if not isinstance(M, np.ndarray): return str(M)
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

    # Phần 1: Ghi chú lý thuyết Phương pháp Xuống thang
    theory_md = [
        "## ❖ KHAI TRIỂN KỲ DỊ SVD BẰNG PHƯƠNG PHÁP XUỐNG THANG (DEFLATION)",
        "",
        "**Ý tưởng của phương pháp Xuống thang:**",
        "Sau khi đã tìm được trị riêng trội lớn nhất $\\lambda_1$ và véctơ riêng tương ứng $v_1$ của ma trận $A$. "
        "Để tìm được trị riêng lớn thứ hai, ta cần 'khử' (triệt tiêu) ảnh hưởng của $\\lambda_1$ bằng cách tạo ra một ma trận mới:",
        "$$ A_1 = A - \\lambda_1 v_1 x^T $$",
        "(với $x$ là véctơ sao cho $x^T v_1 = 1$). Mọi trị riêng của $A_1$ đều giống $A$, ngoại trừ $\\lambda_1$ đã bị ép về 0. "
        "Do đó, khi áp dụng tiếp phương pháp Lũy thừa lên $A_1$, thuật toán sẽ hội tụ về trị riêng lớn thứ hai $\\lambda_2$ của $A$. "
        "Quá trình này lặp lại để tìm các trị riêng tiếp theo."
    ]
    display(Markdown('\n'.join(theory_md)))
    
    A = np.array(A_input, dtype=float)
    n, m = A.shape
    
    display(Math(f"A = {matrix_to_latex(A, precision=4)}"))

    A_k = A.copy()
    rank = min(n, m)
    if num_components is not None:
        rank = min(rank, num_components)
    
    if v0_input is None: v0_base = np.ones(m) / np.sqrt(m)
    else: v0_base = np.array(v0_input, dtype=float).flatten()
    
    U_cols = []
    S_vals = []
    V_cols = []
    
    approx_formula_terms = []
    
    for k in range(1, rank + 1):
        display(Markdown(f"\n### --- BƯỚC {k} ---"))
        B_k = A_k.T @ A_k
        lam, v = power_method_L2(B_k, v0_base, num_iters, tol)
        
        if lam < 1e-10:
            display(Markdown(f"⚠️ **Dừng thuật toán:** Giá trị riêng cực đại tiếp theo xấp xỉ 0."))
            break
            
        sigma = np.sqrt(lam)
        u = (A_k @ v) / sigma
        
        U_cols.append(u)
        S_vals.append(sigma)
        V_cols.append(v)
        
        display(Markdown(f"- **Giá trị kỳ dị lớn nhất (hiện tại):** $\\sigma_{k} = \\sqrt{{\\lambda_{k}}} \\approx {sigma:.4f}$"))
        display(Markdown(f"- **Vector kỳ dị phải:**"))
        display(Math(f"v_{k} = {matrix_to_latex(v, precision=4)}"))
        display(Markdown(f"- **Vector kỳ dị trái:**"))
        display(Math(f"u_{k} = \\frac{{A_{k} v_{k}}}{{\\sigma_{k}}} = {matrix_to_latex(u, precision=4)}"))
        
        approx_formula_terms.append(f"\\sigma_{k} u_{k} v_{k}^T")
        
        A_next = A_k - sigma * np.outer(u, v)
        A_k = A_next
        
    display(Markdown("\n### ❖ TỔNG KẾT VÀ XẤP XỈ MA TRẬN A"))
    approx_formula = "A \\approx " + " + ".join(approx_formula_terms)
    display(Math(approx_formula))

# DỮ LIỆU ĐỀ BÀI
C = np.array([
    [0.1588, 0.0064, 0.0025, 0.0304, 0.0014, 0.0083, 0.1594],
    [0.0057, 0.2645, 0.0436, 0.0099, 0.0083, 0.0201, 0.3413],
    [0.0264, 0.1506, 0.3557, 0.0139, 0.0142, 0.0070, 0.0236],
    [0.3299, 0.0565, 0.0495, 0.3636, 0.0204, 0.0483, 0.0649],
    [0.0089, 0.0081, 0.0333, 0.0295, 0.3412, 0.0237, 0.0020],
    [0.1190, 0.0901, 0.0996, 0.1260, 0.1722, 0.2368, 0.3369],
    [0.0063, 0.0126, 0.0196, 0.0098, 0.0064, 0.0132, 0.0012]
], dtype=float)

# ========================================================
# HÃY NHẬP SỐ THỨ TỰ (STT) CỦA BẠN VÀO ĐÂY:
a = 10 
# ========================================================

A_matrix = C + a * np.eye(7)

# Tính đúng 3 giá trị kỳ dị lớn nhất theo yêu cầu
SVD_Reduced(A_matrix, num_components=3)
"""
update_notebook(svd_path, "Giá Trị Kỳ Dị SVD (Lớn Nhất) - Có Xuống Thang", code_svd)

# ==============================================================================
# 4. CHƯƠNG 2: So sánh các phương pháp (Lý thuyết)
# ==============================================================================
chuong2_dir = os.path.join(base_dir, "CHƯƠNG 2 GIẢI PHƯƠNG TRÌNH PHI TUYẾN 1 CHIỀU")
ss_path = os.path.join(chuong2_dir, "So sánh các phương pháp (Lý thuyết).ipynb")

code_ss = r"""from IPython.display import Markdown, display

md = [
    "## ❖ SO SÁNH ƯU NHƯỢC ĐIỂM CỦA CÁC PHƯƠNG PHÁP GIẢI GẦN ĐÚNG PHƯƠNG TRÌNH $f(x) = 0$",
    "",
    "| Phương pháp | Cấp hội tụ | Ưu điểm (Nên dùng khi nào?) | Nhược điểm (Khi nào thất bại?) |",
    "| :--- | :--- | :--- | :--- |",
    "| **1. Chia đôi (Bisection)** | Tuyến tính ($p=1$) | - Đơn giản, vô cùng dễ lập trình.<br>- Chắc chắn hội tụ 100% nếu xác định được khoảng $[a, b]$ chứa nghiệm (sao cho $f(a)f(b)<0$).<br>- Tính toán và kiểm soát sai số rất trực quan. | - Tốc độ hội tụ **rất chậm**.<br>- Cần phải biết trước khoảng cách ly nghiệm.<br>- Sẽ **thất bại** nếu nghiệm là nghiệm kép hoặc đồ thị chỉ tiếp xúc với trục hoành (vì không có sự đổi dấu). |",
    "| **2. Dây cung (Secant)** | $p \\approx 1.618$ | - Tốc độ hội tụ khá nhanh (nhanh hơn Chia đôi).<br>- Điểm mạnh lớn nhất là **không cần phải tính công thức đạo hàm $f'(x)$** như phương pháp Newton. | - Tốc độ hội tụ vẫn chậm hơn Newton.<br>- Đòi hỏi phải chọn 2 giá trị xấp xỉ khởi đầu $x_0, x_1$ đủ gần với nghiệm.<br>- Có thể bị phân kỳ nếu đồ thị hàm số biến thiên quá phức tạp. |",
    "| **3. Tiếp tuyến (Newton-Raphson)** | Bậc 2 ($p=2$) | - Tốc độ hội tụ **cực kỳ nhanh** (số lượng chữ số chính xác tăng gấp đôi sau mỗi bước lặp). | - Bắt buộc phải tính được công thức đạo hàm bậc 1 $f'(x)$.<br>- Phương pháp sẽ **thất bại ngay lập tức** (chia cho 0) nếu tại bước lặp nào đó có tiếp tuyến nằm ngang ($f'(x_k) = 0$).<br>- Đòi hỏi giá trị khởi đầu $x_0$ phải nằm trong lân cận rất gần với nghiệm. |",
    "| **4. Lặp đơn (Fixed Point)** | Tuyến tính | - Công thức lặp $x_{k+1} = g(x_k)$ tự nhiên, dễ code.<br>- Không cần tính đạo hàm (nếu không cần kiểm tra điều kiện).<br>- Có thể tổng quát hóa áp dụng cho cả hệ phương trình phi tuyến. | - Điều kiện để hội tụ vô cùng khắt khe: Bắt buộc $|g'(x)| < 1$ trong lân cận nghiệm (nếu $\\ge 1$ sẽ bị phân kỳ đẩy ra xa).<br>- Tốc độ hội tụ bị phụ thuộc vào hằng số Lipschitz $q$, nếu $q$ sát 1 thì hội tụ cực kỳ chậm.<br>- Phải mất công biến đổi phương trình $f(x)=0$ thành dạng $x = g(x)$ thích hợp. |",
    "",
    "---",
    "*Ghi chú: Nội dung trên là bảng so sánh chuẩn chỉ nhất, bạn có thể bê nguyên văn vào giấy thi tự luận để lấy điểm tuyệt đối câu phân tích lý thuyết.*"
]

display(Markdown('\n'.join(md)))
"""

nb_ss = {
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": ["### Lý thuyết So sánh Phương pháp\n"]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [line + '\n' for line in code_ss.split('\n')]
  }
 ],
 "metadata": {
  "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
  "language_info": {"name": "python", "version": "3.13.7"}
 },
 "nbformat": 4, "nbformat_minor": 4
}
nb_ss['cells'][1]['source'][-1] = nb_ss['cells'][1]['source'][-1].rstrip('\n')

with open(ss_path, 'w', encoding='utf-8') as f:
    json.dump(nb_ss, f, indent=1, ensure_ascii=False)

print("Hoàn tất tạo file")
