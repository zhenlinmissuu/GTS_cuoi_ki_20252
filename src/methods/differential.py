from src.utils.math_utils import evaluate_f_xy

def euler(f_str, x0, y0, h, n):
    """
    Phương pháp Euler hiện giải phương trình vi phân y' = f(x, y).
    """
    history = []
    x, y = x0, y0
    
    history.append({
        "Bước i": 0,
        "x_i": x,
        "y_i": y,
        "f(x_i, y_i)": evaluate_f_xy(f_str, x, y)
    })
    
    for i in range(1, n + 1):
        f_xy = evaluate_f_xy(f_str, x, y)
        y = y + h * f_xy
        x = x + h
        
        history.append({
            "Bước i": i,
            "x_i": x,
            "y_i": y,
            "f(x_i, y_i)": evaluate_f_xy(f_str, x, y) if i < n else "-"
        })
        
    return y, history, f"Giá trị xấp xỉ tại x = {x:.4f} là y = {y:.6f}"

def rk4(f_str, x0, y0, h, n):
    """
    Phương pháp Runge-Kutta bậc 4 (RK4).
    """
    history = []
    x, y = x0, y0
    
    for i in range(n):
        k1 = h * evaluate_f_xy(f_str, x, y)
        k2 = h * evaluate_f_xy(f_str, x + h/2, y + k1/2)
        k3 = h * evaluate_f_xy(f_str, x + h/2, y + k2/2)
        k4 = h * evaluate_f_xy(f_str, x + h, y + k3)
        
        y_new = y + (k1 + 2*k2 + 2*k3 + k4) / 6
        x_new = x + h
        
        history.append({
            "Bước i": i,
            "x_i": x,
            "y_i": y,
            "k1": k1,
            "k2": k2,
            "k3": k3,
            "k4": k4,
            "y_{i+1}": y_new
        })
        
        x, y = x_new, y_new
        
    return y, history, f"Giá trị xấp xỉ tại x = {x:.4f} là y = {y:.6f}"
