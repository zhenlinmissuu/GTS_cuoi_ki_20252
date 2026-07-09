import json

notebook_path = "scripts/CHƯƠNG 2 GIẢI PHƯƠNG TRÌNH PHI TUYẾN 1 CHIỀU/Dây cung.ipynb"

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

source = nb['cells'][1]['source']

for i in range(len(source)):
    if 'display(Markdown(rf"**Nghiệm xấp xỉ' in source[i]:
        source[i] = '    display(Markdown(rf"**Nghiệm xấp xỉ:** $x^* \\approx {c_star:.10f}$"))\n'
    elif 'display(Markdown(rf"**Sai số cuối' in source[i]:
        source[i] = '    display(Markdown(rf"**Sai số cuối:** $\\Delta = {er_final:.4e}$"))\n'
    elif 'display(Math(rrf"f(x^*)' in source[i] or 'display(Math(rf"f(x^*)' in source[i]:
        source[i] = '    display(Math(rf"f(x^*) = {f(c_star):.6e} \\approx 0"))\n'

nb['cells'][1]['source'] = source
nb['cells'][1]['outputs'] = []

with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print("Fixed SyntaxError in Day Cung.")
