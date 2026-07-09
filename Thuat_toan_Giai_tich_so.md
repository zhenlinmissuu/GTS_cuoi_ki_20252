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

**Input:**
- Ma trận vuông $A \in Mat(n, n)$

**Output:**
- Ma trận A được phân rã chứa cả L và U

**Thuật toán:**

**B1. Khởi tạo:**
- Tạo ma trận $B \leftarrow A$ (sao chép để cập nhật).

**B2. Lặp:**
- Với mỗi cột $k \leftarrow 0$ đến $n-2$:
  - Nếu $B[k,k] = 0$, báo lỗi "Ma trận suy biến, không thể phân rã LU."
  - Với mỗi hàng $i \leftarrow k+1$ đến $n-1$:
    - Tính hệ số $L[i,k]$: $B[i,k] \leftarrow B[i,k] / B[k,k]$
    - Cập nhật phần còn lại của hàng $i$:
      với mỗi $j \leftarrow k+1$ đến $n-1$: $B[i,j] \leftarrow B[i,j] - B[i,k] \times B[k,j]$.

**B3. Tách L và U:**
- Khởi tạo $L = I_n, U = 0_{n \times n}$.
- Với mỗi chỉ số $i, j = 0, \ldots, n-1$:
  $L_{i,j} = \begin{cases} 1, & i = j, \\ B_{i,j}, & i > j, \\ 0, & i < j, \end{cases} \quad U_{i,j} = \begin{cases} B_{i,j}, & i \le j, \\ 0, & i > j. \end{cases}$

**B4. Trả về: Ma trận L, ma trận U.**

### 9. Phân tách LU (Có Pivoting)

**Input:**
- Ma trận vuông $A \in \mathbb{R}^{n \times n}$.
- Vector vế phải $B \in \mathbb{R}^{n \times 1}$.

**Output:**
- Ma trận tam giác dưới L với đường chéo chính bằng 1.
- Ma trận tam giác trên U.
- Ma trận hoán vị P.
- Vector hoán vị $perm$.
- Vector nghiệm $X \in \mathbb{R}^{n \times 1}$ của hệ $AX = B$.

**Thuật toán:**

**B1. Khởi tạo:**
- Tạo ma trận P là ma trận đơn vị cấp n.
- Tạo bản sao của ma trận A.
- Tạo vector $perm = [0, 1, 2, \ldots, n-1]$.

**B2. Phân tích LU có pivoting:**
- Với mỗi cột $k \leftarrow 0$ đến $n-2$:
  - Tìm chỉ số $p \leftarrow \arg\max_{k \le i \le n-1} |A[i, k]|$. $\triangleright$ Chọn pivot lớn nhất trong cột k
  - Nếu $A[p, k] = 0$, báo lỗi: "Ma trận suy biến, không thể phân rã LU."
  - Nếu $p \neq k$, hoán đổi:
    - Hoán đổi hàng k và p trong A.
    - Hoán đổi hàng k và p trong P.
    - Hoán đổi $perm[k]$ và $perm[p]$.
  - Với mỗi hàng $i \leftarrow k+1$ đến $n-1$:
    - Nếu $A[i, k] \neq 0$:
      - Tính hệ số $A[i, k]$: $A[i, k] \leftarrow A[i, k] / A[k, k]$. (Phần tử $L[i,k]$)
      - Cập nhật các phần tử còn lại: $A[i, k+1:n] \leftarrow A[i, k+1:n] - A[i, k] \cdot A[k, k+1:n]$.

**B3. Tách L và U:**
- Tạo ma trận L với đường chéo chính bằng 1 và phần dưới đường chéo lấy từ A.
- Tạo ma trận U với phần trên đường chéo và đường chéo chính lấy từ A.

**B4. Giải hệ phương trình $AX = B$:**
- Hoán vị vector B theo $perm$: $B' \leftarrow B[perm]$.
- Giải hệ tam giác dưới $LY = B'$:
  - Với mỗi $i \leftarrow 0$ đến $n-1$: $Y[i] \leftarrow B'[i] - \sum_{k=0}^{i-1} L[i,k] \cdot Y[k]$.
