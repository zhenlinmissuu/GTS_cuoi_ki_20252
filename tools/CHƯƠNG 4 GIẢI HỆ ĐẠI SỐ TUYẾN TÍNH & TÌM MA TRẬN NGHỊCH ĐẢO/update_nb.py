import json

notebook_path = "d:/code/Uni/On_thi_cuoi_ky/Giải tích số/scripts/CHƯƠNG 4 GIẢI HỆ ĐẠI SỐ TUYẾN TÍNH & TÌM MA TRẬN NGHỊCH ĐẢO/Viền quanh.ipynb"

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

new_source = """import numpy as np

def print_latex(M, precision=4):
    import numpy as np
    if not isinstance(M, np.ndarray):
        latex_str = f"{M}"
    elif M.ndim == 1:
        inner = " & ".join([f"{x:.{precision}f}" for x in M])
        latex_str = f"\\\\begin{{bmatrix}} {inner} \\\\end{{bmatrix}}"
    else:
        rows = " \\\\\\\\ ".join([" & ".join([f"{x:.{precision}f}" for x in row]) for row in M])
        latex_str = f"\\\\begin{{bmatrix}} {rows} \\\\end{{bmatrix}}"

    try:
        get_ipython()
        in_jupyter = True
    except NameError:
        in_jupyter = False

    if in_jupyter:
        from IPython.display import display, Math
        display(Math(latex_str))
    else:
        print(f"$$ {latex_str} $$")

def Vien_Quanh(A_input):
    SEP = "═" * 62
    sep = "─" * 62
    print(SEP)
    print("    TÌM MA TRẬN NGHỊCH ĐẢO BẰNG PHƯƠNG PHÁP VIỀN QUANH")
    print(SEP)

    n = len(A_input)
    A = A_input.copy().astype(float)
    
    print("\\nI. CƠ SỞ LÝ THUYẾT")
    print("   Tính ma trận nghịch đảo A_k⁻¹ của các ma trận con chính A_k (k=1..n).")
    print("   Tại bước k, phân hoạch A_k = [A_{k-1}  u_k ; v_k^T  a_kk].")
    print("   Tính x_k = A_{k-1}⁻¹·u_k,  y_k^T = v_k^T·A_{k-1}⁻¹.")
    print("   Tính α_k = a_kk - v_k^T·x_k. Nếu α_k = 0, hoán vị dòng (nếu cần).")
    print("   Tính các khối của A_k⁻¹:")
    print("     s_k = 1/α_k, q_k = -s_k·x_k, r_k^T = -s_k·y_k^T")
    print("     P_k = A_{k-1}⁻¹ + s_k·x_k·y_k^T")
    print("     A_k⁻¹ = [P_k  q_k ; r_k^T  s_k]")

    print(f"\\nII. DỮ LIỆU BÀI TOÁN")
    print(f"   Ma trận gốc A ({n}×{n}):")
    print_latex(A_input, precision=4)

    print(f"\\nIII. QUÁ TRÌNH TÍNH TOÁN")
    row_swaps = []
    
    if abs(A[0, 0]) < 1e-14:
        found = False
        for j in range(1, n):
            if abs(A[j, 0]) >= 1e-14:
                A[[0, j]] = A[[j, 0]]
                row_swaps.append((0, j))
                print(f"   [!] a_11 = 0. Đã hoán vị dòng 1 và dòng {j+1} của ma trận.")
                found = True
                break
        if not found:
            print("   => LỖI: Cột 1 toàn số 0, ma trận suy biến.")
            return

    A_inv_k = np.array([[1.0 / A[0, 0]]])
    print(f"\\n   -- Bước 1 (k = 1) --")
    print(f"   A_1 = [{A[0,0]:.4f}], A_1⁻¹ = [{A_inv_k[0,0]:.6f}]")

    for k in range(2, n + 1):
        print(f"\\n   -- Bước {k} (k = {k}) --")
        u_k = A[0:k-1, k-1].reshape(-1, 1)
        v_k_T = A[k-1, 0:k-1].reshape(1, -1)
        a_kk = A[k-1, k-1]

        x_k = A_inv_k @ u_k
        y_k_T = v_k_T @ A_inv_k
        alpha_k = a_kk - (v_k_T @ x_k)[0, 0]

        if abs(alpha_k) < 1e-14:
            found = False
            for j in range(k, n):
                v_temp_T = A[j, 0:k-1].reshape(1, -1)
                a_temp = A[j, k-1]
                alpha_temp = a_temp - (v_temp_T @ x_k)[0, 0]
                if abs(alpha_temp) >= 1e-14:
                    A[[k-1, j]] = A[[j, k-1]]
                    row_swaps.append((k-1, j))
                    print(f"   [!] α_{k} = 0. Đã hoán vị dòng {k} và dòng {j+1}.")
                    v_k_T = v_temp_T
                    a_kk = a_temp
                    alpha_k = alpha_temp
                    y_k_T = v_k_T @ A_inv_k
                    found = True
                    break
            if not found:
                print(f"   => LỖI: Không thể hoán vị để α_{k} != 0. Ma trận suy biến.")
                return

        print(f"   u_k:")
        print_latex(u_k, precision=4)
        print(f"   v_k^T:")
        print_latex(v_k_T, precision=4)
        print(f"   x_k = A_{k-1}⁻¹·u_k:")
        print_latex(x_k, precision=4)
        print(f"   y_k^T = v_k^T·A_{k-1}⁻¹:")
        print_latex(y_k_T, precision=4)

        print(f"   α_k = a_kk - v_k^T·x_k = {a_kk:.4f} - {(a_kk - alpha_k):.4f} = {alpha_k:.6f}")
        
        s_k = 1.0 / alpha_k
        q_k = -s_k * x_k
        r_k_T = -s_k * y_k_T
        P_k = A_inv_k + s_k * (x_k @ y_k_T)

        print(f"   s_k = 1 / α_k = {s_k:.6f}")
        print(f"   q_k = -s_k·x_k:")
        print_latex(q_k, precision=4)
        print(f"   r_k^T = -s_k·y_k^T:")
        print_latex(r_k_T, precision=4)
        print(f"   P_k:")
        print_latex(P_k, precision=4)

        A_inv_next = np.zeros((k, k))
        A_inv_next[0:k-1, 0:k-1] = P_k
        A_inv_next[0:k-1, k-1] = q_k.flatten()
        A_inv_next[k-1, 0:k-1] = r_k_T.flatten()
        A_inv_next[k-1, k-1] = s_k

        A_inv_k = A_inv_next
        print(f"   Ma trận A_{k}⁻¹:")
        print_latex(A_inv_k, precision=6)

    print(f"\\nIV. KẾT LUẬN")
    if row_swaps:
        print("   Ma trận (A')⁻¹ (trước khi hoán vị ngược lại):")
        print_latex(A_inv_k, precision=6)
        
        A_inv_final = A_inv_k.copy()
        for i, j in reversed(row_swaps):
            A_inv_final[:, [i, j]] = A_inv_final[:, [j, i]]
            print(f"   [!] Đã hoán vị cột {i+1} và cột {j+1}.")
            
        print("   Ma trận nghịch đảo A⁻¹ (sau khi hoán vị cột):")
        print_latex(A_inv_final, precision=6)
    else:
        A_inv_final = A_inv_k
        print("   Ma trận nghịch đảo A⁻¹:")
        print_latex(A_inv_final, precision=6)
        
    err = np.linalg.norm(A_input @ A_inv_final - np.eye(n), np.inf)
    print(f"   Kiểm tra: ||A·A⁻¹ − I||∞ = {err:.2e}  {'✓' if err < 1e-6 else '≈0'}")


# Ví dụ ma trận A
A = np.array([
    [ 0, -5, -8, -5, -1, -4],
    [10,  0, -7,  9, -3,  5],
    [-3,  4, -5, -3,  7,  5],
    [ 2,  8,  7, -6,  2, -3],
    [-6, 10, -5, -5,  1,  1],
    [ 5,  1,  7,  2,  9, -9]
])

Vien_Quanh(A)
"""

# Convert to list of lines with newlines
source_lines = [line + '\\n' for line in new_source.split('\\n')]
source_lines[-1] = source_lines[-1][:-1] # remove last newline

# Find the code cell with Vien_Quanh
for cell in nb.get('cells', []):
    if cell['cell_type'] == 'code':
        # Check if def Vien_Quanh is in this cell
        if any('def Vien_Quanh' in line for line in cell.get('source', [])):
            cell['source'] = source_lines
            # Also clear outputs so it can be re-run freshly
            cell['outputs'] = []

with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print("Updated notebook successfully!")
