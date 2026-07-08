# Chương trình Học phần Giải tích số (MI3041) - ĐHBK Hà Nội

Học phần **Giải tích số (Numerical Analysis - MI3041)** cung cấp các phương pháp tính toán số học để giải gần đúng hoặc giải đúng các bài toán toán học trên không gian hữu hạn chiều mà việc tìm nghiệm chính xác bằng giải tích thông thường là cực kỳ khó khăn hoặc bất khả thi.

Dưới đây là cấu trúc chương trình học chi tiết dựa trên đề cương chính thức:

---

## 1. THÔNG TIN CHUNG
*   **Mã học phần:** MI3041
*   **Khối lượng:** 2 (2 – 1 – 0 - 4)
    *   Lý thuyết: 30 tiết
    *   Bài tập / Bài tập lớn: 15 tiết
*   **Học phần học trước:** Giải tích 1 & 2, Đại số, Cơ sở giải tích hàm.
*   **Học phần tiên quyết:** Tin học đại cương IT1110 (để phục vụ kỹ năng lập trình thuật toán).
*   **Phương pháp đánh giá:**
    *   Điểm quá trình (A1): **30%** (Thi viết / Thi vấn đáp / Trắc nghiệm / Bài tập lớn)
    *   Điểm thi cuối kỳ (A2): **70%** (Thi viết / Thi vấn đáp)

---

## 2. NỘI DUNG CHI TIẾT 5 CHƯƠNG HỌC

### CHƯƠNG 1: LÝ THUYẾT SAI SỐ
*   **Mục tiêu:** Hiểu rõ nguồn gốc phát sinh sai số và cách kiểm soát sai số trong quá trình tính toán cơ bản.
*   **Nội dung chính:**
    *   **Phân loại sai số:** Sai số tuyệt đối, sai số tương đối, sai số hệ thống, sai số ngẫu nhiên, sai số phương pháp và sai số làm tròn.
    *   **Quy ước biểu diễn:** Quy ước viết số gần đúng, chữ số có nghĩa và các nguyên tắc làm tròn số.
    *   **Lan truyền sai số:** Công thức tổng quát tính sai số của một hàm số nhiều biến $u = f(x_1, x_2,..., x_n)$ thông qua đạo hàm riêng, đánh giá sai số qua các phép tính cộng, trừ, nhân, chia.

---

