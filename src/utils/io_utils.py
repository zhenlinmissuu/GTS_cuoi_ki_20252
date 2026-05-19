from tabulate import tabulate
import json
import os

def print_table(headers, data, title=""):
    """In bảng dữ liệu với định dạng đẹp."""
    if title:
        print(f"\n--- {title} ---")
    print(tabulate(data, headers=headers, tablefmt="fancy_grid", floatfmt=".6f"))
    print()

def print_step(message):
    """In thông báo bước thực hiện."""
    print(f"[*] {message}")

def print_success(message):
    """In thông báo thành công."""
    print(f"[+] {message}")

def print_error(message):
    """In thông báo lỗi."""
    print(f"[-] LỖI: {message}")

def print_formula(formula_name, formula_text):
    """In công thức toán học được áp dụng."""
    print(f"\n[Công thức] {formula_name}:")
    print(f"    {formula_text}\n")

def generate_sample_files(target_dir):
    """Tạo các file mẫu (.json) để người dùng tham khảo cách nhập dữ liệu."""
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    samples = {
        "roots_sample.json": {
            "method": "bisection",
            "f": "x^3 - x - 2",
            "a": 1.0,
            "b": 2.0,
            "tol": 1e-5,
            "max_iter": 50
        },
        "linear_sample.json": {
            "method": "gauss",
            "A": [
                [3, -0.1, -0.2],
                [0.1, 7, -0.3],
                [0.3, -0.2, 10]
            ],
            "b": [7.85, -19.3, 71.4]
        },
        "interpolation_sample.json": {
            "method": "lagrange",
            "x": [0, 1, 2, 3],
            "y": [1, 2, 1, 10],
            "x_eval": 1.5
        },
        "integration_sample.json": {
            "method": "simpson_13",
            "f": "sin(x)",
            "a": 0,
            "b": 3.14159265359,
            "n": 10
        },
        "differential_sample.json": {
            "method": "rk4",
            "f": "x + y",
            "x0": 0,
            "y0": 1,
            "h": 0.1,
            "n": 5
        }
    }

    for filename, content in samples.items():
        filepath = os.path.join(target_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(content, f, indent=4, ensure_ascii=False)
    
    print_success(f"Đã tạo các file dữ liệu mẫu tại: {target_dir}")

def read_json_input(filepath):
    """Đọc dữ liệu từ file JSON."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print_error(f"Không thể đọc file {filepath}. Lỗi: {e}")
        return None
