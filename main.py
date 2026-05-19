import argparse
import sys
import os

# Thêm thư mục gốc vào sys.path để import dễ dàng
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.utils.io_utils import (
    generate_sample_files, read_json_input, print_table, 
    print_step, print_success, print_error, print_formula
)

import src.methods.roots as roots
import src.methods.linear as linear
import src.methods.interpolation as interpolation
import src.methods.integration as integration
import src.methods.differential as differential

def handle_roots(data):
    method = data.get("method")
    f_str = data.get("f")
    tol = data.get("tol", 1e-5)
    max_iter = data.get("max_iter", 50)
    
    print_formula("Hàm số", f"f(x) = {f_str}")
    
    if method == "bisection":
        a, b = data.get("a"), data.get("b")
        print_formula("Phương pháp Phân đôi", "c = (a + b) / 2")
        result, history, msg = roots.phan_doi(f_str, a, b, tol, max_iter)
        if history:
            print_table(history[0].keys(), [list(row.values()) for row in history], "Bảng phân đôi")
            
    elif method == "newton":
        x0 = data.get("x0")
        print_formula("Phương pháp Tiếp tuyến", "x_{n+1} = x_n - f(x_n)/f'(x_n)")
        result, history, msg = roots.tiep_tuyen(f_str, x0, tol, max_iter)
        if history:
            print_table(history[0].keys(), [list(row.values()) for row in history], "Bảng tiếp tuyến")
            
    elif method == "secant":
        x0, x1 = data.get("x0"), data.get("x1")
        print_formula("Phương pháp Dây cung", "x_{n+1} = x_n - f(x_n)*(x_n - x_{n-1})/(f(x_n) - f(x_{n-1}))")
        result, history, msg = roots.day_cung(f_str, x0, x1, tol, max_iter)
        if history:
            print_table(history[0].keys(), [list(row.values()) for row in history], "Bảng dây cung")
    else:
        print_error("Phương pháp không hợp lệ.")
        return
        
    print_step(msg)
    if result is not None:
        print_success(f"Nghiệm xấp xỉ cuối cùng: {result:.6f}")

def handle_linear(data):
    method = data.get("method")
    A = data.get("A")
    b = data.get("b")
    
    print_formula("Hệ phương trình", "A * x = b")
    
    if method == "gauss":
        print_step("Áp dụng Khử Gauss với xoay vòng một phần...")
        result, history, msg = linear.khu_gauss(A, b)
        for step_name, mat in history:
            print(f"\n[*] {step_name}")
            print_table([], mat, "")
            
    elif method in ["jacobi", "gauss_seidel"]:
        x0 = data.get("x0")
        tol = data.get("tol", 1e-5)
        max_iter = data.get("max_iter", 50)
        
        if method == "jacobi":
            print_formula("Phương pháp Jacobi", "x_i^{(k+1)} = (b_i - sum(A_{ij} * x_j^{(k)})) / A_{ii}")
            result, history, msg = linear.jacobi(A, b, x0, tol, max_iter)
        else:
            print_formula("Phương pháp Gauss-Seidel", "Sử dụng giá trị x mới nhất ngay khi tính được")
            result, history, msg = linear.gauss_seidel(A, b, x0, tol, max_iter)
            
        if history:
            print_table(history[0].keys(), [list(row.values()) for row in history], f"Bảng lặp {method.capitalize()}")
    else:
        print_error("Phương pháp không hợp lệ.")
        return
        
    print_step(msg)
    if result is not None:
        print_success(f"Nghiệm của hệ: {result}")

def handle_interpolation(data):
    method = data.get("method")
    x_pts = data.get("x")
    y_pts = data.get("y")
    
    if method == "lagrange":
        x_eval = data.get("x_eval")
        print_formula("Nội suy Lagrange", "P(x) = sum(y_i * L_i(x))")
        result, history, msg = interpolation.lagrange(x_pts, y_pts, x_eval)
        if history:
            print_table(history[0].keys(), [list(row.values()) for row in history], "Tính các đa thức cơ sở L_i")
        print_success(msg)
        
    elif method == "newton":
        x_eval = data.get("x_eval")
        print_formula("Nội suy Newton", "Dựa trên bảng sai phân tỷ đối")
        result, (history_table, calc_steps), msg = interpolation.newton_sai_phan(x_pts, y_pts, x_eval)
        if history_table:
            print_table(history_table[0].keys(), [list(row.values()) for row in history_table], "Bảng sai phân tỷ đối")
        print_step("Các bước tính giá trị:")
        for step in calc_steps:
            print(f"    {step}")
        print_success(msg)
        
    elif method == "least_squares":
        degree = data.get("degree", 1)
        print_formula("Bình phương tối thiểu", f"Tìm đa thức bậc {degree}")
        result, history, msg = interpolation.binh_phuong_toi_thieu(x_pts, y_pts, degree)
        for k, v in history.items():
            print(f"[*] {k}:")
            if isinstance(v[0], list):
                for row in v:
                    print(f"    {row}")
            else:
                print(f"    {v}")
        print_success(msg)

