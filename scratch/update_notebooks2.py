import json
import os
import sys

def process_notebook(path, func_name, template_code):
    print(f"Processing {path}")
    try:
        with open(path, 'r', encoding='utf-8') as f:
            nb = json.load(f)
    except FileNotFoundError:
        print(f"File not found: {path}")
        return
        
    for cell in nb['cells']:
        if cell['cell_type'] == 'code':
            source = cell['source']
            split_idx = -1
            for i, line in enumerate(source):
                if "# DỮ LIỆU" in line or "# ═══════" in line or "# NHẬP DỮ LIỆU" in line:
                    split_idx = i
                    break
            
            if split_idx != -1:
                user_data = source[split_idx:]
                
                # Split template_code into lines, keeping \n
                new_func = [line + '\n' for line in template_code.split('\n')]
                if new_func:
                    new_func[-1] = new_func[-1].rstrip('\n')
                
                cell['source'] = new_func + ['\n'] + user_data
                break
                
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)
    print(f"Done {path}")

# ==============================================================================
# TEMPLATES
# ==============================================================================

lap_don_template = '''import numpy as np
from IPython.display import display, Math, Markdown

def _mat(M, p=5):
    if hasattr(M[0], "__len__"):
        rows = " \\\\\\\\ ".join([" & ".join([f"{x:.{p}f}" for x in row]) for row in M])
        return f"\\\\begin{{bmatrix}} {rows} \\\\end{{bmatrix}}"
    inner = " \\\\\\\\ ".join([f"{x:.{p}f}" for x in M])
    return f"\\\\begin{{bmatrix}} {inner} \\\\end{{bmatrix}}"

def lap_don_he(B_input, d_input, X0_input=None, epsilon=1e-6, p_norm=np.inf):
    B = np.array(B_input, dtype=float)
    d = np.array(d_input, dtype=float).flatten()
    n = len(d)
    
    if X0_input is None:
        X_k = np.zeros(n)
    else:
        X_k = np.array(X0_input, dtype=float).flatten()
        
    display(Markdown("## ❖ PHƯƠNG PHÁP LẶP ĐƠN (HỆ PHƯƠNG TRÌNH $X = BX + d$)"))
    
    q = np.linalg.norm(B, p_norm)
    display(Markdown("### 1. Kiểm tra hội tụ"))
    display(Math(f"\\\\text{{Chuẩn }} p={p_norm} \\\\text{{ của B: }} q = {q:.4f}"))
    if q < 1:
        display(Markdown("=> $q < 1$, phương pháp lặp **hội tụ**."))
    else:
        display(Markdown("=> ⚠️ **Cảnh báo:** $q \\\\ge 1$, chưa chắc hội tụ."))
        
    display(Markdown("### 2. Quá trình lặp"))
    
    eps0 = epsilon * (1 - q) / q if q < 1 else epsilon
    display(Math(f"\\\\varepsilon_0 = \\\\frac{{\\\\varepsilon(1-q)}}{{q}} = {eps0:.5e}"))
    
    k = 1
    history = []
    diffs = []
    
    while True:
        X_new = B @ X_k + d
        diff = np.linalg.norm(X_new - X_k, p_norm)
        
        history.append(X_new.copy())
        diffs.append(diff)
        
        if diff < eps0 or k > 200:
            break
            
        X_k = X_new.copy()
        k += 1
        
    N = len(history)
    if N <= 5:
        cols = list(range(1, N+1))
    else:
        cols = [1, 2, -1, N-1, N]
        
    header = "| | " + " | ".join([f"Lần {c}" if c != -1 else "..." for c in cols]) + " |"
    sep = "|---|" + "|".join(["---" for c in cols]) + "|"
    lines = [header, sep]
    
    for i in range(n):
        row = [f"$x_{{{i+1}}}$"]
        for c in cols:
            if c == -1:
                row.append("...")
            else:
                row.append(f"{history[c-1][i]:.5f}")
        lines.append("| " + " | ".join(row) + " |")
        
    row = [f"$|| x_k - x_{{k-1}} ||$"]
    for c in cols:
        if c == -1:
            row.append("...")
        else:
            val_str = f"{diffs[c-1]:.5f}"
            if c == N:
                val_str += f" < \\\\varepsilon_0"
            elif c == N-1:
                val_str += f" > \\\\varepsilon_0"
            row.append(val_str)
    lines.append("| " + " | ".join(row) + " |")
    
    display(Markdown("\\n".join(lines)))
    
    display(Markdown("### 3. Kết luận"))
    display(Markdown(f"Hội tụ tại bước $k = {N}$. Nghiệm xấp xỉ là:"))
    display(Math(f"X \\\\approx {_mat(history[-1], 5)}"))
'''