- Giải hệ tam giác trên $UX = Y$:
  - Với mỗi $i \leftarrow n-1$ xuống $0$: $X[i] \leftarrow (Y[i] - \sum_{k=i+1}^{n-1} U[i,k] \cdot X[k]) / U[i,i]$.

**B5. Trả về: L, U, P, perm, X.**

### 10. Phân tách Cholesky

**Input:**
- Ma trận vuông $A \in Mat(n, n)$

**Output:**
- Ma trận tam giác dưới L sao cho $A = L L^T$

**Thuật toán:**

**B1. Khởi tạo:**
- Tạo ma trận sao chép $L \leftarrow A$

**B2. Tính các phần tử của L:**
- Với $i \leftarrow 0$ đến $n-1$:
  - Gán: $temp \leftarrow L[i,i] - \sum_{k=0}^{i-1} L[i,k]^2$
  - Nếu $temp < 0$ thì báo lỗi "Ma trận không dương xác định".
  - Tính phần tử đường chéo: $L[i,i] = \sqrt{temp}$
  - Tính các phần tử dưới đường chéo:
    với mỗi $j \leftarrow i+1$ đến $n-1$: $L[j,i] \leftarrow \frac{1}{L[i,i]} \left( L[j,i] - \sum_{k=0}^{i-1} L[j,k] L[i,k] \right)$
- Xóa các phần tử trên: với mỗi $j \leftarrow i+1$ đến $n-1$: $L[i,j] \leftarrow 0$

**B3. Trả về: Ma trận L.**

### 11. Phương pháp Lặp đơn (Hệ phương trình)

**Input:**
- Ma trận $B \in Mat(n, n)$, vector tự do $d_n$.
- Sai số $\varepsilon > 0$ cho trước.
- Số lần lặp tối đa N.

**Output:** Nghiệm $X = (x_1, x_2, \ldots, x_n)^T$ với số lần lặp k với sai số không quá $\varepsilon$ hoặc thông báo thất bại.

**Thuật toán:**
B1: Gán $q = \|B\|_{(p)} \quad (p = \infty, 1, 2)$

**B2. Kiểm tra điều kiện hội tụ: $q < 1$, nếu không thỏa mãn thì thông báo "Điều kiện hội tụ không thỏa mãn, phương pháp có thể không hội tụ" và dừng chương trình.**

**B3. Khởi tạo: $k = 0$, $X^{(0)} = 0_n$**

**B4. Trong khi $k < N$, lặp:**
- Tính dựa trên công thức lặp: $X^{(k+1)} = B X^{(k)} + d$
- Kiểm tra điều kiện dừng: $\frac{q}{1-q} \| X^{(k+1)} - X^{(k)} \| < \varepsilon$. Nếu thỏa mãn thì trả về nghiệm gần đúng $X = X^{(k+1)}$ với số lần lặp $k+1$ và dừng chương trình.
- Cập nhật cho vòng lặp sau: $k = k+1, X^{(k)} = X^{(k+1)}$.

**B5. Thông báo "Thất bại: Không tìm được nghiệm sau N lần lặp với sai số cho trước." và dừng chương trình.**

### 12. Phương pháp Lặp Jacobi
**Mục đích:** Giải hệ $AX = b$ bằng cách tính vòng lặp mà nghiệm mới ở bước $k+1$ chỉ phụ thuộc hoàn toàn vào nghiệm cũ ở bước $k$.
**Các bước thực hiện:**
* **Bước 1 (Kiểm tra hội tụ):** Đảm bảo tính chéo trội hàng của ma trận $A$: $|a_{ii}| > \sum_{j \neq i} |a_{ij}|$.
* **Bước 2 (Lặp):** Tại bước $k+1$, tính thành phần thứ $i$:
  $x_i^{(k+1)} = \frac{1}{a_{ii}} \left( b_i - \sum_{j \neq i} a_{ij} x_j^{(k)} \right)$
* **Bước 3 (Kết luận):** Dừng khi sai số $\max|x_i^{(k+1)} - x_i^{(k)}| < \epsilon$.

