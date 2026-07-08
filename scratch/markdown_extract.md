

# --- FROM NOTEBOOK: scripts\Giai_tich_so.ipynb ---


# TỔNG HỢP CÁC PHƯƠNG PHÁP GIẢI TÍCH SỐ



## CHƯƠNG 2: GIẢI PHƯƠNG TRÌNH PHI TUYẾN 1 CHIỀU



### Chia đôi



### Dây cung



### Tiếp tuyến (Newton)



### Lặp đơn (1 chiều)



## CHƯƠNG 3: GIẢI HỆ PHƯƠNG TRÌNH PHI TUYẾN NHIỀU CHIỀU



### Lặp đơn nhiều chiều

Phương pháp biến đổi hệ phương trình phi tuyến $F(X) = 0$ thành hệ $X = G(X)$ sao cho thỏa mãn điều kiện hội tụ (hệ số co $q < 1$).

*   **Input:** Hàm lặp $G(X) = (g_1(X), g_2(X), \dots, g_n(X))^T$, xấp xỉ ban đầu $X^{(0)}$, hệ số co $q < 1$, sai số cho phép $\epsilon$.
*   **Thuật toán:**
    *   **B1:** Lặp tính xấp xỉ mới $X^{(k+1)} = G(X^{(k)})$.
    *   **B2:** Đánh giá sai số hậu nghiệm: $\text{err} = \frac{q}{1-q} \|X^{(k+1)} - X^{(k)}\|_\infty$.
    *   **B3:** Nếu $\text{err} < \epsilon$, thuật toán dừng và trả về nghiệm $X^{(k+1)}$.


### Newton nhiều chiều



## CHƯƠNG 4: GIẢI HỆ ĐẠI SỐ TUYẾN TÍNH & TÌM MA TRẬN NGHỊCH ĐẢO



### Phân tách LU



### LU có Pivoting



### Phân tách Cholesky



### Lặp đơn (Hệ phương trình)



### Lặp Gauss-Seidel



### Nghịch đảo bằng Cholesky



### Nghịch đảo bằng Lặp Jacobi / Gauss-Seidel



### Ma trận nghịch đảo bằng phương pháp Viền quanh



## CHƯƠNG 5: GIÁ TRỊ RIÊNG VÀ VECTOR RIÊNG CỦA MA TRẬN



### Phương pháp Danielevski



### Phương pháp Xuống thàng



### Giá trị kỳ dị SVD (Lớn nhất)



### Số điều kiện Cond(A)





# --- FROM NOTEBOOK: scripts\CHƯƠNG 2 GIẢI PHƯƠNG TRÌNH PHI TUYẾN 1 CHIỀU\Chia đôi.ipynb ---


### Phương pháp Chia đôi (Bisection)





# --- FROM NOTEBOOK: scripts\CHƯƠNG 2 GIẢI PHƯƠNG TRÌNH PHI TUYẾN 1 CHIỀU\Dây cung.ipynb ---


### Phương pháp Dây cung (Secant)





# --- FROM NOTEBOOK: scripts\CHƯƠNG 2 GIẢI PHƯƠNG TRÌNH PHI TUYẾN 1 CHIỀU\Giải Đa Thức Toàn Tập.ipynb ---


### Giải Đa Thức (Cách ly & Newton)





# --- FROM NOTEBOOK: scripts\CHƯƠNG 2 GIẢI PHƯƠNG TRÌNH PHI TUYẾN 1 CHIỀU\Lặp đơn (1 chiều).ipynb ---


### Phương pháp Lặp đơn 1 chiều





# --- FROM NOTEBOOK: scripts\CHƯƠNG 2 GIẢI PHƯƠNG TRÌNH PHI TUYẾN 1 CHIỀU\So sánh các phương pháp (Lý thuyết).ipynb ---


### Lý thuyết So sánh Phương pháp





# --- FROM NOTEBOOK: scripts\CHƯƠNG 2 GIẢI PHƯƠNG TRÌNH PHI TUYẾN 1 CHIỀU\Tiếp tuyến (Newton).ipynb ---


### Phương pháp Tiếp tuyến Newton-Raphson





# --- FROM NOTEBOOK: scripts\CHƯƠNG 3 GIẢI HỆ PHƯƠNG TRÌNH PHI TUYẾN NHIỀU CHIỀU\Lặp đơn nhiều chiều.ipynb ---


### Phương pháp Lặp đơn nhiều chiều





