import json
import os

notebook_path = "scripts/CHƯƠNG 4 GIẢI HỆ ĐẠI SỐ TUYẾN TÍNH & TÌM MA TRẬN NGHỊCH ĐẢO/LU có Pivoting.ipynb"

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

source = nb['cells'][1]['source']

new_source = []
for line in source:
    if 'inner = " \\\\\\\\ ".join([f"{x:.{p}f}" for x in M])' in line:
        new_source.append(line.replace(' \\\\\\\\ ', ' & '))
    elif line.strip() == 'LU_Pivoting(A, b)':
        new_source.append(line.replace('LU_Pivoting(A, b)', '_ = LU_Pivoting(A, b)'))
    else:
        new_source.append(line)

nb['cells'][1]['source'] = new_source

# Also clear the outputs so the user can re-run and see it fresh
nb['cells'][1]['outputs'] = []

with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print("LU Pivoting notebook fixed.")
