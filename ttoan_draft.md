

**Câu 27.** Viết thuật toán tìm phân tách LU cho ma trận $A$. Áp dụng cho ma trận vuông $A$ cấp 6 cụ thể.

**Input:**

- Ma trận vuông $A \in Mat(n,n)$

**Output:**

- Ma trận $A$ được phân rã chứa cả $L$ và $U$

**Thuật toán:**

- **B1. Khởi tạo:**
  
  - Tạo ma trận $B \leftarrow A$ (sao chép để cập nhật).

- **B2. Lặp:**
  
  - Với mỗi cột $k \leftarrow 0$ đến $n-2$:
    
    - Nếu $B[k,k] = 0$, báo lỗi "Ma trận suy biến, không thể phân rã LU."
    
    - Với mỗi hàng $i \leftarrow k+1$ đến $n-1$:
      
      - Tính hệ số $L[i,k]$: $B[i,k] \leftarrow \frac{B[i,k]}{B[k,k]}$
      
      - Cập nhật phần còn lại của hàng $i$:
        
        Với mỗi $j \leftarrow k+1$ đến $n-1$: $B[i,j] \leftarrow B[i,j] - B[i,k] \times B[k,j]$.

- **B3. Tách $L$ và $U$:**
  
  - Khởi tạo $L = I_n$, $U = 0_{n \times n}$.
  
  - Với mọi chỉ số $i, j = 0, \dots, n-1$:
    
    $L_{i,j} = \begin{cases} 1, & i = j, \\ B_{i,j}, & i > j, \\ 0, & i < j, \end{cases} \quad U_{i,j} = \begin{cases} B_{i,j}, & i \le j, \\ 0, & i > j. \end{cases}$

- **B4. Trả về:** Ma trận $L$, ma trận $U$.

Dưới đây là văn bản được chép lại nguyên văn từ phần hình ảnh bạn vừa gửi:

**Câu 28.** Viết thuật toán cho phương pháp phân tách LU giải phương trình $AX = B$. Áp dụng cho bài toán cụ thể cấp 7.

**Input:**

- Ma trận vuông $A \in \mathbb{R}^{n \times n}$.

- Vector vế phải $B \in \mathbb{R}^{n \times 1}$.

**Output:**

- Ma trận tam giác dưới $L$ với đường chéo chính bằng 1.

- Ma trận tam giác trên $U$.

- Ma trận hoán vị $P$.

- Vector hoán vị $perm$.

- Vector nghiệm $X \in \mathbb{R}^{n \times 1}$ của hệ $AX = B$.

**Thuật toán:**

- **B1. Khởi tạo:**
  
  - Tạo ma trận $P$ là ma trận đơn vị cấp $n$.
  
  - Tạo bản sao của ma trận $A$.
  
  - Tạo vector $perm = [0, 1, 2, \dots, n-1]$.

- **B2. Phân tách LU có pivoting:**
  
  - Với mỗi cột $k \leftarrow 0$ đến $n-2$:
    
    - Tìm chỉ số $p \leftarrow \arg\max_{k \le i \le n-1} |A[i, k]|$. $\quad \triangleright$ Chọn pivot lớn nhất trong cột $k$
    
    - Nếu $A[p, k] = 0$, báo lỗi: "Ma trận suy biến, không thể phân rã LU."
    
    - Nếu $p \neq k$, hoán đổi:
      
      - Hoán đổi hàng $k$ và $p$ trong $A$.
      - 