### 13. Phương pháp Lặp Gauss-Seidel

**Input:**
- Ma trận $A_{n \times n}$, ma trận $B_{n \times m}$.
- Sai số $\varepsilon$ cho trước.

**Output:**
- Nghiệm X của hệ $AX = b$ với sai số không quá $\varepsilon$

**Thuật toán:**

**B1. Xác định ma trận A chéo trội:**
- Với $\sum_{j \neq i} |a_{ij}| < |a_{ii}| \forall i$: A chéo trội hàng. Gán $s = 0, \quad q = \max_{i=\overline{1,n}} \frac{\sum_{j<i} |a_{ij}|}{|a_{ii}| - \sum_{j>i} |a_{ij}|}$
- Với $\sum_{i \neq j} |a_{ij}| < |a_{jj}| \forall j$: A chéo trội cột. Gán $s = \max_{j=\overline{1,n}} \frac{1}{|a_{jj}|} \sum_{i>j} |a_{ij}|, \quad q = \max_{j=\overline{1,n}} \frac{\sum_{i<j} |a_{ij}|}{|a_{jj}| - \sum_{i>j} |a_{ij}|}$
- Nếu không thỏa mãn, cảnh báo phương pháp có thể không hội tụ.

**B2. Khởi tạo: $k = 0$, $X^{(0)} = 0_n$**

**B3. Lặp:**
- Với mỗi cột $1, 2, \ldots, m$ của ma trận B, tính dựa trên công thức lặp:
  $x_{i,t}^{(k+1)} = \frac{1}{a_{ii}} \left( b_{i,t} - \sum_{j=1}^{i-1} a_{ij} x_{j,t}^{(k+1)} - \sum_{j=i+1}^n a_{ij} x_{j,t}^{(k)} \right), \quad i = \overline{1, n}$
- Kiểm tra điều kiện dừng:
  $\frac{q}{(1-s)(1-q)} \| X_k - X_{k-1} \| < \varepsilon.$
  Nếu thỏa mãn thì dừng lặp.
- Ngược lại, gán $k = k+1$ và tiếp tục vòng lặp

**B4. Trả về kết quả nghiệm gần đúng $X^{(k+1)}$ cùng sai số không quá $\varepsilon$.**

**Lưu ý (Đổi dòng tạo chéo trội):** Nếu ma trận $A$ ban đầu không chéo trội, ta phải tiến hành hoán vị các phương trình (đổi dòng) để ma trận thỏa mãn điều kiện $|A_{ii}| > \sum_{j \neq i} |A_{ij}| \quad \forall i$ trước khi áp dụng Jacobi hoặc Gauss-Seidel.

### 14. & 15. Tìm ma trận nghịch đảo $A^{-1}$
#### Tìm ma trận nghịch đảo bằng phương pháp phân tích Choleski

**Input:**
- Ma trận vuông $A \in Mat(n, n)$.

**Output:**
- Ma trận nghịch đảo $A^{-1}$ (nếu A thỏa mãn điều kiện).

**Thuật toán:**

**B1. Kiểm tra ma trận A:**
- Kiểm tra xem A có đối xứng không (tức là $A = A^T$).
- Nếu A không đối xứng, báo lỗi: "Ma trận A không đối xứng. Không thể áp dụng trực tiếp phương pháp Cholesky." và dừng thuật toán.

**B2. Phân tách Cholesky $A = L L^T$:**
- Khởi tạo ma trận L kích thước $n \times n$ với tất cả các phần tử bằng 0.
- Với $i \leftarrow 0$ đến $n-1$:
  - Gán: $temp \leftarrow A[i,i] - \sum_{k=0}^{i-1} L[i,k]^2$
  - Nếu $temp < 0$ thì báo lỗi "Ma trận A không dương xác định. Không thể phân tách Cholesky". và dừng thuật toán.
  - Tính đường chéo: $L[i,i] \leftarrow \sqrt{temp}$
  - Tính các phần tử dưới đường chéo:
    với mỗi $j \leftarrow i+1$ đến $n-1$: $L[j,i] \leftarrow \frac{1}{L[i,i]} \left( A[j,i] - \sum_{k=0}^{i-1} L[j,k] L[i,k] \right)$

