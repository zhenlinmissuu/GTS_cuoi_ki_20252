import os
import json

def create_markdown_cell(source):
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": [line + "\n" for line in source.split('\n')]
    }

def create_code_cell(source):
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [line + "\n" for line in source.split('\n')]
    }

CODE_TEMPLATES = {
    "Chia đôi": """import math

def f(x):
    return x**3 - x - 1

def chia_doi(a, b, epsilon):
    print("="*60)
    print("PHƯƠNG PHÁP CHIA ĐÔI")
    print("="*60)
    
    # B1: Kiểm tra điều kiện
    fa = f(a)
    fb = f(b)
    print(f"Bước 1: Kiểm tra điều kiện")
    print(f"  f(a) = f({a}) = {fa:.5f}")
    print(f"  f(b) = f({b}) = {fb:.5f}")
    if fa * fb < 0:
        print("  => f(a)*f(b) < 0. Khoảng [a, b] chứa nghiệm.")
    else:
        print("  => f(a)*f(b) >= 0. Điều kiện không thỏa mãn!")
        return

    # B2: Đánh giá số bước lặp tiên nghiệm
    n_expected = math.ceil(math.log2((b - a) / epsilon)) - 1
    print(f"\\nBước 2: Sai số tiên nghiệm")
    print(f"  Để sai số (b-a)/2^n < {epsilon}, số bước lặp dự kiến n >= {n_expected}")
    
    # B3: Bảng lặp
    print(f"\\nBước 3: Lập bảng tính")
    print("-" * 75)
    print(f"{'n':<5} | {'a':<10} | {'b':<10} | {'c=(a+b)/2':<15} | {'f(c)':<10} | {'Sai số (b-a)/2':<15}")
    print("-" * 75)
    
    k = 1
    while True:
        c = (a + b) / 2
        fc = f(c)
        sai_so = (b - a) / 2
        
        print(f"{k:<5} | {a:<10.5f} | {b:<10.5f} | {c:<15.5f} | {fc:<10.5f} | {sai_so:<15.5f}")
        
        if sai_so < epsilon or fc == 0:
            print("-" * 75)
            print(f"\\nBước 4: Kết luận")
            print(f"  Thỏa mãn điều kiện sai số ở bước {k}.")
            print(f"  Nghiệm gần đúng: x ≈ {c:.5f}")
            print(f"  Sai số hậu nghiệm: Delta = {sai_so:.5f} < {epsilon}")
            break
            
        if fa * fc < 0:
            b = c
        else:
            a = c
            fa = fc
        k += 1

# Gọi hàm với khoảng [1, 2] và sai số 0.05
chia_doi(1, 2, 0.05)""",

    "Dây cung": """import math

def f(x):
    return x**3 - x - 1

def day_cung(a, b, d, epsilon, m1, M1):
    print("="*60)
    print("PHƯƠNG PHÁP DÂY CUNG")
    print("="*60)
    
    print("Bước 1: Kiểm tra điều kiện")
    print(f"  Khoảng cách ly nghiệm: [{a}, {b}]")
    print(f"  Điểm cố định d = {d} (yêu cầu f(d)*f''(d) > 0)")
    print(f"  m1 = min|f'(x)| = {m1}, M1 = max|f'(x)| = {M1}")
    
    x_k = b if d == a else a
    print(f"  Chọn x_0 = {x_k}")
    
    print(f"\\nBước 2: Lập bảng tính")
    print("-" * 65)
    print(f"{'k':<5} | {'x_k':<12} | {'f(x_k)':<12} | {'|x_k - x_{k-1}|':<15}")
    print("-" * 65)
    
    k = 0
    fd = f(d)
    x_prev = x_k
    
    while True:
        fx = f(x_k)
        if k > 0:
            diff = abs(x_k - x_prev)
            print(f"{k:<5} | {x_k:<12.5f} | {fx:<12.5f} | {diff:<15.5f}")
            sai_so_hau_nghiem = (M1 - m1) / m1 * diff
            
            if sai_so_hau_nghiem < epsilon or fx == 0:
                print("-" * 65)
                print(f"\\nBước 3: Kết luận")
                print(f"  Nghiệm gần đúng: x ≈ {x_k:.5f}")
                print(f"  Sai số hậu nghiệm: ((M1-m1)/m1)*|x_k - x_k-1| = {sai_so_hau_nghiem:.5f} < {epsilon}")
                break
        else:
            print(f"{k:<5} | {x_k:<12.5f} | {fx:<12.5f} | {'-':<15}")
            
        x_new = x_k - fx * (x_k - d) / (fx - fd)
        x_prev = x_k
        x_k = x_new
        k += 1

# m1 = 2 (tại x=1), M1 = 11 (tại x=2) cho f(x) = x^3 - x - 1
day_cung(a=1, b=2, d=1, epsilon=0.01, m1=2, M1=11)""",

    "Tiếp tuyến (Newton)": """import math

def f(x):
    return x**3 - x - 1

def df(x):
    return 3*x**2 - 1

def d2f(x):
    return 6*x

def newton(a, b, x0, epsilon, m1, M2):
    print("="*60)
    print("PHƯƠNG PHÁP TIẾP TUYẾN (NEWTON)")
    print("="*60)
    
    print("Bước 1: Kiểm tra điều kiện")
    print(f"  m1 = min|f'(x)| trên [{a}, {b}] = {m1}")
    print(f"  M2 = max|f''(x)| trên [{a}, {b}] = {M2}")
    
    fx0 = f(x0)
    d2fx0 = d2f(x0)
    print(f"  f(x0) = {fx0:.5f}, f''(x0) = {d2fx0:.5f}")
    if fx0 * d2fx0 > 0:
        print("  => Điều kiện Fourier f(x0)*f''(x0) > 0 được thỏa mãn.")
    else:
        print("  => Cảnh báo: Điều kiện Fourier không được thỏa mãn!")
        
    print(f"\\nBước 2: Lập bảng tính")
    print("-" * 65)
    print(f"{'k':<5} | {'x_k':<12} | {'f(x_k)':<12} | {'|x_k - x_{k-1}|':<15}")
    print("-" * 65)
    
    x_k = x0
    k = 0
    while True:
        fx = f(x_k)
        if k > 0:
            diff = abs(x_k - x_prev)
            print(f"{k:<5} | {x_k:<12.5f} | {fx:<12.5f} | {diff:<15.5f}")
            
            sai_so_hau_nghiem = (M2 / (2 * m1)) * (diff ** 2)
            if sai_so_hau_nghiem < epsilon:
                print("-" * 65)
                print(f"\\nBước 3: Kết luận")
                print(f"  Nghiệm gần đúng: x ≈ {x_k:.5f}")
                print(f"  Sai số hậu nghiệm: [M2/(2*m1)] * |x_k - x_k-1|^2 = {sai_so_hau_nghiem:.8f} < {epsilon}")
                break
        else:
            print(f"{k:<5} | {x_k:<12.5f} | {fx:<12.5f} | {'-':<15}")
            
        x_prev = x_k
        x_k = x_k - f(x_k) / df(x_k)
        k += 1

# m1 = 2 (tại x=1), M2 = 12 (tại x=2)
newton(a=1, b=2, x0=2, epsilon=0.001, m1=2, M2=12)""",

    "Lặp đơn (1 chiều)": """import math

def g(x):
    return (x + 1)**(1/3)

def lap_don(x0, q, epsilon):
    print("="*60)
    print("PHƯƠNG PHÁP LẶP ĐƠN (1 CHIỀU)")
    print("="*60)
    
    print("Bước 1: Kiểm tra hệ số co")
    print(f"  Ta có hệ số co q = {q}")
    if q < 1:
        print("  => q < 1, thỏa mãn điều kiện hội tụ.")
    else:
        print("  => q >= 1, phương pháp có thể không hội tụ.")
        
    print(f"\\nBước 2: Lập bảng tính")
    print("-" * 50)
    print(f"{'k':<5} | {'x_k':<12} | {'|x_k - x_{k-1}|':<15}")
    print("-" * 50)
    
    x_k = x0
    k = 0
    x_prev = None
    
    while True:
        if k > 0:
            diff = abs(x_k - x_prev)
            print(f"{k:<5} | {x_k:<12.5f} | {diff:<15.5f}")
            sai_so_hau_nghiem = (q / (1 - q)) * diff
            
            if sai_so_hau_nghiem < epsilon:
                print("-" * 50)
                print(f"\\nBước 3: Kết luận")
                print(f"  Nghiệm gần đúng: x ≈ {x_k:.5f}")
                print(f"  Sai số hậu nghiệm: [q/(1-q)] * |x_k - x_k-1| = {sai_so_hau_nghiem:.5f} < {epsilon}")
                break
        else:
            print(f"{k:<5} | {x_k:<12.5f} | {'-':<15}")
            
        x_prev = x_k
        x_k = g(x_k)
        k += 1

lap_don(x0=1.5, q=0.333, epsilon=0.005)""",

    "Lặp đơn (Hệ phương trình)": """import numpy as np

def lap_don_he(B, d, X0, epsilon, p_norm=np.inf):
    print("="*60)
    print("PHƯƠNG PHÁP LẶP ĐƠN (HỆ PHƯƠNG TRÌNH X = BX + d)")
    print("="*60)
    
    q = np.linalg.norm(B, p_norm)
    print("Bước 1: Kiểm tra hội tụ")
    print(f"  Ma trận B = \\n{B}")
    print(f"  Vector d = {d}")
    print(f"  Chuẩn {p_norm} của B: q = {q:.4f}")
    if q < 1:
        print("  => q < 1, phương pháp lặp hội tụ.")
    else:
        print("  => Cảnh báo: q >= 1, chưa chắc hội tụ.")
        
    print(f"\\nBước 2: Bảng tính")
    n = len(d)
    header = f"{'k':<5} | " + " | ".join([f"x_{i+1:<8}" for i in range(n)]) + " | ||X_k - X_{k-1}||"
    print("-" * len(header))
    print(header)
    print("-" * len(header))
    
    X_k = np.array(X0, dtype=float)
    k = 0
    X_prev = None
    
    while True:
        if k > 0:
            diff = np.linalg.norm(X_k - X_prev, p_norm)
            row = f"{k:<5} | " + " | ".join([f"{xi:<10.5f}" for xi in X_k]) + f" | {diff:.5f}"
            print(row)
            
            # Sai số hậu nghiệm
            sai_so_hau_nghiem = (q / (1 - q)) * diff if q < 1 else diff
            
            if sai_so_hau_nghiem < epsilon:
                print("-" * len(header))
                print(f"\\nBước 3: Kết luận")
                print(f"  Hội tụ tại bước {k}.")
                print(f"  Nghiệm X ≈ {np.round(X_k, 5)}")
                print(f"  Sai số hậu nghiệm: {sai_so_hau_nghiem:.5f} < {epsilon}")
                break
        else:
            row = f"{k:<5} | " + " | ".join([f"{xi:<10.5f}" for xi in X_k]) + f" | -"
            print(row)
            
        X_prev = X_k
        X_k = B @ X_k + d
        k += 1

B = np.array([[0, 0.1, 0.2], [0.1, 0, 0.3], [0.2, 0.3, 0]], dtype=float)
d = np.array([1, 2, 3], dtype=float)
X0 = np.array([0, 0, 0], dtype=float)
lap_don_he(B, d, X0, epsilon=0.01)""",

    "Newton nhiều chiều": """import numpy as np

def F(X):
    x, y = X[0], X[1]
    return np.array([
        x**2 + y**2 - 1,
        x**3 - y
    ])

def J(X):
    x, y = X[0], X[1]
    return np.array([
        [2*x, 2*y],
        [3*x**2, -1]
    ])

def newton_he(X0, epsilon, max_iter=10):
    print("="*60)
    print("PHƯƠNG PHÁP NEWTON (HỆ PHƯƠNG TRÌNH PHI TUYẾN)")
    print("="*60)
    
    print("Bước 1: Chọn xấp xỉ ban đầu X_0")
    X_k = np.array(X0, dtype=float)
    print(f"  X_0 = {X_k}")
    
    print(f"\\nBước 2: Các bước lặp giải hệ J(X_k) * deltaX = -F(X_k)")
    print("-" * 65)
    print(f"{'k':<5} | {'X_k':<20} | {'||delta X||_inf':<15}")
    print("-" * 65)
    
    for k in range(max_iter):
        F_val = F(X_k)
        J_val = J(X_k)
        
        # Giải hệ tuyến tính
        dX = np.linalg.solve(J_val, -F_val)
        X_new = X_k + dX
        sai_so = np.linalg.norm(dX, np.inf)
        
        print(f"{k:<5} | {np.array2string(X_k, precision=5, suppress_small=True):<20} | {sai_so:<15.5f}")
        
        if sai_so < epsilon:
            print(f"{k+1:<5} | {np.array2string(X_new, precision=5, suppress_small=True):<20} | {'-':<15}")
            print("-" * 65)
            print(f"\\nBước 3: Kết luận")
            print(f"  Hội tụ tại bước {k+1}, Nghiệm X ≈ {np.round(X_new, 5)}")
            print(f"  Sai số ||delta X||_inf = {sai_so:.5f} < {epsilon}")
            return
            
        X_k = X_new

newton_he([0.8, 0.6], 0.001)""",

    "Phân tách LU": """import numpy as np

def LU_decomposition(A):
    print("="*60)
    print("PHƯƠNG PHÁP PHÂN TÁCH LU (CƠ BẢN)")
    print("="*60)
    
    n = len(A)
    L = np.eye(n)
    U = np.zeros((n, n))
    B = np.copy(A)
    
    print("Bước 1: Bắt đầu khử Gauss trên ma trận B = A")
    print(B)
    
    for k in range(n-1):
        if B[k, k] == 0:
            print(f"  => Lỗi: Phần tử pivot B[{k},{k}] = 0, ma trận suy biến!")
            return
            
        print(f"\\n-- Khử cột {k+1} --")
        for i in range(k+1, n):
            L[i, k] = B[i, k] / B[k, k]
            print(f"  L[{i+1},{k+1}] = {B[i, k]:.2f} / {B[k, k]:.2f} = {L[i, k]:.4f}")
            for j in range(k+1, n):
                B[i, j] = B[i, j] - L[i, k] * B[k, j]
                
        print(f"  Ma trận B cập nhật:\\n{np.round(B, 4)}")
                
    for i in range(n):
        for j in range(i, n):
            U[i, j] = B[i, j]
            
    print("\\nBước 2: Kết luận ma trận L và U")
    print("Ma trận L (Dưới đường chéo chính):")
    print(np.round(L, 4))
    print("\\nMa trận U (Trên đường chéo chính):")
    print(np.round(U, 4))
    print("\\nKiểm tra lại L @ U = A:")
    print(np.round(L @ U, 4))

A = np.array([[2, 1, 1], [4, -6, 0], [-2, 7, 2]], dtype=float)
LU_decomposition(A)""",

    "LU có Pivoting": """import numpy as np

def LU_pivoting(A, b):
    print("="*60)
    print("PHƯƠNG PHÁP PHÂN TÁCH LU (CÓ PIVOTING)")
    print("="*60)
    
    n = len(A)
    A_work = np.copy(A)
    P = np.eye(n)
    perm = list(range(n))
    
    print("Bước 1: Bắt đầu phân tách LU với Pivoting")
    for k in range(n-1):
        p = np.argmax(np.abs(A_work[k:, k])) + k
        print(f"\\n-- Vòng {k+1}: Tìm pivot cột {k+1} --")
        print(f"  Pivot lớn nhất ở hàng {p+1}: giá trị {A_work[p, k]:.4f}")
        
        if A_work[p, k] == 0:
            print("  => Lỗi: Ma trận suy biến!")
            return
            
        if p != k:
            print(f"  -> Hoán đổi hàng {k+1} và hàng {p+1}")
            A_work[[k, p]] = A_work[[p, k]]
            P[[k, p]] = P[[p, k]]
            perm[k], perm[p] = perm[p], perm[k]
            
        for i in range(k+1, n):
            A_work[i, k] = A_work[i, k] / A_work[k, k]
            A_work[i, k+1:] = A_work[i, k+1:] - A_work[i, k] * A_work[k, k+1:]
            
        print(f"  Ma trận làm việc A cập nhật:\\n{np.round(A_work, 4)}")
            
    L = np.tril(A_work, -1) + np.eye(n)
    U = np.triu(A_work)
    
    print("\\nBước 2: Trích xuất L, U, P, vector hoán vị perm")
    print("L:\\n", np.round(L, 4))
    print("U:\\n", np.round(U, 4))
    print("P:\\n", P)
    print("perm:", perm)
    
    print("\\nBước 3: Giải hệ phương trình AX = b")
    b_perm = b[perm]
    print(f"  Hoán vị vector b: {b_perm}")
    
    y = np.linalg.solve(L, b_perm)
    print(f"  Giải hệ LY = b': Y = {np.round(y, 4)}")
    
    x = np.linalg.solve(U, y)
    print(f"  Giải hệ UX = Y: X = {np.round(x, 4)}")

A = np.array([[0, 2, 1], [1, -2, -3], [-1, 1, 2]], dtype=float)
b = np.array([-8, 0, 3], dtype=float)
LU_pivoting(A, b)""",

    "Phân tách Cholesky": """import numpy as np

def Cholesky(A):
    print("="*60)
    print("PHƯƠNG PHÁP PHÂN TÁCH CHOLESKY (A = L * L^T)")
    print("="*60)
    
    n = len(A)
    L = np.zeros_like(A, dtype=float)
    
    print("Bước 1: Tính toán từng phần tử của ma trận L")
    for i in range(n):
        sum_l_k2 = sum(L[i, k]**2 for k in range(i))
        temp = A[i, i] - sum_l_k2
        print(f"  Tính L[{i+1},{i+1}]: L[{i+1},{i+1}]^2 = A[{i+1},{i+1}] - sum = {A[i, i]} - {sum_l_k2:.4f} = {temp:.4f}")
        
        if temp <= 0:
            print("  => Lỗi: Temp <= 0, Ma trận không xác định dương!")
            return
            
        L[i, i] = np.sqrt(temp)
        print(f"  => L[{i+1},{i+1}] = {L[i, i]:.4f}")
        
        for j in range(i+1, n):
            sum_l_jk = sum(L[j, k] * L[i, k] for k in range(i))
            L[j, i] = (A[j, i] - sum_l_jk) / L[i, i]
            print(f"    L[{j+1},{i+1}] = ({A[j, i]} - {sum_l_jk:.4f}) / {L[i,i]:.4f} = {L[j, i]:.4f}")
            
    print("\\nBước 2: Kết luận")
    print("Ma trận L thu được:")
    print(np.round(L, 5))
    print("\\nKiểm tra lại L @ L.T = A:")
    print(np.round(L @ L.T, 5))

A = np.array([[4, 12, -16], [12, 37, -43], [-16, -43, 98]], dtype=float)
Cholesky(A)""",

    "Lặp Gauss-Seidel": """import numpy as np

def Gauss_Seidel(A, b, epsilon, max_iter=20):
    print("="*60)
    print("PHƯƠNG PHÁP LẶP GAUSS-SEIDEL")
    print("="*60)
    
    n = len(b)
    
    print("Bước 1: Kiểm tra tính chéo trội và thiết lập hệ số")
    # Kiểm tra chéo trội hàng đơn giản
    is_row_dominant = True
    q = 0
    s = 0
    for i in range(n):
        sum_row = sum(abs(A[i][j]) for j in range(n) if j != i)
        if sum_row >= abs(A[i][i]):
            is_row_dominant = False
    
    if is_row_dominant:
        print("  => Ma trận A chéo trội hàng.")
        # Cần tính q, s theo công thức. Ở đây đơn giản hóa việc tính sai số
    else:
        print("  => Cảnh báo: Ma trận A không chéo trội hàng, chưa chắc hội tụ.")
        
    X_k = np.zeros(n)
    
    print(f"\\nBước 2: Bảng tính")
    header = f"{'k':<5} | " + " | ".join([f"x_{i+1:<8}" for i in range(n)]) + " | Sai số max|x_new - x_old|"
    print("-" * len(header))
    print(header)
    print("-" * len(header))
    
    for k in range(1, max_iter + 1):
        X_new = np.copy(X_k)
        for i in range(n):
            s1 = sum(A[i][j] * X_new[j] for j in range(i))
            s2 = sum(A[i][j] * X_k[j] for j in range(i+1, n))
            X_new[i] = (b[i] - s1 - s2) / A[i][i]
            
        sai_so = np.linalg.norm(X_new - X_k, np.inf)
        
        row = f"{k-1:<5} | " + " | ".join([f"{xi:<10.5f}" for xi in X_k]) + f" | {sai_so:.5f}"
        print(row)
        
        if sai_so < epsilon:
            row_new = f"{k:<5} | " + " | ".join([f"{xi:<10.5f}" for xi in X_new]) + f" | -"
            print(row_new)
            print("-" * len(header))
            print(f"\\nBước 3: Kết luận")
            print(f"  Nghiệm hội tụ X ≈ {np.round(X_new, 5)}")
            break
            
        X_k = X_new

A = np.array([[10, 1, 1], [2, 10, 1], [2, 2, 10]], dtype=float)
b = np.array([12, 13, 14], dtype=float)
Gauss_Seidel(A, b, epsilon=0.001)""",

    "Nghịch đảo bằng Cholesky": """import numpy as np

def Cholesky_Inverse(A):
    print("="*60)
    print("TÌM MA TRẬN NGHỊCH ĐẢO BẰNG CHOLESKY")
    print("="*60)
    
    n = len(A)
    L = np.zeros_like(A, dtype=float)
    
    print("Bước 1: Phân tách Cholesky A = L*L^T")
    for i in range(n):
        temp = A[i, i] - np.sum(L[i, :i]**2)
        L[i, i] = np.sqrt(temp)
        for j in range(i+1, n):
            L[j, i] = (A[j, i] - np.sum(L[j, :i] * L[i, :i])) / L[i, i]
            
    print("  Ma trận L:")
    print(np.round(L, 4))
            
    print("\\nBước 2: Tìm ma trận nghịch đảo A^-1 từng cột")
    A_inv = np.zeros_like(A, dtype=float)
    I = np.eye(n)
    
    for j in range(n):
        print(f"  - Giải cột {j+1}:")
        y = np.zeros(n)
        for i in range(n):
            y[i] = (I[i, j] - np.sum(L[i, :i] * y[:i])) / L[i, i]
        print(f"    + Giải Ly = e_{j+1}  => y = {np.round(y, 4)}")
            
        for i in range(n-1, -1, -1):
            A_inv[i, j] = (y[i] - np.sum(L[i+1:, i] * A_inv[i+1:, j])) / L[i, i]
        print(f"    + Giải L^Tx = y => Cột {j+1} của A^-1 = {np.round(A_inv[:, j], 4)}")
            
    print("\\nBước 3: Kết luận")
    print("Ma trận nghịch đảo A^-1:")
    print(np.round(A_inv, 5))

A = np.array([[4, 12, -16], [12, 37, -43], [-16, -43, 98]], dtype=float)
Cholesky_Inverse(A)""",

    "Nghịch đảo bằng Lặp Jacobi / Gauss-Seidel": """import numpy as np

def Inverse_Gauss_Seidel(A, epsilon=0.001, max_iter=20):
    print("="*60)
    print("TÌM MA TRẬN NGHỊCH ĐẢO BẰNG GAUSS-SEIDEL")
    print("="*60)
    
    n = len(A)
    A_inv = np.zeros((n, n))
    I = np.eye(n)
    
    print("Tiến hành giải hệ A * X_j = e_j cho từng cột j")
    
    for l in range(n):
        print(f"\\n--- Giải cột {l+1} (vế phải e_{l+1}) ---")
        x_old = np.zeros(n)
        e_l = I[:, l]
        
        for k in range(max_iter):
            x_new = np.copy(x_old)
            for i in range(n):
                s1 = sum(A[i, j] * x_new[j] for j in range(i))
                s2 = sum(A[i, j] * x_old[j] for j in range(i+1, n))
                x_new[i] = (e_l[i] - s1 - s2) / A[i, i]
                
            sai_so = np.linalg.norm(x_new - x_old, np.inf)
            print(f"  Lặp k={k+1}: x = {np.round(x_new, 4)} | sai số = {sai_so:.5f}")
            
            if sai_so < epsilon:
                print(f"  => Cột {l+1} hội tụ.")
                break
            x_old = x_new
            
        A_inv[:, l] = x_new
        
    print("\\nKết luận ma trận nghịch đảo A^-1:")
    print(np.round(A_inv, 5))

A = np.array([[10, 1, 1], [2, 10, 1], [2, 2, 10]], dtype=float)
Inverse_Gauss_Seidel(A, epsilon=0.01)""",

    "Phương pháp Danielevski": """import numpy as np

def Danielevski(A):
    print("="*60)
    print("PHƯƠNG PHÁP DANIELEVSKI (TÌM ĐA THỨC ĐẶC TRƯNG)")
    print("="*60)
    
    n = len(A)
    P = np.copy(A)
    
    print("Bước 1: Khởi tạo")
    print("  Ma trận P = A:\\n", P)
    
    print("\\nBước 2: Lặp khử dần từng cột")
    for k in range(n-1, 0, -1):
        if P[k, k-1] == 0:
            print(f"\\nLỗi: p_{k},{k-1} = 0, cần hoán vị khối. Thuật toán cơ bản dừng.")
            return P
            
        M = np.eye(n)
        M[k-1, :] = P[k, :]
        
        M_inv = np.eye(n)
        for j in range(n):
            if j != k-1:
                M_inv[k-1, j] = -P[k, j] / P[k, k-1]
        M_inv[k-1, k-1] = 1 / P[k, k-1]
        
        print(f"\\n-- Xử lý cột k = {k} --")
        print(f"  Ma trận biến đổi M_{k}:\\n{np.round(M, 4)}")
        print(f"  Ma trận nghịch đảo M_{k}^-1:\\n{np.round(M_inv, 4)}")
        
        P = M @ P @ M_inv
        print(f"  Ma trận P cập nhật (P = M*P*M^-1):\\n{np.round(P, 4)}")
        
    print("\\nBước 3: Kết luận")
    print("  Đa thức đặc trưng có các hệ số (từ bậc n-1 đến 0) ở hàng đầu tiên:")
    print(f"  P(lambda) = (-1)^n * (lambda^n - " + " - ".join([f"({P[0, i]:.4f})lambda^{n-1-i}" for i in range(n)]) + ")")

A = np.array([[1, 2, 3], [2, 1, 4], [3, 4, 1]], dtype=float)
Danielevski(A)""",

    "Phương pháp Xuống thang": """import numpy as np

def Power_Method(A, X0, epsilon, max_iter=50):
    v = X0 / np.linalg.norm(X0, 2)
    for k in range(max_iter):
        Y = A @ v
        lam = v.T @ Y
        v_new = Y / np.linalg.norm(Y, 2)
        if np.linalg.norm(v_new - v, 2) < epsilon or np.linalg.norm(v_new + v, 2) < epsilon:
            return lam, v_new
        v = v_new
    return lam, v

def Deflation(A, lam1, v1, X0, epsilon):
    print("="*60)
    print("PHƯƠNG PHÁP XUỐNG THANG (TÌM TRỊ RIÊNG THỨ 2)")
    print("="*60)
    
    print("Bước 1: Dữ liệu đầu vào")
    print(f"  Trị riêng trội nhất lambda_1 = {lam1:.5f}")
    print(f"  Vector riêng tương ứng v_1 = {np.round(v1, 5)}")
    
    x = v1 / (v1.T @ v1)
    print(f"  Chọn vector phụ x = v_1 / ||v_1||^2 = {np.round(x, 5)}")
    
    print("\\nBước 2: Xây dựng ma trận xuống thang B")
    B = A - lam1 * np.outer(v1, x.T)
    print("  B = A - lambda_1 * v_1 * x^T")
    print("  Ma trận B:\\n", np.round(B, 5))
    
    print("\\nBước 3: Dùng pp lũy thừa tìm trị riêng của B")
    lam2, u2 = Power_Method(B, X0, epsilon)
    print(f"  Trị riêng trội của B: lambda_2 = {lam2:.5f}")
    print(f"  Vector riêng của B: u_2 = {np.round(u2, 5)}")
    
    print("\\nBước 4: Khôi phục vector riêng v_2 của A")
    v2 = (lam2 - lam1) * u2 + lam1 * (x.T @ u2) * v1
    v2 = v2 / np.linalg.norm(v2, 2)
    
    print(f"  Kết luận:\\n  lambda_2 = {lam2:.5f}\\n  v_2 = {np.round(v2, 5)}")

A = np.array([[2, 1, 1], [1, 3, 2], [1, 2, 2]], dtype=float)
# Tính sẵn lam1, v1 để demo
lam1, v1 = Power_Method(A, np.array([1, 1, 1]), 0.0001)
Deflation(A, lam1, v1, np.array([1, 0, 0]), 0.0001)""",

    "Giá trị kỳ dị SVD (Lớn nhất)": """import numpy as np

def SVD_Largest(A, X0, epsilon, max_iter=50):
    print("="*60)
    print("PHƯƠNG PHÁP TÌM GIÁ TRỊ KỲ DỊ LỚN NHẤT (SVD)")
    print("="*60)
    
    print("Bước 1: Thiết lập ma trận B")
    B = A.T @ A
    print("  Ma trận B = A^T * A:")
    print(np.round(B, 4))
    
    v = X0 / np.linalg.norm(X0, 2)
    print(f"  Vector khởi tạo v_0 chuẩn hóa: {np.round(v, 4)}")
    
    print(f"\\nBước 2: Phương pháp lặp lũy thừa trên B")
    print("-" * 55)
    print(f"{'Lần k':<6} | {'Vector v_k':<20} | {'lambda_k (Rayleigh)':<20}")
    print("-" * 55)
    
    for k in range(max_iter):
        v_old = np.copy(v)
        Y = B @ v_old
        lam = v_old.T @ Y
        v = Y / np.linalg.norm(Y, 2)
        
        v_str = np.array2string(v_old, precision=4, suppress_small=True)
        print(f"{k:<6} | {v_str:<20} | {lam:.5f}")
        
        if np.linalg.norm(v - v_old, 2) < epsilon or np.linalg.norm(v + v_old, 2) < epsilon:
            sigma = np.sqrt(lam)
            print("-" * 55)
            print("\\nBước 3: Kết luận")
            print(f"  Trị riêng cực đại của B: lambda_max = {lam:.5f}")
            print(f"  Giá trị kỳ dị lớn nhất sigma_1 = sqrt(lambda_max) = {sigma:.5f}")
            return sigma
            
A = np.array([[1, 2], [3, 4], [5, 6]], dtype=float)
SVD_Largest(A, np.array([1, 1]), epsilon=0.001)""",

    "Số điều kiện Cond(A)": """import numpy as np

def Cond_Number(A):
    print("="*60)
    print("TÍNH SỐ ĐIỀU KIỆN CỦA MA TRẬN COND(A)")
    print("="*60)
    
    print("Bước 1: Phân tích SVD để tìm các giá trị kỳ dị")
    U, S, VT = np.linalg.svd(A)
    
    print("  Danh sách các giá trị kỳ dị (sigma_i):")
    print(f"  {np.round(S, 5)}")
    
    sigma_max = np.max(S)
    sigma_min = np.min(S)
    
    print("\\nBước 2: Kết luận")
    print(f"  Giá trị kỳ dị lớn nhất sigma_max = {sigma_max:.5f}")
    print(f"  Giá trị kỳ dị nhỏ nhất sigma_min = {sigma_min:.5f}")
    
    if np.isclose(sigma_min, 0):
        print("  => Ma trận A suy biến, Số điều kiện Cond(A) = Vô cùng")
    else:
        cond_A = sigma_max / sigma_min
        print(f"  Số điều kiện Cond(A) = sigma_max / sigma_min = {cond_A:.5f}")

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 10]], dtype=float)
Cond_Number(A)"""
}

