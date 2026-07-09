# BÀI TẬP GIẢI TÍCH SỐ MI3041

## 1 TUẦN 8.

Câu 27. Viết thuật toán tìm phân tích LU cho ma trận A. Áp dụng cho ma trận vuông A cấp 6 cụ thể.

Input:

- Ma trận vuông $A \in Mat(n, n)$
  Output:
- Ma trận A được phân rã chứa cả L và U
  Thuật toán:
  B1. Khởi tạo:
- Tạo ma trận $B \leftarrow A$ (sao chép để cập nhật).
  B2. Lặp:
- Với mỗi cột $k \leftarrow 0$ đến $n-2$:
  - Nếu $B[k,k] = 0$, báo lỗi "Ma trận suy biến, không thể phân rã LU."
  - Với mỗi hàng $i \leftarrow k+1$ đến $n-1$:
    - Tính hệ số $L[i,k]$: $B[i,k] \leftarrow B[i,k] / B[k,k]$
    - Cập nhật phần còn lại của hàng $i$:
      với mỗi $j \leftarrow k+1$ đến $n-1$: $B[i,j] \leftarrow B[i,j] - B[i,k] \times B[k,j]$.
      B3. Tách L và U:
- Khởi tạo $L = I_n, U = 0_{n \times n}$.
- Với mỗi chỉ số $i, j = 0, \ldots, n-1$:
  $L_{i,j} = \begin{cases} 1, & i = j, \\ B_{i,j}, & i > j, \\ 0, & i < j, \end{cases} \quad U_{i,j} = \begin{cases} B_{i,j}, & i \le j, \\ 0, & i > j. \end{cases}$
  B4. Trả về: Ma trận L, ma trận U.

Câu 28. Viết thuật toán cho phương pháp phân tích LU giải phương trình AX = B. Áp dụng cho bài toán cụ thể cấp 7.

Input:

- Ma trận vuông $A \in \mathbb{R}^{n \times n}$.
- Vector vế phải $B \in \mathbb{R}^{n \times 1}$.
  Output:
- Ma trận tam giác dưới L với đường chéo chính bằng 1.
- Ma trận tam giác trên U.
- Ma trận hoán vị P.
- Vector hoán vị $perm$.
- Vector nghiệm $X \in \mathbb{R}^{n \times 1}$ của hệ $AX = B$.
  Thuật toán:
  B1. Khởi tạo:
- Tạo ma trận P là ma trận đơn vị cấp n.
- Tạo bản sao của ma trận A.
- Tạo vector $perm = [0, 1, 2, \ldots, n-1]$.
  B2. Phân tích LU có pivoting:
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
        B3. Tách L và U:
- Tạo ma trận L với đường chéo chính bằng 1 và phần dưới đường chéo lấy từ A.
- Tạo ma trận U với phần trên đường chéo và đường chéo chính lấy từ A.
  B4. Giải hệ phương trình $AX = B$:
- Hoán vị vector B theo $perm$: $B' \leftarrow B[perm]$.
- Giải hệ tam giác dưới $LY = B'$:
  - Với mỗi $i \leftarrow 0$ đến $n-1$: $Y[i] \leftarrow B'[i] - \sum_{k=0}^{i-1} L[i,k] \cdot Y[k]$.
- Giải hệ tam giác trên $UX = Y$:
  - Với mỗi $i \leftarrow n-1$ xuống $0$: $X[i] \leftarrow (Y[i] - \sum_{k=i+1}^{n-1} U[i,k] \cdot X[k]) / U[i,i]$.
    B5. Trả về: L, U, P, perm, X.

Câu 29. Viết thuật toán tìm phân tích Choleski của ma trận A. Áp dụng cho trường hợp cụ thể với ma trận A cấp 8.

Input:

- Ma trận vuông $A \in Mat(n, n)$
  Output:
- Ma trận tam giác dưới L sao cho $A = L L^T$
  Thuật toán:
  B1. Khởi tạo:
- Tạo ma trận sao chép $L \leftarrow A$
  B2. Tính các phần tử của L:
- Với $i \leftarrow 0$ đến $n-1$:
  - Gán: $temp \leftarrow L[i,i] - \sum_{k=0}^{i-1} L[i,k]^2$
  - Nếu $temp < 0$ thì báo lỗi "Ma trận không dương xác định".
  - Tính phần tử đường chéo: $L[i,i] = \sqrt{temp}$
  - Tính các phần tử dưới đường chéo:
    với mỗi $j \leftarrow i+1$ đến $n-1$: $L[j,i] \leftarrow \frac{1}{L[i,i]} \left( L[j,i] - \sum_{k=0}^{i-1} L[j,k] L[i,k] \right)$
- Xóa các phần tử trên: với mỗi $j \leftarrow i+1$ đến $n-1$: $L[i,j] \leftarrow 0$
  B3. Trả về: Ma trận L.

## 2 TUẦN 9.

Câu 31. Viết thuật toán cho phương pháp lặp đơn giải hệ phương trình $X = BX + d$ với sai số $\varepsilon$ cho trước.

Input:

