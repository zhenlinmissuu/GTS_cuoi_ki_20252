import math
from src.utils.math_utils import evaluate_f, get_derivative

def phan_doi(f_str, a, b, tol=1e-5, max_iter=50):
    """
    Phương pháp Phân đôi (Bisection Method).
    Trả về (nghiệm, lịch_sử, thông_báo).
    """
    fa = evaluate_f(f_str, a)
    fb = evaluate_f(f_str, b)
    
    if fa * fb > 0:
        return None, [], "Lỗi: f(a) và f(b) phải trái dấu."

    history = []
    c = a
    for i in range(1, max_iter + 1):
        c = (a + b) / 2
        fc = evaluate_f(f_str, c)
        error = abs(b - a) / 2
        
        history.append({
            "Lần lặp": i,
            "a": a,
            "b": b,
            "c (Nghiệm xấp xỉ)": c,
            "f(c)": fc,
            "Sai số": error
        })
        
        if error < tol or abs(fc) < 1e-15:
            return c, history, f"Hội tụ sau {i} vòng lặp."
            
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
            
    return c, history, f"Đạt số lần lặp tối đa ({max_iter}) nhưng chưa hội tụ."

def tiep_tuyen(f_str, x0, tol=1e-5, max_iter=50):
    """
    Phương pháp Tiếp tuyến (Newton-Raphson).
    """
    df_str = get_derivative(f_str)
    history = []
    x = x0
    
    for i in range(1, max_iter + 1):
        fx = evaluate_f(f_str, x)
        dfx = evaluate_f(df_str, x)
        
        if dfx == 0:
            return None, history, "Lỗi: Đạo hàm bằng 0, không thể tiếp tục."
            
        x_new = x - fx / dfx
        error = abs(x_new - x)
        
        history.append({
            "Lần lặp": i,
            "x_n": x,
            "f(x_n)": fx,
            "f'(x_n)": dfx,
            "x_{n+1}": x_new,
            "Sai số": error
        })
        
        if error < tol:
            return x_new, history, f"Hội tụ sau {i} vòng lặp."
            
        x = x_new
        
    return x, history, f"Đạt số lần lặp tối đa ({max_iter}) nhưng chưa hội tụ."

def day_cung(f_str, x0, x1, tol=1e-5, max_iter=50):
    """
    Phương pháp Dây cung (Secant Method).
    """
    history = []
    
    for i in range(1, max_iter + 1):
        fx0 = evaluate_f(f_str, x0)
        fx1 = evaluate_f(f_str, x1)
        
        if fx1 - fx0 == 0:
            return None, history, "Lỗi: Mẫu số bằng 0, không thể tiếp tục."
            
        x_new = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        error = abs(x_new - x1)
        
        history.append({
            "Lần lặp": i,
            "x_{n-1}": x0,
            "x_n": x1,
            "f(x_n)": fx1,
            "x_{n+1}": x_new,
            "Sai số": error
        })
        
        if error < tol:
            return x_new, history, f"Hội tụ sau {i} vòng lặp."
            
        x0 = x1
        x1 = x_new
        
    return x1, history, f"Đạt số lần lặp tối đa ({max_iter}) nhưng chưa hội tụ."
