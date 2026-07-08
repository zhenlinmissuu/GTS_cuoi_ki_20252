# Hướng Dẫn Trình Bày Bài Tập & Thuật Toán Giải Tích Số (MI3041)

Tài liệu này được biên soạn từ các hình ảnh bài tập thực hành môn Giải tích số. Đây là tài liệu hướng dẫn chuẩn về cách viết thuật toán, cách trình bày lời giải tự luận/bài tập lớn và các tiêu chí đánh giá sai số để đạt điểm tối đa trong kỳ thi.

---

## 1. TUẦN 8: PHÂN TÍCH LU & CHOLESKY GIẢI HỆ PT TUYẾN TÍNH

### Câu 27: Thuật toán phân tách LU cho ma trận vuông $A \in \text{Mat}(n,n)$

* **Input:** Ma trận vuông $A \in \text{Mat}(n,n)$
* **Output:** Ma trận $A$ sau khi chạy thuật toán sẽ chứa cả $L$ (dưới đường chéo chính) và $U$ (từ đường chéo chính trở lên).
* **Thuật toán:**
  * **B1. Khởi tạo:** Tạo ma trận $B \leftarrow A$ (sao chép để cập nhật trực tiếp).
  * **B2. Lặp:** 
    * Với mỗi cột $k$ chạy từ $0$ đến $n-2$:
      * Nếu $B[k,k] = 0$, báo lỗi: *"Ma trận suy biến, không thể phân rã LU"* và dừng thuật toán.
      * Với mỗi hàng $i$ từ $k+1$ đến $n-1$:
        * Tính hệ số $L[i,k]$: $B[i,k] \leftarrow \frac{B[i,k]}{B[k,k]}$
        * Cập nhật phần còn lại của hàng $i$: với mỗi cột $j$ từ $k+1$ đến $n-1$:
          $$B[i,j] \leftarrow B[i,j] - B[i,k] \times B[k,j]$$
  * **B3. Tách $L$ và $U$:**
    * Khởi tạo $L = I_n$ (ma trận đơn vị), $U = 0_{n \times n}$ (ma trận không).
    * Với mọi chỉ số $i, j = 0, \dots, n-1$:
      $$L_{i,j} = \begin{cases} 1, & i=j \\ B_{i,j}, & i > j \\ 0, & i < j \end{cases} \quad ; \quad U_{i,j} = \begin{cases} B_{i,j}, & i \le j \\ 0, & i > j \end{cases}$$
  * **B4. Trả về:** Ma trận $L$ và ma trận $U$.

---

### Câu 28: Thuật toán phân tách LU có chọn phần tử trội (Pivoting) giải hệ $AX = B$

* **Input:** Ma trận vuông $A \in \mathbb{R}^{n \times n}$, vector vế phải $B \in \mathbb{R}^{n \times 1}$
* **Output:** Ma trận tam giác dưới $L$ (đường chéo chính bằng 1), ma trận tam giác trên $U$, ma trận hoán vị $P$, vector hoán vị $perm$, vector nghiệm $X \in \mathbb{R}^{n \times 1}$.
* **Thuật toán:**
  * **B1. Khởi tạo:** 
    * Tạo ma trận $P$ là ma trận đơn vị cấp $n$.
    * Tạo bản sao của ma trận $A$.
    * Tạo vector $perm = [0, 1, 2, \dots, n-1]$.
  * **B2. Phân tách LU có pivoting:**
    * Với mỗi cột $k$ từ $0$ đến $n-2$:
      * Tìm chỉ số hàng $p \leftarrow \text{arg max}_{k \le i \le n-1} |A[i,k]|$ (chọn pivot lớn nhất trong cột $k$).
      * Nếu $A[p,k] = 0$, báo lỗi: *"Ma trận suy biến, không thể phân rã LU"* và dừng thuật toán.
      * Nếu $p \neq k$, tiến hành hoán đổi:
        * Hoán đổi hàng $k$ và $p$ trong ma trận $A$.
        * Hoán đổi hàng $k$ and $p$ trong ma trận $P$.
        * Hoán đổi $perm[k]$ và $perm[p]$ trong vector $perm$.
      * Với mỗi hàng $i$ từ $k+1$ đến $n-1$:
        * Nếu $A[i,k] \neq 0$:
          * Tính hệ số $L[i,k]$: $A[i,k] \leftarrow \frac{A[i,k]}{A[k,k]}$
          * Cập nhật các phần tử còn lại: 
            $$A[i, k+1 : n] \leftarrow A[i, k+1 : n] - A[i,k] \times A[k, k+1 : n]$$
  * **B3. Tách $L$ và $U$:**
    * Tạo ma trận $L$ với đường chéo chính bằng $1$ và phần dưới đường chéo lấy từ $A$.
    * Tạo ma trận $U$ với phần trên đường chéo và đường chéo chính lấy từ $A$.
  * **B4. Giải hệ phương trình $AX = B$:**
    * Hoán vị vector $B$ theo $perm$: $B' \leftarrow B[perm]$.
    * Giải hệ tam giác dưới $LY = B'$ bằng thế tiến:
      $$Y[i] \leftarrow B'[i] - \sum_{k=0}^{i-1} L[i,k] \times Y[k] \quad (i = 0 \dots n-1)$$
    * Giải hệ tam giác trên $UX = Y$ bằng thế ngược:
      $$X[i] \leftarrow \frac{Y[i] - \sum_{k=i+1}^{n-1} U[i,k] \times X[k]}{U[i,i]} \quad (i = n-1 \dots 0)$$
  * **B5. Trả về:** $L$, $U$, $P$, $perm$, $X$.

