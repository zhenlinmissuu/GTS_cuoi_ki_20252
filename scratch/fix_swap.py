import json
import sys

def modify_swap(path):
    with open(path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
        
    for cell in nb['cells']:
        if cell['cell_type'] == 'code':
            source = "".join(cell['source'])
            
            # Find the start of the table block
            start_idx = source.find('    header = "| $k$ | "')
            if start_idx == -1: continue
            
            # Find the end of the display block
            end_idx = source.find("    display(Markdown('\\n'.join(md)))")
            if end_idx == -1: continue
            end_idx += len("    display(Markdown('\\n'.join(md)))")
            
            # The replacement code
            replacement = '''    history = []
    diffs = []
    k = 1
    max_safe_iters = max_iter if max_iter is not None else 100
    eps0 = epsilon if epsilon is not None else 1e-5
    
    while True:
        X_new = np.copy(X_k)
        for i in range(n):
            s1 = sum(B[i, j] * X_new[j] for j in range(i))
            s2 = sum(B[i, j] * X_k[j] for j in range(i, n))
            X_new[i] = s1 + s2 + d[i]
            
        diff = np.linalg.norm(X_new - X_k, np.inf)
        history.append(X_new.copy())
        diffs.append(diff)
        
        if diff < eps0 or k >= max_safe_iters:
            break
        k += 1
        X_k = np.copy(X_new)
        
    N = len(history)
    if N <= 5:
        cols = list(range(1, N+1))
    else:
        cols = [1, 2, -1, N-1, N]
        
    header = "| | " + " | ".join([f"Lần {c}" if c != -1 else "..." for c in cols]) + " |"
    sep = "|---|" + "|".join(["---" for c in cols]) + "|"
    lines = [header, sep]
    
    for i in range(n):
        row = [f"$x_{{{i+1}}}$"]
        for c in cols:
            if c == -1:
                row.append("...")
            else:
                row.append(f"{history[c-1][i]:.5f}")
        lines.append("| " + " | ".join(row) + " |")
        
    row = [f"$|| x_k - x_{{k-1}} ||$"]
    for c in cols:
        if c == -1:
            row.append("...")
        else:
            val_str = f"{diffs[c-1]:.5f}"
            if c == N:
                val_str += f" < \\\\varepsilon_0"
            elif c == N-1:
                val_str += f" > \\\\varepsilon_0"
            row.append(val_str)
    lines.append("| " + " | ".join(row) + " |")
    
    md.extend(lines)
    
    md.append("\\n---\\n### IV. KẾT LUẬN")
    md.append(f"Hệ dừng lại tại bước lặp $k = {N}$. Nghiệm gần đúng là:")
    md.append(f"$$ X \\\\approx {{matrix_to_latex(history[-1], precision=5)}} $$")
    
    display(Markdown('\\n'.join(md)))'''
            
            new_source = source[:start_idx] + replacement + source[end_idx:]
            
            # Update cell source by re-splitting into lines
            lines = [line + '\n' for line in new_source.split('\n')]
            if lines: lines[-1] = lines[-1].rstrip('\n')
            cell['source'] = lines
            break
            
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)

modify_swap('scripts/CHƯƠNG 4 GIẢI HỆ ĐẠI SỐ TUYẾN TÍNH & TÌM MA TRẬN NGHỊCH ĐẢO/Lặp Gauss-Seidel/Lặp Gauss-Seidel (Đổi dòng tạo chéo trội).ipynb')