**B3. Tính các cột của ma trận nghịch đảo $A_{inv}$**
- Khởi tạo ma trận $A_{inv} \in Mat(n,n)$.
- Khởi tạo vector cột tạm thời $y_{col}$ kích thước $n \times 1$.
- Với $j \leftarrow 0$ đến $n-1$:
  - Với $i \leftarrow 0$ đến $n-1$:
    $y_{col}[i] \leftarrow \frac{1}{L[i,i]} \left( \delta_{ij} - \sum_{k=0}^{i-1} L[i,k] y_{col}[k] \right)$
  - Với $i \leftarrow n-1$ xuống $0$:
    $A_{inv}[i,j] \leftarrow \frac{1}{L[i,i]} \left( y_{col}[i] - \sum_{k=i+1}^{n-1} L[k,i] A_{inv}[k,j] \right)$

**B4. Trả về: Ma trận $A_{inv}$.**

#### Tìm ma trận nghịch đảo bằng phương pháp lặp Jacobi

**Input:**
- Ma trận vuông $A_{n \times n}$.
- Sai số cho trước $\varepsilon$.
- Số lần lặp tối đa cho phép N.

**Output:**
- Ma trận nghịch đảo $A^{-1}$.

**Thuật toán:**

**B1. Khởi tạo:**
- Xây dựng ma trận đơn vị $I_{n \times n}$.
- Khởi tạo ma trận kết quả $X \leftarrow 0_{n \times n}$.

**B2. Kiểm tra tính chéo trội và tính hệ số:**
- Nếu A chéo trội hàng: Gán $p = \infty$ và
  $\lambda = 1, \quad q = \max_{1 \le i \le n} \left( \frac{1}{|a_{ii}|} \sum_{j \neq i} |a_{ij}| \right)$
- Nếu A chéo trội cột: Gán $p = 1$ và
  $\lambda = \frac{\max_{1 \le i \le n} |a_{ii}|}{\min_{1 \le i \le n} |a_{ii}|}, \quad q = \max_{1 \le j \le n} \left( \frac{1}{|a_{jj}|} \sum_{i \neq j} |a_{ij}| \right)$
- Nếu không, dừng thuật toán.

**B3. Lặp:**
Cho $t$ chạy từ $1$ đến $n$ (tương ứng với mỗi cột của $I$ và $X$):
- Khởi tạo vector lặp $x_{old} \leftarrow 0_{n \times 1}$.
- Cho $k$ chạy từ $1$ đến $N$:
  - Tính vector lặp mới $x_{new}$:
    $(x_{new})_i = \frac{1}{a_{ii}} \left( (e_t)_i - \sum_{j \neq i} a_{ij} (x_{old})_j \right), \quad i = \overline{1, n}$
  - Kiểm tra điều kiện dừng: Nếu $\| x_{new} - x_{old} \|_p < \frac{\varepsilon(1-q)}{\lambda q}$, thoát vòng lặp k.
  - Gán $x_{old} \leftarrow x_{new}$.
- Gán cột thứ t của ma trận X bằng $x_{new}$.

**B4. Trả về kết quả: Trả về ma trận X là ma trận $A^{-1}$.**

#### Tìm ma trận nghịch đảo bằng phương pháp lặp Gauss-Seidel

**Input:**
- Ma trận vuông $A_{n \times n}$.
- Sai số cho trước $\varepsilon$.
- Số lần lặp tối đa cho phép N.

**Output:**
- Ma trận nghịch đảo $A^{-1}$.

**Thuật toán:**

**B1. Khởi tạo:**
- Xây dựng ma trận đơn vị $I_{n \times n}$.
- Khởi tạo ma trận kết quả $X \leftarrow 0_{n \times n}$.