---

### Câu 29: Thuật toán tìm phân tách Cholesky $A = LL^T$

Áp dụng cho ma trận đối xứng xác định dương.

* **Input:** Ma trận vuông $A \in \text{Mat}(n,n)$
* **Output:** Ma trận tam giác dưới $L$ sao cho $A = LL^T$.
* **Thuật toán:**
  * **B1. Khởi tạo:** Tạo ma trận sao chép $L \leftarrow A$
  * **B2. Tính các phần tử của $L$:**
    * Với $i$ chạy từ $0$ đến $n-1$:
      * Gán: $temp \leftarrow L[i,i] - \sum_{k=0}^{i-1} L[i,k]^2$
      * Nếu $temp < 0$, báo lỗi: *"Ma trận không dương xác định. Không thể phân tách Cholesky"* và dừng thuật toán.
      * Tính đường chéo: $L[i,i] \leftarrow \sqrt{temp}$
      * Tính các phần tử dưới đường chéo: với mỗi $j$ từ $i+1$ đến $n-1$:
        $$L[j,i] \leftarrow \frac{1}{L[i,i]} \left( L[j,i] - \sum_{k=0}^{i-1} L[j,k] \times L[i,k] \right)$$
      * Xóa các phần tử trên đường chéo chính: với mỗi $j$ từ $i+1$ đến $n-1$: $L[i,j] \leftarrow 0$.
  * **B3. Trả về:** Ma trận $L$.

---

## 2. TUẦN 9: PHƯƠNG PHÁP LẶP ĐƠN GIẢI HỆ TUYẾN TÍNH & ỨNG DỤNG LEONTIEF

### Câu 31: Thuật toán phương pháp lặp đơn giải hệ $X = BX + d$

* **Input:** Ma trận lặp $B \in \text{Mat}(n,n)$, vector tự do $d \in \mathbb{R}^n$, sai số $\epsilon > 0$, số lần lặp tối đa $N$.
* **Output:** Vector nghiệm gần đúng $X = (x_1, \dots, x_n)^T$ hoặc thông báo thất bại.
* **Thuật toán:**
  * **B1. Tính chuẩn:** Gán $q \leftarrow \|B\|_p$ (với $p = \infty, 1$ hoặc $2$).
  * **B2. Kiểm tra điều kiện hội tụ:** Nếu $q \ge 1$, thông báo *"Điều kiện hội tụ không thỏa mãn, phương pháp có thể không hội tụ"* và dừng chương trình.
  * **B3. Khởi tạo:** Gán $k \leftarrow 0, X^{(0)} \leftarrow 0_n$.
  * **B4. Lặp (trong khi $k < N$):**
    * Tính xấp xỉ mới: $X^{(k+1)} \leftarrow BX^{(k)} + d$
    * Kiểm tra sai số (điều kiện dừng):
      $\text{Nếu } \frac{q}{1-q} \|X^{(k+1)} - X^{(k)}\| < \epsilon$ thì trả về nghiệm $X = X^{(k+1)}$ và dừng chương trình.
    * Cập nhật vòng lặp: $k \leftarrow k+1, X^{(k)} \leftarrow X^{(k+1)}$.
  * **B5. Kết thúc:** Thông báo *"Thất bại sau N lần lặp"* và dừng chương trình.

