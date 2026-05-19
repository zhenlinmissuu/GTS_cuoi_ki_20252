from src.utils.math_utils import evaluate_f

def hinh_thang(f_str, a, b, n):
    """
    Phương pháp tích phân Hình thang (Trapezoidal Rule).
    """
    h = (b - a) / n
    history = []
    
    sum_val = 0.0
    for i in range(n + 1):
        xi = a + i * h
        fi = evaluate_f(f_str, xi)
        
        weight = 1 if (i == 0 or i == n) else 2
        sum_val += weight * fi
        
        history.append({
            "i": i,
            "x_i": xi,
            "f(x_i)": fi,
            "Hệ số": weight,
            "Thành phần": weight * fi
        })
        
    result = (h / 2) * sum_val
    return result, history, f"Tích phân xấp xỉ bằng PP Hình thang: {result:.6f}"

def simpson_13(f_str, a, b, n):
    """
    Phương pháp Simpson 1/3. Yêu cầu n chẵn.
    """
    if n % 2 != 0:
        return None, [], "Lỗi: Phương pháp Simpson 1/3 yêu cầu n là số chẵn."
        
    h = (b - a) / n
    history = []
    
    sum_val = 0.0
    for i in range(n + 1):
        xi = a + i * h
        fi = evaluate_f(f_str, xi)
        
        if i == 0 or i == n:
            weight = 1
        elif i % 2 != 0:
            weight = 4
        else:
            weight = 2
            
        sum_val += weight * fi
        history.append({
            "i": i,
            "x_i": xi,
            "f(x_i)": fi,
            "Hệ số": weight,
            "Thành phần": weight * fi
        })
        
    result = (h / 3) * sum_val
    return result, history, f"Tích phân xấp xỉ bằng PP Simpson 1/3: {result:.6f}"

def simpson_38(f_str, a, b, n):
    """
    Phương pháp Simpson 3/8. Yêu cầu n chia hết cho 3.
    """
    if n % 3 != 0:
        return None, [], "Lỗi: Phương pháp Simpson 3/8 yêu cầu n chia hết cho 3."
        
    h = (b - a) / n
    history = []
    
    sum_val = 0.0
    for i in range(n + 1):
        xi = a + i * h
        fi = evaluate_f(f_str, xi)
        
        if i == 0 or i == n:
            weight = 1
        elif i % 3 != 0:
            weight = 3
        else:
            weight = 2
            
        sum_val += weight * fi
        history.append({
            "i": i,
            "x_i": xi,
            "f(x_i)": fi,
            "Hệ số": weight,
            "Thành phần": weight * fi
        })
        
    result = (3 * h / 8) * sum_val
    return result, history, f"Tích phân xấp xỉ bằng PP Simpson 3/8: {result:.6f}"
