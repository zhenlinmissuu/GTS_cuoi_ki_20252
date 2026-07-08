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

def make_nb(title, code):
    src = [line + "\n" for line in code.split("\n")]
    if src: src[-1] = src[-1].rstrip("\n")
    return {
        "cells": [
            {"cell_type": "markdown", "metadata": {}, "source": [f"### {title}\n"]},
            {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": src}
        ],
        "metadata": METADATA,
        "nbformat": 4, "nbformat_minor": 4
    }

def write_nb(path, title, code):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    nb = make_nb(title, code)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)

C2 = os.path.join(BASE, "CHƯƠNG 2 GIẢI PHƯƠNG TRÌNH PHI TUYẾN 1 CHIỀU")
C3 = os.path.join(BASE, "CHƯƠNG 3 GIẢI HỆ PHƯƠNG TRÌNH PHI TUYẾN NHIỀU CHIỀU")
C4 = os.path.join(BASE, "CHƯƠNG 4 GIẢI HỆ ĐẠI SỐ TUYẾN TÍNH & TÌM MA TRẬN NGHỊCH ĐẢO")
C5 = os.path.join(BASE, "CHƯƠNG 5 GIÁ TRỊ RIÊNG VÀ VECTOR RIÊNG CỦA MA TRẬN")
C6 = os.path.join(BASE, "CHƯƠNG 6 NỘI SUY VÀ ĐẠO HÀM SỐ")
C7 = os.path.join(BASE, "CHƯƠNG 7 GIẢI PHƯƠNG TRÌNH VI PHÂN")

# ──────────────────────────────────────────────────────────────────────────────
# Utility: print compact table (3 head + ... + 3 tail if long)
# ──────────────────────────────────────────────────────────────────────────────
TABLE_UTIL = '''
def _print_table(header_cols, sep_cols, rows, labels, threshold=8):
    header = "| " + " | ".join(header_cols) + " |"
    sep    = "| " + " | ".join(sep_cols) + " |"
    lines  = [header, sep]
    n = len(rows)
    if n <= threshold:
        display_rows = rows
        dots = False
    else:
        display_rows = rows[:3]
        dots = True
    for r in display_rows:
        lines.append("| " + " | ".join(str(c) for c in r) + " |")
    if dots:
        lines.append("| " + " | ".join(["$\\\\vdots$"] * len(header_cols)) + " |")
        for r in rows[-3:]:
            lines.append("| " + " | ".join(str(c) for c in r) + " |")
    display(Markdown("\\n".join(lines)))
'''