---

### Câu 33 & 34: Lời giải mẫu Bài toán Mô hình cân bằng liên ngành Leontief (7 và 10 ngành)

**Đề bài:** Cho ma trận tiêu thụ nội bộ $C$ (hoặc $A$) và vector nhu cầu bên ngoài $d$ (hoặc $b$). Xác định lượng tổng sản phẩm cần sản xuất $X$ sao cho $X = CX + d$.

#### Phương pháp trình bày tự luận:

1. **Thiết lập hệ phương trình:**
   * Gọi $X = (x_1, x_2, \dots, x_n)^T$ là vector lượng sản phẩm cần sản xuất.
   * Hệ phương trình cân bằng có dạng: $X = CX + d$.
2. **Khảo sát điều kiện hội tụ:**
   * Tính chuẩn cột $\|C\|_1$.
   * Ví dụ với bài toán 7 ngành: $\|C\|_1 = 0.9293 < 1$. Do đó hệ phương trình lặp đơn hội tụ với mọi xấp xỉ ban đầu $X^{(0)}$.
3. **Lựa chọn xấp xỉ ban đầu:** Chọn $X^{(0)} = d$.
4. **Thiết lập điều kiện dừng:**
   * Với yêu cầu sai lệch không vượt quá $\Delta$ (ví dụ $\Delta = 10$ triệu đô):
     $$\|X_n - X^*\| \le \frac{\|C\|_1}{1 - \|C\|_1} \|X_n - X_{n-1}\|_1 \le \Delta$$
   * Biến đổi tìm điều kiện thực tế cho khoảng cách giữa 2 bước lặp liên tiếp:
     $$\|X_n - X_{n-1}\|_1 \le \frac{\Delta (1 - \|C\|_1)}{\|C\|_1} = \epsilon_0$$
     * *Ví dụ với hệ 7 ngành:* $\epsilon_0 = \frac{10(1 - 0.9293)}{0.9293} \approx 0.7608$.
     * *Ví dụ với hệ 10 ngành:* $\epsilon_0 = \frac{10(1 - 0.63344)}{0.63344} \approx 5.78681$.
5. **Bảng kết quả trung gian trong bài thi:**

| Biến                  | Lần 1 | Lần 2 | ... | Lần $k-1$     | Lần $k$ (Nghiệm $X^*$)   |
|:---------------------:|:-----:|:-----:|:---:|:-------------:|:------------------------:|
| $x_1$                 | ...   | ...   | ... | ...           | ...                      |
| $x_2$                 | ...   | ...   | ... | ...           | ...                      |
| ...                   | ...   | ...   | ... | ...           | ...                      |
| $\|X_k - X_{k-1}\|_1$ | ...   | ...   | ... | $>\epsilon_0$ | $<\epsilon_0$ (Thỏa mãn) |

---

## 3. TUẦN 10: PHƯƠNG PHÁP LẶP GAUSS-SEIDEL GIẢI HỆ TUYẾN TÍNH

### Câu 37: Thuật toán Gauss-Seidel giải hệ $AX = b$