- Ma trận $B \in Mat(n, n)$, vector tự do $d_n$.
- Sai số $\varepsilon > 0$ cho trước.
- Số lần lặp tối đa N.
  Output: Nghiệm $X = (x_1, x_2, \ldots, x_n)^T$ với số lần lặp k với sai số không quá $\varepsilon$ hoặc thông báo thất bại.
  B1: Gán $q = \|B\|_{(p)} \quad (p = \infty, 1, 2)$
  B2. Kiểm tra điều kiện hội tụ: $q < 1$, nếu không thỏa mãn thì thông báo "Điều kiện hội tụ không thỏa mãn, phương pháp có thể không hội tụ" và dừng chương trình.
  B3. Khởi tạo: $k = 0$, $X^{(0)} = 0_n$
  B4. Trong khi $k < N$, lặp:
- Tính dựa trên công thức lặp: $X^{(k+1)} = B X^{(k)} + d$
- Kiểm tra điều kiện dừng: $\frac{q}{1-q} \| X^{(k+1)} - X^{(k)} \| < \varepsilon$. Nếu thỏa mãn thì trả về nghiệm gần đúng $X = X^{(k+1)}$ với số lần lặp $k+1$ và dừng chương trình.
- Cập nhật cho vòng lặp sau: $k = k+1, X^{(k)} = X^{(k+1)}$.
  B5. Thông báo "Thất bại: Không tìm được nghiệm sau N lần lặp với sai số cho trước." và dừng chương trình.

Câu 33. Nền kinh tế gồm 10 ngành chính (1) bất động sản, (2) máy móc công nghiệp, (3) khai khoáng, (4) nông nghiệp, (5) thủy sản, (6) may mặc, (7) năng lượng, (8) dịch vụ, (9) giải trí, (10) đồ gia dụng. Ma trận tiêu thụ nội bộ (thể hiện lượng sản phẩm cần thiết để sản xuất một đơn vị sản phẩm) và vector nhu cầu bên ngoài (mức nhu cầu tiêu thụ sản phẩm ngoài thị trường của 10 ngành trên) cho trong file GK20222 kèm với pass mở là 20svxk222. Tính lượng sản phẩm cần sản xuất để đáp ứng nhu cầu trên (đơn vị tính theo triệu đô la). Cần nêu rõ phương pháp, thuật toán bạn dùng để tìm kiếm. (Cần ghi lại một số kết quả trung gian mà bạn nghĩ là cần thiết đối với phương pháp đã lựa chọn).

Ta có ma trận tiêu thụ nội bộ A:
$A = \begin{bmatrix}
0.05953 & 0.03186 & 0.09466 & 0.09514 & 0.03478 & 0.04700 & 0.01516 & 0.09841 & 0.01701 & 0.03281 \\
0.06035 & 0.07194 & 0.09583 & 0.08516 & 0.00064 & 0.05308 & 0.08699 & 0.06794 & 0.04468 & 0.06082 \\
0.07307 & 0.08444 & 0.06385 & 0.07472 & 0.04107 & 0.08514 & 0.07277 & 0.09001 & 0.07051 & 0.03364 \\
0.07984 & 0.04551 & 0.05665 & 0.04349 & 0.05256 & 0.01644 & 0.08910 & 0.01881 & 0.00140 & 0.06476 \\
0.05603 & 0.00980 & 0.07562 & 0.04857 & 0.01058 & 0.03132 & 0.06842 & 0.04374 & 0.00275 & 0.09992 \\
0.05876 & 0.05356 & 0.01616 & 0.01209 & 0.00999 & 0.07356 & 0.02366 & 0.05048 & 0.08056 & 0.02100 \\
0.07454 & 0.08970 & 0.03872 & 0.03786 & 0.03373 & 0.00599 & 0.08687 & 0.04372 & 0.05682 & 0.06200 \\
0.07909 & 0.03647 & 0.09861 & 0.04025 & 0.03746 & 0.00255 & 0.04359 & 0.06612 & 0.04205 & 0.02439 \\
0.02533 & 0.09595 & 0.00065 & 0.04671 & 0.03464 & 0.04578 & 0.07115 & 0.04019 & 0.04568 & 0.01673 \\
0.00902 & 0.09266 & 0.09269 & 0.07965 & 0.05633 & 0.00469 & 0.00403 & 0.07378 & 0.06584 & 0.06873
\end{bmatrix}$

và vector nhu cầu bên ngoài b:
$b = \begin{bmatrix}
29852 \\ 5035 \\ 15243 \\ 4198 \\ 25630 \\ 24127 \\ 18750 \\ 32496 \\ 19828 \\ 9846
\end{bmatrix}$

Gọi $X = (x_1, x_2, \ldots, x_{10})$ là vector lượng sản phẩm cần sản xuất với $x_i$ là lượng sản phẩm của ngành i.
Khi đó, ta có: $X = AX + b$.

Ta chọn phương pháp lặp đơn để giải quyết bài toán. Vì $\|A\|_1 = 0.63344 < 1$ nên thỏa mãn điều kiện hội tụ của phương pháp.
Chọn nghiệm xấp xỉ đầu $X_0 = b$.
Thiết lập điều kiện dừng:
$\| X_n - X^* \| \le \frac{\|A\|_1}{1 - \|A\|_1} \| X_n - X_{n-1} \| \le 10$
(tức là sai lệch của mỗi ngành không vượt quá 10 triệu đô)
$\Leftrightarrow \| X_n - X_{n-1} \| \le \frac{10(1 - \|A\|_1)}{\|A\|_1} = \varepsilon_0 = 5.78681$
Ta có kết quả:

|                       | Lần 1       | Lần 2       | ... | Lần 12                     | Lần 13                    |
| --------------------- | ----------- | ----------- | --- | -------------------------- | ------------------------- |
| $x_1$                 | 39799.68806 | 44871.49663 | ... | 50376.11660                | 50380.39349               |
| $x_2$                 | 15637.67833 | 21681.33630 | ... | 28369.72876                | 28374.93802               |
| $x_3$                 | 28255.96461 | 34657.46911 | ... | 41683.90004                | 41689.36791               |
| $x_4$                 | 12547.63510 | 17040.49894 | ... | 22109.72352                | 22113.67491               |
| $x_5$                 | 33477.93548 | 37784.12861 | ... | 42600.26083                | 42604.01448               |
| $x_6$                 | 32372.72500 | 35970.25709 | ... | 39887.49629                | 39890.54069               |
| $x_7$                 | 28099.85943 | 33124.66737 | ... | 38846.11167                | 38850.57284               |
| $x_8$                 | 41774.18587 | 46410.73298 | ... | 51501.69144                | 51505.64900               |
| $x_9$                 | 26976.15656 | 30800.05633 | ... | 35114.38847                | 35117.75413               |
| $x_{10}$              | 18341.25452 | 23542.13158 | ... | 29426.79022                | 29431.37612               |
| $\| x_k - x_{k-1} \|$ | 13012.96461 | 6401.50450  | ... | 10.38184 > $\varepsilon_0$ | 5.46788 < $\varepsilon_0$ |

Nghiệm xấp xỉ sau 13 lần lặp:
$X \approx \begin{bmatrix}
50380.3934920956 \\
28374.9380200000 \\
41689.3679142336 \\
22113.6749107140 \\
42604.0144815773 \\
39890.5406886077 \\
38850.5728387585 \\
51505.6490047878 \\
35117.7541341151 \\
29431.3761150430
\end{bmatrix}$

Câu 34. Nền kinh tế gồm 7 ngành chính (1) bất động sản, (2) sản xuất máy móc công nghiệp, (3) khai khoáng, (4) nông nghiệp, (5) năng lượng, (6) dịch vụ, (7) giải trí có ma trận tiêu thụ nội bộ (thể hiện lượng sản phẩm cần thiết để sản xuất một đơn vị sản phẩm) và vector nhu cầu bên ngoài (mức nhu cầu tiêu thụ của các ngành ngoài 7 ngành trên) là:

$C = \begin{bmatrix}
0.1588 & 0.0064 & 0.0025 & 0.0304 & 0.0014 & 0.0083 & 0.1594 \\
0.0057 & 0.2645 & 0.0436 & 0.0099 & 0.0083 & 0.0201 & 0.3413 \\
0.0264 & 0.1506 & 0.3557 & 0.0139 & 0.0142 & 0.0070 & 0.0236 \\
0.3299 & 0.0565 & 0.0495 & 0.3636 & 0.0204 & 0.0483 & 0.0649 \\
0.0089 & 0.0081 & 0.0333 & 0.0295 & 0.3412 & 0.0237 & 0.0020 \\
0.1190 & 0.0901 & 0.0996 & 0.1260 & 0.1722 & 0.2368 & 0.3360 \\
0.0063 & 0.0126 & 0.0196 & 0.0098 & 0.0064 & 0.0132 & 0.0012
\end{bmatrix}, \quad d = \begin{bmatrix}
74000 \\ 56000 \\ 10500 \\ 25000 \\ 17500 \\ 196000 \\ 5000
\end{bmatrix}$

(đơn vị tính theo triệu đô). Tính lượng sản phẩm cần sản xuất để đáp ứng nhu cầu trên. Cần nêu rõ phương pháp, thuật toán bạn dùng để tìm kiếm. (Nếu dùng một phương pháp lặp để giải thì cần ghi rõ số lần lặp, xấp xỉ đầu và 3 xấp xỉ cuối, nếu dùng một phương pháp tính đúng, cần ghi lại một số kết quả trung gian mà bạn nghĩ là quan trọng nhất trong phương pháp.)

Gọi $X = (x_1, x_2, \ldots, x_7)$ là vector lượng sản phẩm cần sản xuất với $x_i$ là lượng sản phẩm của ngành i. Khi đó, ta có: $X = CX + d$.
Chọn phương pháp lặp đơn vì $\|C\|_1 = 0.9293 < 1$ thỏa mãn điều kiện hội tụ của phương pháp.
Chọn $X_0 = d$.
Thiết lập điều kiện dừng:
$\| X_n - X^* \|_\infty \le \frac{\|C\|_1}{1 - \|C\|_1} \| X_n - X_{n-1} \|_\infty \le 10$
(tức là sai lệch của mỗi ngành không vượt quá 10 triệu đô)
$\Leftrightarrow \| X_n - X_{n-1} \|_\infty \le \frac{10(1 - \|C\|_1)}{\|C\|_1} = \varepsilon_0 \approx 0.7608$
Ta có kết quả:

|                              | Lần 1        | Lần 2        | ... | Lần 18                    | Lần 19                    |
| ---------------------------- | ------------ | ------------ | --- | ------------------------- | ------------------------- |
| $x_1$                        | 89344.15000  | 94681.18954  | ... | 99575.50254               | 99575.57423               |
| $x_2$                        | 77730.45000  | 87714.50972  | ... | 97702.70142               | 97702.85416               |
| $x_3$                        |              |              | ... | 51230.04237               | 51230.27082               |
| $x_4$                        |              |              | ... | 131568.94179              | 131569.40757              |
| $x_5$                        |              |              | ... | 49488.08316               | 49488.27714               |
| $x_6$                        | 265158.20000 | 296563.81237 | ... | 329553.35874              | 329553.87853              |
| $x_7$                        | 9327.80000   | 11479.99429  | ... | 13835.25726               | 13835.29454               |
| $\| x_k - x_{k-1} \|_\infty$ | 69158.20000  | 31405.61237  | ... | 0.99045 > $\varepsilon_0$ | 0.51979 < $\varepsilon_0$ |

Nghiệm xấp xỉ sau 19 lần lặp:
$X \approx \begin{bmatrix}
99575.6 \\ 97702.9 \\ 51230.3 \\ 131569.4 \\ 49488.3 \\ 329553.9 \\ 13835.3
\end{bmatrix}$

## 3 TUẦN 10.

Câu 37. Viết thuật toán cho phương pháp lặp Gauss-Seidel giải hệ phương trình $AX = B$ với sai số $\varepsilon$ cho trước.

Để bảo rằng giải hệ $AX = B$, tuy nhiên thuật toán áp dụng cho hệ $AX = b$, vì đánh giá chuẩn ma trận phức tạp hơn. Đề thi cũng chỉ là cột vector b.
Input:

- Ma trận $A_{n \times n}$, ma trận $B_{n \times m}$.
- Sai số $\varepsilon$ cho trước.
  Output:
- Nghiệm X của hệ $AX = b$ với sai số không quá $\varepsilon$
  Thuật toán:
  B1. Xác định ma trận A chéo trội:
- Với $\sum_{j \neq i} |a_{ij}| < |a_{ii}| \forall i$: A chéo trội hàng. Gán $s = 0, \quad q = \max_{i=\overline{1,n}} \frac{\sum_{j<i} |a_{ij}|}{|a_{ii}| - \sum_{j>i} |a_{ij}|}$
- Với $\sum_{i \neq j} |a_{ij}| < |a_{jj}| \forall j$: A chéo trội cột. Gán $s = \max_{j=\overline{1,n}} \frac{1}{|a_{jj}|} \sum_{i>j} |a_{ij}|, \quad q = \max_{j=\overline{1,n}} \frac{\sum_{i<j} |a_{ij}|}{|a_{jj}| - \sum_{i>j} |a_{ij}|}$
- Nếu không thỏa mãn, cảnh báo phương pháp có thể không hội tụ.
  B2. Khởi tạo: $k = 0$, $X^{(0)} = 0_n$
  B3. Lặp:
- Với mỗi cột $1, 2, \ldots, m$ của ma trận B, tính dựa trên công thức lặp:
  $x_{i,t}^{(k+1)} = \frac{1}{a_{ii}} \left( b_{i,t} - \sum_{j=1}^{i-1} a_{ij} x_{j,t}^{(k+1)} - \sum_{j=i+1}^n a_{ij} x_{j,t}^{(k)} \right), \quad i = \overline{1, n}$
- Kiểm tra điều kiện dừng:
  $\frac{q}{(1-s)(1-q)} \| X_k - X_{k-1} \| < \varepsilon.$
  Nếu thỏa mãn thì dừng lặp.
- Ngược lại, gán $k = k+1$ và tiếp tục vòng lặp
  B4. Trả về kết quả nghiệm gần đúng $X^{(k+1)}$ cùng sai số không quá $\varepsilon$.

Câu 38. Dùng phương pháp lặp Gauss-Seidel tìm nghiệm gần đúng của phương trình $(A + a I)x = b$ với sai số tuyệt đối không vượt quá $10^{-5}$ biết $a$ là số thứ tự theo danh sách thi của bạn; $I$ là ma trận đơn vị cùng cấp với $A$, ma trận $A$, vector $b$ cho trong file GK20222 với pass mở file là gts2023gts.

Thực hiện thuật toán theo phương pháp đã chọn để tìm nghiệm theo yêu cầu. Đánh giá sai số tương đối cho nghiệm tìm được.

Ma trận A:
$A = \begin{bmatrix}
130.75 & 3.75 & 5.25 & 11.25 & 18.25 & 6.5 & 12 & 15.5 & 2.75 & 20 \\
-7 & 156 & 4 & 8 & 17.6667 & -3.6667 & -3 & 4 & 9 & 21.6667 \\
2.8 & 4.2 & 89 & 5.4 & 10.8 & 12.6 & -7.8 & 8 & 14.8 & 13 \\
16.5714 & 14.8571 & 25.4286 & 140.4286 & 25.7143 & 2.1429 & 5.5714 & 10.5714 & 5.4286 & 6.4286 \\
6.1667 & -19 & 9.8333 & 12.1667 & 114 & -6.1667 & 14.5 & 3.6667 & -10.5 & -14.1667 \\
-0.875 & 11.125 & 7.125 & 6.375 & 13.375 & 81.75 & -6 & 1.875 & -15.75 & -8.75 \\
-7.5714 & -1.4286 & 5.2857 & 9.8571 & -18 & 7.1429 & 96.8571 & -10.1429 & -8.8571 & -12.8571 \\
17.2 & 11 & 15.6 & 2.8 & 2.2 & 14.2 & 15.6 & 106.8 & 5.2 & 6.4 \\
15.8333 & 4.8333 & -5.8333 & 5.5 & -9.6667 & 7.6667 & 5.6667 & 9.5 & 81.1667 & -3 \\
0.9167 & -2 & -2.5833 & 2.9167 & 3.9167 & 10.6667 & 2.1667 & 9.5833 & -3.5833 & 52.0833
\end{bmatrix}$

