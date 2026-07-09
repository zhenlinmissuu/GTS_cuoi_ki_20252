import json

# Fix 1: Dây cung.ipynb
path_day_cung = "scripts/CHƯƠNG 2 GIẢI PHƯƠNG TRÌNH PHI TUYẾN 1 CHIỀU/Dây cung.ipynb"
with open(path_day_cung, 'r', encoding='utf-8') as f:
    nb = json.load(f)

source = nb['cells'][1]['source']
for i in range(len(source)):
    if 'display(Markdown(f"**Nghiệm xấp xỉ' in source[i]:
        source[i] = '    display(Markdown(f"**Nghiệm xấp xỉ:** $x^* \\\\approx {c_star:.10f}$"))\n'
    elif 'display(Markdown(f"**Sai số cuối' in source[i]:
        source[i] = '    display(Markdown(f"**Sai số cuối:** $\\\\Delta = {er_final:.4e}$"))\n'
    elif 'display(Math(f"f(x^*)' in source[i]:
        source[i] = '    display(Math(f"f(x^*) = {f(c_star):.6e} \\\\approx 0"))\n'

nb['cells'][1]['source'] = source
with open(path_day_cung, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)


# Fix 2: Nghịch đảo bằng Lặp Jacobi Gauss-Seidel.ipynb
path_inv = "scripts/CHƯƠNG 4 GIẢI HỆ ĐẠI SỐ TUYẾN TÍNH & TÌM MA TRẬN NGHỊCH ĐẢO/Nghịch đảo bằng Lặp Jacobi  Gauss-Seidel.ipynb"
with open(path_inv, 'r', encoding='utf-8') as f:
    nb2 = json.load(f)

changed = False
for cell in nb2.get('cells', []):
    if cell.get('cell_type') == 'code':
        source2 = cell.get('source', [])
        for i in range(len(source2)):
            if 'display(Markdown(f"**Nhận xét:** Tích $A \cdot A^{{-1}}$' in source2[i]:
                source2[i] = source2[i].replace(r'\cdot', r'\\cdot')
                changed = True
        
        if changed:
            cell['source'] = source2

with open(path_inv, 'w', encoding='utf-8') as f:
    json.dump(nb2, f, indent=1, ensure_ascii=False)

print("Fixed specific latex escapes.")
