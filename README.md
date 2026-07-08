# 🧮 Tài Liệu Ôn Thi Cuối Kỳ - Môn Giải Tích Số (GTS_cuoi_ki_20252)

Chào mừng bạn đến với kho lưu trữ tài liệu ôn tập và bộ công cụ tự động hóa môn **Giải tích số (Numerical Analysis)**. Kho lưu trữ này được thiết kế nhằm giúp sinh viên ôn tập lý thuyết, thực hành thuật toán bằng code Python/Jupyter Notebook và đối chiếu kết quả bài tập thông qua giao diện Web trực quan.

---

## 📁 Cấu Trúc Kho Lưu Trữ

```text
├── De thi mau/             # Đề thi cuối kỳ các năm học trước (20162 - 20242)
├── anh_bai_tap/            # Hình ảnh các bài tập tự luyện và ví dụ thực hành
├── tai_lieu_pdf/           # Các tài liệu ôn tập định dạng PDF
├── tai_lieu_chu/           # Diễn giải chi tiết từng bước giải của các thuật toán chính
├── scripts/                # File học tập & thực hành chính
│   └── Giai_tich_so.ipynb  # Jupyter Notebook chứa toàn bộ thuật toán và bài tập minh họa
├── tools/                  # Bộ công cụ Python hỗ trợ tạo, cập nhật & đồng bộ hóa bài học
│   ├── generate_notebook.py
│   ├── rebuild_all.py
│   └── ...
├── web/                    # Ứng dụng Web (Flask API + HTML/CSS/JS frontend)
└── Thuat_toan_Giai_tich_so.md # Bản tóm tắt chi tiết lý thuyết và thuật toán
```

---

## 🚀 Các Thành Phần Chính

### 1. File Học Tập Chính (`Giai_tich_so.ipynb`)
Nằm trong thư mục [scripts/](file:///d:/code/Uni/On_thi_cuoi_ky/Gi%E1%BA%A3i%20t%C3%ADch%20s%E1%BB%91/scripts), đây là Jupyter Notebook toàn diện bao gồm code Python cho tất cả các chương học của môn Giải tích số:
- **Chương 2:** Giải phương trình phi tuyến 1 chiều (Chia đôi, Dây cung, Tiếp tuyến, Lặp đơn).
- **Chương 3:** Giải hệ phương trình phi tuyến nhiều chiều (Lặp đơn nhiều chiều, Newton).
- **Chương 4:** Giải hệ phương trình đại số tuyến tính & Tìm ma trận nghịch đảo (Phân tách LU, Cholesky, Gauss-Jordan, Jacobi, Gauss-Seidel).
- **Chương 5:** Giá trị riêng và Vector riêng (Phương pháp Lũy thừa, Lũy thừa giảm cấp, Khai triển SVD).
- **Chương 6:** Nội suy và Đạo hàm số (Nội suy Lagrange, Newton tiến/lùi, Đạo hàm số).
- **Chương 7:** Tính tích phân gần đúng (Hình thang, Simpson).

### 2. Bộ Công Cụ Tự Động Hóa (`tools/`)
Thư mục [tools/](file:///d:/code/Uni/On_thi_cuoi_ky/Gi%E1%BA%A3i%20t%C3%ADch%20s%E1%BB%91/tools) chứa các script Python giúp tự động hóa việc xây dựng và cập nhật tài liệu học tập:
- `rebuild_all.py`: Tự động build lại toàn bộ các phần lý thuyết và bài tập vào file notebook chính.
- `generate_notebook.py`: Tạo file Jupyter Notebook cấu trúc từ các template mã nguồn.

### 3. Ứng Dụng Web Giải Toán (`web/`)
Hỗ trợ giao diện tương tác trực quan để nhập dữ liệu bài toán (Ma trận, Hàm số, Đầu vào) và nhận lời giải chi tiết từng bước.
*Chi tiết cách khởi chạy xem tại phần hướng dẫn bên dưới.*

---

## 🛠️ Hướng Dẫn Cài Đặt và Sử Dụng

### Yêu Cầu Hệ Thống
- Đã cài đặt **Python 3.8+**
- Đã cài đặt **Git**

### Cài Đặt Thư Viện
Mở terminal tại thư mục gốc và chạy lệnh cài đặt các thư viện cần thiết:
```bash
pip install -r web/requirements.txt
```

### Chạy Ứng Dụng Web Trực Quan
1. Di chuyển vào thư mục `web`:
   ```bash
   cd web
   ```
2. Khởi chạy Flask Server:
   ```bash
   python app.py
   ```
3. Truy cập vào địa chỉ [http://localhost:5000](http://localhost:5000) trên trình duyệt để sử dụng.

### Thực Hành Jupyter Notebook
Bạn có thể mở file `scripts/Giai_tich_so.ipynb` bằng VS Code (đã cài extension Jupyter) hoặc chạy bằng Jupyter Lab:
```bash
pip install jupyterlab
jupyter lab
```

---

## 📝 Tài Liệu Hướng Dẫn Nhanh
- Để xem tóm tắt thuật toán và cách tính sai số lý thuyết, xem tại: [Thuat_toan_Giai_tich_so.md](file:///d:/code/Uni/On_thi_cuoi_ky/Gi%E1%BA%A3i%20t%C3%ADch%20s%E1%BB%91/Thuat_toan_Giai_tich_so.md)
- Để xem quy chuẩn trình bày các bài tập thi cuối kỳ, xem tại: [huong_dan_trinh_bay_bai_tap.md](file:///d:/code/Uni/On_thi_cuoi_ky/Gi%E1%BA%A3i%20t%C3%ADch%20s%E1%BB%91/tools/huong_dan_trinh_bay_bai_tap.md)
