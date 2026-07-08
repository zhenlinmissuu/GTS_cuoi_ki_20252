import json
import os

notebook_path = "d:/code/Uni/On_thi_cuoi_ky/Giải tích số/scripts/CHƯƠNG 5 GIÁ TRỊ RIÊNG VÀ VECTOR RIÊNG CỦA MA TRẬN/Giá trị kỳ dị SVD (Lớn nhất).ipynb"

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# The new matrix
A_code = """A = np.array([
    [3,  3,  8],
    [3,  9,  4],
    [7, 10,  6],
    [0,  4, -2]
], dtype=float)

# Đề bài không cho véctơ khởi tạo, nên ta cứ để nó tự động dùng np.ones(3) = [1, 1, 1]^T
SVD_Reduced(A)
"""

# Read the existing source code lines and replace the final part
source_lines = nb['cells'][1]['source']

# Find where the old A definition starts
start_idx = 0
for i, line in enumerate(source_lines):
    if line.startswith("# Ma trận đề bài"):
        start_idx = i
        break

# Replace the lines from start_idx onwards
new_lines = source_lines[:start_idx] + [line + "\n" for line in A_code.split("\n")]
new_lines[-1] = new_lines[-1].rstrip('\n')

nb['cells'][1]['source'] = new_lines
nb['cells'][1]['outputs'] = []

with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)
