# Phần Mềm Giải Tích Số - Phương Pháp Tính (CLI)

Đây là một ứng dụng Command Line Interface (CLI) được viết bằng Python, chuyên dùng để giải các bài toán Giải Tích Số (Phương Pháp Tính) cơ bản. 

Ứng dụng được thiết kế theo hướng module hóa, tách biệt logic toán học và giao diện người dùng. Đặc biệt, ứng dụng không chỉ đưa ra kết quả cuối cùng mà còn **in ra chi tiết từng bước giải**, bảng các lần lặp và công thức được áp dụng, rất hữu ích cho việc học tập và kiểm tra kết quả tính toán tay.

## 🚀 Tính Năng Chính

*   **Tìm Nghiệm Phương Trình (Root-Finding):**
    *   Phương pháp Phân đôi (Bisection)
    *   Phương pháp Tiếp tuyến (Newton-Raphson)
    *   Phương pháp Dây cung (Secant)
*   **Giải Hệ Phương Trình Tuyến Tính (Linear Systems):**
    *   Phương pháp Khử Gauss (với xoay vòng một phần - Partial Pivoting)
    *   Phương pháp lặp Jacobi
    *   Phương pháp lặp Gauss-Seidel
*   **Nội Suy và Xấp Xỉ (Interpolation & Approximation):**
    *   Đa thức nội suy Lagrange
    *   Đa thức nội suy Newton (với bảng sai phân tỷ đối)
    *   Xấp xỉ Bình phương tối thiểu (Least Squares)
*   **Tính Tích Phân Số (Numerical Integration):**
    *   Phương pháp Hình thang (Trapezoidal)
    *   Phương pháp Simpson 1/3
    *   Phương pháp Simpson 3/8
*   **Giải Phương Trình Vi Phân (Differential Equations):**
    *   Phương pháp Euler (hiện)
    *   Phương pháp Runge-Kutta bậc 4 (RK4)

## 📁 Cấu Trúc Thư Mục

```text
.
├── requirements.txt         # Khai báo các thư viện Python cần thiết
├── main.py                  # Entry-point của ứng dụng CLI
└── src/
    ├── utils/
    │   ├── math_utils.py    # Tiện ích xử lý biểu thức toán học (Sympy)
    │   └── io_utils.py      # Tiện ích định dạng bảng (Tabulate) và File I/O
    └── methods/
        ├── roots.py         # Module tìm nghiệm
        ├── linear.py        # Module giải hệ phương trình
        ├── interpolation.py # Module nội suy & xấp xỉ
        ├── integration.py   # Module tính tích phân
        └── differential.py  # Module giải phương trình vi phân
```

## 🛠️ Cài Đặt

1. Đảm bảo bạn đã cài đặt **Python 3.8+**.
2. Mở terminal tại thư mục dự án và cài đặt các thư viện yêu cầu:

```bash
pip install -r requirements.txt
```

*(Các thư viện sử dụng: `numpy` cho tính toán ma trận/mảng, `sympy` để phân tích biểu thức và tính đạo hàm tự động, `tabulate` để vẽ bảng kết quả đẹp mắt trên terminal).*

## 📖 Hướng Dẫn Sử Dụng

Ứng dụng hỗ trợ 3 chế độ chạy (modes) thông qua tham số dòng lệnh `--mode`.

### 1. Chế Độ Sinh File Mẫu (`samples`)
Nếu bạn không biết cách cấu hình file đầu vào cho từng phương pháp, hãy dùng lệnh này để tự động sinh ra các file `.json` mẫu vào thư mục `samples/`.

```bash
python main.py --mode samples
```

### 2. Chế Độ Đọc File (`file`) - Khuyên dùng
Đây là chế độ mạnh mẽ nhất. Bạn định nghĩa toàn bộ bài toán (hàm số, ma trận, khoảng phân ly, sai số...) vào một file JSON và truyền cho ứng dụng.

```bash
# Ví dụ chạy giải phương trình tìm nghiệm:
python main.py --mode file --file samples/roots_sample.json

# Ví dụ chạy giải hệ phương trình:
python main.py --mode file --file samples/linear_sample.json
```

**Cấu trúc mẫu của một bài toán giải tích phân (integration_sample.json):**
```json
{
    "method": "simpson_13",
    "f": "sin(x)",
    "a": 0,
    "b": 3.14159265359,
    "n": 10
}
```

### 3. Chế Độ Nhập Tay (`interactive`)
Chế độ tương tác trực tiếp trên Terminal. Phù hợp cho các bài toán đơn giản, nhập tay nhanh các thông số.

```bash
python main.py --mode interactive
# Hoặc đơn giản là gọi:
python main.py
```
*(Lưu ý: Chế độ này có thể bị giới hạn ở một số phương pháp phức tạp như nhập ma trận lớn, khuyên dùng chế độ `file` để trải nghiệm tốt nhất).*

## 📝 Lưu Ý Khi Nhập Hàm Số (Hàm `f(x)`)
*   Sử dụng biến `x` (và `y` đối với hệ phương trình vi phân).
*   Các phép toán cơ bản: `+`, `-`, `*`, `/`.
*   Lũy thừa có thể dùng `^` hoặc `**` (ví dụ: `x^2` hoặc `x**2`).
*   Các hàm lượng giác/mũ: `sin(x)`, `cos(x)`, `exp(x)`, `log(x)` (logarit tự nhiên). (Được phân tích tự động thông qua thư viện `sympy`).

---
*Chúc bạn học tốt môn Giải Tích Số / Phương Pháp Tính!*