def handle_integration(data):
    method = data.get("method")
    f_str = data.get("f")
    a, b, n = data.get("a"), data.get("b"), data.get("n")
    
    print_formula("Hàm số dưới dấu tích phân", f"f(x) = {f_str} trên đoạn [{a}, {b}] với n={n}")
    
    if method == "trapezoidal":
        result, history, msg = integration.hinh_thang(f_str, a, b, n)
    elif method == "simpson_13":
        result, history, msg = integration.simpson_13(f_str, a, b, n)
    elif method == "simpson_38":
        result, history, msg = integration.simpson_38(f_str, a, b, n)
    else:
        print_error("Phương pháp không hợp lệ.")
        return
        
    if history:
        print_table(history[0].keys(), [list(row.values()) for row in history], "Bảng chi tiết các điểm")
    print_step(msg)

def handle_differential(data):
    method = data.get("method")
    f_str = data.get("f")
    x0, y0, h, n = data.get("x0"), data.get("y0"), data.get("h"), data.get("n")
    
    print_formula("Phương trình vi phân", f"y' = {f_str}, y({x0}) = {y0}, h = {h}, số bước n = {n}")
    
    if method == "euler":
        result, history, msg = differential.euler(f_str, x0, y0, h, n)
    elif method == "rk4":
        result, history, msg = differential.rk4(f_str, x0, y0, h, n)
    else:
        print_error("Phương pháp không hợp lệ.")
        return
        
    if history:
        print_table(history[0].keys(), [list(row.values()) for row in history], f"Bảng tính {method.upper()}")
    print_success(msg)

def process_data(data):
    method = data.get("method")
    if method in ["bisection", "newton", "secant"]:
        handle_roots(data)
    elif method in ["gauss", "jacobi", "gauss_seidel"]:
        handle_linear(data)
    elif method in ["lagrange", "newton", "least_squares"]:
        handle_interpolation(data)
    elif method in ["trapezoidal", "simpson_13", "simpson_38"]:
        handle_integration(data)
    elif method in ["euler", "rk4"]:
        handle_differential(data)
    else:
        print_error(f"Không nhận diện được phương pháp: {method}")

def interactive_mode():
    print("="*50)
    print(" PHẦN MỀM GIẢI TÍCH SỐ - PHƯƠNG PHÁP TÍNH ".center(50))
    print("="*50)
    print("1. Tìm nghiệm (Phân đôi, Tiếp tuyến, Dây cung)")
    print("2. Hệ PT tuyến tính (Gauss, Jacobi, Gauss-Seidel)")
    print("3. Nội suy & Xấp xỉ (Lagrange, Newton, Bình phương tối thiểu)")
    print("4. Tích phân số (Hình thang, Simpson 1/3, Simpson 3/8)")
    print("5. PT Vi phân (Euler, RK4)")
    print("0. Thoát")
    print("="*50)
    
    choice = input("Chọn dạng bài toán (0-5): ")
    if choice == '0':
        sys.exit(0)
        
    print("\n[MẸO] Chế độ nhập tay (interactive) bị giới hạn để dễ sử dụng.")
    print("Để khai thác toàn bộ sức mạnh, vui lòng dùng chế độ chạy file JSON (python main.py --mode file --file <path.json>).")
    print("Sử dụng 'python main.py --mode samples' để tạo file mẫu.\n")
    
    if choice == '1':
        f_str = input("Nhập hàm số f(x) (vd: x**3 - x - 2): ")
        a = float(input("Nhập khoảng [a, b], a = "))
        b = float(input("Nhập khoảng [a, b], b = "))
        data = {"method": "bisection", "f": f_str, "a": a, "b": b, "tol": 1e-5, "max_iter": 50}
        process_data(data)
    elif choice == '4':
        f_str = input("Nhập hàm f(x) (vd: sin(x)): ")
        a = float(input("Nhập cận dưới a = "))
        b = float(input("Nhập cận trên b = "))
        n = int(input("Nhập số khoảng chia n = "))
        data = {"method": "simpson_13", "f": f_str, "a": a, "b": b, "n": n}
        process_data(data)
    else:
        print_error("Chế độ tương tác chi tiết chưa hỗ trợ đầy đủ cho lựa chọn này.")
        print("Vui lòng sử dụng cấu hình qua file JSON. Đang thoát...")

def main():
    parser = argparse.ArgumentParser(description="Chương trình Giải Tích Số CLI (Phương Pháp Tính)")
    parser.add_argument('--mode', choices=['interactive', 'file', 'samples'], default='interactive', 
                        help='Chế độ chạy: interactive (nhập tay), file (đọc json), samples (tạo mẫu)')
    parser.add_argument('--file', type=str, help='Đường dẫn file JSON nếu chọn --mode file')
    
    args = parser.parse_args()
    
    if args.mode == 'samples':
        samples_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'samples')
        generate_sample_files(samples_dir)
    elif args.mode == 'file':
        if not args.file:
            print_error("Vui lòng cung cấp đường dẫn file bằng tham số --file")
            return
        data = read_json_input(args.file)
        if data:
            print(f"[*] Đang giải quyết bài toán cấu hình từ file: {args.file}")
            process_data(data)
    else:
        interactive_mode()

if __name__ == "__main__":
    main()
