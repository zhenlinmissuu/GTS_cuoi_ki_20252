import sympy as sp
import numpy as np

def parse_expr(f_str):
    """Phân tích chuỗi thành biểu thức sympy."""
    # Thay thế các ký hiệu toán học thông thường để tương thích với sympy
    f_str = f_str.replace('^', '**')
    return sp.sympify(f_str)

def evaluate_f(f_str, x_val):
    """Tính giá trị của hàm f(x) tại điểm x_val."""
    x = sp.Symbol('x')
    expr = parse_expr(f_str)
    return float(expr.subs(x, x_val))

def evaluate_f_xy(f_str, x_val, y_val):
    """Tính giá trị của hàm f(x, y) tại (x_val, y_val)."""
    x, y = sp.symbols('x y')
    expr = parse_expr(f_str)
    return float(expr.subs({x: x_val, y: y_val}))

def get_derivative(f_str):
    """Lấy đạo hàm bậc 1 của hàm số (trả về chuỗi)."""
    x = sp.Symbol('x')
    expr = parse_expr(f_str)
    d_expr = sp.diff(expr, x)
    return str(d_expr)