# --- FROM NOTEBOOK: scripts\CHƯƠNG 3 GIẢI HỆ PHƯƠNG TRÌNH PHI TUYẾN NHIỀU CHIỀU\Newton nhiều chiều.ipynb ---


### Phương pháp Newton nhiều chiều





# --- FROM NOTEBOOK: scripts\CHƯƠNG 4 GIẢI HỆ ĐẠI SỐ TUYẾN TÍNH & TÌM MA TRẬN NGHỊCH ĐẢO\LU có Pivoting.ipynb ---


### LU có Hoán vị Pivot (PA = LU)





# --- FROM NOTEBOOK: scripts\CHƯƠNG 4 GIẢI HỆ ĐẠI SỐ TUYẾN TÍNH & TÌM MA TRẬN NGHỊCH ĐẢO\Lặp đơn (Hệ phương trình).ipynb ---


### Lặp Đơn (Hệ phương trình X=BX+d)





# --- FROM NOTEBOOK: scripts\CHƯƠNG 4 GIẢI HỆ ĐẠI SỐ TUYẾN TÍNH & TÌM MA TRẬN NGHỊCH ĐẢO\Nghịch đảo bằng Cholesky.ipynb ---


### Nghịch đảo qua Cholesky





# --- FROM NOTEBOOK: scripts\CHƯƠNG 4 GIẢI HỆ ĐẠI SỐ TUYẾN TÍNH & TÌM MA TRẬN NGHỊCH ĐẢO\Nghịch đảo bằng Lặp Jacobi  Gauss-Seidel.ipynb ---


### Nghịch đảo Ma Trận (Lặp Gauss-Seidel)



**Hoặc chạy theo số lần lặp cố định:**




# --- FROM NOTEBOOK: scripts\CHƯƠNG 4 GIẢI HỆ ĐẠI SỐ TUYẾN TÍNH & TÌM MA TRẬN NGHỊCH ĐẢO\Phân tách Cholesky.ipynb ---


### Phân tách Cholesky (A = LL^T)





# --- FROM NOTEBOOK: scripts\CHƯƠNG 4 GIẢI HỆ ĐẠI SỐ TUYẾN TÍNH & TÌM MA TRẬN NGHỊCH ĐẢO\Phân tách LU.ipynb ---


### Phân tách LU và Giải hệ Ax=b





# --- FROM NOTEBOOK: scripts\CHƯƠNG 4 GIẢI HỆ ĐẠI SỐ TUYẾN TÍNH & TÌM MA TRẬN NGHỊCH ĐẢO\Viền quanh.ipynb ---


### Phương pháp Viền quanh (Bordering)





# --- FROM NOTEBOOK: scripts\CHƯƠNG 4 GIẢI HỆ ĐẠI SỐ TUYẾN TÍNH & TÌM MA TRẬN NGHỊCH ĐẢO\Lặp Gauss-Seidel\Lặp Gauss-Seidel (Ax=B).ipynb ---


### Lặp Gauss-Seidel

### Yêu cầu trình bày (Ghi vào bài thi)
**1. Điều kiện hội tụ:**
Ma trận $A$ chéo trội hàng:
$$|A_{ii}| > \sum_{j \neq i} |A_{ij}| \quad \forall i$$

**2. Công thức lặp Gauss-Seidel:**
$$x_i^{(k+1)} = \frac{1}{A_{ii}} \left( b_i - \sum_{j=1}^{i-1} A_{ij} x_j^{(k+1)} - \sum_{j=i+1}^n A_{ij} x_j^{(k)} \right)$$
*(Nghĩa là: nghiệm $x_i$ ở bước mới nhất được tính bằng cách dùng ngay các $x_j$ mới nhất vừa tính được ở cùng bước)*





# --- FROM NOTEBOOK: scripts\CHƯƠNG 4 GIẢI HỆ ĐẠI SỐ TUYẾN TÍNH & TÌM MA TRẬN NGHỊCH ĐẢO\Lặp Gauss-Seidel\Lặp Gauss-Seidel (x=Bx+d).ipynb ---


### Lặp Gauss-Seidel (Hệ x = Bx + d)





# --- FROM NOTEBOOK: scripts\CHƯƠNG 4 GIẢI HỆ ĐẠI SỐ TUYẾN TÍNH & TÌM MA TRẬN NGHỊCH ĐẢO\Lặp Gauss-Seidel\Lặp Gauss-Seidel (Đổi dòng tạo chéo trội).ipynb ---


