import numpy as np
from IPython.display import display, Math, Markdown

def _mat(M, p=5):
    if hasattr(M[0], "__len__"):
        rows = " \\\\ ".join([" & ".join([f"{x:.{p}f}" for x in row]) for row in M])
        return f"\\begin{{bmatrix}} {rows} \\end{{bmatrix}}"
    inner = " \\\\ ".join([f"{x:.{p}f}" for x in M])
    return f"\\begin{{bmatrix}} {inner} \\end{{bmatrix}}"

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
        
        if diff < eps0 or (max_iter is not None and k >= max_iter) or k > 200:
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
                val_str += f" < \\varepsilon_0"
            elif c == N-1:
                val_str += f" > \\varepsilon_0"
            row.append(val_str)
    lines.append("| " + " | ".join(row) + " |")
    
    display(Markdown("\n".join(lines)))
    
    display(Markdown("### 2. Kết luận"))
    display(Markdown(f"Nghiệm xấp xỉ sau {N} lần lặp:"))
    display(Math(f"X \\approx {_mat(history[-1], 5)}"))

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