# ──────────────────────────────────────────────────────────────────────────────
# CHAPTER 2
# ──────────────────────────────────────────────────────────────────────────────
code_chia_doi = '''import numpy as np
from IPython.display import display, Math, Markdown

def chia_doi(f, a, b, max_iter=None, epsilon=None):
    # Phuong phap Chia doi (Bisection)
    # f: ham f(x) can tim nghiem
    # a, b: khoang co lap nghiem voi f(a)*f(b) < 0
    # max_iter: so vong lap co dinh (None = khong gioi han)
    # epsilon: sai so dung |b-a|/2 (None = khong kiem tra)
    display(Markdown("## phong PHUONG PHAP CHIA DOI (BISECTION)"))
    display(Math(r"\\text{Tim } x^* \\in [" + f"{a}, {b}" + r"] \\text{ sao cho } f(x^*)=0"))

    if f(a) * f(b) > 0:
        display(Markdown("WARNING: f(a) va f(b) cung dau - khong dam bao ton tai nghiem!"))
        return None

    fa = f(a)
    history = []
    k = 0
    while True:
        k += 1
        c  = (a + b) / 2.0
        fc = f(c)
        err = (b - a) / 2.0
        history.append((k, a, b, c, fc, err))

        stop = False
        if max_iter is not None and k >= max_iter: stop = True
        if epsilon  is not None and err < epsilon:  stop = True
        if abs(fc) < 1e-14: stop = True
        if k >= 300: stop = True
        if stop: break

        if fa * fc < 0:
            b = c
        else:
            a = c; fa = fc

    # ── In ket qua ──
    n = len(history)
    display(Markdown(f"### Ket qua ({n} vong lap)"))
    cols = ["$k$", "$a_k$", "$b_k$", "$c_k = (a_k+b_k)/2$", "$f(c_k)$", "$\\\\Delta_k = (b-a)/2$"]
    seps = [":---:"]*6
    rows = []
    for (k_, a_, b_, c_, fc_, er_) in history:
        rows.append([f"${k_}$", f"${a_:.6f}$", f"${b_:.6f}$",
                     f"${c_:.6f}$", f"${fc_:.4e}$", f"${er_:.4e}$"])

    header = "| " + " | ".join(cols) + " |"
    sep    = "| " + " | ".join(seps) + " |"
    lines  = [header, sep]
    if n <= 8:
        for r in rows: lines.append("| " + " | ".join(r) + " |")
    else:
        for r in rows[:3]: lines.append("| " + " | ".join(r) + " |")
        lines.append("| $\\\\vdots$ | $\\\\vdots$ | $\\\\vdots$ | $\\\\vdots$ | $\\\\vdots$ | $\\\\vdots$ |")
        for r in rows[-3:]: lines.append("| " + " | ".join(r) + " |")
    display(Markdown("\\n".join(lines)))

    c_star = history[-1][3]
    er_final = history[-1][5]
    display(Markdown(f"**Nghiem xap xi:** $x^* \\\\approx {c_star:.10f}$"))
    display(Markdown(f"**Sai so:** $\\\\Delta \\\\leq {er_final:.4e}$"))
    display(Math(f"f(x^*) = {f(c_star):.6e} \\\\approx 0"))
    return c_star

# ═══════════════════════════════════════════════════════════════════
# NHAP DU LIEU CUA BAN VAO DAY
# ═══════════════════════════════════════════════════════════════════
f = lambda x: x**3 - x - 2   # ham can tim nghiem

a, b = 1.0, 2.0               # khoang co lap nghiem
# ═══════════════════════════════════════════════════════════════════

chia_doi(f, a, b, max_iter=None, epsilon=1e-6)
'''