Vector cột b:
$b = \begin{bmatrix}
310.2275 \\
-193.5166 \\
238.112 \\
-165.0229 \\
214.4215 \\
108.6325 \\
28.8543 \\
291.732 \\
-256.5717 \\
197.1857
\end{bmatrix}$

Với a = 7, đặt $C = A + 7I$, ta có:
$C = \begin{bmatrix}
137.75 & 3.75 & 5.25 & 11.25 & 18.25 & 6.5 & 12 & 15.5 & 2.75 & 20 \\
-7 & 163 & 4 & 8 & 17.6667 & -3.6667 & -3 & 4 & 9 & 21.6667 \\
2.8 & 4.2 & 96 & 5.4 & 10.8 & 12.6 & -7.8 & 8 & 14.8 & 13 \\
16.5714 & 14.8571 & 25.4286 & 147.4286 & 25.7143 & 2.1429 & 5.5714 & 10.5714 & 5.4286 & 6.4286 \\
6.1667 & -19 & 9.8333 & 12.1667 & 121 & -6.1667 & 14.5 & 3.6667 & -10.5 & -14.1667 \\
-0.875 & 11.125 & 7.125 & 6.375 & 13.375 & 88.75 & -6 & 1.875 & -15.75 & -8.75 \\
-7.5714 & -1.4286 & 5.2857 & 9.8571 & -18 & 7.1429 & 103.8571 & -10.1429 & -8.8571 & -12.8571 \\
17.2 & 11 & 15.6 & 2.8 & 2.2 & 14.2 & 15.6 & 113.8 & 5.2 & 6.4 \\
15.8333 & 4.8333 & -5.8333 & 5.5 & -9.6667 & 7.6667 & 5.6667 & 9.5 & 88.1667 & -3 \\
0.9167 & -2 & -2.5833 & 2.9167 & 3.9167 & 10.6667 & 2.1667 & 9.5833 & -3.5833 & 59.0833
\end{bmatrix}$

Kiểm tra điều kiện hội tụ: Ma trận C chéo trội hàng, phương pháp hội tụ.
Khởi tạo: $s = 0, q \approx 0.7690802, k = 0, X^{(0)} = 0_n$.
Thiết lập điều kiện dừng:
$\frac{q}{(1-s)(1-q)} \| X_n - X_{n-1} \|_\infty < 10^{-5}.$
$\Leftrightarrow \| X_n - X_{n-1} \|_\infty \le \frac{10^{-5}(1-s)(1-q)}{q} = \varepsilon_0 \approx 3.002545 \times 10^{-6}$
Ta có kết quả:

|                       | Lần 1         | Lần 2         | ... | Lần 7                          | Lần 8                                         |
| --------------------- | ------------- | ------------- | --- | ------------------------------ | --------------------------------------------- |
| $x_1$                 | 2.2521052632  | 1.5022425660  | ... | 1.5077743699                   | 1.5077740324                                  |
| $x_2$                 | -1.0905022280 | -1.4449911006 | ... | -1.4413161861                  | -1.4413160997                                 |
| $x_3$                 | 2.4623564023  | 2.3178282080  | ... | 2.3290766524                   | 2.3290771055                                  |
| $x_4$                 | -1.6872982075 | -1.9637621784 | ... | -1.9876844392                  | -1.9876844687                                 |
| $x_5$                 | 1.4556170416  | 1.4402349373  | ... | 1.4221591608                   | 1.4221588468                                  |
| $x_6$                 | 1.0870793033  | 0.8659472790  | ... | 0.9266486934                   | 0.9266486278                                  |
| $x_7$                 | 0.6393476828  | 0.8601792739  | ... | 0.8913604413                   | 0.8913599740                                  |
| $x_8$                 | 1.7811096805  | 1.9474841956  | ... | 1.9219623652                   | 1.9219624857                                  |
| $x_9$                 | -3.1545046057 | -2.9167882009 | ... | -2.9215157656                  | -2.9215156958                                 |
| $x_{10}$              | 2.6601096279  | 2.6873480643  | ... | 2.6820082729                   | 2.6820083359                                  |
| $\| x_k - x_{k-1} \|$ | 3.1545046057  | 0.7498626972  | ... | $0.0000073397 > \varepsilon_0$ | $4.6725716296 \times 10^{-7} < \varepsilon_0$ |

Nghiệm xấp xỉ sau 8 lần lặp:
$x \approx \begin{bmatrix}
1.50777403 \\
-1.4413161 \\
2.32907711 \\
-1.98768447 \\
1.42215885 \\
0.92664863 \\
0.89135997 \\
1.92196249 \\
-2.9215157 \\
2.68200834
\end{bmatrix}$