* **Input:** Ma trận $A_{n \times n}$, vector vế phải $b_{n \times 1}$, sai số $\epsilon$.
* **Output:** Vector nghiệm $X$ với sai số không quá $\epsilon$.
* **Thuật toán:**
  * **B1. Xác định ma trận chéo trội và tính hệ số:**
    * **Nếu chéo trội hàng** ($\sum_{j \neq i} |a_{ij}| < |a_{ii}|, \forall i$): 
      Gán $s \leftarrow 0$, $q \leftarrow \max_{1 \le i \le n} \frac{\sum_{j > i} |a_{ij}|}{|a_{ii}| - \sum_{j < i} |a_{ij}|}$.
    * **Nếu chéo trội cột** ($\sum_{i \neq j} |a_{ij}| < |a_{jj}|, \forall j$): 
      Gán $s \leftarrow \max_{1 \le j \le n} \frac{1}{|a_{jj}|} \sum_{i > j} |a_{ij}|$, $q \leftarrow \max_{1 \le j \le n} \frac{\sum_{i < j} |a_{ij}|}{|a_{jj}| - \sum_{i > j} |a_{ij}|}$.
    * Nếu cả hai đều không thỏa mãn, cảnh báo phương pháp có thể không hội tụ.
  * **B2. Khởi tạo:** Gán $k \leftarrow 0, X^{(0)} \leftarrow 0_n$.
  * **B3. Lặp:**
    * Tính các ẩn số tuần tự, cập nhật trực tiếp giá trị mới vừa tính:
      $$x_i^{(k+1)} = \frac{1}{a_{ii}} \left( b_i - \sum_{j=1}^{i-1} a_{ij} x_j^{(k+1)} - \sum_{j=i+1}^n a_{ij} x_j^{(k)} \right) \quad (i = 1 \dots n)$$
    * Kiểm tra điều kiện dừng:
      $$\text{Nếu } \frac{q}{(1-s)(1-q)} \|X^{(k+1)} - X^{(k)}\| < \epsilon$$
      thì thoát vòng lặp. Ngược lại, gán $k \leftarrow k+1$ và tiếp tục.
  * **B4. Trả về:** Nghiệm gần đúng $X^{(k+1)}$.

---

## 4. TUẦN 11+12: TÌM MA TRẬN NGHỊCH ĐẢO

### Câu 40: Thuật toán Cholesky tìm ma trận nghịch đảo $A^{-1}$

* **Input:** Ma trận đối xứng xác định dương $A \in \text{Mat}(n,n)$.
* **Output:** Ma trận nghịch đảo $A^{-1}$ (nếu thỏa mãn điều kiện).
* **Thuật toán:**
  * **B1. Kiểm tra tính đối xứng:** Nếu $A \neq A^T$, báo lỗi và dừng thuật toán.
  * **B2. Phân tách Cholesky $A = LL^T$:**
    * (Tính ma trận tam giác dưới $L$ tương tự như Câu 29). Nếu có $temp < 0$ trong lúc tính đường chéo thì báo lỗi *"Ma trận không xác định dương"* và dừng.
  * **B3. Tính từng cột của ma trận nghịch đảo $A^{-1}$:**
    * Với mỗi cột $j$ chạy từ $0$ đến $n-1$:
      * Giải hệ $L y = e_j$ (với $e_j$ là cột thứ $j$ của ma trận đơn vị $I_n$):
        $$y[i] \leftarrow \frac{1}{L[i,i]} \left( \delta_{ij} - \sum_{k=0}^{i-1} L[i,k] \times y[k] \right) \quad (i = 0 \dots n-1)$$
      * Giải hệ $L^T x = y$ (tìm cột thứ $j$ của ma trận nghịch đảo $A^{-1}$):
        $$A^{-1}[i,j] \leftarrow \frac{1}{L[i,i]} \left( y[i] - \sum_{k=i+1}^{n-1} L[k,i] \times A^{-1}[k,j] \right) \quad (i = n-1 \dots 0)$$
  * **B4. Trả về:** Ma trận nghịch đảo $A^{-1}$.

---

### Câu 42: Thuật toán Lặp Jacobi và Gauss-Seidel tìm ma trận nghịch đảo $A^{-1}$

Dùng phương pháp lặp để giải hệ $A X_j = e_j$ song song cho $n$ cột của ma trận nghịch đảo.

#### A. Phương pháp lặp Jacobi:

* **B1. Khởi tạo:** Xây dựng ma trận đơn vị $I_{n \times n}$, khởi tạo ma trận kết quả $X \leftarrow 0_{n \times n}$.
* **B2. Kiểm tra tính chéo trội và tính hệ số:**
  * **Nếu A chéo trội hàng:** Gán $p = \infty, \lambda = 1$, và $q = \max_{1 \le i \le n} \left( \frac{1}{|a_{ii}|} \sum_{j \neq i} |a_{ij}| \right)$.
  * **Nếu A chéo trội cột:** Gán $p = 1$, $\lambda = \frac{\max |a_{ii}|}{\min |a_{ii}|}$, và $q = \max_{1 \le j \le n} \left( \frac{1}{|a_{jj}|} \sum_{i \neq j} |a_{ij}| \right)$.
  * Nếu không chéo trội, dừng thuật toán.
