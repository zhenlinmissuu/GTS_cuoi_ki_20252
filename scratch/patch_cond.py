import json
import os
import sys

def patch_axb(path):
    with open(path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    for cell in nb['cells']:
        if cell['cell_type'] == 'code':
            source = "".join(cell['source'])
            if 'def Gauss_Seidel_Ax_B' not in source: continue
            
            start_str = '    display(Markdown("### 1. Kiểm tra điều kiện hội tụ"))\n'
            end_str = '    display(Markdown("### 2. Quá trình lặp"))\n'
            
            start_idx = source.find(start_str)
            end_idx = source.find(end_str)
            
            if start_idx != -1 and end_idx != -1:
                replacement = '''    display(Markdown("### 1. Kiểm tra điều kiện hội tụ"))
    
    is_row_dom = True
    for i in range(n):
        if sum(abs(A[i, j]) for j in range(n) if j != i) >= abs(A[i,i]):
            is_row_dom = False
            break
            
    is_col_dom = True
    for j in range(n):
        if sum(abs(A[i, j]) for i in range(n) if i != j) >= abs(A[j,j]):
            is_col_dom = False
            break
            
    if is_row_dom:
        display(Markdown("Ma trận A **chéo trội hàng**, phương pháp lặp chắc chắn hội tụ."))
        s = 0.0
        q = 0.0
        for i in range(n):
            sum_l = sum(abs(A[i, j]) for j in range(i))
            sum_u = sum(abs(A[i, j]) for j in range(i+1, n))
            q_i = sum_l / (abs(A[i,i]) - sum_u) if (abs(A[i,i]) - sum_u) > 0 else float('inf')
            q = max(q, q_i)
        display(Math(f"s = {s:.5f}, \\\\quad q = \\\\max_i \\\\frac{{\\\\sum_{{j<i}} |a_{{ij}}|}}{{|a_{{ii}}| - \\\\sum_{{j>i}} |a_{{ij}}|}} \\\\approx {q:.5f}"))
        
    elif is_col_dom:
        display(Markdown("Ma trận A **chéo trội cột**, phương pháp lặp chắc chắn hội tụ."))
        s = 0.0
        q = 0.0
        for j in range(n):
            sum_u = sum(abs(A[i, j]) for i in range(j+1, n))
            s = max(s, sum_u / abs(A[j,j]) if abs(A[j,j]) != 0 else float('inf'))
            sum_l = sum(abs(A[i, j]) for i in range(j))
            q_j = sum_l / (abs(A[j,j]) - sum_u) if (abs(A[j,j]) - sum_u) > 0 else float('inf')
            q = max(q, q_j)
        display(Math(f"s = \\\\max_j \\\\frac{{1}}{{|a_{{jj}}|}} \\\\sum_{{i>j}} |a_{{ij}}| \\\\approx {s:.5f}, \\\\quad q = \\\\max_j \\\\frac{{\\\\sum_{{i<j}} |a_{{ij}}|}}{{|a_{{jj}}| - \\\\sum_{{i>j}} |a_{{ij}}|}} \\\\approx {q:.5f}"))
        
    else:
        display(Markdown("**Cảnh báo:** Ma trận A không chéo trội ngặt hàng/cột. Phương pháp lặp có thể không hội tụ."))
        s = 0.0
        q = 0.0
        for i in range(n):
            sum_l = sum(abs(A[i, j]) for j in range(i))
            sum_u = sum(abs(A[i, j]) for j in range(i+1, n))
            q_i = sum_l / (abs(A[i,i]) - sum_u) if (abs(A[i,i]) - sum_u) > 0 else float('inf')
            if q_i != float('inf'): q = max(q, q_i)
        if q >= 1: q = 0.99
        display(Math(f"s = {s:.5f}, \\\\quad q \\\\approx {q:.5f}"))
        
    eps0 = epsilon * (1 - s) * (1 - q) / q if q < 1 and q > 0 else epsilon
    display(Math(f"\\\\varepsilon_0 = \\\\frac{{\\\\varepsilon(1-s)(1-q)}}{{q}} = {eps0:.5e}"))
    
'''
                new_source = source[:start_idx] + replacement + source[end_idx:]
                lines = [line + '\n' for line in new_source.split('\n')]
                if lines: lines[-1] = lines[-1].rstrip('\n')
                cell['source'] = lines
    
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)