def main():
    workspace = r"d:/code/Uni/On_thi_cuoi_ky/Giải tích số"
    
    notebook = {
        "cells": [],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "codemirror_mode": {"name": "ipython", "version": 3},
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.8.0"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }
    
    def add_md(text):
        if text.strip():
            notebook['cells'].append(create_markdown_cell(text))
            
    def add_code(text):
        if text.strip():
            notebook['cells'].append(create_code_cell(text))
    
    add_md("# TỔNG HỢP CÁC PHƯƠNG PHÁP GIẢI TÍCH SỐ (FULL TRÌNH BÀY)\n\nTài liệu này chứa các script Python hoàn chỉnh, mô phỏng lại từng bước trình bày chuẩn mực theo cách làm bài thi (Kiểm tra điều kiện -> Bảng lặp -> Đánh giá sai số hậu nghiệm).")
    
    chapters = [
        {
            "id": "C2",
            "title": "CHƯƠNG 2: GIẢI PHƯƠNG TRÌNH PHI TUYẾN 1 CHIỀU",
            "methods": ["Chia đôi", "Dây cung", "Tiếp tuyến (Newton)", "Lặp đơn (1 chiều)"]
        },
        {
            "id": "C3",
            "title": "CHƯƠNG 3: GIẢI HỆ PHƯƠNG TRÌNH PHI TUYẾN NHIỀU CHIỀU",
            "methods": ["Lặp đơn nhiều chiều", "Newton nhiều chiều"]
        },
        {
            "id": "C4",
            "title": "CHƯƠNG 4: GIẢI HỆ ĐẠI SỐ TUYẾN TÍNH & TÌM MA TRẬN NGHỊCH ĐẢO",
            "methods": ["Phân tách LU", "LU có Pivoting", "Phân tách Cholesky", "Lặp đơn (Hệ phương trình)", "Lặp Gauss-Seidel", "Nghịch đảo bằng Cholesky", "Nghịch đảo bằng Lặp Jacobi / Gauss-Seidel"]
        },
        {
            "id": "C5",
            "title": "CHƯƠNG 5: GIÁ TRỊ RIÊNG VÀ VECTOR RIÊNG CỦA MA TRẬN",
            "methods": ["Phương pháp Danielevski", "Phương pháp Xuống thang", "Giá trị kỳ dị SVD (Lớn nhất)", "Số điều kiện Cond(A)"]
        }
    ]
    
    for ch in chapters:
        add_md(f"## {ch['title']}")
        for method in ch["methods"]:
            add_md(f"### {method}")
            if method in CODE_TEMPLATES:
                add_code(CODE_TEMPLATES[method])
            else:
                add_code(f"# TODO: Implement {method}")
                
    output_path = os.path.join(workspace, "Giai_tich_so.ipynb")
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=2, ensure_ascii=False)
        
if __name__ == '__main__':
    main()
