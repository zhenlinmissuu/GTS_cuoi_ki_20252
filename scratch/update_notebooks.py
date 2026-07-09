import json
import os
import sys
sys.stdout.reconfigure(encoding='utf-8')

def modify_notebook(path, new_code):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            nb = json.load(f)
    except FileNotFoundError:
        print(f"Skipping {path}, not found.")
        return
        
    # Find the first code cell
    for cell in nb['cells']:
        if cell['cell_type'] == 'code':
            # Split new_code by lines, appending \n
            lines = [line + '\n' for line in new_code.split('\n')]
            # Remove trailing \n from the last line to be clean
            if lines:
                lines[-1] = lines[-1].rstrip('\n')
            cell['source'] = lines
            break
            
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)
    print(f"Updated {path}")

lap_don_code = '''import numpy as np
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
        X_k = np.copy(d)
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
    X_prev = np.copy(X_k)
    X_k = B @ X_prev + d
    
    history = []
    diffs = []
    
    while True:
        diff = np.linalg.norm(X_k - X_prev, p_norm)
        history.append(X_k.copy())
        diffs.append(diff)
        
        if diff < eps0 or k > 200:
            break
            
        X_prev = X_k.copy()
        X_k = B @ X_prev + d
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

# ═══════════════════════════════════════════════════════════════════
# NHẬP DỮ LIỆU CỦA BẠN VÀO ĐÂY
# ═══════════════════════════════════════════════════════════════════
# Vi du: Ax = b, viet lai thanh x = Bx + d
# A = I - C voi C la ma trận he so va d la ve phai
A = np.array([
    [10.0, 1.0,  2.0],
    [ 1.0, 10.0, 3.0],
    [ 2.0,  3.0, 10.0]
], dtype=float)

b = np.array([7.0, 8.0, 9.0], dtype=float)
n = len(b)
I = np.eye(n)

# Bien doi ve dang x = Bx + d
B = I - A / np.diag(A)[:, None]
d = b / np.diag(A)
# ═══════════════════════════════════════════════════════════════════

lap_don_he(B, d, np.zeros(n), epsilon=1e-6)
'''

gauss_code = '''import numpy as np
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
        
    display(Markdown("## ❖ PHƯƠNG PHÁP LẶP GAUSS-SEIDEL"))
    
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

# ═══════════════════════════════════════════════════════════════════
# NHẬP DỮ LIỆU CỦA BẠN VÀO ĐÂY
# ═══════════════════════════════════════════════════════════════════
A = np.array([
    [10.0, 1.0,  2.0],
    [ 1.0, 10.0, 3.0],
    [ 2.0,  3.0, 10.0]
], dtype=float)

b = np.array([7.0, 8.0, 9.0], dtype=float)
# ═══════════════════════════════════════════════════════════════════

Gauss_Seidel_Ax_B(A, b, max_iter=200, epsilon=1e-5)
'''

base = r'd:\code\Uni\On_thi_cuoi_ky\Giai_tich_so\scripts\CHƯƠNG 4 GIẢI HỆ ĐẠI SỐ TUYẾN TÍNH & TÌM MA TRẬN NGHỊCH ĐẢO'
modify_notebook(os.path.join(base, 'Lặp đơn (Hệ phương trình).ipynb'), lap_don_code)
modify_notebook(os.path.join(base, r'Lặp Jacobi - Lặp Đơn\Lặp Đơn (x=Bx+d).ipynb'), lap_don_code)

modify_notebook(os.path.join(base, r'Lặp Gauss-Seidel\Lặp Gauss-Seidel (Ax=B).ipynb'), gauss_code)
modify_notebook(os.path.join(base, r'Lặp Gauss-Seidel\Lặp Gauss-Seidel (x=Bx+d).ipynb'), gauss_code)
modify_notebook(os.path.join(base, r'Lặp Gauss-Seidel\Lặp Gauss-Seidel (Đổi dòng tạo chéo trội).ipynb'), gauss_code)