gauss_axb_template = '''import numpy as np
from IPython.display import display, Math, Markdown

def _mat(M, p=5):
    if hasattr(M[0], "__len__"):
        rows = " \\\\\\\\ ".join([" & ".join([f"{x:.{p}f}" for x in row]) for row in M])
        return f"\\\\begin{{bmatrix}} {rows} \\\\end{{bmatrix}}"
    inner = " \\\\\\\\ ".join([f"{x:.{p}f}" for x in M])
    return f"\\\\begin{{bmatrix}} {inner} \\\\end{{bmatrix}}"

def Gauss_Seidel_Ax_B(A_input, b_input, max_iter=200, epsilon=1e-5, x0=None):
    A = np.array(A_input, dtype=float)
    b = np.array(b_input, dtype=float).flatten()
    n = len(b)
    
    if x0 is None:
        X_k = np.zeros(n)
    else:
        X_k = np.array(x0, dtype=float).flatten()
        
    display(Markdown("## ❖ PHƯƠNG PHÁP LẶP GAUSS-SEIDEL (HỆ $Ax = b$)"))
    
    D = np.diag(np.diag(A))
    L = np.tril(A, -1)
    U = np.triu(A, 1)
    
    D_inv = np.linalg.inv(D)
    B = -D_inv @ (L + U)
    d = D_inv @ b
    
    display(Markdown("### 1. Kiểm tra điều kiện hội tụ"))
    
    # Tính s, q theo chuẩn vô cùng
    s = 0.0
    q = 0.0
    for i in range(n):
        sum_l = sum(abs(A[i, j]) for j in range(i))
        sum_u = sum(abs(A[i, j]) for j in range(i+1, n))
        s_i = sum_u / abs(A[i,i]) if abs(A[i,i]) != 0 else float('inf')
        q_i = sum_l / (abs(A[i,i]) - sum_u) if (abs(A[i,i]) - sum_u) > 0 else float('inf')
        s = max(s, s_i)
        q = max(q, q_i)
        
    display(Math(f"s = {s:.5f}, \\\\quad q \\\\approx {q:.5f}"))
    
    eps0 = epsilon * (1 - s) * (1 - q) / q if q < 1 else epsilon
    display(Math(f"\\\\varepsilon_0 = \\\\frac{{\\\\varepsilon(1-s)(1-q)}}{{q}} = {eps0:.5e}"))
    
    display(Markdown("### 2. Quá trình lặp"))
    
    history = []
    diffs = []
    k = 1
    
    while True:
        X_new = np.copy(X_k)
        for i in range(n):
            s1 = sum(B[i, j] * X_new[j] for j in range(i))
            s2 = sum(B[i, j] * X_k[j] for j in range(i, n))
            X_new[i] = s1 + s2 + d[i]
            
        diff = np.linalg.norm(X_new - X_k, np.inf)
        history.append(X_new.copy())
        diffs.append(diff)
        
        if diff < eps0 or k >= max_iter:
            break
            
        X_k = np.copy(X_new)
        k += 1
        
    N = len(history)
    if N <= 5:
        cols = list(range(1, N+1))
    else:
        cols = [1, 2, -1, N-1, N]
        
    header = "| | " + " | ".join([f"Lần {c}" if c != -1 else "..." for c in cols]) + " |"
    sep = "|---|" + "|".join(["---" for c in cols]) + "|"
    lines = [header, sep]
    
    for i in range(n):
        row = [f"$x_{{{i+1}}}$"]
        for c in cols:
            if c == -1:
                row.append("...")
            else:
                row.append(f"{history[c-1][i]:.5f}")
        lines.append("| " + " | ".join(row) + " |")
        
    row = [f"$|| x_k - x_{{k-1}} ||$"]
    for c in cols:
        if c == -1:
            row.append("...")
        else:
            val_str = f"{diffs[c-1]:.5f}"
            if c == N:
                val_str += f" < \\\\varepsilon_0"
            elif c == N-1:
                val_str += f" > \\\\varepsilon_0"
            row.append(val_str)
    lines.append("| " + " | ".join(row) + " |")
    
    display(Markdown("\\n".join(lines)))
    
    display(Markdown("### 3. Kết luận"))
    display(Markdown(f"Nghiệm xấp xỉ sau {N} lần lặp:"))
    display(Math(f"X \\\\approx {_mat(history[-1], 5)}"))
'''