* **B3. Lặp:** Cho cột $l$ chạy từ $0$ đến $n-1$ (giải cho cột thứ $l$ của $A^{-1}$):
  * Khởi tạo vector lặp $x_{old} \leftarrow 0_{n \times 1}$.
  * Lặp $k$ từ $1$ đến $N$:
    * Tính mới: $(x_{new})_i \leftarrow \frac{1}{a_{ii}} \left( (e_l)_i - \sum_{j \neq i} a_{ij} (x_{old})_j \right) \quad (i = 0 \dots n-1)$
    * Nếu $\|x_{new} - x_{old}\|_p < \frac{\epsilon(1-q)}{\lambda q}$, thoát vòng lặp.
    * Cập nhật: $x_{old} \leftarrow x_{new}$.
  * Gán cột $l$ của ma trận kết quả $X$ bằng $x_{new}$.
* **B4. Trả về:** Ma trận nghịch đảo $X = A^{-1}$.

#### B. Phương pháp lặp Gauss-Seidel:

* **B1. Khởi tạo:** Tương tự Jacobi.
* **B2. Kiểm tra tính chéo trội và tính hệ số:**
  * **Nếu A chéo trội hàng:** Gán $s = 0$, $q = \max_{1 \le i \le n} \frac{\sum_{j>i} |a_{ij}|}{|a_{ii}| - \sum_{j<i} |a_{ij}|}$.
  * **Nếu A chéo trội cột:** Gán $s = \max_{1 \le j \le n} \frac{1}{|a_{jj}|} \sum_{i>j} |a_{ij}|$, $q = \max_{1 \le j \le n} \frac{\sum_{i<j} |a_{ij}|}{|a_{jj}| - \sum_{i>j} |a_{ij}|}$.
* **B3. Lặp:** Cho cột $l$ chạy từ $0$ đến $n-1$:
  * Khởi tạo vector lặp $x_{old} \leftarrow 0_{n \times 1}$.
  * Lặp $k$ từ $1$ đến $N$:
    * Tính mới sử dụng giá trị mới nhất trong vòng lặp:
      $$(x_{new})_i \leftarrow \frac{1}{a_{ii}} \left( (e_l)_i - \sum_{j=0}^{i-1} a_{ij} (x_{new})_j - \sum_{j=i+1}^{n-1} a_{ij} (x_{old})_j \right) \quad (i = 0 \dots n-1)$$
    * Nếu $\frac{q}{(1-s)(1-q)} \|x_{new} - x_{old}\|_\infty < \epsilon$, thoát vòng lặp.
    * Cập nhật: $x_{old} \leftarrow x_{new}$.
  * Gán cột $l$ của ma trận kết quả $X$ bằng $x_{new}$.
* **B4. Trả về:** Ma trận nghịch đảo $X = A^{-1}$.

---

## 5. TUẦN 13+14: GIÁ TRỊ RIÊNG & ĐA THỨC ĐẶC TRƯNG

### Câu 43: Thuật toán Danielevski tìm đa thức đặc trưng của ma trận $A_{n \times n}$

Đưa ma trận về dạng chuẩn Frobenius bằng các phép nhân ma trận biến đổi tương đương $M_k \cdot P \cdot M_k^{-1}$.