Sai số tương đối cho nghiệm tìm được:
$\frac{\| X_8 - X^* \|_\infty}{\| X_8 \|_\infty} \le \frac{q}{(1-s)(1-q)} \cdot \frac{\| X_8 - X_7 \|_\infty}{\| X_8 \|_\infty} \approx 5.32670 \times 10^{-7}.$

## 4 TUẦN 11+12

Câu 40. Viết thuật toán cho phương pháp phân tích Choleski tìm ma trận nghịch đảo của ma trận vuông A. Áp dụng cho một ma trận vuông cấp 5.

Thuật toán (Giải hệ phương trình bằng Cholesky):
Input:

- Ma trận vuông $A \in Mat(n, n)$.
  Output:
- Ma trận nghịch đảo $A^{-1}$ (nếu A thỏa mãn điều kiện).
  B1. Kiểm tra ma trận A:
- Kiểm tra xem A có đối xứng không (tức là $A = A^T$).
- Nếu A không đối xứng, báo lỗi: "Ma trận A không đối xứng. Không thể áp dụng trực tiếp phương pháp Cholesky." và dừng thuật toán.
  B2. Phân tách Cholesky $A = L L^T$:
- Khởi tạo ma trận L kích thước $n \times n$ với tất cả các phần tử bằng 0.
- Với $i \leftarrow 0$ đến $n-1$:
  - Gán: $temp \leftarrow A[i,i] - \sum_{k=0}^{i-1} L[i,k]^2$
  - Nếu $temp < 0$ thì báo lỗi "Ma trận A không dương xác định. Không thể phân tách Cholesky". và dừng thuật toán.
  - Tính đường chéo: $L[i,i] \leftarrow \sqrt{temp}$
  - Tính các phần tử dưới đường chéo:
    với mỗi $j \leftarrow i+1$ đến $n-1$: $L[j,i] \leftarrow \frac{1}{L[i,i]} \left( A[j,i] - \sum_{k=0}^{i-1} L[j,k] L[i,k] \right)$
    B3. Tính các cột của ma trận nghịch đảo $A_{inv}$
- Khởi tạo ma trận $A_{inv} \in Mat(n,n)$.
- Khởi tạo vector cột tạm thời $y_{col}$ kích thước $n \times 1$.
- Với $j \leftarrow 0$ đến $n-1$:
  - Với $i \leftarrow 0$ đến $n-1$:
    $y_{col}[i] \leftarrow \frac{1}{L[i,i]} \left( \delta_{ij} - \sum_{k=0}^{i-1} L[i,k] y_{col}[k] \right)$
  - Với $i \leftarrow n-1$ xuống $0$:
    $A_{inv}[i,j] \leftarrow \frac{1}{L[i,i]} \left( y_{col}[i] - \sum_{k=i+1}^{n-1} L[k,i] A_{inv}[k,j] \right)$
    B4. Trả về: Ma trận $A_{inv}$.
    Áp dụng cho ma trận vuông cấp 5:

Câu 42. Viết thuật toán tìm ma trận nghịch đảo của ma trận A bằng phương pháp lặp Jacobi/lặp Gauss-Seidel với sai số tuyệt đối/sai số tương đối cho trước. Áp dụng với ma trận cấp 8 ở câu 39 và so sánh.

Phương pháp lặp Jacobi
Input:

- Ma trận vuông $A_{n \times n}$.
- Sai số cho trước $\varepsilon$.
- Số lần lặp tối đa cho phép N.
  Output:
- Ma trận nghịch đảo $A^{-1}$.
  Thuật toán:
  B1. Khởi tạo:
- Xây dựng ma trận đơn vị $I_{n \times n}$.
- Khởi tạo ma trận kết quả $X \leftarrow 0_{n \times n}$.
  B2. Kiểm tra tính chéo trội và tính hệ số:
- Nếu A chéo trội hàng: Gán $p = \infty$ và
  $\lambda = 1, \quad q = \max_{1 \le i \le n} \left( \frac{1}{|a_{ii}|} \sum_{j \neq i} |a_{ij}| \right)$
- Nếu A chéo trội cột: Gán $p = 1$ và
  $\lambda = \frac{\max_{1 \le i \le n} |a_{ii}|}{\min_{1 \le i \le n} |a_{ii}|}, \quad q = \max_{1 \le j \le n} \left( \frac{1}{|a_{jj}|} \sum_{i \neq j} |a_{ij}| \right)$
- Nếu không, dừng thuật toán.
  B3. Lặp:
  Cho $t$ chạy từ $1$ đến $n$ (tương ứng với mỗi cột của $I$ và $X$):
- Khởi tạo vector lặp $x_{old} \leftarrow 0_{n \times 1}$.
- Cho $k$ chạy từ $1$ đến $N$:
  - Tính vector lặp mới $x_{new}$:
    $(x_{new})_i = \frac{1}{a_{ii}} \left( (e_t)_i - \sum_{j \neq i} a_{ij} (x_{old})_j \right), \quad i = \overline{1, n}$
  - Kiểm tra điều kiện dừng: Nếu $\| x_{new} - x_{old} \|_p < \frac{\varepsilon(1-q)}{\lambda q}$, thoát vòng lặp k.
  - Gán $x_{old} \leftarrow x_{new}$.
- Gán cột thứ t của ma trận X bằng $x_{new}$.
  B4. Trả về kết quả: Trả về ma trận X là ma trận $A^{-1}$.

Phương pháp lặp Gauss-Seidel
Input:

- Ma trận vuông $A_{n \times n}$.
- Sai số cho trước $\varepsilon$.
- Số lần lặp tối đa cho phép N.
  Output:
- Ma trận nghịch đảo $A^{-1}$.
  Thuật toán:
  B1. Khởi tạo:
- Xây dựng ma trận đơn vị $I_{n \times n}$.
- Khởi tạo ma trận kết quả $X \leftarrow 0_{n \times n}$.
  B2. Xác định ma trận chéo trội và tính hệ số:
- Nếu A chéo trội hàng: Gán $s = 0, \quad q = \max_{i=\overline{1,n}} \frac{\sum_{j<i} |a_{ij}|}{|a_{ii}| - \sum_{j>i} |a_{ij}|}$
- Nếu A chéo trội cột: Gán $s = \max_{j=\overline{1,n}} \frac{1}{|a_{jj}|} \sum_{i>j} |a_{ij}|, \quad q = \max_{j=\overline{1,n}} \frac{\sum_{i<j} |a_{ij}|}{|a_{jj}| - \sum_{i>j} |a_{ij}|}$
- Nếu không, dừng thuật toán.
  B3. Lặp:
  Cho $t$ chạy từ $1$ đến $n$ (tương ứng với mỗi cột của $I$ và $X$):
- Khởi tạo vector lặp $x_{old} \leftarrow 0_{n \times 1}$.
- Cho $k$ chạy từ $1$ đến $N$:
  - Tạo một bản sao $x_{new} \leftarrow x_{old}$.
  - Tính vector lặp mới:
    $(x_{new})_i = \frac{1}{a_{ii}} \left( (e_t)_i - \sum_{j=1}^{i-1} a_{ij} (x_{new})_j - \sum_{j=i+1}^n a_{ij} (x_{old})_j \right), \quad i = \overline{1, n}$
  - Kiểm tra điều kiện dừng: Nếu $\frac{q}{(1-s)(1-q)} \| x_{new} - x_{old} \|_\infty < \varepsilon$, thoát vòng lặp k.
  - Gán $x_{old} \leftarrow x_{new}$.
- Gán cột thứ t của ma trận X bằng $x_{new}$.
  B4. Trả về kết quả: Trả về ma trận X là ma trận $A^{-1}$.

## 5 TUẦN 13+14

Câu 43. Viết thuật toán tìm đa thức đặc trưng của ma trận A bằng phương pháp Danielevski. Áp dụng với một ma trận cấp 5.

Input:

- Ma trận vuông $A_{n \times n}$.
  Output:
- Một danh sách các đa thức đặc trưng $P_1(\lambda), P_2(\lambda), \ldots$ của các khối Frobenius. Đa thức đặc trưng của A là tích của chúng.
  Các bước:
  B1. Khởi tạo:
- Gán ma trận làm việc $P \leftarrow A$.
- Khởi tạo danh sách đa thức kết quả: $list\_poly$.
- Gán $m \leftarrow n$ với n là kích thước của khối ma trận đang xét.
  B2. Lặp: Lặp $k$ từ $m$ xuống $2$:
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
        3. Cập nhật kích thước bài toán: $m \leftarrow k - 1$.
        4. Thu nhỏ ma trận P: P được gán bằng ma trận con của P bao gồm các hàng và cột từ chỉ số $1$ đến $m$.
        5. Gán $k \leftarrow m + 1$ để vòng lặp bắt đầu lại.
           B3. Xử lý khối cuối cùng:
- Sau khi vòng lặp kết thúc, P là khối Frobenius cuối cùng (hoặc một ma trận con $1 \times 1$). Trích xuất đa thức đặc trưng của nó và thêm vào $list\_poly$.
  B4. Trả về kết quả: Trả về danh sách $list\_poly$.

Các thuật toán phụ

Thuật toán phụ M (Xây dựng ma trận biến đổi):

- Input: Hàng $k$, ma trận P.
- Output: $M_k, M_k^{-1}$.
- Các bước:
  B1. Tạo $M_k$ là ma trận đơn vị, sau đó thay thế hàng $k-1$ của $M_k$ bằng hàng $k$ của P.
  B2. Tạo $M_k^{-1}$ là ma trận đơn vị, sau đó thay thế hàng $k-1$ của $M_k^{-1}$ với các phần tử $(M_k^{-1})_{k-1, j} \leftarrow -p_{k, j} / p_{k, k-1}$ (với $j \neq k-1$) và $(M_k^{-1})_{k-1, k-1} \leftarrow 1 / p_{k, k-1}$.

Thuật toán phụ C (Xây dựng ma trận hoán vị):

- Input: Các chỉ số cột $j$ và $k-1$.
- Output: Ma trận C.
- Các bước: Tạo ma trận đơn vị, sau đó hoán vị cột $j$ và cột $k-1$. ($C = C^{-1}$).

Thuật toán phụ S (Xây dựng ma trận khử khối $S_q$):

- Input: Ma trận P đang khối, cột 'q' của khối B.
- Output: $S_q, S_q^{-1}$.
- Các bước: Xây dựng ma trận $S_q$ là ma trận đơn vị với một khối con ngoài đường chéo được điền các giá trị lấy từ cột 'q' của B (với dấu ngược lại) để khi nhân ma trận sẽ triệt tiêu được cột 'q' đó.