**B2. Xác định ma trận chéo trội và tính hệ số:**
- Nếu A chéo trội hàng: Gán $s = 0, \quad q = \max_{i=\overline{1,n}} \frac{\sum_{j<i} |a_{ij}|}{|a_{ii}| - \sum_{j>i} |a_{ij}|}$
- Nếu A chéo trội cột: Gán $s = \max_{j=\overline{1,n}} \frac{1}{|a_{jj}|} \sum_{i>j} |a_{ij}|, \quad q = \max_{j=\overline{1,n}} \frac{\sum_{i<j} |a_{ij}|}{|a_{jj}| - \sum_{i>j} |a_{ij}|}$
- Nếu không, dừng thuật toán.

**B3. Lặp:**
Cho $t$ chạy từ $1$ đến $n$ (tương ứng với mỗi cột của $I$ và $X$):
- Khởi tạo vector lặp $x_{old} \leftarrow 0_{n \times 1}$.
- Cho $k$ chạy từ $1$ đến $N$:
  - Tạo một bản sao $x_{new} \leftarrow x_{old}$.
  - Tính vector lặp mới:
    $(x_{new})_i = \frac{1}{a_{ii}} \left( (e_t)_i - \sum_{j=1}^{i-1} a_{ij} (x_{new})_j - \sum_{j=i+1}^n a_{ij} (x_{old})_j \right), \quad i = \overline{1, n}$
  - Kiểm tra điều kiện dừng: Nếu $\frac{q}{(1-s)(1-q)} \| x_{new} - x_{old} \|_\infty < \varepsilon$, thoát vòng lặp k.
  - Gán $x_{old} \leftarrow x_{new}$.
- Gán cột thứ t của ma trận X bằng $x_{new}$.

**B4. Trả về kết quả: Trả về ma trận X là ma trận $A^{-1}$.**

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

**Input:**
- Ma trận vuông $A_{n \times n}$.

**Output:**
- Một danh sách các đa thức đặc trưng $P_1(\lambda), P_2(\lambda), \ldots$ của các khối Frobenius. Đa thức đặc trưng của A là tích của chúng.

**Thuật toán:**

**B1. Khởi tạo:**
- Gán ma trận làm việc $P \leftarrow A$.
- Khởi tạo danh sách đa thức kết quả: $list\_poly$.
- Gán $m \leftarrow n$ với n là kích thước của khối ma trận đang xét.

**B2. Lặp: Lặp $k$ từ $m$ xuống $2$:**
- TH1: Nếu $p_{k, k-1} \neq 0$.
  - Gọi Thuật toán phụ M (với đầu vào là chỉ số hàng k và ma trận P hiện tại) để xây dựng ma trận $M_k$ và $M_k^{-1}$.
  - Cập nhật $P$: $P \leftarrow M_k \cdot P \cdot M_k^{-1}$.
- TH2: Nếu $p_{k, k-1} = 0$.
  - Hoán vị: Tìm $j$ sao cho $1 \le j < k-1$ và $p_{k, j} \neq 0$.
    - Nếu tìm thấy một $j$ như vậy:
      - Gọi Thuật toán phụ C (với đầu vào là các chỉ số cột $j$ và $k-1$) để xây dựng ma trận hoán vị C.
      - Cập nhật P: $P \leftarrow C \cdot P \cdot C^{-1}$.
      - Quay lại kiểm tra TH1 với giá trị k hiện tại.
    - Ngược lại, nếu không tìm thấy $j$ như trên:
      - Phân rã:
        1. Xác định và xử lý khối Frobenius: Khối Frobenius $P'$ được xác định là ma trận con của $P$ bao gồm các hàng và cột từ chỉ số $k$ đến $m$.
        2. Trích xuất đa thức đặc trưng của khối $P'$ (là một khối Frobenius) và thêm vào $list\_poly$, với 2 dạng:
           +) Nếu P là một khối Frobenius dạng 1, các hệ số của đa thức đặc trưng có thể được đọc trực tiếp từ hàng đầu tiên của P
           +) Nếu P là một khối Frobenius dạng 2, các hệ số được đọc trực tiếp từ hàng cuối cùng của P.
        Thiết lập lại bài toán:
        1. Cập nhật kích thước bài toán: $m \leftarrow k - 1$.
        2. Thu nhỏ ma trận P: P được gán bằng ma trận con của P bao gồm các hàng và cột từ chỉ số $1$ đến $m$.
        3. Gán $k \leftarrow m + 1$ để vòng lặp bắt đầu lại.

