# TỔNG HỢP CÁC THUẬT TOÁN GIẢI TÍCH SỐ CHI TIẾT
*(Trích xuất từ file `Giai_tich_so.ipynb`)*

Tài liệu này hướng dẫn chi tiết từng bước thực hiện, điều kiện áp dụng và cách tính toán sai số cho các phương pháp giải tích số.

## 📖 Mục lục
- [CHƯƠNG 2: GIẢI PHƯƠNG TRÌNH PHI TUYẾN 1 CHIỀU](#chương-2-giải-phương-trình-phi-tuyến-1-chiều)
- [CHƯƠNG 3: GIẢI HỆ PHƯƠNG TRÌNH PHI TUYẾN NHIỀU CHIỀU](#chương-3-giải-hệ-phương-trình-phi-tuyến-nhiều-chiều)
- [CHƯƠNG 4: GIẢI HỆ ĐẠI SỐ TUYẾN TÍNH & MA TRẬN NGHỊCH ĐẢO](#chương-4-giải-hệ-đại-số-tuyến-tính--ma-trận-nghịch-đảo)
- [CHƯƠNG 5: GIÁ TRỊ RIÊNG VÀ VECTOR RIÊNG](#chương-5-giá-trị-riêng-và-vector-riêng)

---

## CHƯƠNG 2: GIẢI PHƯƠNG TRÌNH PHI TUYẾN 1 CHIỀU
**Mục tiêu:** Tìm nghiệm $x$ sao cho $f(x) = 0$.

**Chiến lược chọn phương pháp:**
- **Chia đôi:** Luôn hội tụ nhưng số bước lặp nhiều. Dùng khi chỉ biết khoảng phân ly nghiệm $[a,b]$ mà không tính được đạo hàm.
- **Dây cung & Tiếp tuyến (Newton):** Hội tụ nhanh hơn nhưng đòi hỏi điều kiện khắt khe (hàm số phải có đạo hàm bậc 1, bậc 2 và không đổi dấu trên $[a,b]$).
- **Lặp đơn:** Dùng khi phương trình có thể dễ dàng biến đổi về dạng $x = g(x)$ và chứng minh được hệ số co $q < 1$.

### 1. Phân ly nghiệm đa thức (Định lý Sturm)
**Mục đích:** Tìm các khoảng cách ly nghiệm thực của đa thức $P(x) = 0$.
**Các bước thực hiện:**
* **Bước 1:** Lập dãy Sturm $f_0(x), f_1(x), f_2(x), \dots$:
  - $f_0(x) = P(x)$
  - $f_1(x) = P'(x)$
  - $f_2(x) = -( \text{phần dư của phép chia } f_0 \text{ cho } f_1 )$
  - $f_k(x) = -( \text{phần dư của phép chia } f_{k-2} \text{ cho } f_{k-1} )$
* **Bước 2:** Lập bảng xét dấu dãy Sturm tại các điểm đầu mút khoảng (thường là $-\infty$, $+\infty$ hoặc các giá trị nguyên).
* **Bước 3:** Số lần đổi dấu của dãy Sturm tại $x=a$ trừ đi số lần đổi dấu tại $x=b$ ($V(a) - V(b)$) chính là số nghiệm thực trong khoảng $[a, b]$.

### 2. Phương pháp Chia đôi
**Điều kiện áp dụng:** Hàm $f(x)$ liên tục trên $[a, b]$ và $f(a) \cdot f(b) < 0$.
**Các bước thực hiện:**
* **Bước 1 (Kiểm tra điều kiện):** Tính $f(a)$ và $f(b)$. Xác nhận $f(a) \cdot f(b) < 0$.
* **Bước 2 (Tính sai số tiên nghiệm):** Nếu đề bài yêu cầu tìm số lần lặp để đạt sai số $\epsilon$, ta giải bất phương trình: $\frac{b-a}{2^n} < \epsilon \implies n \ge \lceil \log_2(\frac{b-a}{\epsilon}) \rceil - 1$.
* **Bước 3 (Quá trình lặp):** Tại mỗi bước lặp $k$:
  1. Tính trung điểm $c = \frac{a+b}{2}$.
  2. Tính giá trị $f(c)$.
  3. Tính sai số hiện tại $\Delta = \frac{b-a}{2}$. (Lưu ý: qua mỗi bước, khoảng $[a, b]$ bị thu hẹp một nửa).
  4. Thu hẹp khoảng cách ly nghiệm mới:
     - Nếu $f(a) \cdot f(c) < 0$: Nghiệm nằm trong nửa trái $[a, c]$, gán $b = c$.
     - Nếu $f(c) \cdot f(b) < 0$: Nghiệm nằm trong nửa phải $[c, b]$, gán $a = c$.
* **Bước 4 (Kết luận):** Dừng lặp khi $\Delta < \epsilon$ hoặc $f(c) = 0$. Nghiệm xấp xỉ là $c$.

### 3. Phương pháp Dây cung
**Điều kiện áp dụng:** $f(a) \cdot f(b) < 0$ và đạo hàm $f'(x), f''(x)$ không đổi dấu trên khoảng $[a, b]$.
**Các bước thực hiện:**
* **Bước 1 (Chuẩn bị):**
  - Tìm đạo hàm $f'(x)$ và $f''(x)$.
  - Tìm $m_1 = \min_{[a,b]}|f'(x)|$ và $M_1 = \max_{[a,b]}|f'(x)|$.
  - Chọn **điểm cố định** $d \in \{a, b\}$ sao cho điều kiện Fourier thỏa mãn: $f(d) \cdot f''(d) > 0$.
  - Chọn xấp xỉ ban đầu $x_0$ là đầu mút còn lại: $x_0 \in \{a, b\} \setminus \{d\}$.
* **Bước 2 (Lập bảng tính):** Tính nghiệm xấp xỉ mới theo công thức: 
  $x_{k+1} = x_k - f(x_k) \frac{x_k - d}{f(x_k) - f(d)}$
* **Bước 3 (Kết luận):** Dừng lặp khi sai số hậu nghiệm thỏa mãn: $\Delta = \frac{M_1 - m_1}{m_1} |x_k - x_{k-1}| < \epsilon$. Trả về $x_{k+1}$.

### 4. Phương pháp Tiếp tuyến (Newton-Raphson)
**Điều kiện áp dụng:** Giống PP Dây cung (các đạo hàm không đổi dấu).
**Các bước thực hiện:**
* **Bước 1 (Chuẩn bị):**
  - Tìm $m_1 = \min_{[a,b]}|f'(x)|$ và $M_2 = \max_{[a,b]}|f''(x)|$.
  - Chọn điểm khởi tạo $x_0 \in \{a, b\}$ thỏa mãn điều kiện Fourier: $f(x_0) \cdot f''(x_0) > 0$.
* **Bước 2 (Lập bảng tính):** Tính nghiệm xấp xỉ tiếp theo bằng công thức:
  $x_{k+1} = x_k - \frac{f(x_k)}{f'(x_k)}$
* **Bước 3 (Kết luận):** Dừng lặp khi sai số hậu nghiệm thỏa mãn: $\Delta = \frac{M_2}{2m_1} |x_k - x_{k-1}|^2 < \epsilon$. Trả về $x_{k+1}$.

### 5. Phương pháp Lặp đơn (1 chiều)
**Điều kiện áp dụng:** Biến đổi $f(x)=0$ thành $x = g(x)$ sao cho hệ số co $q = \max_{[a,b]}|g'(x)| < 1$.
**Các bước thực hiện:**
* **Bước 1 (Kiểm tra hệ số co):** Tính đạo hàm $g'(x)$. Tìm $q = \max|g'(x)|$. Khẳng định $q < 1$ để đảm bảo sự hội tụ.
* **Bước 2 (Bảng tính):** Chọn $x_0 \in [a, b]$. Lặp tính giá trị mới:
  $x_{k+1} = g(x_k)$
* **Bước 3 (Kết luận):** Tính sai số hậu nghiệm $\Delta = \frac{q}{1-q} |x_{k+1} - x_k|$. Dừng khi $\Delta < \epsilon$. Trả về $x_{k+1}$.

---

## CHƯƠNG 3: GIẢI HỆ PHƯƠNG TRÌNH PHI TUYẾN NHIỀU CHIỀU
**Mục tiêu:** Giải hệ $F(X) = 0$, với $X = (x_1, x_2, \dots, x_n)^T$.

### 6. Phương pháp Lặp đơn nhiều chiều
**Các bước thực hiện:**
* **Bước 1 (Khởi tạo):** Biến đổi hệ $F(X) = 0$ thành hệ $X = G(X)$.
  - Tìm ma trận đạo hàm (Jacobian) của $G(X)$. Đánh giá chuẩn ma trận (thường dùng chuẩn hàng lớn nhất) để tìm hệ số co $q = \|J_G\|_\infty < 1$.
  - Chọn vector khởi tạo $X^{(0)}$.
* **Bước 2 (Bảng tính):** Tính vector xấp xỉ mới ở bước $k+1$ bằng cách thế trực tiếp $X^{(k)}$ vào hàm $G$:
  $X^{(k+1)} = G(X^{(k)})$
* **Bước 3 (Kết luận):** Tính sai số hậu nghiệm theo chuẩn vô cùng (max): $\Delta = \frac{q}{1-q} \|X^{(k+1)} - X^{(k)}\|_\infty$. Dừng lặp khi $\Delta < \epsilon$.

### 7. Phương pháp Newton nhiều chiều
**Các bước thực hiện:**
* **Bước 1 (Chuẩn bị):** Tính ma trận Jacobian $J(X)$ của hệ hàm $F(X)$. Chọn vector xấp xỉ ban đầu $X^{(0)}$.
* **Bước 2 (Các bước lặp):** Tại mỗi bước $k$, thay vì tính ma trận nghịch đảo, ta giải hệ phương trình tuyến tính đối với vector số gia $\Delta X$: 
  $J(X^{(k)}) \cdot \Delta X = -F(X^{(k)})$
  Sau khi giải được hệ tuyến tính, tính vector xấp xỉ mới:
  $X^{(k+1)} = X^{(k)} + \Delta X$
* **Bước 3 (Kết luận):** Sai số ở mỗi bước được tính bằng chuẩn vô cùng của vector gia số: $\Delta = \|\Delta X\|_\infty$. Dừng lặp khi $\Delta < \epsilon$.

---

## CHƯƠNG 4: GIẢI HỆ ĐẠI SỐ TUYẾN TÍNH & MA TRẬN NGHỊCH ĐẢO
**Mục tiêu:** Giải hệ tuyến tính $AX = b$ hoặc tìm ma trận nghịch đảo $A^{-1}$.

### 8. Phân tách LU (Cơ bản)
**Mục đích:** Tách $A = LU$ để biến đổi hệ $AX = b$ thành 2 hệ tam giác dễ giải là $LY = b$ và $UX = Y$.
**Các bước thực hiện:**
* **Bước 1:** Khởi tạo ma trận $L$ là ma trận đơn vị $I$, ma trận $B$ copy toàn bộ từ $A$.
* **Bước 2 (Khử Gauss):** Duyệt từng cột $k$ (từ 1 đến $n-1$):
  - Hệ số nhân (lưu vào $L$): $L_{ik} = \frac{B_{ik}}{B_{kk}}$ (với $i > k$).
  - Khử các hàng dưới (cập nhật $B$): $B_{ij} = B_{ij} - L_{ik} \cdot B_{kj}$.
* **Bước 3:** Ma trận $U$ chính là nửa trên của $B$ sau khi khử xong.
* **Bước 4 (Giải hệ):** Giải $LY = b$ (dùng phép thế tiến), sau đó giải $UX = Y$ (dùng phép thế lùi).

### 9. Phân tách LU (Có Pivoting)
**Mục đích:** Tránh sai số làm tròn hoặc lỗi chia cho 0 khi phần tử chéo $B_{kk}$ quá nhỏ hoặc bằng 0.
**Các bước thực hiện:**
* **Bước 1:** Khởi tạo ma trận hoán vị $P = I$.
* **Bước 2 (Tìm Pivot và Hoán vị):** Ở mỗi bước khử cột $k$:
  - Tìm phần tử có trị tuyệt đối lớn nhất (gọi là pivot) từ hàng $k$ trở xuống.
  - Hoán vị hàng $k$ với hàng chứa pivot trong ma trận $B$ và tương tự trong ma trận $P$.
* **Bước 3 (Khử):** Tiến hành khử Gauss như bình thường trên ma trận đã được hoán vị.
* **Bước 4:** Trích xuất $L$, $U$, $P$. Giải hệ $AX = b$ bằng cách giải 2 hệ $LY = P \cdot b$ và $UX = Y$.

### 10. Phân tách Cholesky
**Điều kiện:** Ma trận $A$ phải đối xứng ($A = A^T$) và xác định dương. Ta phân tách $A = LL^T$.
**Các bước thực hiện:**
* **Bước 1 (Tính ma trận L):** Duyệt từng cột từ trái sang phải, tính từng phần tử:
  - Đường chéo: $L_{ii} = \sqrt{A_{ii} - \sum_{k=1}^{i-1} L_{ik}^2}$
  - Dưới đường chéo ($j > i$): $L_{ji} = \frac{A_{ji} - \sum_{k=1}^{i-1} L_{jk} L_{ik}}{L_{ii}}$
* **Bước 2 (Giải hệ):** Giải lần lượt $LY = b$ và $L^T X = Y$.

### 11. Phương pháp Lặp đơn (Hệ phương trình)
**Mục đích:** Giải hệ biến đổi dạng $X = BX + d$.
**Các bước thực hiện:**
* **Bước 1 (Kiểm tra hội tụ):** Tính chuẩn $q = \|B\|$ (thường dùng chuẩn hàng vô cùng). Đảm bảo $q < 1$.
* **Bước 2 (Bảng lặp):** Chọn $X^{(0)}$ (thường lấy $X^{(0)} = d$). Áp dụng công thức lặp vector:
  $X^{(k+1)} = B \cdot X^{(k)} + d$
* **Bước 3 (Kết luận):** Dừng lặp khi sai số hậu nghiệm $\Delta = \frac{q}{1-q} \|X^{(k+1)} - X^{(k)}\| < \epsilon$ (với $q<1$).

### 12. Phương pháp Lặp Jacobi
**Mục đích:** Giải hệ $AX = b$ bằng cách tính vòng lặp mà nghiệm mới ở bước $k+1$ chỉ phụ thuộc hoàn toàn vào nghiệm cũ ở bước $k$.
**Các bước thực hiện:**
* **Bước 1 (Kiểm tra hội tụ):** Đảm bảo tính chéo trội hàng của ma trận $A$: $|a_{ii}| > \sum_{j \neq i} |a_{ij}|$.
* **Bước 2 (Lặp):** Tại bước $k+1$, tính thành phần thứ $i$:
  $x_i^{(k+1)} = \frac{1}{a_{ii}} \left( b_i - \sum_{j \neq i} a_{ij} x_j^{(k)} \right)$
* **Bước 3 (Kết luận):** Dừng khi sai số $\max|x_i^{(k+1)} - x_i^{(k)}| < \epsilon$.

### 13. Phương pháp Lặp Gauss-Seidel
**Mục đích:** Giải hệ $AX = b$. Tối ưu hơn lặp Jacobi vì cập nhật cuốn chiếu (dùng ngay giá trị mới tính được thay vì đợi hết vòng lặp).
**Các bước thực hiện:**
* **Bước 1 (Kiểm tra hội tụ):** Đảm bảo tính chéo trội hàng của ma trận $A$.
* **Bước 2 (Lặp):** Tại bước $k+1$, tính thành phần thứ $i$ dựa vào các thành phần $1 \dots i-1$ (vừa mới tính ở bước $k+1$) và các thành phần $i+1 \dots n$ (đã tính ở bước $k$):
  $x_i^{(k+1)} = \frac{1}{a_{ii}} \left( b_i - \sum_{j=1}^{i-1} a_{ij} x_j^{(k+1)} - \sum_{j=i+1}^n a_{ij} x_j^{(k)} \right)$
* **Bước 3 (Kết luận):** Dừng khi sai số lớn nhất giữa 2 bước lặp $\max|x_i^{(k+1)} - x_i^{(k)}| < \epsilon$.

**Lưu ý (Đổi dòng tạo chéo trội):** Nếu ma trận $A$ ban đầu không chéo trội, ta phải tiến hành hoán vị các phương trình (đổi dòng) để ma trận thỏa mãn điều kiện $|A_{ii}| > \sum_{j \neq i} |A_{ij}| \quad \forall i$ trước khi áp dụng Jacobi hoặc Gauss-Seidel.

### 14. & 15. Tìm ma trận nghịch đảo $A^{-1}$
**Chiến lược chung:** Tìm ma trận nghịch đảo tương đương với việc giải $n$ hệ phương trình tuyến tính $A \cdot x_j = e_j$, với $e_j$ là cột thứ $j$ của ma trận đơn vị.
* **Dùng Cholesky:** Phân tách $A = LL^T$ một lần duy nhất. Giải 2 hệ tam giác $Ly = e_j$ và $L^T x_j = y$ lặp lại cho từng cột $j$.
* **Dùng Gauss-Seidel/Jacobi:** Chạy vòng lặp cho từng vế phải $e_j$ cho đến khi hội tụ ra nghiệm $x_j$. Hợp nhất các vector $x_j$ thành ma trận $A^{-1}$.

### 16. Ma trận nghịch đảo bằng phương pháp Viền quanh (Bordering)
**Mục đích:** Tính nghịch đảo ma trận cấp $n$ bằng cách viền quanh dần từ ma trận con cấp 1 đến $n$.
**Các bước thực hiện:**
* **Bước 1 (Khởi tạo):** Lấy ma trận con $A_1 = [a_{11}]$. Nghịch đảo của nó là $A_1^{-1} = [1/a_{11}]$. Nếu $a_{11} = 0$, thuật toán dừng (phương pháp cơ bản thất bại).
* **Bước 2 (Lặp viền quanh):** Lặp $k$ từ $2$ đến $n$. Tại bước $k$, ta viền quanh ma trận nghịch đảo $A_{k-1}^{-1}$ bằng cột $u_k$ và hàng $v_k^T$ từ ma trận gốc $A$.
  - Tính vector $x_k = A_{k-1}^{-1} u_k$ và vector $y_k^T = v_k^T A_{k-1}^{-1}$.
  - Tính hệ số $\alpha_k = a_{kk} - v_k^T x_k$. Nếu $\alpha_k = 0$, $A_k$ suy biến, thuật toán dừng.
  - Tính các khối của ma trận $A_k^{-1}$:
    + $s_k = \frac{1}{\alpha_k}$
    + $q_k = -s_k x_k$
    + $r_k^T = -s_k y_k^T$
    + $P_k = A_{k-1}^{-1} + s_k x_k y_k^T$
  - Ráp thành ma trận khối: $A_k^{-1} = \begin{bmatrix} P_k & q_k \\ r_k^T & s_k \end{bmatrix}$.
* **Bước 3 (Kết luận):** Trả về $A_n^{-1}$ ở bước lặp cuối cùng.

---

## CHƯƠNG 5: GIÁ TRỊ RIÊNG VÀ VECTOR RIÊNG

### 17. Phương pháp Danielevski (Tìm đa thức đặc trưng)
**Mục đích:** Đưa ma trận $A$ về dạng Frobenius để đọc trực tiếp hệ số của đa thức đặc trưng.
**Các bước thực hiện:**
* **Bước 1:** Khởi tạo ma trận biến đổi $P = A$.
* **Bước 2 (Khử ngược):** Duyệt lùi cột $k$ từ $n-1$ về $1$. Xây dựng ma trận $M_k$:
  - Hàng $k-1$ của $M_k$ chính là hàng $k$ của $P$. Các hàng khác giữ nguyên (như ma trận đơn vị $I$).
  - Tính ma trận nghịch đảo $M_k^{-1}$.
  - Cập nhật ma trận mới $P_{mới} = M_k \cdot P_{cũ} \cdot M_k^{-1}$.
* **Bước 3 (Kết luận):** Hàng đầu tiên của ma trận Frobenius cuối cùng chính là hệ số của đa thức đặc trưng:
  $P(\lambda) = (-1)^n \left(\lambda^n - p_{0,0}\lambda^{n-1} - \dots - p_{0,n-1}\right)$

### 18. Phương pháp Xuống thang
**Mục đích:** Tìm giá trị riêng trội (lớn nhất) thứ 2 sau khi đã biết giá trị riêng lớn nhất $\lambda_1$ và vector riêng $v_1$.
**Các bước thực hiện:**
* **Bước 1 (Lập vector phụ):** Tính vector $x = \frac{v_1}{\|v_1\|^2}$.
* **Bước 2 (Lập ma trận xuống thang):** "Khử" thành phần $\lambda_1$ ra khỏi $A$ để tạo ma trận $B$:
  $B = A - \lambda_1 v_1 x^T$
* **Bước 3 (Tìm trị riêng thứ 2):** Sử dụng phương pháp lũy thừa (Power Method) trên ma trận $B$ để tìm $\lambda_2$ (là trị riêng trội của $B$) và vector riêng $u_2$.
* **Bước 4 (Khôi phục vector riêng):** Vector riêng thực sự của $A$ tương ứng với $\lambda_2$ là:
  $v_2 = (\lambda_2 - \lambda_1) u_2 + \lambda_1 (x^T u_2) v_1$

### 19. Phân tích giá trị kỳ dị (SVD) và Phương pháp lũy thừa
**Mục đích:** Phân tích ma trận $A = U \Sigma V^T$ hoặc tìm giá trị kỳ dị lớn nhất $\sigma_1$. 
**Các bước tìm $\sigma_1$ bằng PP Lũy thừa:**
* **Bước 1 (Chuẩn bị):** Giá trị kỳ dị lớn nhất $\sigma_1 = \sqrt{\lambda_{\max}(A^T A)}$. Ta đặt $B = A^T A$. Chọn ngẫu nhiên vector $v_0$ rồi chuẩn hóa về chuẩn 2 ($\|v_0\|_2 = 1$).
* **Bước 2 (Lặp tìm trị riêng trội của B):** Tại bước $k$:
  - Nhân ma trận: $Y = B \cdot v_k$.
  - Tính xấp xỉ trị riêng (hệ số Rayleigh): $\lambda = v_k^T \cdot Y$.
  - Chuẩn hóa vector cho vòng tiếp theo: $v_{k+1} = \frac{Y}{\|Y\|_2}$.
* **Bước 3 (Kết luận):** Dừng lặp khi $\|v_{k+1} - v_k\| < \epsilon$. Ta có $\sigma_1 = \sqrt{\lambda}$.
  - Vector kỳ dị phải (cột của V): $v = v_{k+1}$
  - Vector kỳ dị trái (cột của U): $u = \frac{1}{\sigma_1} A \cdot v_{k+1}$.

**Ứng dụng SVD (Phân tích thành phần chính - PCA / Nén ảnh):** 
SVD cho phép biểu diễn ma trận $A$ dưới dạng tổng các ma trận hạng 1: $A = \sum_{i=1}^r \sigma_i u_i v_i^T$. Trong nén ảnh, ta chỉ giữ lại $k$ giá trị kỳ dị lớn nhất đầu tiên ($k \ll r$) để tái tạo ảnh xấp xỉ $A_k = \sum_{i=1}^k \sigma_i u_i v_i^T$ giúp tiết kiệm đáng kể không gian lưu trữ mà vẫn giữ được đặc trưng chính của ảnh ban đầu.

### 20. Tính số điều kiện Cond(A)
**Mục đích:** Đánh giá độ ổn định của ma trận trong giải hệ phương trình tuyến tính. Số $Cond(A)$ càng lớn thì hệ càng dễ bị nhiễu do sai số làm tròn.
**Các bước thực hiện:**
* **Bước 1:** Dùng SVD để tìm toàn bộ phổ giá trị kỳ dị của $A$.
* **Bước 2:** Lấy giá trị kỳ dị cực đại $\sigma_{\max}$ và cực tiểu $\sigma_{\min}$.
* **Bước 3:** Tính số điều kiện: $Cond(A) = \frac{\sigma_{\max}}{\sigma_{\min}} = \|A\|_2 \|A^{-1}\|_2$. 
  - Nếu $\sigma_{\min} \approx 0$, hệ rất kém ổn định hoặc suy biến ($Cond(A) \to \infty$).
