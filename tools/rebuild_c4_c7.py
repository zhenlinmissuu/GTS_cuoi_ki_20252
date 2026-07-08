import os, json

BASE = "d:/code/Uni/On_thi_cuoi_ky/Giải tích số/scripts"
METADATA = {
    "kernelspec": {"display_name": "Python 3 (ipykernel)", "language": "python", "name": "python3"},
    "language_info": {
        "codemirror_mode": {"name": "ipython", "version": 3},
        "file_extension": ".py", "mimetype": "text/x-python",
        "name": "python",
        "nbconvert_exporter": "python", "pygments_lexer": "ipython3",
        "version": "3.13.7"
    }
}

def write_nb(path, title, code):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    src = [line + "\n" for line in code.split("\n")]
    if src: src[-1] = src[-1].rstrip("\n")
    nb = {
        "cells": [
            {"cell_type": "markdown", "metadata": {}, "source": [f"### {title}\n"]},
            {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": src}
        ],
        "metadata": METADATA, "nbformat": 4, "nbformat_minor": 4
    }
    with open(path, "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)

C4  = os.path.join(BASE, "CHƯƠNG 4 GIẢI HỆ ĐẠI SỐ TUYẾN TÍNH & TÌM MA TRẬN NGHỊCH ĐẢO")
C4GS = os.path.join(C4, "Lặp Gauss-Seidel")
C4JA = os.path.join(C4, "Lặp Jacobi - Lặp Đơn")
C5   = os.path.join(BASE, "CHƯƠNG 5 GIÁ TRỊ RIÊNG VÀ VECTOR RIÊNG CỦA MA TRẬN")
C6   = os.path.join(BASE, "CHƯƠNG 6 NỘI SUY VÀ ĐẠO HÀM SỐ")
C7   = os.path.join(BASE, "CHƯƠNG 7 GIẢI PHƯƠNG TRÌNH VI PHÂN")
C2   = os.path.join(BASE, "CHƯƠNG 2 GIẢI PHƯƠNG TRÌNH PHI TUYẾN 1 CHIỀU")

# Shared LaTeX helpers (included at top of each notebook)
LATEX_HELPERS = '''
def _mat(M, p=4):
    if hasattr(M, "__len__") and hasattr(M[0], "__len__"):
        rows = " \\\\\\\\ ".join([" & ".join([f"{x:.{p}f}" for x in row]) for row in M])
        return f"\\\\begin{{bmatrix}} {rows} \\\\end{{bmatrix}}"
    else:
        inner = " \\\\\\\\ ".join([f"{x:.{p}f}" for x in M])
        return f"\\\\begin{{bmatrix}} {inner} \\\\end{{bmatrix}}^T"
'''

# ══════════════════════════════════════════════════════════════════════════════
# CHAPTER 4 – Phân tách LU
# ══════════════════════════════════════════════════════════════════════════════
code_lu = '''import numpy as np
from IPython.display import display, Math, Markdown

def _mat(M, p=4):
    if hasattr(M[0], "__len__"):
        rows = " \\\\\\\\ ".join([" & ".join([f"{x:.{p}f}" for x in row]) for row in M])
        return f"\\\\begin{{bmatrix}} {rows} \\\\end{{bmatrix}}"
    inner = " \\\\\\\\ ".join([f"{x:.{p}f}" for x in M])
    return f"\\\\begin{{bmatrix}} {inner} \\\\end{{bmatrix}}^T"

def phan_tach_LU(A_input):
    # Phan tach LU khong hoán vi: A = L * U
    # A_input: ma tran vuong n x n
    A = np.array(A_input, dtype=float)
    n = A.shape[0]
    display(Markdown("## phong PHÂN TÁCH LU (Gaussian Elimination)"))
    display(Math(f"A = {_mat(A)}"))
    display(Math(r"A = L \\cdot U"))

    L = np.eye(n)
    U = A.copy()

    for k in range(n - 1):
        display(Markdown(f"#### Khử cột $k = {k+1}$"))
        if abs(U[k, k]) < 1e-14:
            display(Markdown(f"WARNING: Phan tu pivot $U_{{{k+1},{k+1}}} = 0$ — ma tran suy bien!"))
            return None, None
        for i in range(k + 1, n):
            m = U[i, k] / U[k, k]
            L[i, k] = m
            U[i, :] -= m * U[k, :]
            display(Math(f"l_{{{i+1},{k+1}}} = \\\\frac{{U_{{{i+1},{k+1}}}}}{{U_{{{k+1},{k+1}}}}} = \\\\frac{{{U[i,k] + m*U[k,k]:.4f}}}{{{U[k,k]+0:.4f}}} = {m:.4f}"))
        display(Math(f"U \\\\leftarrow {_mat(U)}"))

    display(Markdown("### Ket qua"))
    display(Math(f"L = {_mat(L)}"))
    display(Math(f"U = {_mat(U)}"))
    display(Markdown("**Kiem tra:** $L \\\\cdot U$:"))
    display(Math(f"L \\\\cdot U = {_mat(L @ U)}"))
    return L, U

def giai_he_LU(A_input, b_input):
    # Giai Ax = b qua phan tach LU: Ly = b, Ux = y
    A = np.array(A_input, dtype=float)
    b = np.array(b_input, dtype=float).flatten()
    n = len(b)
    L, U = phan_tach_LU(A)
    if L is None: return None

    # Giai Ly = b (thay the tien)
    display(Markdown("#### Giai $Ly = b$ (the the tien)"))
    y = np.zeros(n)
    for i in range(n):
        y[i] = b[i] - sum(L[i, j] * y[j] for j in range(i))
        display(Math(f"y_{{{i+1}}} = {y[i]:.6f}"))

    # Giai Ux = y (thay the lui)
    display(Markdown("#### Giai $Ux = y$ (the the lui)"))
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - sum(U[i, j] * x[j] for j in range(i + 1, n))) / U[i, i]
        display(Math(f"x_{{{i+1}}} = {x[i]:.6f}"))

    display(Markdown("**Kiem tra:** $Ax$:"))
    display(Math(f"Ax = {_mat(A @ x)} \\\\approx b = {_mat(b)}"))
    return x

# ═══════════════════════════════════════════════════════════════════
# NHAP DU LIEU CUA BAN VAO DAY
# ═══════════════════════════════════════════════════════════════════
A = np.array([
    [2.0, 1.0,  1.0],
    [4.0, -6.0, 0.0],
    [-2.0, 7.0, 2.0]
])

b = np.array([5.0, -2.0, 9.0])
# ═══════════════════════════════════════════════════════════════════

# Chi phan tach LU:
# phan_tach_LU(A)

# Hoac giai he Ax = b:
giai_he_LU(A, b)
'''

# ══════════════════════════════════════════════════════════════════════════════
# CHAPTER 4 – Phân tách Cholesky
# ══════════════════════════════════════════════════════════════════════════════
code_cholesky = '''import numpy as np
from IPython.display import display, Math, Markdown

def _mat(M, p=4):
    if hasattr(M[0], "__len__"):
        rows = " \\\\\\\\ ".join([" & ".join([f"{x:.{p}f}" for x in row]) for row in M])
        return f"\\\\begin{{bmatrix}} {rows} \\\\end{{bmatrix}}"
    inner = " \\\\\\\\ ".join([f"{x:.{p}f}" for x in M])
    return f"\\\\begin{{bmatrix}} {inner} \\\\end{{bmatrix}}^T"

def phan_tach_Cholesky(A_input):
    # Phan tach Cholesky: A = L * L^T (A phai doi xung xac dinh duong)
    A = np.array(A_input, dtype=float)
    n = A.shape[0]
    display(Markdown("## phong PHÂN TÁCH CHOLESKY ($A = L L^T$)"))
    display(Math(f"A = {_mat(A)}"))

    L = np.zeros((n, n))
    for i in range(n):
        # Tinh duong cheo
        s = sum(L[i, k]**2 for k in range(i))
        val = A[i, i] - s
        if val <= 0:
            display(Markdown(f"WARNING: $A_{{{i+1},{i+1}}} - \\\\sum l^2 = {val:.4f} \\\\leq 0$ — ma tran khong xac dinh duong!"))
            return None
        L[i, i] = np.sqrt(val)
        display(Math(f"l_{{{i+1},{i+1}}} = \\\\sqrt{{A_{{{i+1},{i+1}}} - \\\\sum_{{k<{i+1}}} l_{{ik}}^2}} = \\\\sqrt{{{val:.4f}}} = {L[i,i]:.4f}"))

        # Tinh phan duoi duong cheo
        for j in range(i + 1, n):
            s2 = sum(L[j, k] * L[i, k] for k in range(i))
            L[j, i] = (A[j, i] - s2) / L[i, i]
            display(Math(f"l_{{{j+1},{i+1}}} = \\\\frac{{A_{{{j+1},{i+1}}} - \\\\sum_{{k}} l_{{jk}}l_{{ik}}}}{{{L[i,i]:.4f}}} = {L[j,i]:.4f}"))

    display(Markdown("### Ket qua"))
    display(Math(f"L = {_mat(L)}"))
    display(Markdown("**Kiem tra:** $L \\\\cdot L^T$:"))
    display(Math(f"L L^T = {_mat(L @ L.T)}"))
    return L

def giai_he_Cholesky(A_input, b_input):
    # Giai Ax = b qua Cholesky: Ly = b, L^T x = y
    A = np.array(A_input, dtype=float)
    b = np.array(b_input, dtype=float).flatten()
    n = len(b)
    L = phan_tach_Cholesky(A)
    if L is None: return None

    # Ly = b
    display(Markdown("#### Giai $Ly = b$"))
    y = np.zeros(n)
    for i in range(n):
        y[i] = (b[i] - sum(L[i, j]*y[j] for j in range(i))) / L[i, i]
        display(Math(f"y_{{{i+1}}} = {y[i]:.6f}"))

    # L^T x = y
    display(Markdown("#### Giai $L^T x = y$"))
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - sum(L[j, i]*x[j] for j in range(i + 1, n))) / L[i, i]
        display(Math(f"x_{{{i+1}}} = {x[i]:.6f}"))

    display(Markdown("**Kiem tra:** $Ax$:"))
    display(Math(f"Ax = {_mat(A @ x)} \\\\approx b = {_mat(b)}"))
    return x

# ═══════════════════════════════════════════════════════════════════
# NHAP DU LIEU CUA BAN VAO DAY
# ═══════════════════════════════════════════════════════════════════
# A phai doi xung xac dinh duong
A = np.array([
    [4.0,  12.0, -16.0],
    [12.0, 37.0, -43.0],
    [-16.0, -43.0, 98.0]
])

b = np.array([1.0, 0.0, 0.0])
# ═══════════════════════════════════════════════════════════════════

# Chi phan tach:
# phan_tach_Cholesky(A)

# Hoac giai he Ax = b:
giai_he_Cholesky(A, b)
'''

# ══════════════════════════════════════════════════════════════════════════════
# CHAPTER 4 – LU có Pivoting
# ══════════════════════════════════════════════════════════════════════════════
code_lu_pivot = '''import numpy as np
from IPython.display import display, Math, Markdown

def _mat(M, p=4):
    if hasattr(M[0], "__len__"):
        rows = " \\\\\\\\ ".join([" & ".join([f"{x:.{p}f}" for x in row]) for row in M])
        return f"\\\\begin{{bmatrix}} {rows} \\\\end{{bmatrix}}"
    inner = " \\\\\\\\ ".join([f"{x:.{p}f}" for x in M])
    return f"\\\\begin{{bmatrix}} {inner} \\\\end{{bmatrix}}^T"

def LU_Pivoting(A_input, b_input=None):
    # Phan tach LU voi chon pivot rieng phan (PA = LU)
    # A_input: ma tran vuong n x n
    # b_input: ve phai (tuy chon) de giai he Ax = b
    A = np.array(A_input, dtype=float)
    n = A.shape[0]
    display(Markdown("## phong PHÂN TÁCH LU CÓ HOÁN VỊ ($PA = LU$)"))
    display(Math(f"A = {_mat(A)}"))

    P = np.eye(n)
    L = np.zeros((n, n))
    U = A.copy()

    for k in range(n - 1):
        # Chon pivot
        max_row = k + np.argmax(np.abs(U[k:, k]))
        if max_row != k:
            U[[k, max_row], :] = U[[max_row, k], :]
            P[[k, max_row], :] = P[[max_row, k], :]
            if k > 0:
                L[[k, max_row], :k] = L[[max_row, k], :k]
            display(Markdown(f"Hoan vi hang {k+1} va hang {max_row+1}"))

        for i in range(k + 1, n):
            if abs(U[k, k]) < 1e-14: continue
            m = U[i, k] / U[k, k]
            L[i, k] = m
            U[i, :] -= m * U[k, :]
        L[k, k] = 1.0

    L[n-1, n-1] = 1.0

    display(Markdown("### Ket qua phan tach"))
    display(Math(f"P = {_mat(P)}"))
    display(Math(f"L = {_mat(L)}"))
    display(Math(f"U = {_mat(U)}"))
    display(Markdown("**Kiem tra $PA = LU$:**"))
    display(Math(f"PA = {_mat(P @ A_input)}"))
    display(Math(f"LU = {_mat(L @ U)}"))

    if b_input is not None:
        b = np.array(b_input, dtype=float).flatten()
        pb = P @ b
        # Ly = Pb
        display(Markdown("#### Giai $Ly = Pb$"))
        y = np.zeros(n)
        for i in range(n):
            y[i] = pb[i] - sum(L[i, j]*y[j] for j in range(i))
            display(Math(f"y_{{{i+1}}} = {y[i]:.6f}"))
        # Ux = y
        display(Markdown("#### Giai $Ux = y$"))
        x = np.zeros(n)
        for i in range(n - 1, -1, -1):
            x[i] = (y[i] - sum(U[i, j]*x[j] for j in range(i + 1, n))) / U[i, i]
            display(Math(f"x_{{{i+1}}} = {x[i]:.6f}"))
        display(Markdown("**Kiem tra $Ax$:**"))
        display(Math(f"Ax = {_mat(np.array(A_input) @ x)} \\\\approx b = {_mat(b)}"))
        return L, U, P, x
    return L, U, P

# ═══════════════════════════════════════════════════════════════════
# NHAP DU LIEU CUA BAN VAO DAY
# ═══════════════════════════════════════════════════════════════════
A = np.array([
    [2.0, 1.0,  1.0],
    [4.0, 3.0,  3.0],
    [8.0, 7.0,  9.0]
])

b = np.array([1.0, 1.0, -1.0])   # bo qua neu chi can phan tach
# ═══════════════════════════════════════════════════════════════════

LU_Pivoting(A, b)
'''

# ══════════════════════════════════════════════════════════════════════════════
# CHAPTER 4 – Nghịch đảo bằng Cholesky
# ══════════════════════════════════════════════════════════════════════════════
code_inv_chol = '''import numpy as np
from IPython.display import display, Math, Markdown

def _mat(M, p=4):
    if hasattr(M[0], "__len__"):
        rows = " \\\\\\\\ ".join([" & ".join([f"{x:.{p}f}" for x in row]) for row in M])
        return f"\\\\begin{{bmatrix}} {rows} \\\\end{{bmatrix}}"
    inner = " \\\\\\\\ ".join([f"{x:.{p}f}" for x in M])
    return f"\\\\begin{{bmatrix}} {inner} \\\\end{{bmatrix}}^T"

def nghich_dao_Cholesky(A_input):
    # Tim nghich dao A^-1 qua phan tach Cholesky (A = LL^T)
    # Giai LL^T * X = I cot theo cot
    A = np.array(A_input, dtype=float)
    n = A.shape[0]
    display(Markdown("## phong TÌM MA TRẬN NGHỊCH ĐẢO $A^{-1}$ QUA CHOLESKY"))
    display(Math(f"A = {_mat(A)}"))

    # Phan tach Cholesky
    L = np.zeros((n, n))
    for i in range(n):
        s = sum(L[i, k]**2 for k in range(i))
        val = A[i, i] - s
        if val <= 0:
            display(Markdown("WARNING: Khong xac dinh duong — khong the dung Cholesky!"))
            return None
        L[i, i] = np.sqrt(val)
        for j in range(i + 1, n):
            L[j, i] = (A[j, i] - sum(L[j, k]*L[i, k] for k in range(i))) / L[i, i]

    display(Math(f"L = {_mat(L)}"))

    # Giai LL^T x_j = e_j cho moi cot j
    X = np.zeros((n, n))
    for j in range(n):
        e = np.zeros(n); e[j] = 1.0
        # Ly = e
        y = np.zeros(n)
        for i in range(n):
            y[i] = (e[i] - sum(L[i, k]*y[k] for k in range(i))) / L[i, i]
        # L^T x = y
        x = np.zeros(n)
        for i in range(n - 1, -1, -1):
            x[i] = (y[i] - sum(L[k, i]*x[k] for k in range(i + 1, n))) / L[i, i]
        X[:, j] = x

    display(Markdown("### Ket qua"))
    display(Math(f"A^{{-1}} = {_mat(X)}"))
    display(Markdown("**Kiem tra $A \\\\cdot A^{{-1}}$:**"))
    display(Math(f"A A^{{-1}} = {_mat(A @ X)}"))
    return X

# ═══════════════════════════════════════════════════════════════════
# NHAP DU LIEU CUA BAN VAO DAY
# ═══════════════════════════════════════════════════════════════════
A = np.array([
    [4.0,  2.0,  2.0],
    [2.0,  5.0,  3.0],
    [2.0,  3.0, 10.0]
])
# ═══════════════════════════════════════════════════════════════════

nghich_dao_Cholesky(A)
'''

# ══════════════════════════════════════════════════════════════════════════════
# CHAPTER 4 – Viền quanh (Bordering method for inverse)
# ══════════════════════════════════════════════════════════════════════════════
code_vien_quanh = '''import numpy as np
from IPython.display import display, Math, Markdown

def _mat(M, p=4):
    if hasattr(M[0], "__len__"):
        rows = " \\\\\\\\ ".join([" & ".join([f"{x:.{p}f}" for x in row]) for row in M])
        return f"\\\\begin{{bmatrix}} {rows} \\\\end{{bmatrix}}"
    inner = " \\\\\\\\ ".join([f"{x:.{p}f}" for x in M])
    return f"\\\\begin{{bmatrix}} {inner} \\\\end{{bmatrix}}^T"

def vien_quanh(A_input):
    # Phuong phap Vien quanh de tinh A^-1 theo tung buoc tang kich thuoc
    # A_input: ma tran vuong n x n
    A = np.array(A_input, dtype=float)
    n = A.shape[0]
    display(Markdown("## phong PHƯƠNG PHÁP VIỀN QUANH (Bordering Method)"))
    display(Math(f"A = {_mat(A)}"))
    display(Markdown("Xay dung $A_k^{-1}$ tu $A_1^{-1}$ len $A_n^{-1}$ theo tung buoc."))

    # A_1^-1
    if abs(A[0, 0]) < 1e-14:
        display(Markdown("WARNING: A[0,0] = 0"))
        return None
    Ak_inv = np.array([[1.0 / A[0, 0]]])
    display(Math(f"A_1^{{-1}} = {_mat(Ak_inv)}"))

    for k in range(1, n):
        # Phan mo rong
        a_new = A[:k, k]         # cot k moi (phan tren)
        b_new = A[k, :k]         # hang k moi (phan trai)
        alpha = A[k, k]          # phan tu goc duoi-phai

        u = Ak_inv @ a_new
        v = b_new @ Ak_inv

        delta = alpha - b_new @ u
        if abs(delta) < 1e-14:
            display(Markdown(f"WARNING: delta = {delta:.4e} xap xi 0 tai buoc k={k+1}!"))
            return None

        # Cong thuc vien quanh
        A_new_inv = np.zeros((k + 1, k + 1))
        A_new_inv[:k, :k] = Ak_inv + np.outer(u, v) / delta
        A_new_inv[:k, k]  = -u / delta
        A_new_inv[k, :k]  = -v / delta
        A_new_inv[k, k]   = 1.0 / delta

        Ak_inv = A_new_inv
        display(Markdown(f"**Buoc k = {k+1}:** $\\\\delta_{{k+1}} = {delta:.4f}$"))
        display(Math(f"A_{{{k+1}}}^{{-1}} = {_mat(Ak_inv)}"))

    display(Markdown("### Ket qua cuoi cung"))
    display(Math(f"A^{{-1}} = {_mat(Ak_inv)}"))
    display(Markdown("**Kiem tra $A \\\\cdot A^{{-1}}$:**"))
    display(Math(f"A A^{{-1}} = {_mat(A @ Ak_inv)}"))
    return Ak_inv

# ═══════════════════════════════════════════════════════════════════
# NHAP DU LIEU CUA BAN VAO DAY
# ═══════════════════════════════════════════════════════════════════
A = np.array([
    [3.0, 1.0, 2.0],
    [1.0, 4.0, 1.0],
    [2.0, 1.0, 5.0]
])
# ═══════════════════════════════════════════════════════════════════

vien_quanh(A)
'''

write_nb(os.path.join(C4, "Phân tách LU.ipynb"),            "Phân tách LU và Giải hệ Ax=b",            code_lu)
write_nb(os.path.join(C4, "Phân tách Cholesky.ipynb"),      "Phân tách Cholesky (A = LL^T)",            code_cholesky)
write_nb(os.path.join(C4, "LU có Pivoting.ipynb"),          "LU có Hoán vị Pivot (PA = LU)",            code_lu_pivot)
write_nb(os.path.join(C4, "Nghịch đảo bằng Cholesky.ipynb"), "Nghịch đảo qua Cholesky",               code_inv_chol)
write_nb(os.path.join(C4, "Viền quanh.ipynb"),              "Phương pháp Viền quanh (Bordering)",       code_vien_quanh)
print("Chapter 4 direct files done")

# ══════════════════════════════════════════════════════════════════════════════
# CHAPTER 4 – GS Ax=B and Gauss-Seidel permutation: clean data section only
# ══════════════════════════════════════════════════════════════════════════════
# Read existing GS Ax=B, strip stale data at bottom
for nb_path, call_example in [
    (os.path.join(C4GS, "Lặp Gauss-Seidel (Ax=B).ipynb"),
     '''# ═══════════════════════════════════════════════════════════════════
# NHAP DU LIEU CUA BAN VAO DAY
# ═══════════════════════════════════════════════════════════════════
A = np.array([
    [10.0, 1.0,  2.0],
    [ 1.0, 10.0, 3.0],
    [ 2.0,  3.0, 10.0]
], dtype=float)

b = np.array([7.0, 8.0, 9.0], dtype=float)
# ═══════════════════════════════════════════════════════════════════

Gauss_Seidel_Axb(A, b, max_iter=None, epsilon=1e-6)
'''),
    (os.path.join(C4GS, "Lặp Gauss-Seidel (Đổi dòng tạo chéo trội).ipynb"),
     '''# ═══════════════════════════════════════════════════════════════════
# NHAP DU LIEU CUA BAN VAO DAY
# ═══════════════════════════════════════════════════════════════════
A = np.array([
    [ 2.0, 10.0,  1.0],
    [10.0,  1.0,  2.0],
    [ 1.0,  2.0, 10.0]
], dtype=float)

b = np.array([13.0, 13.0, 13.0], dtype=float)
# ═══════════════════════════════════════════════════════════════════

Gauss_Seidel_permute(A, b, max_iter=None, epsilon=1e-6)
'''),
    (os.path.join(C4JA, "Lặp Jacobi (Ax=b).ipynb"),
     '''# ═══════════════════════════════════════════════════════════════════
# NHAP DU LIEU CUA BAN VAO DAY
# ═══════════════════════════════════════════════════════════════════
A = np.array([
    [10.0, 1.0,  2.0],
    [ 1.0, 10.0, 3.0],
    [ 2.0,  3.0, 10.0]
], dtype=float)

b = np.array([7.0, 8.0, 9.0], dtype=float)
# ═══════════════════════════════════════════════════════════════════

Jacobi_Axb(A, b, max_iter=None, epsilon=1e-6)
'''),
    (os.path.join(C4JA, "Lặp Jacobi (Đổi dòng tạo chéo trội).ipynb"),
     '''# ═══════════════════════════════════════════════════════════════════
# NHAP DU LIEU CUA BAN VAO DAY
# ═══════════════════════════════════════════════════════════════════
A = np.array([
    [ 2.0, 10.0,  1.0],
    [10.0,  1.0,  2.0],
    [ 1.0,  2.0, 10.0]
], dtype=float)

b = np.array([13.0, 13.0, 13.0], dtype=float)
# ═══════════════════════════════════════════════════════════════════

Jacobi_permute(A, b, max_iter=None, epsilon=1e-6)
'''),
]:
    if not os.path.exists(nb_path):
        continue
    with open(nb_path, "r", encoding="utf-8") as f:
        nb = json.load(f)
    # Find main code cell (index 1)
    code_cell = nb["cells"][1]
    src_lines = code_cell["source"]
    # Strip everything from "# DU LIEU" or "# ════" marker
    combined = "".join(src_lines)
    # Find function definition end and chop old data
    markers = ["# DỮ LIỆU", "# ═══", "# ====", "# Dữ liệu", "C = np.array", "a = 10", "A = np.array(["]
    cut_pos = len(combined)
    for marker in markers:
        pos = combined.rfind(marker)
        if pos > 100:  # not too early
            cut_pos = min(cut_pos, pos)
    new_src = combined[:cut_pos].rstrip() + "\n\n" + call_example
    new_lines = [line + "\n" for line in new_src.split("\n")]
    if new_lines: new_lines[-1] = new_lines[-1].rstrip("\n")
    code_cell["source"] = new_lines
    code_cell["outputs"] = []
    with open(nb_path, "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
    print(f"  Cleaned: {os.path.basename(nb_path)}")

print("Chapter 4 GS/Jacobi files cleaned")

# ══════════════════════════════════════════════════════════════════════════════
# CHAPTER 4 – Lặp đơn (Hệ phương trình): clean data
# ══════════════════════════════════════════════════════════════════════════════
lap_don_he_path = os.path.join(C4, "Lặp đơn (Hệ phương trình).ipynb")
if os.path.exists(lap_don_he_path):
    with open(lap_don_he_path, "r", encoding="utf-8") as f:
        nb = json.load(f)
    code_cell = nb["cells"][1]
    combined = "".join(code_cell["source"])
    markers = ["# DỮ LIỆU", "# ═══", "# ====", "B_demo", "G_demo", "A = np.array"]
    cut_pos = len(combined)
    for marker in markers:
        pos = combined.rfind(marker)
        if pos > 100:
            cut_pos = min(cut_pos, pos)
    data_section = '''# ═══════════════════════════════════════════════════════════════════
# NHAP DU LIEU CUA BAN VAO DAY
# ═══════════════════════════════════════════════════════════════════
# Vi du: Ax = b, viet lai thanh x = Bx + d
# A = I - C voi C la ma tran he so va d la ve phai
A = np.array([
    [10.0, 1.0,  2.0],
    [ 1.0, 10.0, 3.0],
    [ 2.0,  3.0, 10.0]
], dtype=float)

b = np.array([7.0, 8.0, 9.0], dtype=float)
n = len(b)
I = np.eye(n)

# Bien doi ve dang x = Bx + d
# Neu dang thuan tuy x = Bx + d, chi can nhap B va d truc tiep:
B = I - A / np.diag(A)[:, None]   # thu nghiem - co the khong hop le
d = b / np.diag(A)
# ═══════════════════════════════════════════════════════════════════

Lap_Don_x_Bx_d(B, d, max_iter=None, epsilon=1e-6)
'''
    new_src = combined[:cut_pos].rstrip() + "\n\n" + data_section
    new_lines = [line + "\n" for line in new_src.split("\n")]
    if new_lines: new_lines[-1] = new_lines[-1].rstrip("\n")
    code_cell["source"] = new_lines
    code_cell["outputs"] = []
    with open(lap_don_he_path, "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
    print("Cleaned: Lap don He phuong trinh")

# ══════════════════════════════════════════════════════════════════════════════
# CHAPTER 4 – Nghịch đảo bằng Lặp: clean data
# ══════════════════════════════════════════════════════════════════════════════
inv_lap_path = os.path.join(C4, "Nghịch đảo bằng Lặp Jacobi  Gauss-Seidel.ipynb")
if os.path.exists(inv_lap_path):
    with open(inv_lap_path, "r", encoding="utf-8") as f:
        nb = json.load(f)
    code_cell = nb["cells"][1]
    combined = "".join(code_cell["source"])
    markers = ["# NHAP", "# ═══", "a = 200", "A = np.array(["]
    cut_pos = len(combined)
    for marker in markers:
        pos = combined.rfind(marker)
        if pos > 100:
            cut_pos = min(cut_pos, pos)
    data_section = '''# ═══════════════════════════════════════════════════════════════════
# NHAP DU LIEU CUA BAN VAO DAY
# ═══════════════════════════════════════════════════════════════════
A = np.array([
    [10.0, 1.0,  2.0],
    [ 1.0, 10.0, 3.0],
    [ 2.0,  3.0, 10.0]
], dtype=float)
# ═══════════════════════════════════════════════════════════════════

Inverse_Gauss_Seidel(A, epsilon=1e-6)
'''
    new_src = combined[:cut_pos].rstrip() + "\n\n" + data_section
    new_lines = [line + "\n" for line in new_src.split("\n")]
    if new_lines: new_lines[-1] = new_lines[-1].rstrip("\n")
    code_cell["source"] = new_lines
    code_cell["outputs"] = []
    with open(inv_lap_path, "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
    print("Cleaned: Nghich dao Lap")

print("Chapter 4 ALL done")

# ══════════════════════════════════════════════════════════════════════════════
# CHAPTER 5 – Clean data sections (SVD, Luy thua, Xuong thang, Danielevski)
# ══════════════════════════════════════════════════════════════════════════════
c5_cleanups = [
    (os.path.join(C5, "Giá trị kỳ dị SVD (Lớn nhất).ipynb"),
     '''# ═══════════════════════════════════════════════════════════════════
# NHAP DU LIEU CUA BAN VAO DAY
# ═══════════════════════════════════════════════════════════════════
A = np.array([
    [3.0, 2.0, 1.0],
    [1.0, 4.0, 2.0],
    [2.0, 1.0, 5.0]
], dtype=float)
# ═══════════════════════════════════════════════════════════════════

# num_components: so luong gia tri ky di can tinh (None = tinh het)
SVD_Reduced(A, num_components=2)
'''),
    (os.path.join(C5, "Phương pháp Lũy thừa.ipynb"),
     '''# ═══════════════════════════════════════════════════════════════════
# NHAP DU LIEU CUA BAN VAO DAY
# ═══════════════════════════════════════════════════════════════════
A = np.array([
    [4.0, 1.0, 1.0],
    [1.0, 5.0, 1.0],
    [1.0, 1.0, 6.0]
], dtype=float)
# ═══════════════════════════════════════════════════════════════════

Power_Method_L2(A, tol=1e-6)
'''),
    (os.path.join(C5, "Phương pháp Xuống thang.ipynb"),
     '''# ═══════════════════════════════════════════════════════════════════
# NHAP DU LIEU CUA BAN VAO DAY
# ═══════════════════════════════════════════════════════════════════
A = np.array([
    [4.0, 1.0, 1.0],
    [1.0, 5.0, 1.0],
    [1.0, 1.0, 6.0]
], dtype=float)

# So luong tri rieng can tim
num_eigenvalues = 2
# ═══════════════════════════════════════════════════════════════════

XuongThang(A, num_eigenvalues)
'''),
    (os.path.join(C5, "Phương pháp Danielevski.ipynb"),
     '''# ═══════════════════════════════════════════════════════════════════
# NHAP DU LIEU CUA BAN VAO DAY
# ═══════════════════════════════════════════════════════════════════
A = np.array([
    [1.0, 2.0, 3.0],
    [4.0, 5.0, 6.0],
    [7.0, 8.0, 10.0]
], dtype=float)
# ═══════════════════════════════════════════════════════════════════

Danielevski(A)
'''),
    (os.path.join(C5, "Khoảng cách ly nghiệm đa thức.ipynb"),
     '''# ═══════════════════════════════════════════════════════════════════
# NHAP DU LIEU CUA BAN VAO DAY
# ═══════════════════════════════════════════════════════════════════
# He so da thuc tu bac cao nhat: a_n, ..., a_1, a_0
# Vi du: P(x) = x^3 - 6x^2 + 11x - 6
P_coeffs = [1.0, -6.0, 11.0, -6.0]
# ═══════════════════════════════════════════════════════════════════

tim_khoang_cach_ly(P_coeffs)
'''),
    (os.path.join(C5, "Số điều kiện Cond(A).ipynb"),
     '''# ═══════════════════════════════════════════════════════════════════
# NHAP DU LIEU CUA BAN VAO DAY
# ═══════════════════════════════════════════════════════════════════
A = np.array([
    [4.0, 1.0],
    [3.0, 1.0]
], dtype=float)
# ═══════════════════════════════════════════════════════════════════

so_dieu_kien(A)
'''),
]

for nb_path, data_section in c5_cleanups:
    if not os.path.exists(nb_path):
        print(f"  SKIP (not found): {os.path.basename(nb_path)}")
        continue
    with open(nb_path, "r", encoding="utf-8") as f:
        nb = json.load(f)
    code_cell = nb["cells"][1]
    combined = "".join(code_cell["source"])
    markers = ["# NHAP", "# ═══", "a = 10", "C = np.array", "A = np.array([", "P_coeffs = "]
    cut_pos = len(combined)
    for marker in markers:
        pos = combined.rfind(marker)
        if pos > 200:
            cut_pos = min(cut_pos, pos)
    new_src = combined[:cut_pos].rstrip() + "\n\n" + data_section
    new_lines = [line + "\n" for line in new_src.split("\n")]
    if new_lines: new_lines[-1] = new_lines[-1].rstrip("\n")
    code_cell["source"] = new_lines
    code_cell["outputs"] = []
    with open(nb_path, "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
    print(f"  Cleaned: {os.path.basename(nb_path)}")

print("Chapter 5 done")

# ══════════════════════════════════════════════════════════════════════════════
# CHAPTER 6 – Clean data sections
# ══════════════════════════════════════════════════════════════════════════════
c6_cleanups = [
    (os.path.join(C6, "Nội suy Newton (Tiến - Lùi).ipynb"),
     '''# ═══════════════════════════════════════════════════════════════════
# NHAP DU LIEU CUA BAN VAO DAY
# ═══════════════════════════════════════════════════════════════════
# Bang so lieu (x_i, f(x_i))
x_nodes = [1.0, 2.0, 3.0, 4.0, 5.0]
f_nodes = [1.0, 8.0, 27.0, 64.0, 125.0]  # Vi du: f(x) = x^3

x_target = 2.5    # gia tri can noi suy
# ═══════════════════════════════════════════════════════════════════

Newton_Interpolation(x_nodes, f_nodes, x_target)
'''),
    (os.path.join(C6, "Nội suy ngược.ipynb"),
     '''# ═══════════════════════════════════════════════════════════════════
# NHAP DU LIEU CUA BAN VAO DAY
# ═══════════════════════════════════════════════════════════════════
x_nodes = [1.0, 2.0, 3.0, 4.0, 5.0]
f_nodes = [1.0, 8.0, 27.0, 64.0, 125.0]

y_target = 15.0   # gia tri f can tim x (f(x*) = y_target)
# ═══════════════════════════════════════════════════════════════════

Inverse_Interpolation(x_nodes, f_nodes, y_target, epsilon=1e-6)
'''),
    (os.path.join(C6, "Nội suy Spline bậc 3.ipynb"),
     '''# ═══════════════════════════════════════════════════════════════════
# NHAP DU LIEU CUA BAN VAO DAY
# ═══════════════════════════════════════════════════════════════════
x_nodes = [0.0, 1.0, 2.0, 3.0]
f_nodes = [0.0, 1.0, 4.0, 9.0]   # Vi du: f(x) = x^2

x_target = 1.5
# ═══════════════════════════════════════════════════════════════════

Spline_Cubic(x_nodes, f_nodes, x_target)
'''),
]

for nb_path, data_section in c6_cleanups:
    if not os.path.exists(nb_path):
        print(f"  SKIP (not found): {os.path.basename(nb_path)}")
        continue
    with open(nb_path, "r", encoding="utf-8") as f:
        nb = json.load(f)
    code_cell = nb["cells"][1]
    combined = "".join(code_cell["source"])
    markers = ["# NHAP", "# ═══", "x_nodes = ", "x_table = "]
    cut_pos = len(combined)
    for marker in markers:
        pos = combined.rfind(marker)
        if pos > 200:
            cut_pos = min(cut_pos, pos)
    new_src = combined[:cut_pos].rstrip() + "\n\n" + data_section
    new_lines = [line + "\n" for line in new_src.split("\n")]
    if new_lines: new_lines[-1] = new_lines[-1].rstrip("\n")
    code_cell["source"] = new_lines
    code_cell["outputs"] = []
    with open(nb_path, "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
    print(f"  Cleaned: {os.path.basename(nb_path)}")

print("Chapter 6 done")

# ══════════════════════════════════════════════════════════════════════════════
# CHAPTER 7 – Clean data
# ══════════════════════════════════════════════════════════════════════════════
c7_path = os.path.join(C7, "Hệ PTVP - Công thức Hình thang.ipynb")
if os.path.exists(c7_path):
    with open(c7_path, "r", encoding="utf-8") as f:
        nb = json.load(f)
    code_cell = nb["cells"][1]
    combined = "".join(code_cell["source"])
    markers = ["# NHAP", "# ═══", "def F(", "F = lambda"]
    cut_pos = len(combined)
    for marker in markers:
        pos = combined.rfind(marker)
        if pos > 200:
            cut_pos = min(cut_pos, pos)
    data_section = '''# ═══════════════════════════════════════════════════════════════════
# NHAP DU LIEU CUA BAN VAO DAY
# ═══════════════════════════════════════════════════════════════════
# He PTVP: y\' = F(t, y)
# y la vector trang thai, F tra ve vector dao ham
def F(t, y):
    return np.array([
        y[1],           # y1\' = y2
        -y[0] + t       # y2\' = -y1 + t  (vi du)
    ])

t0, t_end = 0.0, 2.0   # khoang thoi gian
h = 0.5                 # buoc luoi
y0 = np.array([1.0, 0.0])  # dieu kien dau
# ═══════════════════════════════════════════════════════════════════

giai_he_PTVP_hinh_thang(F, t0, t_end, y0, h)
'''
    new_src = combined[:cut_pos].rstrip() + "\n\n" + data_section
    new_lines = [line + "\n" for line in new_src.split("\n")]
    if new_lines: new_lines[-1] = new_lines[-1].rstrip("\n")
    code_cell["source"] = new_lines
    code_cell["outputs"] = []
    with open(c7_path, "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
    print("Cleaned: He PTVP hinh thang")

print("Chapter 7 done")

# ══════════════════════════════════════════════════════════════════════════════
# Also clean Giải Đa Thức Toàn Tập
# ══════════════════════════════════════════════════════════════════════════════
dt_path = os.path.join(C2, "Giải Đa Thức Toàn Tập.ipynb")
if os.path.exists(dt_path):
    with open(dt_path, "r", encoding="utf-8") as f:
        nb = json.load(f)
    code_cell = nb["cells"][1]
    combined = "".join(code_cell["source"])
    markers = ["# NHAP", "# ═══", "STT = ", "P_coeffs = ["]
    cut_pos = len(combined)
    for marker in markers:
        pos = combined.rfind(marker)
        if pos > 200:
            cut_pos = min(cut_pos, pos)
    data_section = '''# ═══════════════════════════════════════════════════════════════════
# NHAP DU LIEU CUA BAN VAO DAY
# ═══════════════════════════════════════════════════════════════════
# He so da thuc theo thu tu tu bac cao nhat: [a_n, a_{n-1}, ..., a_1, a_0]
# Vi du: P(x) = x^5 - 2x^4 - 5x^3 + 4x^2 + 6x - 3
P_coeffs = [1.0, -2.0, -5.0, 4.0, 6.0, -3.0]
# ═══════════════════════════════════════════════════════════════════

Polynomial_Solver_Full(P_coeffs, epsilon=1e-6)
'''
    new_src = combined[:cut_pos].rstrip() + "\n\n" + data_section
    new_lines = [line + "\n" for line in new_src.split("\n")]
    if new_lines: new_lines[-1] = new_lines[-1].rstrip("\n")
    code_cell["source"] = new_lines
    code_cell["outputs"] = []
    with open(dt_path, "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
    print("Cleaned: Giai Da Thuc Toan Tap")

print("\nALL CHAPTERS DONE")

# ══════════════════════════════════════════════════════════════════════════════
# CLEANUP: Move all AI helper .py files to tools/
# ══════════════════════════════════════════════════════════════════════════════
import shutil

TOOLS_DIR = "d:/code/Uni/On_thi_cuoi_ky/Giải tích số/tools"
os.makedirs(TOOLS_DIR, exist_ok=True)

# Collect all helper .py files across scripts/ and subdirs
py_files_to_move = []
for root, dirs, files in os.walk(BASE):
    # Exclude checkpoint dirs
    dirs[:] = [d for d in dirs if ".ipynb_checkpoints" not in d]
    for fn in files:
        if fn.endswith(".py") or fn.endswith(".log") or fn.endswith(".txt") or fn.endswith(".md"):
            # Keep only specific files that are NOT helper scripts
            keep_list = []  # none to keep in scripts folders
            full = os.path.join(root, fn)
            py_files_to_move.append(full)

moved = []
for src_path in py_files_to_move:
    fname = os.path.basename(src_path)
    # Create subdirectory structure mirroring origin
    rel = os.path.relpath(os.path.dirname(src_path), BASE)
    dest_dir = os.path.join(TOOLS_DIR, rel) if rel != "." else TOOLS_DIR
    os.makedirs(dest_dir, exist_ok=True)
    dest = os.path.join(dest_dir, fname)
    try:
        shutil.move(src_path, dest)
        moved.append(fname)
    except Exception as e:
        print(f"  Could not move {fname}: {e}")

print(f"\nMoved {len(moved)} helper files to tools/")
for m in moved:
    print(f"  -> {m}")
print("\nCLEANUP DONE")