code_day_cung = '''import numpy as np
from IPython.display import display, Math, Markdown

def day_cung(f, a, b, max_iter=None, epsilon=None):
    # Phuong phap Day cung (Secant Method)
    # f: ham f(x)
    # a, b: hai diem khoi dau
    # max_iter: so vong lap co dinh
    # epsilon: sai so |x_{k+1} - x_k|
    display(Markdown("## phong PHUONG PHAP DAY CUNG (SECANT)"))
    display(Math(r"x_{k+1} = x_k - f(x_k) \\cdot \\frac{x_k - x_{k-1}}{f(x_k) - f(x_{k-1})}"))

    x0, x1 = float(a), float(b)
    f0, f1 = f(x0), f(x1)
    history = []
    k = 0
    while True:
        k += 1
        denom = f1 - f0
        if abs(denom) < 1e-15:
            display(Markdown("WARNING: Mau so xap xi 0 - dung lai."))
            break
        x2 = x1 - f1 * (x1 - x0) / denom
        f2 = f(x2)
        err = abs(x2 - x1)
        history.append((k, x0, x1, x2, f2, err))

        stop = False
        if max_iter is not None and k >= max_iter: stop = True
        if epsilon  is not None and err < epsilon:  stop = True
        if k >= 200: stop = True
        if stop: break
        x0, f0 = x1, f1
        x1, f1 = x2, f2

    n = len(history)
    display(Markdown(f"### Ket qua ({n} vong lap)"))
    cols = ["$k$", "$x_{k-1}$", "$x_k$", "$x_{k+1}$", "$f(x_{k+1})$", "$\\\\|\\\\Delta\\\\|$"]
    seps = [":---:"]*6
    rows = []
    for (k_, a_, b_, c_, fc_, er_) in history:
        rows.append([f"${k_}$", f"${a_:.6f}$", f"${b_:.6f}$",
                     f"${c_:.6f}$", f"${fc_:.4e}$", f"${er_:.4e}$"])
    header = "| " + " | ".join(cols) + " |"
    sep    = "| " + " | ".join(seps) + " |"
    lines  = [header, sep]
    if n <= 8:
        for r in rows: lines.append("| " + " | ".join(r) + " |")
    else:
        for r in rows[:3]: lines.append("| " + " | ".join(r) + " |")
        lines.append("| $\\\\vdots$ | $\\\\vdots$ | $\\\\vdots$ | $\\\\vdots$ | $\\\\vdots$ | $\\\\vdots$ |")
        for r in rows[-3:]: lines.append("| " + " | ".join(r) + " |")
    display(Markdown("\\n".join(lines)))

    c_star = history[-1][3]
    er_final = history[-1][5]
    display(Markdown(f"**Nghiem xap xi:** $x^* \\\\approx {c_star:.10f}$"))
    display(Markdown(f"**Sai so cuoi:** $\\\\Delta = {er_final:.4e}$"))
    display(Math(f"f(x^*) = {f(c_star):.6e} \\\\approx 0"))
    return c_star

# ═══════════════════════════════════════════════════════════════════
# NHAP DU LIEU CUA BAN VAO DAY
# ═══════════════════════════════════════════════════════════════════
f = lambda x: x**3 - x - 2

a, b = 1.0, 2.0
# ═══════════════════════════════════════════════════════════════════

day_cung(f, a, b, max_iter=None, epsilon=1e-8)
'''

code_newton_1d = '''import numpy as np
from IPython.display import display, Math, Markdown

def tiep_tuyen(f, df, x0, max_iter=None, epsilon=None):
    # Phuong phap Tiep tuyen (Newton-Raphson)
    # f: ham f(x)
    # df: dao ham f'(x)
    # x0: xap xi khoi dau
    # max_iter: so vong lap co dinh
    # epsilon: sai so |x_{k+1} - x_k|
    display(Markdown("## phong PHUONG PHAP TIEP TUYEN (NEWTON-RAPHSON)"))
    display(Math(r"x_{k+1} = x_k - \\frac{f(x_k)}{f\'(x_k)}"))

    history = [(0, float(x0), f(float(x0)), None)]
    x_k = float(x0)
    k = 0
    while True:
        k += 1
        fk  = f(x_k)
        dfk = df(x_k)
        if abs(dfk) < 1e-14:
            display(Markdown("WARNING: f\'(x_k) xap xi 0 - tiep tuyen nam ngang!"))
            break
        x_new = x_k - fk / dfk
        err   = abs(x_new - x_k)
        history.append((k, x_new, f(x_new), err))

        stop = False
        if max_iter is not None and k >= max_iter: stop = True
        if epsilon  is not None and err < epsilon:  stop = True
        if k >= 200: stop = True
        if stop: break
        x_k = x_new

    n = len(history) - 1
    display(Markdown(f"### Ket qua ({n} vong lap)"))
    cols = ["$k$", "$x_k$", "$f(x_k)$", "$\\\\|x_{k+1}-x_k\\\\|$"]
    seps = [":---:"]*4
    rows = []
    for (k_, x_, fx_, er_) in history:
        er_str = f"${er_:.4e}$" if er_ is not None else "—"
        rows.append([f"${k_}$", f"${x_:.10f}$", f"${fx_:.4e}$", er_str])
    header = "| " + " | ".join(cols) + " |"
    sep    = "| " + " | ".join(seps) + " |"
    lines  = [header, sep]
    m = len(rows)
    if m <= 8:
        for r in rows: lines.append("| " + " | ".join(r) + " |")
    else:
        for r in rows[:3]: lines.append("| " + " | ".join(r) + " |")
        lines.append("| $\\\\vdots$ | $\\\\vdots$ | $\\\\vdots$ | $\\\\vdots$ |")
        for r in rows[-3:]: lines.append("| " + " | ".join(r) + " |")
    display(Markdown("\\n".join(lines)))

    x_star = history[-1][1]
    display(Markdown(f"**Nghiem xap xi:** $x^* \\\\approx {x_star:.10f}$"))
    display(Math(f"f(x^*) = {f(x_star):.6e} \\\\approx 0"))
    return x_star

# ═══════════════════════════════════════════════════════════════════
# NHAP DU LIEU CUA BAN VAO DAY
# ═══════════════════════════════════════════════════════════════════
f  = lambda x: x**3 - x - 2
df = lambda x: 3*x**2 - 1

x0 = 2.0         # xap xi khoi dau
# ═══════════════════════════════════════════════════════════════════

tiep_tuyen(f, df, x0, max_iter=None, epsilon=1e-10)
'''

