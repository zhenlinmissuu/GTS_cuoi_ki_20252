import json
import os

filepath = "d:/code/Uni/On_thi_cuoi_ky/Giải tích số/scripts/CHƯƠNG 4 GIẢI HỆ ĐẠI SỐ TUYẾN TÍNH & TÌM MA TRẬN NGHỊCH ĐẢO/Lặp Jacobi - Lặp Đơn/Lặp Jacobi (Đổi dòng tạo chéo trội).ipynb"

with open(filepath, 'r', encoding='utf-8') as f:
    nb = json.load(f)

source = "".join(nb['cells'][1]['source'])
source = source.replace("Jacobi_Ax_b_Permute(A, b, x0, num_iters=5)", "Jacobi_Ax_b_Permute(A, b, x0, num_iters=5, epsilon=None)")

source_lines = [line + '\n' for line in source.split('\n')]
if source_lines:
    source_lines[-1] = source_lines[-1].rstrip('\n')
nb['cells'][1]['source'] = source_lines

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)