**B3. Xử lý khối cuối cùng:**
- Sau khi vòng lặp kết thúc, P là khối Frobenius cuối cùng (hoặc một ma trận con $1 \times 1$). Trích xuất đa thức đặc trưng của nó và thêm vào $list\_poly$.

**B4. Trả về kết quả: Trả về danh sách $list\_poly$.**

**Các thuật toán phụ:**
* Thuật toán phụ M (Xây dựng ma trận biến đổi):
  - Input: Hàng $k$, ma trận P.
  - Output: $M_k, M_k^{-1}$.
  - Các bước:
    B1. Tạo $M_k$ là ma trận đơn vị, sau đó thay thế hàng $k-1$ của $M_k$ bằng hàng $k$ của P.
    B2. Tạo $M_k^{-1}$ là ma trận đơn vị, sau đó thay thế hàng $k-1$ của $M_k^{-1}$ với các phần tử $(M_k^{-1})_{k-1, j} \leftarrow -p_{k, j} / p_{k, k-1}$ (với $j \neq k-1$) và $(M_k^{-1})_{k-1, k-1} \leftarrow 1 / p_{k, k-1}$.
* Thuật toán phụ C (Xây dựng ma trận hoán vị):
  - Input: Các chỉ số cột $j$ và $k-1$.
  - Output: Ma trận C.
  - Các bước: Tạo ma trận đơn vị, sau đó hoán vị cột $j$ và cột $k-1$. ($C = C^{-1}$).
* Thuật toán phụ S (Xây dựng ma trận khử khối $S_q$):
  - Input: Ma trận P đang khối, cột 'q' của khối B.
  - Output: $S_q, S_q^{-1}$.
  - Các bước: Xây dựng ma trận $S_q$ là ma trận đơn vị với một khối con ngoài đường chéo được điền các giá trị lấy từ cột 'q' của B (với dấu ngược lại) để khi nhân ma trận sẽ triệt tiêu được cột 'q' đó.

### 18. Phương pháp Xuống thang

**Input:**
- Ma trận vuông $A_{n \times n}$.
- Giá trị riêng trội nhất đã biết $\lambda_1$.
- Vector riêng phải tương ứng $v_1$ (đã chuẩn hóa: $\|v_1\|_2 = 1$).
- Các tham số cho phương pháp lũy thừa con: Vector ban đầu $X^{(0)}$, sai số $\varepsilon$, số lặp tối đa $k_{max}$.

**Output:**
- Giá trị riêng trội thứ hai $\lambda_2$.
- Vector riêng tương ứng $v_2$.

**Thuật toán:**

**B1. Xây dựng ma trận xuống thang:**
- Chuẩn hóa vector riêng: $v_1 \leftarrow \frac{v_1}{\|v_1\|}$
- Chọn vector phụ x: Chọn một vector x sao cho $x \leftarrow \frac{v_1}{v_1^T v_1}$
- Tính ma trận xuống thang B:
  $B \leftarrow A - \lambda_1 v_1 x^T$

**B2. Tìm trị riêng trội của ma trận B:**
- Áp dụng thuật toán phương pháp lũy thừa cho ma trận B với vector ban đầu $X^{(0)}$.
- Kết quả thu được:
  - Trị riêng trội của B, chính là trị riêng trội thứ hai của A: $\lambda_2$.
  - Vector riêng tương ứng thu được là vector riêng $u_2$ của ma trận B

**B3. Tìm vector riêng của A:**
- Sử dụng công thức biến đổi ngược để tìm vector riêng $v_2$ của A từ $u_2$:
  $v_2 \leftarrow (\lambda_2 - \lambda_1) u_2 + \lambda_1 (x^T u_2) v_1$
- Chuẩn hóa vector riêng kết quả: $v_2 \leftarrow \frac{v_2}{\|v_2\|_2}$