code_lap_don_1d = '''import numpy as np
from IPython.display import display, Math, Markdown

def lap_don_1d(g, x0, max_iter=None, epsilon=None):
    # Phuong phap Lap don 1 chieu (Fixed-Point Iteration)
    # g: ham lap g(x) sao cho x = g(x) tuong duong f(x) = 0
    # x0: xap xi khoi dau
    # max_iter: so vong lap co dinh
    # epsilon: sai so |x_{k+1} - x_k|
    display(Markdown("## phong PHUONG PHAP LAP DON 1 CHIEU"))
    display(Math(r"x_{k+1} = g(x_k)"))

    history = [(0, float(x0), None)]
    x_k = float(x0)
    k = 0
    while True:
        k += 1
        x_new = g(x_k)
        err   = abs(x_new - x_k)
        history.append((k, x_new, err))

        stop = False
        if max_iter is not None and k >= max_iter: stop = True
        if epsilon  is not None and err < epsilon:  stop = True
        if k >= 200: stop = True
        if stop: break
        x_k = x_new

    n = len(history) - 1
    display(Markdown(f"### Ket qua ({n} vong lap)"))
    cols = ["$k$", "$x_k$", "$\\\\|x_{k+1}-x_k\\\\|$"]
    seps = [":---:"]*3
    rows = []
    for (k_, x_, er_) in history:
        er_str = f"${er_:.4e}$" if er_ is not None else "—"
        rows.append([f"${k_}$", f"${x_:.10f}$", er_str])
    header = "| " + " | ".join(cols) + " |"
    sep    = "| " + " | ".join(seps) + " |"
    lines  = [header, sep]
    m = len(rows)
    if m <= 8:
        for r in rows: lines.append("| " + " | ".join(r) + " |")
    else:
        for r in rows[:3]: lines.append("| " + " | ".join(r) + " |")
        lines.append("| $\\\\vdots$ | $\\\\vdots$ | $\\\\vdots$ |")
        for r in rows[-3:]: lines.append("| " + " | ".join(r) + " |")
    display(Markdown("\\n".join(lines)))

    x_star = history[-1][1]
    display(Markdown(f"**Nghiem xap xi:** $x^* \\\\approx {x_star:.10f}$"))
    return x_star

# ═══════════════════════════════════════════════════════════════════
# NHAP DU LIEU CUA BAN VAO DAY
# ═══════════════════════════════════════════════════════════════════
# Vi du: x^3 - x - 2 = 0  =>  x = (x+2)^(1/3)
g = lambda x: (x + 2) ** (1.0/3)

x0 = 1.5          # xap xi khoi dau
# ═══════════════════════════════════════════════════════════════════

lap_don_1d(g, x0, max_iter=None, epsilon=1e-6)
'''