gauss_bxd_template = '''import numpy as np
from IPython.display import display, Math, Markdown

def _mat(M, p=5):
    if hasattr(M[0], "__len__"):
        rows = " \\\\\\\\ ".join([" & ".join([f"{x:.{p}f}" for x in row]) for row in M])
        return f"\\\\begin{{bmatrix}} {rows} \\\\end{{bmatrix}}"
    inner = " \\\\\\\\ ".join([f"{x:.{p}f}" for x in M])
    return f"\\\\begin{{bmatrix}} {inner} \\\\end{{bmatrix}}"

def Gauss_Seidel_Bd(B_input, d_input, max_iter=200, epsilon=1e-5, x0=None):
    B = np.array(B_input, dtype=float)
    d = np.array(d_input, dtype=float).flatten()
    n = len(d)
    
    if x0 is None:
        X_k = np.zeros(n)
    else:
        X_k = np.array(x0, dtype=float).flatten()
        
    display(Markdown("## ❖ PHƯƠNG PHÁP LẶP GAUSS-SEIDEL (HỆ $x = Bx + d$)"))
    
    display(Markdown("### 1. Quá trình lặp"))
    
    eps0 = epsilon if epsilon is not None else 1e-5
    
    history = []
    diffs = []
    k = 1
    
    while True:
        X_new = np.copy(X_k)
        for i in range(n):
            sum_val = d[i]
            for j in range(n):
                sum_val += B[i, j] * X_new[j]
            X_new[i] = sum_val
            
        diff = np.linalg.norm(X_new - X_k, np.inf)
        history.append(X_new.copy())
        diffs.append(diff)
        
        if diff < eps0 or k >= max_iter:
            break
            
        X_k = np.copy(X_new)
        k += 1
        
    N = len(history)
    if N <= 5:
        cols = list(range(1, N+1))
    else:
        cols = [1, 2, -1, N-1, N]
        
    header = "| | " + " | ".join([f"Lần {c}" if c != -1 else "..." for c in cols]) + " |"
    sep = "|---|" + "|".join(["---" for c in cols]) + "|"
    lines = [header, sep]
    
    for i in range(n):
        row = [f"$x_{{{i+1}}}$"]
        for c in cols:
            if c == -1:
                row.append("...")
            else:
                row.append(f"{history[c-1][i]:.5f}")
        lines.append("| " + " | ".join(row) + " |")
        
    row = [f"$|| x_k - x_{{k-1}} ||$"]
    for c in cols:
        if c == -1:
            row.append("...")
        else:
            val_str = f"{diffs[c-1]:.5f}"
            if c == N:
                val_str += f" < \\\\varepsilon_0"
            elif c == N-1:
                val_str += f" > \\\\varepsilon_0"
            row.append(val_str)
    lines.append("| " + " | ".join(row) + " |")
    
    display(Markdown("\\n".join(lines)))
    
    display(Markdown("### 2. Kết luận"))
    display(Markdown(f"Nghiệm xấp xỉ sau {N} lần lặp:"))
    display(Math(f"X \\\\approx {_mat(history[-1], 5)}"))
'''

base = r'd:\code\Uni\On_thi_cuoi_ky\Giai_tich_so\scripts\CHƯƠNG 4 GIẢI HỆ ĐẠI SỐ TUYẾN TÍNH & TÌM MA TRẬN NGHỊCH ĐẢO'
process_notebook(os.path.join(base, 'Lặp đơn (Hệ phương trình).ipynb'), 'lap_don_he', lap_don_template)
process_notebook(os.path.join(base, r'Lặp Jacobi - Lặp Đơn\Lặp Đơn (x=Bx+d).ipynb'), 'lap_don_he', lap_don_template)
process_notebook(os.path.join(base, r'Lặp Gauss-Seidel\Lặp Gauss-Seidel (Ax=B).ipynb'), 'Gauss_Seidel_Ax_B', gauss_axb_template)
process_notebook(os.path.join(base, r'Lặp Gauss-Seidel\Lặp Gauss-Seidel (x=Bx+d).ipynb'), 'Gauss_Seidel_Bd', gauss_bxd_template)
process_notebook(os.path.join(base, r'Lặp Gauss-Seidel\Lặp Gauss-Seidel (Đổi dòng tạo chéo trội).ipynb'), 'Gauss_Seidel_Ax_B', gauss_axb_template)