* **Input:** Ma trận vuông $A_{n \times n}$
* **Output:** Danh sách các đa thức đặc trưng $P_1(\lambda), P_2(\lambda), \dots$ của các khối Frobenius của ma trận $A$.
* **Thuật toán:**
  * **B1. Khởi tạo:** Gán ma trận làm việc $P \leftarrow A$. Khởi tạo danh sách kết quả $list\_poly = []$. Gán kích thước khối $m \leftarrow n$.
  * **B2. Lặp:** Cho chỉ số $k$ chạy từ $m$ xuống 2:
    * **TH1: Nếu $p_{k, k-1} \neq 0$:**
      * Gọi *Thuật toán phụ M* để xây dựng ma trận biến đổi $M_k$ và $M_k^{-1}$.
      * Cập nhật $P \leftarrow M_k \cdot P \cdot M_k^{-1}$.
    * **TH2: Nếu $p_{k, k-1} = 0$:**
      * *Hoán vị cột:* Tìm chỉ số $j$ sao cho $1 \le j < k-1$ và $p_{k, j} \neq 0$.
      * **Nếu tìm thấy $j$:**
        * Gọi *Thuật toán phụ C* để xây dựng ma trận hoán vị $C$ cho cột $j$ và $k-1$.
        * Cập nhật $P \leftarrow C \cdot P \cdot C^{-1}$.
        * Quay lại kiểm tra TH1 tại giá trị $k$ hiện tại.
      * **Nếu không tìm thấy $j$:** (Ma trận bị phân rã thành các khối con độc lập)
        * *Phân rã:* Khối Frobenius con $P'$ được xác định từ các hàng và cột từ $k$ đến $m$.
        * Trích xuất đa thức đặc trưng của $P'$ và thêm vào $list\_poly$:
          * Dạng 1 (Frobenius dòng 1): Đọc các hệ số từ hàng đầu tiên của khối $P'$.
          * Dạng 2 (Frobenius dòng cuối): Đọc các hệ số từ hàng cuối cùng của khối $P'$.
        * *Tái thiết lập bài toán:*
          * Cập nhật kích thước khối: $m \leftarrow k-1$.
          * Thu nhỏ ma trận $P$ về kích thước $m \times m$ (lấy từ hàng/cột $1 \dots m$).
          * Đặt $k \leftarrow m+1$ để vòng lặp bắt đầu lại với khối mới.
  * **B3. Xử lý khối cuối cùng:** Sau khi thoát lặp, khối $P$ còn lại kích thước $m \times m$ là khối Frobenius cuối cùng (hoặc ma trận $1 \times 1$). Trích xuất đa thức đặc trưng của nó thêm vào $list\_poly$.
  * **B4. Trả về:** Danh sách $list\_poly$. (Đa thức đặc trưng tổng quát là tích của tất cả đa thức trong danh sách).

#### Các thuật toán phụ cho Danielevski:

1. **Thuật toán phụ M (Xây dựng ma trận biến đổi):**
   * *Input:* Chỉ số hàng $k$, ma trận $P$.
   * *Output:* Ma trận $M_k$ và nghịch đảo $M_k^{-1}$.
   * *Cách tính:*
     * $M_k$ là ma trận đơn vị cấp $n$, ngoại trừ dòng $k$ được thay thế bởi dòng $k$ của $P$:
       $$M_k[k, j] = p_{k, j} \quad (j = 0 \dots n-1)$$
     * $M_k^{-1}$ là ma trận đơn vị cấp $n$, ngoại trừ dòng $k$ có các phần tử được tính như sau:
       $$(M_k^{-1})_{k, j} = -\frac{p_{k, j}}{p_{k, k-1}} \quad (j \neq k-1) \quad ; \quad (M_k^{-1})_{k, k-1} = \frac{1}{p_{k, k-1}}$$
2. **Thuật toán phụ C (Xây dựng ma trận hoán vị):**
   * *Input:* Chỉ số cột $j$ và $k-1$.
   * *Output:* Ma trận hoán vị $C$ (lưu ý $C = C^{-1}$).
   * *Cách tính:* Hoán đổi cột $j$ và $k-1$ của ma trận đơn vị.
3. **Thuật toán phụ S (Xử lý khử khối chéo):**
   * Khử các phần tử ngoài khối chéo chính bằng cách tạo ma trận $S_q$ với các giá trị đối số của cột cần triệt tiêu.

---

### Câu 46: Thuật toán xuống thang (Deflation) tìm giá trị riêng trội thứ hai