write_nb(os.path.join(C2, "Chia đôi.ipynb"),           "Phương pháp Chia đôi (Bisection)",         code_chia_doi)
write_nb(os.path.join(C2, "Dây cung.ipynb"),            "Phương pháp Dây cung (Secant)",            code_day_cung)
write_nb(os.path.join(C2, "Tiếp tuyến (Newton).ipynb"), "Phương pháp Tiếp tuyến Newton-Raphson",   code_newton_1d)
write_nb(os.path.join(C2, "Lặp đơn (1 chiều).ipynb"),  "Phương pháp Lặp đơn 1 chiều",             code_lap_don_1d)
print("Chapter 2 done")

# ──────────────────────────────────────────────────────────────────────────────
# CHAPTER 3
# ──────────────────────────────────────────────────────────────────────────────
code_lap_don_nd = '''import numpy as np
from IPython.display import display, Math, Markdown

def _vec_latex(v, p=6):
    inner = " \\\\\\\\ ".join([f"{x:.{p}f}" for x in v])
    return f"\\\\begin{{bmatrix}} {inner} \\\\end{{bmatrix}}^T"

def lap_don_nhieu_chieu(G, x0, max_iter=None, epsilon=None):
    # Phuong phap Lap don nhieu chieu: x = G(x)
    # G: ham vector G: R^n -> R^n
    # x0: vector xap xi khoi dau (list hoac ndarray)
    # max_iter: so vong lap co dinh
    # epsilon: sai so ||x_{k+1} - x_k||_inf
    display(Markdown("## phong PHUONG PHAP LAP DON NHIEU CHIEU"))
    display(Math(r"x^{(k+1)} = G(x^{(k)})"))

    x_k = np.array(x0, dtype=float)
    display(Math(f"x^{{(0)}} = {_vec_latex(x_k)}"))

    history = [x_k.copy()]
    k = 0
    while True:
        k += 1
        x_new = np.array(G(x_k), dtype=float)
        err   = np.linalg.norm(x_new - x_k, np.inf)
        history.append(x_new.copy())

        stop = False
        if max_iter is not None and k >= max_iter: stop = True
        if epsilon  is not None and err < epsilon:  stop = True
        if k >= 200: stop = True
        if stop: break
        x_k = x_new

    n = len(history) - 1
    display(Markdown(f"### Ket qua ({n} vong lap)"))

    if n <= 6:
        for i, v in enumerate(history):
            display(Math(f"x^{{({i})}} = {_vec_latex(v)}"))
    else:
        for i in range(3):
            display(Math(f"x^{{({i})}} = {_vec_latex(history[i])}"))
        display(Markdown("$\\\\vdots$"))
        for i in range(n-2, n+1):
            display(Math(f"x^{{({i})}} = {_vec_latex(history[i])}"))

    err_final = np.linalg.norm(history[-1] - history[-2], np.inf)
    display(Markdown(f"**Sai so cuoi:** $\\\\|x^{{({n})}} - x^{{({n-1})}}\\\\|_{{\\\\infty}} = {err_final:.4e}$"))
    return history[-1]

# ═══════════════════════════════════════════════════════════════════
# NHAP DU LIEU CUA BAN VAO DAY
# ═══════════════════════════════════════════════════════════════════
# Vi du: giai he phi tuyen:
#   x1 = cos(x2) / 2
#   x2 = (sin(x1) + 1) / 3
def G(x):
    return [np.cos(x[1]) / 2.0,
            (np.sin(x[0]) + 1) / 3.0]

x0 = [0.5, 0.5]   # xap xi khoi dau
# ═══════════════════════════════════════════════════════════════════

lap_don_nhieu_chieu(G, x0, max_iter=None, epsilon=1e-6)
'''

