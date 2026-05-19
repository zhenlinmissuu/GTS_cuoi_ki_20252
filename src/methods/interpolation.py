import numpy as np

def lagrange(x_pts, y_pts, x_eval):
    """
    Nội suy Lagrange.
    """
    n = len(x_pts)
    result = 0.0
    history = []
    
    for i in range(n):
        term = y_pts[i]
        L_i_str = f"{y_pts[i]}"
        
        for j in range(n):
            if i != j:
                term = term * (x_eval - x_pts[j]) / (x_pts[i] - x_pts[j])
                L_i_str += f" * ({x_eval} - {x_pts[j]}) / ({x_pts[i]} - {x_pts[j]})"
                
        result += term
        history.append({
            "Hạng tử i": i,
            "L_i(x_eval) biểu thức": L_i_str,
            "Giá trị L_i": term
        })
        
    return result, history, f"Giá trị nội suy tại x = {x_eval} là {result}"

def newton_sai_phan(x_pts, y_pts, x_eval):
    """
    Nội suy Newton với bảng sai phân tỷ đối (Divided Differences).
    """
    n = len(x_pts)
    F = np.zeros((n, n))
    F[:, 0] = y_pts
    
    # Tính bảng sai phân tỷ đối
    for j in range(1, n):
        for i in range(n - j):
            F[i, j] = (F[i + 1, j - 1] - F[i, j - 1]) / (x_pts[i + j] - x_pts[i])
            
    # Tạo bảng lịch sử (trace) để in ra
    history_table = []
    for i in range(n):
        row = {"x": x_pts[i]}
        for j in range(n - i):
            row[f"Sai phân bậc {j}"] = F[i, j]
        history_table.append(row)
        
    # Tính giá trị tại x_eval
    result = F[0, 0]
    term = 1.0
    calc_steps = [f"P(x) = {F[0,0]}"]
    
    for i in range(1, n):
        term *= (x_eval - x_pts[i - 1])
        add_val = F[0, i] * term
        result += add_val
        calc_steps.append(f"+ ({F[0,i]}) * tích(x - x_k) = {add_val}")
        
    return result, (history_table, calc_steps), f"Giá trị nội suy tại x = {x_eval} là {result}"

def binh_phuong_toi_thieu(x_pts, y_pts, degree):
    """
    Xấp xỉ bình phương tối thiểu (Least Squares) bậc 'degree'.
    """
    x = np.array(x_pts)
    y = np.array(y_pts)
    
    # Tạo ma trận A
    A = np.vander(x, degree + 1, increasing=True)
    # Giải hệ A^T * A * c = A^T * y
    At = A.T
    Normal_Mat = At @ A
    Normal_Vec = At @ y
    
    coeffs = np.linalg.solve(Normal_Mat, Normal_Vec)
    
    history = {
        "Ma trận A": A.tolist(),
        "Ma trận A^T * A": Normal_Mat.tolist(),
        "Vector A^T * y": Normal_Vec.tolist(),
        "Hệ số (từ bậc 0)": coeffs.tolist()
    }
    
    # Tạo biểu thức
    poly_str = " + ".join([f"({c:.4f})*x^{i}" for i, c in enumerate(coeffs)])
    return coeffs.tolist(), history, f"Đa thức xấp xỉ: {poly_str}"