### CHƯƠNG 2: GIẢI PHƯƠNG TRÌNH PHI TUYẾN 1 CHIỀU
*   **Mục tiêu:** Tìm nghiệm gần đúng của phương trình phi tuyến dạng $f(x) = 0$ trên một khoảng cách ly nghiệm xác định.
*   **Nội dung chính:**
    *   **Khoảng cách ly nghiệm:** Định nghĩa, điều kiện tồn tại nghiệm và tính duy nhất của nghiệm trên khoảng $[a, b]$.
    *   **Phương pháp Chia đôi (Bisection):** 
        *   *Ý tưởng:* Chia đôi khoảng liên tục $[a, b]$, chọn nửa khoảng chứa nghiệm dựa trên định lý đổi dấu $f(a).f(b) < 0$.
        *   *Đánh giá:* Hội tụ chậm nhưng chắc chắn hội tụ (luôn an toàn).
    *   **Phương pháp Dây cung (Secant):** 
        *   *Ý tưởng:* Thay thế đường cong đồ thị $y = f(x)$ bằng dây cung nối hai điểm để tìm giao điểm kế tiếp với trục hoành.
    *   **Phương pháp Tiếp tuyến (Newton-Raphson):** 
        *   *Ý tưởng:* Dùng tiếp tuyến của đồ thị tại điểm xấp xỉ hiện tại để tìm điểm xấp xỉ tiếp theo.
        *   *Điều kiện hội tụ:* Điểm Fourier. Phương pháp có tốc độ hội tụ bậc 2 (hội tụ cực nhanh khi ở gần nghiệm).
    *   **Phương pháp Lặp đơn (Simple Iteration):**
        *   *Ý tưởng:* Biến đổi phương trình $f(x) = 0$ về dạng tương đương $x = g(x)$.
        *   *Điều kiện hội tụ:* Hàm lặp $g(x)$ phải là một ánh xạ co trên khoảng cách ly nghiệm (tức là đạo hàm $|g'(x)| \le q < 1$).

---

### CHƯƠNG 3: GIẢI HỆ PHƯƠNG TRÌNH PHI TUYẾN NHIỀU CHIỀU
*   **Mục tiêu:** Giải gần đúng hệ phương trình phi tuyến dạng $F(X) = 0$ trong không gian nhiều chiều.
*   **Nội dung chính:**
    *   **Phương pháp Lặp đơn trong không gian nhiều chiều:**
        *   *Cách làm:* Chuyển hệ phương trình về dạng $X = G(X)$.
        *   *Điều kiện hội tụ:* Khảo sát ma trận Jacobi của hàm lặp $G(X)$ và kiểm tra điều kiện chuẩn của ma trận Jacobi này phải nhỏ hơn 1.
    *   **Phương pháp Newton nhiều chiều:**
        *   *Cách làm:* Sử dụng ma trận Jacobi $J(X)$ của hệ phương trình $F(X)$ tại mỗi bước lặp để cập nhật nghiệm theo công thức:
            $$X^{(k+1)} = X^{(k)} - [J(X^{(k)})]^{-1} F(X^{(k)})$$
        *   *Thực tế tính toán:* Thường giải hệ phương trình tuyến tính $J(X^{(k)}) \Delta X^{(k)} = -F(X^{(k)})$ để tìm $\Delta X^{(k)}$, sau đó cập nhật $X^{(k+1)} = X^{(k)} + \Delta X^{(k)}$ thay vì tìm ma trận nghịch đảo trực tiếp để tối ưu tốc độ.

---

### CHƯƠNG 4: GIẢI HỆ ĐẠI SỐ TUYẾN TÍNH & TÌM MA TRẬN NGHỊCH ĐẢO
Đây là chương có khối lượng thuật toán lớn nhất và là trọng tâm thực hành lập trình.

#### 1. Các phương pháp giải hệ phương trình tuyến tính $AX = B$
*   **Nhóm phương pháp giải đúng (Direct Methods - Cho nghiệm chính xác sau số bước hữu hạn):**
    *   *Phương pháp Gauss & Gauss-Jordan:* Khử dần các ẩn số để đưa ma trận về dạng tam giác trên hoặc ma trận đơn vị.
    *   *Phương pháp phân tách LU (LU Decomposition):* Tách ma trận hệ số $A = L.U$ (L: tam giác dưới, U: tam giác trên).
    *   *Phương pháp Cholesky:* Tách ma trận $A = L.L^T$ áp dụng riêng cho ma trận đối xứng và xác định dương (giúp giảm một nửa số lượng phép tính so với LU).
*   **Nhóm phương pháp lặp (Iterative Methods - Tiệm cận nghiệm đúng sau vô hạn bước):**
    *   *Phương pháp Lặp đơn và Lặp Jacobi:* Phân tách ma trận $A = D - L - U$, xây dựng công thức lặp song song cho từng ẩn số.
    *   *Phương pháp Lặp Seidel và Gauss-Seidel:* Cải tiến từ Jacobi, giá trị ẩn số vừa tính được ở bước hiện tại sẽ được dùng ngay lập tức để tính các ẩn tiếp theo trong cùng một vòng lặp, giúp đẩy nhanh tốc độ hội tụ.

#### 2. Các phương pháp tìm ma trận nghịch đảo $A^{-1}$
*   **Tìm nghịch đảo bằng phương pháp giải đúng:** Giải hệ phương trình $AX_i = e_i$ với $e_i$ là các cột của ma trận đơn vị.
*   **Phương pháp Viền quanh (Bordering method):** Tìm nghịch đảo của ma trận kích thước $(n+1) \times (n+1)$ dựa trên ma trận nghịch đảo đã biết của ma trận con kích thước $n \times n$.
*   **Tìm nghịch đảo bằng phương pháp lặp:** Sử dụng các phương pháp Jacobi/Gauss-Seidel.
*   **Phương pháp Newton tìm gần đúng ma trận nghịch đảo:**
    *   Sử dụng công thức lặp phi tuyến bậc cao:
        $$V^{(k+1)} = V^{(k)}(2I - AV^{(k)})$$
    *   Hội tụ về $A^{-1}$ nếu ma trận xấp xỉ ban đầu $V^{(0)}$ được chọn tốt.

---

### CHƯƠNG 5: GIÁ TRỊ RIÊNG VÀ VECTOR RIÊNG CỦA MA TRẬN
*   **Mục tiêu:** Tìm các giá trị riêng $\lambda$ và vector riêng $v$ của ma trận $A$ thỏa mãn phương trình $Av = \lambda v$.
*   **Nội dung chính:**
    *   **Phương pháp Danielevski:**
        *   *Ý tưởng:* Sử dụng các biến đổi tương đương để đưa ma trận $A$ về ma trận dạng chuẩn Frobenius (dạng ma trận có các hệ số của đa thức đặc trưng nằm ngay ở dòng/cột cuối). Từ đó dễ dàng tìm được đa thức đặc trưng để giải nghiệm.
    *   **Phương pháp Lũy thừa (Power Method):**
        *   *Ý tưởng:* Tìm **giá trị riêng trội** (giá trị riêng có trị tuyệt đối lớn nhất $|\lambda_1| > |\lambda_2| \ge ...$) bằng cách nhân ma trận $A$ lặp đi lặp lại với một vector bất kỳ.
    *   **Phương pháp Xuống thang (Deflation method):**
        *   *Ý tưởng:* Sau khi đã tìm được giá trị riêng trội $\lambda_1$ bằng phương pháp lũy thừa, ta biến đổi (xuống thang) ma trận $A$ thành ma trận mới để triệt tiêu $\lambda_1$, từ đó tiếp tục dùng phương pháp lũy thừa tìm giá trị riêng lớn thứ hai $\lambda_2$.
    *   **Khai triển kỳ dị (SVD - Singular Value Decomposition):**
        *   *Ý tưởng:* Phân tích ma trận bất kỳ $A$ thành tích của 3 ma trận $A = U \Sigma V^T$ (trong đó $U, V$ là ma trận trực giao, $\Sigma$ là ma trận đường chéo chứa các trị kỳ dị).
        *   *Ứng dụng:* Dùng trong xấp xỉ ma trận, giảm chiều dữ liệu.