code_newton_nd = '''import numpy as np
from IPython.display import display, Math, Markdown

def _vec_latex(v, p=6):
    inner = " \\\\\\\\ ".join([f"{x:.{p}f}" for x in v])
    return f"\\\\begin{{bmatrix}} {inner} \\\\end{{bmatrix}}^T"

def _mat_latex(M, p=6):
    rows = " \\\\\\\\ ".join([" & ".join([f"{x:.{p}f}" for x in row]) for row in M])
    return f"\\\\begin{{bmatrix}} {rows} \\\\end{{bmatrix}}"

def newton_nhieu_chieu(F, J, x0, max_iter=None, epsilon=None):
    # Phuong phap Newton nhieu chieu
    # F: ham vector F: R^n -> R^n (can tim nghiem F(x)=0)
    # J: ham Jacobian J(x) tra ve ma tran n x n
    # x0: vector xap xi khoi dau
    # max_iter: so vong lap co dinh
    # epsilon: sai so ||x_{k+1} - x_k||_inf
    display(Markdown("## phong PHUONG PHAP NEWTON NHIEU CHIEU"))
    display(Math(r"x^{(k+1)} = x^{(k)} - J(x^{(k)})^{-1} F(x^{(k)})"))

    x_k = np.array(x0, dtype=float)
    display(Math(f"x^{{(0)}} = {_vec_latex(x_k)}"))

    history = [x_k.copy()]
    k = 0
    while True:
        k += 1
        Fk = np.array(F(x_k), dtype=float)
        Jk = np.array(J(x_k), dtype=float)

        display(Markdown(f"#### Buoc lap $k = {k}$"))
        display(Math(f"F(x^{{({k-1})}}) = {_vec_latex(Fk)}"))
        display(Math(f"J(x^{{({k-1})}}) = {_mat_latex(Jk)}"))

        try:
            delta = np.linalg.solve(Jk, -Fk)
        except np.linalg.LinAlgError:
            display(Markdown("WARNING: Jacobian suy bien!"))
            break

        x_new = x_k + delta
        err   = np.linalg.norm(delta, np.inf)
        display(Math(f"x^{{({k})}} = {_vec_latex(x_new)}"))
        display(Markdown(f"Sai so: $\\\\|\\\\Delta x\\\\|_{{\\\\infty}} = {err:.4e}$"))

        history.append(x_new.copy())

        stop = False
        if max_iter is not None and k >= max_iter: stop = True
        if epsilon  is not None and err < epsilon:  stop = True
        if k >= 100: stop = True
        if stop: break
        x_k = x_new

    n = len(history) - 1
    display(Markdown(f"### Ket qua ({n} vong lap)"))
    x_star = history[-1]
    display(Math(f"x^* = {_vec_latex(x_star)}"))
    Fstar = np.array(F(x_star), dtype=float)
    display(Markdown("**Kiem tra nghiem:**"))
    display(Math(f"F(x^*) = {_vec_latex(Fstar)} \\\\approx 0"))
    return x_star

# ═══════════════════════════════════════════════════════════════════
# NHAP DU LIEU CUA BAN VAO DAY
# ═══════════════════════════════════════════════════════════════════
# Vi du: giai he phi tuyen F(x) = 0
#   x1^2 + x2^2 - 1 = 0
#   x1 - x2^2       = 0
def F(x):
    return [x[0]**2 + x[1]**2 - 1,
            x[0]   - x[1]**2]

def J(x):
    return [[2*x[0], 2*x[1]],
            [1,     -2*x[1]]]

x0 = [0.8, 0.6]   # xap xi khoi dau
# ═══════════════════════════════════════════════════════════════════

newton_nhieu_chieu(F, J, x0, max_iter=None, epsilon=1e-8)
'''

write_nb(os.path.join(C3, "Lặp đơn nhiều chiều.ipynb"), "Phương pháp Lặp đơn nhiều chiều", code_lap_don_nd)
write_nb(os.path.join(C3, "Newton nhiều chiều.ipynb"),   "Phương pháp Newton nhiều chiều",   code_newton_nd)
print("Chapter 3 done")

print("ALL DONE")