* **Input:** Ma trận $A_{n \times n}$, giá trị riêng trội nhất $\lambda_1$ đã biết, vector riêng tương ứng $v_1$ (đã chuẩn hóa $\|v_1\|_2 = 1$), các tham số lặp: $X^{(0)}, \epsilon, k_{max}$.
* **Output:** Giá trị riêng trội thứ hai $\lambda_2$, vector riêng tương ứng $v_2$.
* **Thuật toán:**
  * **B1. Xây dựng ma trận xuống thang $B$:**
    * Chọn một vector phụ $x$ sao cho $x^T v_1 = 1$. Thông thường chọn $x = \frac{v_1}{v_1^T v_1} = v_1$ (vì $\|v_1\|_2 = 1$).
    * Tính ma trận xuống thang $B$:
      $$B \leftarrow A - \lambda_1 v_1 x^T$$
  * **B2. Tìm trị riêng trội của ma trận $B$:**
    * Áp dụng thuật toán *phương pháp lũy thừa* cho ma trận $B$ với vector ban đầu $X^{(0)}$.
    * Kết quả thu được:
      * Trị riêng trội nhất của $B$ chính là trị riêng thứ hai của $A$: $\lambda_2$.
      * Vector riêng tương ứng của $B$: $u_2$.
  * **B3. Khôi phục vector riêng $v_2$ của ma trận gốc $A$:**
    * Sử dụng công thức biến đổi ngược để tìm $v_2$ từ $u_2$:
      $$v_2 \leftarrow (\lambda_2 - \lambda_1) u_2 + \lambda_1 (x^T u_2) v_1$$
    * Chuẩn hóa kết quả: $v_2 \leftarrow \frac{v_2}{\|v_2\|_2}$.
  * **B4. Trả về:** $\lambda_2$ và $v_2$.

---

## 6. TUẦN 15+16: KHAI TRIỂN KỲ DỊ SVD & ỨNG DỤNG

### Câu 48: Thuật toán tìm giá trị kỳ dị lớn nhất $\sigma_1$ của ma trận $A_{m \times n}$

* **Input:** Ma trận $A_{m \times n}$, các tham số lặp lũy thừa: $X^{(0)}, \epsilon, k_{max}$.
* **Output:** Giá trị kỳ dị lớn nhất $\sigma_1$.
* **Thuật toán:**
  * **B1. Khởi tạo:**
    * Xây dựng ma trận đối xứng: $B \leftarrow A^T A$.
    * Gán chỉ số lặp $k \leftarrow 0$.
    * Chuẩn hóa vector ban đầu: $v \leftarrow \frac{X^{(0)}}{\|X^{(0)}\|_2}$.
  * **B2. Tìm trị riêng trội của ma trận $B$ bằng phương pháp lũy thừa:**
    * Trong khi $k < k_{max}$:
      * Gán $v_{old} \leftarrow v$.
      * Nhân ma trận: $Y \leftarrow B \cdot v_{old}$.
      * Ước lượng trị riêng trội bằng thương Rayleigh: $\lambda_1 \leftarrow v_{old}^T \cdot Y$.
      * Chuẩn hóa vector mới bằng chuẩn 2: $v \leftarrow \frac{Y}{\|Y\|_2}$.
      * Cập nhật $k \leftarrow k+1$.
      * Kiểm tra hội tụ: Nếu $\|v - v_{old}\|_2 < \epsilon$ thì thoát vòng lặp.
  * **B3. Tính giá trị kỳ dị lớn nhất:**
    $$\sigma_1 \leftarrow \sqrt{\lambda_1}$$
  * **B4. Trả về:** $\sigma_1$ và thông báo hội tụ.

---

### Câu 50: Thuật toán tính số điều kiện $\text{cond}(A)$ của ma trận vuông $A_{n \times n}$

* **Input:** Ma trận vuông $A_{n \times n}$.
* **Output:** Số điều kiện $\text{cond}(A)$.
* **Thuật toán:**
  * **B1. Tìm tất cả các giá trị kỳ dị của $A$:**
    * Tìm danh sách tất cả các giá trị kỳ dị của $A$: $\{\sigma_1, \sigma_2, \dots, \sigma_n\}$.
  * **B2. Xác định giá trị cực đại và cực tiểu:**
    * $\sigma_{max} \leftarrow \max(\sigma_1, \dots, \sigma_n)$
    * $\sigma_{min} \leftarrow \min(\sigma_1, \dots, \sigma_n)$
  * **B3. Tính số điều kiện:**
    * Nếu $\sigma_{min} = 0$, báo lỗi: *"Ma trận A suy biến và số điều kiện là vô cùng"*.
    * Ngược lại, tính:
      $$\text{cond}(A) \leftarrow \frac{\sigma_{max}}{\sigma_{min}}$$
  * **B4. Trả về:** Số điều kiện $\text{cond}(A)$.
