import json
import os

dir_path = "d:/code/Uni/On_thi_cuoi_ky/Giải tích số/scripts/CHƯƠNG 4 GIẢI HỆ ĐẠI SỐ TUYẾN TÍNH & TÌM MA TRẬN NGHỊCH ĐẢO/Lặp Gauss-Seidel"

def fix_flatten_in_notebook(filename):
    filepath = os.path.join(dir_path, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        nb = json.load(f)
        
    code_lines = nb['cells'][1]['source']
    for i, line in enumerate(code_lines):
        if "d = np.array(d_input, dtype=float)" in line:
            code_lines[i] = line.replace("d = np.array(d_input, dtype=float)", "d = np.array(d_input, dtype=float).flatten()")
        elif "b = np.array(b_input, dtype=float)" in line:
            code_lines[i] = line.replace("b = np.array(b_input, dtype=float)", "b = np.array(b_input, dtype=float).flatten()")
            
    nb['cells'][1]['source'] = code_lines
    nb['cells'][1]['outputs'] = []
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)

fix_flatten_in_notebook("Lặp Gauss-Seidel (x=Bx+d).ipynb")
fix_flatten_in_notebook("Lặp Gauss-Seidel (Ax=B).ipynb")
fix_flatten_in_notebook("Lặp Gauss-Seidel (Đổi dòng tạo chéo trội).ipynb")

print("Fixed flatten!")