**B4. Trả về kết quả:**
- Trả về trị riêng trội thứ hai cùng vector riêng tương ứng $(\lambda_2, v_2)$ đã tìm được.

### 19. Phân tích giá trị kỳ dị (SVD) và Phương pháp lũy thừa
**Mục đích:** Tìm giá trị kỳ dị lớn nhất $\sigma_1$ bằng Phương pháp lũy thừa.

**Input:**
- Ma trận $A_{m \times n}$.
- Các tham số cho phương pháp lũy thừa: Vector ban đầu $X^{(0)}$, sai số $r$, số lặp tối đa $k_{max}$.

**Output:**
- Giá trị kỳ dị lớn nhất $\sigma_1$.
- Thông báo về sự hội tụ.

**Thuật toán:**

**B1. Khởi tạo:**
- Xây dựng ma trận đối xứng: $B \leftarrow A^T A$.
- Gán $k \leftarrow 0$.
- Chuẩn hóa vector ban đầu theo chuẩn 2: $v \leftarrow \frac{X^{(0)}}{\|X^{(0)}\|_2}$

**B2. Tìm trị riêng trội của B bằng Phương pháp Lũy thừa:**
- Lặp: Lặp trong khi $k < k_{max}$:
  - Gán $v_{old} \leftarrow v$.
  - Tính vector mới: $Y \leftarrow B \cdot v_{old}$.
  - Ước lượng trị riêng bằng thương Rayleigh: $\lambda_1 \leftarrow v_{old}^T \cdot Y$.
  - Chuẩn hóa vector mới bằng chuẩn 2: $v \leftarrow \frac{Y}{\|Y\|_2}$.
  - Cập nhật $k \leftarrow k + 1$.
  - Kiểm tra hội tụ: Nếu $\|v - v_{old}\|_\infty < \varepsilon$, thoát vòng lặp.

**B3. Tính giá trị kỳ dị lớn nhất:**
- Tính giá trị kỳ dị:
  $\sigma_1 \leftarrow \sqrt{\lambda_1}$

**B4. Trả về kết quả:**
- Trả về giá trị $\sigma_1$ và thông báo về sự hội tụ.

**Ứng dụng SVD (Phân tích thành phần chính - PCA / Nén ảnh):** 
SVD cho phép biểu diễn ma trận $A$ dưới dạng tổng các ma trận hạng 1: $A = \sum_{i=1}^r \sigma_i u_i v_i^T$. Trong nén ảnh, ta chỉ giữ lại $k$ giá trị kỳ dị lớn nhất đầu tiên ($k \ll r$) để tái tạo ảnh xấp xỉ $A_k = \sum_{i=1}^k \sigma_i u_i v_i^T$ giúp tiết kiệm đáng kể không gian lưu trữ mà vẫn giữ được đặc trưng chính của ảnh ban đầu.

### 20. Tính số điều kiện Cond(A)

**Input:**
- Ma trận vuông $A_{n \times n}$.

**Output:**
- Số điều kiện của ma trận A, $cond(A)$.

**Thuật toán:**

**B1. Tìm tất cả các giá trị kỳ dị của A:**
- Áp dụng thuật toán tìm khai triển kỳ dị để tìm ra danh sách tất cả các giá trị kỳ dị của ma trận A: $(\sigma_1, \sigma_2, \ldots, \sigma_n)$.

**B2. Xác định $\sigma_{max}$ và $\sigma_{min}$:**
- Tìm giá trị kỳ dị lớn nhất: $\sigma_{max} \leftarrow \max(\sigma_1, \ldots, \sigma_n)$.
- Tìm giá trị kỳ dị nhỏ nhất: $\sigma_{min} \leftarrow \min(\sigma_1, \ldots, \sigma_n)$.

**B3. Tính số điều kiện:**
- Nếu $\sigma_{min} = 0$, hiện thông báo "Ma trận A là ma trận suy biến và số điều kiện là vô cùng".
- Ngược lại, tính số điều kiện theo công thức:
  $cond(A) \leftarrow \frac{\sigma_{max}}{\sigma_{min}}$

**B4. Trả về kết quả:**
- Trả về giá trị $cond(A)$.
