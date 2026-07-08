import json

notebook_path = "scripts/CHƯƠNG 2 GIẢI PHƯƠNG TRÌNH PHI TUYẾN 1 CHIỀU/Dây cung.ipynb"

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Use raw string to prevent \f from becoming form feed and \c becoming warning
new_source = r"""import numpy as np
from IPython.display import display, Math, Markdown

def day_cung_codinh(f, x0, d, max_iter=None, epsilon=None):
    # Phương pháp Day cung 1 điểm cố định (Fixed-point Secant Method)
    # f: ham f(x)
    # x0: điểm xuất phát
    # d: điểm cố định
    # max_iter: số vòng lặp cố định
    # epsilon: sai so |x_{k+1} - x_k|
    display(Markdown("## ❖ PHƯƠNG PHÁP DÂY CUNG (1 ĐIỂM CỐ ĐỊNH)"))
    display(Math(r"x_{k+1} = x_k - f(x_k) \cdot \frac{x_k - d}{f(x_k) - f(d)}"))

    x_k = float(x0)
    d = float(d)
    f_k = f(x_k)
    f_d = f(d)
    history = []
    k = 0
    while True:
        k += 1
        denom = f_k - f_d
        if abs(denom) < 1e-15:
            display(Markdown("⚠️ **Cảnh báo:** Mẫu số xấp xỉ 0 - dừng lại."))
            break
        x_next = x_k - f_k * (x_k - d) / denom
        f_next = f(x_next)
        err = abs(x_next - x_k)
        history.append((k, x_k, d, x_next, f_next, err))

        stop = False
        if max_iter is not None and k >= max_iter: stop = True
        if epsilon  is not None and err < epsilon:  stop = True
        if k >= 200: stop = True
        if stop: break
        
        x_k = x_next
        f_k = f_next

    n = len(history)
    display(Markdown(f"### Kết quả ({n} vòng lặp)"))
    cols = ["$k$", "$x_k$", "$d$", "$x_{k+1}$", "$f(x_{k+1})$", r"$\|\Delta\|$"]
    seps = [":---:"]*6
    rows = []
    for (k_, xk_, d_, xn_, fn_, er_) in history:
        rows.append([f"${k_}$", f"${xk_:.6f}$", f"${d_:.6f}$",
                     f"${xn_:.6f}$", f"${fn_:.4e}$", f"${er_:.4e}$"])
    header = "| " + " | ".join(cols) + " |"
    sep    = "| " + " | ".join(seps) + " |"
    lines  = [header, sep]
    for r in rows: lines.append("| " + " | ".join(r) + " |")
    display(Markdown("\n".join(lines)))

    c_star = history[-1][3]
    er_final = history[-1][5]
    display(Markdown(f"**Nghiệm xấp xỉ:** $x^* \approx {c_star:.10f}$"))
    display(Markdown(f"**Sai số cuối:** $\Delta = {er_final:.4e}$"))
    display(Math(f"f(x^*) = {f(c_star):.6e} \approx 0"))
    return c_star

# ═══════════════════════════════════════════════════════════════════
# NHẬP DỮ LIỆU CỦA BẠN VÀO ĐÂY
# ═══════════════════════════════════════════════════════════════════
f = lambda x: x**3 - x - 2

# d: điểm cố định, x0: điểm xuất phát
d = 2.0
x0 = 1.0
# ═══════════════════════════════════════════════════════════════════

day_cung_codinh(f, x0=x0, d=d, max_iter=None, epsilon=1e-8)
"""

# Convert to list of lines with newlines properly retained
source_lines = new_source.splitlines(keepends=True)

nb['cells'][1]['source'] = source_lines

with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print("Notebook fixed successfully.")