# Giải hệ phương trình bằng lặp Gauss-Seidel
**Dạng bài:** Giải hệ $Ax = b$ nhưng ma trận $A$ chưa thỏa mãn điều kiện chéo trội. Thuật toán sẽ tự động dò tìm hoán vị dòng (đổi chỗ các phương trình) để tạo ra ma trận chéo trội trước khi lặp.

### Yêu cầu trình bày (Ghi vào bài thi)
**1. Kiểm tra và biến đổi chéo trội:**
Chỉ ra ma trận $A$ ban đầu KHÔNG chéo trội, sau đó ghi hoán vị các phương trình để được hệ mới $A_{new} x = b_{new}$ thỏa mãn:
$$|A_{ii}^{new}| > \sum_{j 
eq i} |A_{ij}^{new}| \quad \forall i$$

**2. Công thức lặp Gauss-Seidel:**
$$x_i^{(k+1)} = \frac{1}{A_{ii}^{new}} \left( b_i^{new} - \sum_{j=1}^{i-1} A_{ij}^{new} x_j^{(k+1)} - \sum_{j=i+1}^n A_{ij}^{new} x_j^{(k)} \right)$$





# --- FROM NOTEBOOK: scripts\CHƯƠNG 4 GIẢI HỆ ĐẠI SỐ TUYẾN TÍNH & TÌM MA TRẬN NGHỊCH ĐẢO\Lặp Jacobi - Lặp Đơn\Lặp Jacobi (Ax=b).ipynb ---


### Phương pháp Lặp Jacobi (Hệ phương trình Ax=b)





# --- FROM NOTEBOOK: scripts\CHƯƠNG 4 GIẢI HỆ ĐẠI SỐ TUYẾN TÍNH & TÌM MA TRẬN NGHỊCH ĐẢO\Lặp Jacobi - Lặp Đơn\Lặp Jacobi (Đổi dòng tạo chéo trội).ipynb ---


### Lặp Jacobi (Có đổi dòng tự động)





# --- FROM NOTEBOOK: scripts\CHƯƠNG 4 GIẢI HỆ ĐẠI SỐ TUYẾN TÍNH & TÌM MA TRẬN NGHỊCH ĐẢO\Lặp Jacobi - Lặp Đơn\Lặp Đơn (x=Bx+d).ipynb ---


### Lặp Đơn (Hệ x = Bx + d)





# --- FROM NOTEBOOK: scripts\CHƯƠNG 5 GIÁ TRỊ RIÊNG VÀ VECTOR RIÊNG CỦA MA TRẬN\Giá trị kỳ dị SVD (Lớn nhất).ipynb ---


### Giá Trị Kỳ Dị SVD (Lớn Nhất) - Có Xuống Thàng





# --- FROM NOTEBOOK: scripts\CHƯƠNG 5 GIÁ TRỊ RIÊNG VÀ VECTOR RIÊNG CỦA MA TRẬN\Khoảng cách ly nghiệm đa thức.ipynb ---


### Định lý Sturm - Tìm khoảng cách ly nghiệm





# --- FROM NOTEBOOK: scripts\CHƯƠNG 5 GIÁ TRỊ RIÊNG VÀ VECTOR RIÊNG CỦA MA TRẬN\Lý thuyết Nén Ảnh (SVD - PCA).ipynb ---


### Lý thuyết Ứng dụng Trị riêng trong Nén ảnh





# --- FROM NOTEBOOK: scripts\CHƯƠNG 5 GIÁ TRỊ RIÊNG VÀ VECTOR RIÊNG CỦA MA TRẬN\Phương pháp Danielevski.ipynb ---


### Phương pháp Danielevski





# --- FROM NOTEBOOK: scripts\CHƯƠNG 5 GIÁ TRỊ RIÊNG VÀ VECTOR RIÊNG CỦA MA TRẬN\Phương pháp Lũy thừa.ipynb ---


### Phương pháp Lũy thừa (Tìm Trị Riêng)





# --- FROM NOTEBOOK: scripts\CHƯƠNG 5 GIÁ TRỊ RIÊNG VÀ VECTOR RIÊNG CỦA MA TRẬN\Phương pháp Xuống thang.ipynb ---


### Phương pháp Xuống thang





# --- FROM NOTEBOOK: scripts\CHƯƠNG 5 GIÁ TRỊ RIÊNG VÀ VECTOR RIÊNG CỦA MA TRẬN\Số điều kiện Cond(A).ipynb ---


### Số điều kiện Cond(A)