def patch_bxd(path):
    with open(path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    for cell in nb['cells']:
        if cell['cell_type'] == 'code':
            source = "".join(cell['source'])
            if 'def Gauss_Seidel_Bd' not in source: continue
            
            start_str = '    display(Markdown("### 1. Quá trình lặp"))\n'
            
            start_idx = source.find(start_str)
            
            if start_idx != -1:
                replacement = '''    display(Markdown("### 1. Kiểm tra điều kiện hội tụ"))
    norm_B = np.linalg.norm(B, np.inf)
    if norm_B < 1:
        display(Markdown(f"Chuẩn vô cùng của ma trận $B$: $||B||_\\\\infty = {norm_B:.4f} < 1$, phương pháp chắc chắn hội tụ."))
    else:
        display(Markdown(f"**Cảnh báo:** $||B||_\\\\infty = {norm_B:.4f} \\\\ge 1$, phương pháp chưa chắc hội tụ."))
    
    eps0 = epsilon * (1 - norm_B) / norm_B if norm_B < 1 and norm_B > 0 else (epsilon if epsilon is not None else 1e-5)
    if norm_B < 1:
        display(Math(f"\\\\varepsilon_0 = \\\\frac{{\\\\varepsilon(1-q)}}{{q}} = {eps0:.5e} \\\\quad (\\\\text{{với }} q = ||B||_\\\\infty)"))
    else:
        display(Math(f"\\\\varepsilon_0 = \\\\varepsilon = {eps0:.5e}"))
        
    display(Markdown("### 2. Quá trình lặp"))
'''
                new_source = source[:start_idx] + replacement + source[start_idx + len(start_str):]
                # Also replace eps0 = epsilon if epsilon is not None else 1e-5
                # that is right after "### 1. Quá trình lặp"
                new_source = new_source.replace('    eps0 = epsilon if epsilon is not None else 1e-5\n', '')
                
                lines = [line + '\n' for line in new_source.split('\n')]
                if lines: lines[-1] = lines[-1].rstrip('\n')
                cell['source'] = lines
    
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)

def patch_swap(path):
    with open(path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    for cell in nb['cells']:
        if cell['cell_type'] == 'code':
            source = "".join(cell['source'])
            if 'def Gauss_Seidel_Ax_B_Permute' not in source: continue
            
            # The swap logic prints eps0 inside the loop initialization. We should print it in the md.append block.
            # Find the end of section II
            end_sec_II = source.find('    md.append(f"- **Chuẩn vô cùng của B:** $q = ||B||_\\\\infty = {norm_B:.4f}$")')
            if end_sec_II == -1: end_sec_II = source.find('    md.append(f"- **Chuß║⌐n v├┤ c├╣ng cß╗ºa B:** $q = ||B||_\\infty = {norm_B:.4f}$")')
            if end_sec_II == -1: continue
            
            end_line_idx = source.find('\n', end_sec_II)
            
            replacement_cond = '''
    s = 0.0
    q = 0.0
    for i in range(n):
        sum_l = sum(abs(A[i, j]) for j in range(i))
        sum_u = sum(abs(A[i, j]) for j in range(i+1, n))
        q_i = sum_l / (abs(A[i,i]) - sum_u) if (abs(A[i,i]) - sum_u) > 0 else float('inf')
        q = max(q, q_i)
    
    eps0 = epsilon * (1 - s) * (1 - q) / q if q < 1 and q > 0 else (epsilon if epsilon is not None else 1e-5)
    md.append(f"Ma trận sau hoán vị đã chéo trội hàng ($s = 0$). Hệ số $q \\\\approx {q:.5f}$")
    md.append(f"$$ \\\\varepsilon_0 = \\\\frac{{\\\\varepsilon(1-s)(1-q)}}{{q}} = {eps0:.5e} $$")
'''
            new_source = source[:end_line_idx] + replacement_cond + source[end_line_idx:]
            
            # Now we must make sure eps0 is used inside the loop
            # find: eps0 = epsilon if epsilon is not None else 1e-5
            new_source = new_source.replace('    eps0 = epsilon if epsilon is not None else 1e-5\n', '')
            # Actually, `fix_swap.py` already added `eps0 = epsilon if epsilon is not None else 1e-5`. We just deleted it, which means we will use the `eps0` calculated in `replacement_cond`.
            
            lines = [line + '\n' for line in new_source.split('\n')]
            if lines: lines[-1] = lines[-1].rstrip('\n')
            cell['source'] = lines
    
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)


base = r"scripts/CHƯƠNG 4 GIẢI HỆ ĐẠI SỐ TUYẾN TÍNH & TÌM MA TRẬN NGHỊCH ĐẢO/Lặp Gauss-Seidel/"
patch_axb(os.path.join(base, "Lặp Gauss-Seidel (Ax=B).ipynb"))
patch_bxd(os.path.join(base, "Lặp Gauss-Seidel (x=Bx+d).ipynb"))
patch_swap(os.path.join(base, "Lặp Gauss-Seidel (Đổi dòng tạo chéo trội).ipynb"))

print("Patched all 3 files")