Câu 46. Viết thuật toán cho phương pháp xuống thang tìm giá trị riêng trội thứ hai.
Input:

- Ma trận vuông $A_{n \times n}$.
- Giá trị riêng trội nhất đã biết $\lambda_1$.
- Vector riêng phải tương ứng $v_1$ (đã chuẩn hóa: $\|v_1\|_2 = 1$).
- Các tham số cho phương pháp lũy thừa con: Vector ban đầu $X^{(0)}$, sai số $\varepsilon$, số lặp tối đa $k_{max}$.
  Output:
- Giá trị riêng trội thứ hai $\lambda_2$.
- Vector riêng tương ứng $v_2$.
  Thuật toán:
  B1. Xây dựng ma trận xuống thang:
- Chuẩn hóa vector riêng: $v_1 \leftarrow \frac{v_1}{\|v_1\|}$
- Chọn vector phụ x: Chọn một vector x sao cho $x \leftarrow \frac{v_1}{v_1^T v_1}$
- Tính ma trận xuống thang B:
  $B \leftarrow A - \lambda_1 v_1 x^T$
  B2. Tìm trị riêng trội của ma trận B:
- Áp dụng thuật toán phương pháp lũy thừa cho ma trận B với vector ban đầu $X^{(0)}$.
- Kết quả thu được:
  - Trị riêng trội của B, chính là trị riêng trội thứ hai của A: $\lambda_2$.
  - Vector riêng tương ứng thu được là vector riêng $u_2$ của ma trận B
    B3. Tìm vector riêng của A:
- Sử dụng công thức biến đổi ngược để tìm vector riêng $v_2$ của A từ $u_2$:
  $v_2 \leftarrow (\lambda_2 - \lambda_1) u_2 + \lambda_1 (x^T u_2) v_1$
- Chuẩn hóa vector riêng kết quả: $v_2 \leftarrow \frac{v_2}{\|v_2\|_2}$
  B4. Trả về kết quả:
- Trả về trị riêng trội thứ hai cùng vector riêng tương ứng $(\lambda_2, v_2)$ đã tìm được.

## 6 TUẦN 15+16

Câu 48. Viết thuật toán tìm giá trị kỳ dị lớn nhất của ma trận A. Áp dụng cho một ma trận cấp 5.
Input:

- Ma trận $A_{m \times n}$.
- Các tham số cho phương pháp lũy thừa: Vector ban đầu $X^{(0)}$, sai số $r$, số lặp tối đa $k_{max}$.
  Output:
- Giá trị kỳ dị lớn nhất $\sigma_1$.
- Thông báo về sự hội tụ.
  Thuật toán:
  B1. Khởi tạo:
- Xây dựng ma trận đối xứng: $B \leftarrow A^T A$.
- Gán $k \leftarrow 0$.
- Chuẩn hóa vector ban đầu theo chuẩn 2: $v \leftarrow \frac{X^{(0)}}{\|X^{(0)}\|_2}$
  B2. Tìm trị riêng trội của B bằng Phương pháp Lũy thừa:
- Lặp: Lặp trong khi $k < k_{max}$:
  - Gán $v_{old} \leftarrow v$.
  - Tính vector mới: $Y \leftarrow B \cdot v_{old}$.
  - Ước lượng trị riêng bằng thương Rayleigh: $\lambda_1 \leftarrow v_{old}^T \cdot Y$.
  - Chuẩn hóa vector mới bằng chuẩn 2: $v \leftarrow \frac{Y}{\|Y\|_2}$.
  - Cập nhật $k \leftarrow k + 1$.
  - Kiểm tra hội tụ: Nếu $\|v - v_{old}\|_\infty < \varepsilon$, thoát vòng lặp.
    B3. Tính giá trị kỳ dị lớn nhất:
- Tính giá trị kỳ dị:
  $\sigma_1 \leftarrow \sqrt{\lambda_1}$
  B4. Trả về kết quả:
- Trả về giá trị $\sigma_1$ và thông báo về sự hội tụ.

Câu 50. Viết thuật toán tính số điều kiện của A. Áp dụng cho ma trận vuông cấp 5.
Input:

- Ma trận vuông $A_{n \times n}$.
  Output:
- Số điều kiện của ma trận A, $cond(A)$.
  Thuật toán:
  B1. Tìm tất cả các giá trị kỳ dị của A:
- Áp dụng thuật toán tìm khai triển kỳ dị (như ở ) để tìm ra danh sách tất cả các giá trị kỳ dị của ma trận A: $(\sigma_1, \sigma_2, \ldots, \sigma_n)$.
  B2. Xác định $\sigma_{max}$ và $\sigma_{min}$:
- Tìm giá trị kỳ dị lớn nhất: $\sigma_{max} \leftarrow \max(\sigma_1, \ldots, \sigma_n)$.
- Tìm giá trị kỳ dị nhỏ nhất: $\sigma_{min} \leftarrow \min(\sigma_1, \ldots, \sigma_n)$.
  B3. Tính số điều kiện:
- Nếu $\sigma_{min} = 0$, hiện thông báo "Ma trận A là ma trận suy biến và số điều kiện là vô cùng".
- Ngược lại, tính số điều kiện theo công thức:
  $cond(A) \leftarrow \frac{\sigma_{max}}{\sigma_{min}}$
  B4. Trả về kết quả:
- Trả về giá trị $cond(A)$.
