

# --- CODE FROM NOTEBOOK: scripts\Giai_tich_so.ipynb ---


import math

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
    print(f"\nBước 2: Sai số tiên nghiệm")
    print(f"  Để sai số (b-a)/2^n < {epsilon}, số bước lặp dự kiến n >= {n_expected}")
    
    # B3: Bảng lặp
    print(f"\nBước 3: Lập bảng tính")
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
            print(f"\nBước 4: Kết luận")
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
chia_doi(1, 2, 0.05)



import math

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
    
    print(f"\nBước 2: Lập bảng tính")
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
                print(f"\nBước 3: Kết luận")
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
day_cung(a=1, b=2, d=1, epsilon=0.01, m1=2, M1=11)



import math

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
        
    print(f"\nBước 2: Lập bảng tính")
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
                print(f"\nBước 3: Kết luận")
                print(f"  Nghiệm gần đúng: x ≈ {x_k:.5f}")
                print(f"  Sai số hậu nghiệm: [M2/(2*m1)] * |x_k - x_k-1|^2 = {sai_so_hau_nghiem:.8f} < {epsilon}")
                break
        else:
            print(f"{k:<5} | {x_k:<12.5f} | {fx:<12.5f} | {'-':<15}")
            
        x_prev = x_k
        x_k = x_k - f(x_k) / df(x_k)
        k += 1

# m1 = 2 (tại x=1), M2 = 12 (tại x=2)
newton(a=1, b=2, x0=2, epsilon=0.001, m1=2, M2=12)



import math

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
        
    print(f"\nBước 2: Lập bảng tính")
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
                print(f"\nBước 3: Kết luận")
                print(f"  Nghiệm gần đúng: x ≈ {x_k:.5f}")
                print(f"  Sai số hậu nghiệm: [q/(1-q)] * |x_k - x_k-1| = {sai_so_hau_nghiem:.5f} < {epsilon}")
                break
        else:
            print(f"{k:<5} | {x_k:<12.5f} | {'-':<15}")
            
        x_prev = x_k
        x_k = g(x_k)
        k += 1

lap_don(x0=1.5, q=0.333, epsilon=0.005)



import numpy as np

def lap_don_phi_tuyen_he(G, X0, q, epsilon, max_iter=20):
    print("="*60)
    print("PHƯƠNG PHÁP LẶP ĐƠN (HỆ PHƯƠNG TRÌNH PHI TUYẾN)")
    print("="*60)
    
    print("Bước 1: Khởi tạo và kiểm tra hệ số co")
    print(f"  Hệ số co q = {q}")
    if q >= 1:
        print("  => Cảnh báo: q >= 1, phương pháp có thể không hội tụ.")
    
    X_k = np.array(X0, dtype=float)
    n = len(X0)
    
    print("\nBước 2: Bảng tính")
    header = f"{'k':<5} | " + " | ".join([f"x_{j+1:<8}" for j in range(n)]) + " | ||X_k - X_{k-1}||_inf"
    print("-" * len(header))
    print(header)
    print("-" * len(header))
    
    X_prev = None
    for k in range(max_iter):
        if k > 0:
            diff = np.linalg.norm(X_k - X_prev, np.inf)
            row = f"{k:<5} | " + " | ".join([f"{xi:<10.5f}" for xi in X_k]) + f" | {diff:.5f}"
            print(row)
            
            sai_so_hau_nghiem = (q / (1 - q)) * diff if q < 1 else diff
            
            if sai_so_hau_nghiem < epsilon:
                print("-" * len(header))
                print(f"\nBước 3: Kết luận")
                print(f"  Hội tụ tại bước {k}.")
                print(f"  Nghiệm X ≈ {np.round(X_k, 5)}")
                print(f"  Sai số hậu nghiệm: {sai_so_hau_nghiem:.5f} < {epsilon}")
                return
        else:
            row = f"{k:<5} | " + " | ".join([f"{xi:<10.5f}" for xi in X_k]) + " | -"
            print(row)
            
        X_prev = X_k
        X_k = G(X_k)

# Test thử bài toán
def G_demo(X):
    x, y = X[0], X[1]
    return np.array([
        (x**2 + y**2 + 8) / 10,
        (x * y + x + 8) / 10
    ])

lap_don_phi_tuyen_he(G_demo, [0.5, 0.5], 0.2, 0.001)



import numpy as np

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
    
    print(f"\nBước 2: Các bước lặp giải hệ J(X_k) * deltaX = -F(X_k)")
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
            print(f"\nBước 3: Kết luận")
            print(f"  Hội tụ tại bước {k+1}, Nghiệm X ≈ {np.round(X_new, 5)}")
            print(f"  Sai số ||delta X||_inf = {sai_so:.5f} < {epsilon}")
            return
            
        X_k = X_new

newton_he([0.8, 0.6], 0.001)



import numpy as np

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
            
        print(f"\n-- Khử cột {k+1} --")
        for i in range(k+1, n):
            L[i, k] = B[i, k] / B[k, k]
            print(f"  L[{i+1},{k+1}] = {B[i, k]:.2f} / {B[k, k]:.2f} = {L[i, k]:.4f}")
            for j in range(k+1, n):
                B[i, j] = B[i, j] - L[i, k] * B[k, j]
                
        print(f"  Ma trận B cập nhật:\n{np.round(B, 4)}")
                
    for i in range(n):
        for j in range(i, n):
            U[i, j] = B[i, j]
            
    print("\nBước 2: Kết luận ma trận L và U")
    print("Ma trận L (Dưới đường chéo chính):")
    print(np.round(L, 4))
    print("\nMa trận U (Trên đường chéo chính):")
    print(np.round(U, 4))
    print("\nKiểm tra lại L @ U = A:")
    print(np.round(L @ U, 4))

A = np.array([[2, 1, 1], [4, -6, 0], [-2, 7, 2]], dtype=float)
LU_decomposition(A)



import numpy as np

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
        print(f"\n-- Vòng {k+1}: Tìm pivot cột {k+1} --")
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
            
        print(f"  Ma trận làm việc A cập nhật:\n{np.round(A_work, 4)}")
            
    L = np.tril(A_work, -1) + np.eye(n)
    U = np.triu(A_work)
    
    print("\nBước 2: Trích xuất L, U, P, vector hoán vị perm")
    print("L:\n", np.round(L, 4))
    print("U:\n", np.round(U, 4))
    print("P:\n", P)
    print("perm:", perm)
    
    print("\nBước 3: Giải hệ phương trình AX = b")
    b_perm = b[perm]
    print(f"  Hoán vị vector b: {b_perm}")
    
    y = np.linalg.solve(L, b_perm)
    print(f"  Giải hệ LY = b': Y = {np.round(y, 4)}")
    
    x = np.linalg.solve(U, y)
    print(f"  Giải hệ UX = Y: X = {np.round(x, 4)}")

A = np.array([[0, 2, 1], [1, -2, -3], [-1, 1, 2]], dtype=float)
b = np.array([-8, 0, 3], dtype=float)
LU_pivoting(A, b)



import numpy as np

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
            
    print("\nBước 2: Kết luận")
    print("Ma trận L thu được:")
    print(np.round(L, 5))
    print("\nKiểm tra lại L @ L.T = A:")
    print(np.round(L @ L.T, 5))

A = np.array([[4, 12, -16], [12, 37, -43], [-16, -43, 98]], dtype=float)
Cholesky(A)



import numpy as np

def lap_don_he(B, d, X0, epsilon, p_norm=np.inf):
    print("="*60)
    print("PHƯƠNG PHÁP LẶP ĐƠN (HỆ PHƯƠNG TRÌNH X = BX + d)")
    print("="*60)
    
    q = np.linalg.norm(B, p_norm)
    print("Bước 1: Kiểm tra hội tụ")
    print(f"  Ma trận B = \n{B}")
    print(f"  Vector d = {d}")
    print(f"  Chuẩn {p_norm} của B: q = {q:.4f}")
    if q < 1:
        print("  => q < 1, phương pháp lặp hội tụ.")
    else:
        print("  => Cảnh báo: q >= 1, chưa chắc hội tụ.")
        
    print(f"\nBước 2: Bảng tính")
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
                print(f"\nBước 3: Kết luận")
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
lap_don_he(B, d, X0, epsilon=0.01)



import numpy as np

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
    
    print(f"\nBước 2: Bảng tính")
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
            print(f"\nBước 3: Kết luận")
            print(f"  Nghiệm hội tụ X ≈ {np.round(X_new, 5)}")
            break
            
        X_k = X_new

A = np.array([
    [0.0400, 0.0700, -0.0100, 0.0000, -0.0500],
    [-0.1000, 0.0400, -0.0200, -0.0100, 0.0400],
    [-0.0500, -0.0400, 0.0600, 0.0300, 0.0300],
    [-0.1000, 0.0900, 0.0600, 0.0400, -0.0700],
    [-0.0800, -0.1000, -0.0700, 0.0500, -0.0800]
], dtype=float)
b = np.array([-7.0, 6.0, -4.0, 1.0, -7.0], dtype=float)
Gauss_Seidel(A, b, epsilon=0.001)



import numpy as np

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
            
    print("\nBước 2: Tìm ma trận nghịch đảo A^-1 từng cột")
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
            
    print("\nBước 3: Kết luận")
    print("Ma trận nghịch đảo A^-1:")
    print(np.round(A_inv, 5))

A = np.array([[4, 12, -16], [12, 37, -43], [-16, -43, 98]], dtype=float)
Cholesky_Inverse(A)



import numpy as np

def Inverse_Gauss_Seidel(A, epsilon=0.001, max_iter=20):
    print("="*60)
    print("TÌM MA TRẬN NGHỊCH ĐẢO BẰNG GAUSS-SEIDEL")
    print("="*60)
    
    n = len(A)
    A_inv = np.zeros((n, n))
    I = np.eye(n)
    
    print("Tiến hành giải hệ A * X_j = e_j cho từng cột j")
    
    for l in range(n):
        print(f"\n--- Giải cột {l+1} (vế phải e_{l+1}) ---")
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
        
    print("\nKết luận ma trận nghịch đảo A^-1:")
    print(np.round(A_inv, 5))

A = np.array([[10, 1, 1], [2, 10, 1], [2, 2, 10]], dtype=float)
Inverse_Gauss_Seidel(A, epsilon=0.01)



import numpy as np

def print_latex(M, precision=4):
    import numpy as np
    if not isinstance(M, np.ndarray):
        latex_str = f"{M}"
    elif M.ndim == 1:
        inner = " & ".join([f"{x:.{precision}f}" for x in M])
        latex_str = f"\\begin{{bmatrix}} {inner} \\end{{bmatrix}}"
    else:
        rows = " \\\\ ".join([" & ".join([f"{x:.{precision}f}" for x in row]) for row in M])
        latex_str = f"\\begin{{bmatrix}} {rows} \\end{{bmatrix}}"

    try:
        get_ipython()
        in_jupyter = True
    except NameError:
        in_jupyter = False

    if in_jupyter:
        from IPython.display import display, Math
        display(Math(latex_str))
    else:
        print(f"$$ {latex_str} $$")

def Vien_Quanh(A):
    SEP = "═" * 62
    sep = "─" * 62
    print(SEP)
    print("    TÌM MA TRẬN NGHỊCH ĐẢO BẰNG PHƯƠNG PHÁP VIỀN QUANH")
    print(SEP)

    n = len(A)
    print("\nI. CƠ SỞ LÝ THUYẾT")
    print("   Tính ma trận nghịch đảo A_k⁻¹ của các ma trận con chính A_k (k=1..n).")
    print("   Tại bước k, phân hoạch A_k = [A_{k-1}  u_k ; v_k^T  a_kk].")
    print("   Tính x_k = A_{k-1}⁻¹·u_k,  y_k^T = v_k^T·A_{k-1}⁻¹.")
    print("   Tính α_k = a_kk - v_k^T·x_k. Nếu α_k = 0, A suy biến.")
    print("   Tính các khối của A_k⁻¹:")
    print("     s_k = 1/α_k, q_k = -s_k·x_k, r_k^T = -s_k·y_k^T")
    print("     P_k = A_{k-1}⁻¹ + s_k·x_k·y_k^T")
    print("     A_k⁻¹ = [P_k  q_k ; r_k^T  s_k]")

    print(f"\nII. DỮ LIỆU BÀI TOÁN")
    print(f"   Ma trận A ({n}×{n}):")
    print_latex(A, precision=4)

    print(f"\nIII. QUÁ TRÌNH TÍNH TOÁN")
    if abs(A[0, 0]) < 1e-14:
        print("   => LỖI: a_11 = 0. Phương pháp viền quanh cơ bản thất bại.")
        return

    A_inv_k = np.array([[1.0 / A[0, 0]]])
    print(f"\n   -- Bước 1 (k = 1) --")
    print(f"   A_1 = [{A[0,0]:.4f}], A_1⁻¹ = [{A_inv_k[0,0]:.6f}]")

    for k in range(2, n + 1):
        print(f"\n   -- Bước {k} (k = {k}) --")
        # u_k is column k-1 of A from row 0 to k-2
        u_k = A[0:k-1, k-1].reshape(-1, 1)
        # v_k_T is row k-1 of A from col 0 to k-2
        v_k_T = A[k-1, 0:k-1].reshape(1, -1)
        a_kk = A[k-1, k-1]

        print(f"   u_k:")
        print_latex(u_k, precision=4)
        print(f"   v_k^T:")
        print_latex(v_k_T, precision=4)

        x_k = A_inv_k @ u_k
        y_k_T = v_k_T @ A_inv_k

        alpha_k = a_kk - (v_k_T @ x_k)[0, 0]
        print(f"   α_k = a_kk - v_k^T·x_k = {a_kk:.4f} - {(a_kk - alpha_k):.4f} = {alpha_k:.6f}")

        if abs(alpha_k) < 1e-14:
            print(f"   => LỖI: α_{k} = 0. Ma trận con A_{k} suy biến. Dừng thuật toán.")
            return

        s_k = 1.0 / alpha_k
        q_k = -s_k * x_k
        r_k_T = -s_k * y_k_T
        P_k = A_inv_k + s_k * (x_k @ y_k_T)

        A_inv_next = np.zeros((k, k))
        A_inv_next[0:k-1, 0:k-1] = P_k
        A_inv_next[0:k-1, k-1] = q_k.flatten()
        A_inv_next[k-1, 0:k-1] = r_k_T.flatten()
        A_inv_next[k-1, k-1] = s_k

        A_inv_k = A_inv_next
        print(f"   Ma trận A_{k}⁻¹:")
        print_latex(A_inv_k, precision=6)

    print(f"\nIV. KẾT LUẬN")
    print("   Ma trận nghịch đảo A⁻¹:")
    print_latex(A_inv_k, precision=6)
    err = np.linalg.norm(A @ A_inv_k - np.eye(n), np.inf)
    print(f"   Kiểm tra: ||A·A⁻¹ − I||∞ = {err:.2e}  {'✓' if err < 1e-6 else '≈0'}")


# Ví dụ ma trận A
A = np.array([
    [1.0, 2.0, 3.0],
    [2.0, 3.0, 4.0],
    [3.0, 4.0, 6.0]
])

Vien_Quanh(A)



import numpy as np

def Danielevski(A):
    print("="*60)
    print("PHƯƠNG PHÁP DANIELEVSKI (TÌM ĐA THỨC ĐẶC TRƯNG)")
    print("="*60)
    
    n = len(A)
    P = np.copy(A)
    
    print("Bước 1: Khởi tạo")
    print("  Ma trận P = A:\n", P)
    
    print("\nBước 2: Lặp khử dần từng cột")
    for k in range(n-1, 0, -1):
        if P[k, k-1] == 0:
            print(f"\nLỗi: p_{k},{k-1} = 0, cần hoán vị khối. Thuật toán cơ bản dừng.")
            return P
            
        M = np.eye(n)
        M[k-1, :] = P[k, :]
        
        M_inv = np.eye(n)
        for j in range(n):
            if j != k-1:
                M_inv[k-1, j] = -P[k, j] / P[k, k-1]
        M_inv[k-1, k-1] = 1 / P[k, k-1]
        
        print(f"\n-- Xử lý cột k = {k} --")
        print(f"  Ma trận biến đổi M_{k}:\n{np.round(M, 4)}")
        print(f"  Ma trận nghịch đảo M_{k}^-1:\n{np.round(M_inv, 4)}")
        
        P = M @ P @ M_inv
        print(f"  Ma trận P cập nhật (P = M*P*M^-1):\n{np.round(P, 4)}")
        
    print("\nBước 3: Kết luận")
    print("  Đa thức đặc trưng có các hệ số (từ bậc n-1 đến 0) ở hàng đầu tiên:")
    print(f"  P(lambda) = (-1)^n * (lambda^n - " + " - ".join([f"({P[0, i]:.4f})lambda^{n-1-i}" for i in range(n)]) + ")")

A = np.array([[1, 2, 3], [2, 1, 4], [3, 4, 1]], dtype=float)
Danielevski(A)



import numpy as np

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
    
    print("\nBước 2: Xây dựng ma trận xuống thàng B")
    B = A - lam1 * np.outer(v1, x.T)
    print("  B = A - lambda_1 * v_1 * x^T")
    print("  Ma trận B:\n", np.round(B, 5))
    
    print("\nBước 3: Dùng pp lũy thừa tìm trị riêng của B")
    lam2, u2 = Power_Method(B, X0, epsilon)
    print(f"  Trị riêng trội của B: lambda_2 = {lam2:.5f}")
    print(f"  Vector riêng của B: u_2 = {np.round(u2, 5)}")
    
    print("\nBước 4: Khôi phục vector riêng v_2 của A")
    v2 = (lam2 - lam1) * u2 + lam1 * (x.T @ u2) * v1
    v2 = v2 / np.linalg.norm(v2, 2)
    
    print(f"  Kết luận:\n  lambda_2 = {lam2:.5f}\n  v_2 = {np.round(v2, 5)}")

A = np.array([[2, 1, 1], [1, 3, 2], [1, 2, 2]], dtype=float)
# Tính sẵn lam1, v1 để demo
lam1, v1 = Power_Method(A, np.array([1, 1, 1]), 0.0001)
Deflation(A, lam1, v1, np.array([1, 0, 0]), 0.0001)



import numpy as np

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
    
    print(f"\nBước 2: Phương pháp lặp lũy thừa trên B")
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
            print("\nBước 3: Kết luận")
            print(f"  Trị riêng cực đại của B: lambda_max = {lam:.5f}")
            print(f"  Giá trị kỳ dị lớn nhất sigma_1 = sqrt(lambda_max) = {sigma:.5f}")
            return sigma
            
A = np.array([[1, 2], [3, 4], [5, 6]], dtype=float)
SVD_Largest(A, np.array([1, 1]), epsilon=0.001)



import numpy as np

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
    
    print("\nBước 2: Kết luận")
    print(f"  Giá trị kỳ dị lớn nhất sigma_max = {sigma_max:.5f}")
    print(f"  Giá trị kỳ dị nhỏ nhất sigma_min = {sigma_min:.5f}")
    
    if np.isclose(sigma_min, 0):
        print("  => Ma trận A suy biến, Số điều kiện Cond(A) = Vô cùng")
    else:
        cond_A = sigma_max / sigma_min
        print(f"  Số điều kiện Cond(A) = sigma_max / sigma_min = {cond_A:.5f}")

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 10]], dtype=float)
Cond_Number(A)





# --- CODE FROM NOTEBOOK: scripts\CHƯƠNG 2 GIẢI PHƯƠNG TRÌNH PHI TUYẾN 1 CHIỀU\Chia đôi.ipynb ---


import numpy as np
from IPython.display import display, Math, Markdown

def chia_doi(f, a, b, max_iter=None, epsilon=None):
    # Phương pháp Chia doi (Bisection)
    # f: ham f(x) can tim nghiem
    # a, b: khoảng cô lập nghiệm voi f(a)*f(b) < 0
    # max_iter: số vòng lặp cố định (None = không giới hạn)
    # epsilon: sai số dừng |b-a|/2 (None = không kiểm tra)
    display(Markdown("## ❖ PHƯƠNG PHÁP CHIA ĐÔI (BISECTION)"))
    display(Math(r"\text{Tìm } x^* \in [" + f"{a}, {b}" + r"] \text{ sao cho } f(x^*)=0"))

    if f(a) * f(b) > 0:
        display(Markdown("⚠️ **Cảnh báo:** f(a) va f(b) cùng dấu - không đảm bảo tồn tại nghiệm!"))
        return None

    fa = f(a)
    history = []
    k = 0
    while True:
        k += 1
        c  = (a + b) / 2.0
        fc = f(c)
        err = (b - a) / 2.0
        history.append((k, a, b, c, fc, err))

        stop = False
        if max_iter is not None and k >= max_iter: stop = True
        if epsilon  is not None and err < epsilon:  stop = True
        if abs(fc) < 1e-14: stop = True
        if k >= 300: stop = True
        if stop: break

        if fa * fc < 0:
            b = c
        else:
            a = c; fa = fc

    # ── In kết quả ──
    n = len(history)
    display(Markdown(f"### Kết quả ({n} vòng lặp)"))
    cols = ["$k$", "$a_k$", "$b_k$", "$c_k = (a_k+b_k)/2$", "$f(c_k)$", "$\\Delta_k = (b-a)/2$"]
    seps = [":---:"]*6
    rows = []
    for (k_, a_, b_, c_, fc_, er_) in history:
        rows.append([f"${k_}$", f"${a_:.6f}$", f"${b_:.6f}$",
                     f"${c_:.6f}$", f"${fc_:.4e}$", f"${er_:.4e}$"])

    header = "| " + " | ".join(cols) + " |"
    sep    = "| " + " | ".join(seps) + " |"
    lines  = [header, sep]
    for r in rows: lines.append("| " + " | ".join(r) + " |")
    display(Markdown("\n".join(lines)))

    c_star = history[-1][3]
    er_final = history[-1][5]
    display(Markdown(f"**Nghiệm xấp xỉ:** $x^* \\approx {c_star:.10f}$"))
    display(Markdown(f"**Sai số:** $\\Delta \\leq {er_final:.4e}$"))
    display(Math(f"f(x^*) = {f(c_star):.6e} \\approx 0"))
    return c_star

# ═══════════════════════════════════════════════════════════════════
# NHẬP DỮ LIỆU CỦA BẠN VÀO ĐÂY
# ═══════════════════════════════════════════════════════════════════
f = lambda x: x**3 - x - 2   # hàm cần tìm nghiệm

a, b = 1.0, 2.0               # khoảng cô lập nghiệm
# ═══════════════════════════════════════════════════════════════════

chia_doi(f, a, b, max_iter=None, epsilon=1e-6)





# --- CODE FROM NOTEBOOK: scripts\CHƯƠNG 2 GIẢI PHƯƠNG TRÌNH PHI TUYẾN 1 CHIỀU\Dây cung.ipynb ---


import numpy as np
from IPython.display import display, Math, Markdown

def day_cung(f, a, b, max_iter=None, epsilon=None):
    # Phương pháp Day cung (Secant Method)
    # f: ham f(x)
    # a, b: hai điểm khởi đầu
    # max_iter: số vòng lặp cố định
    # epsilon: sai so |x_{k+1} - x_k|
    display(Markdown("## ❖ PHƯƠNG PHÁP DÂY CUNG (SECANT)"))
    display(Math(r"x_{k+1} = x_k - f(x_k) \cdot \frac{x_k - x_{k-1}}{f(x_k) - f(x_{k-1})}"))

    x0, x1 = float(a), float(b)
    f0, f1 = f(x0), f(x1)
    history = []
    k = 0
    while True:
        k += 1
        denom = f1 - f0
        if abs(denom) < 1e-15:
            display(Markdown("⚠️ **Cảnh báo:** Mẫu số xấp xỉ 0 - dừng lại."))
            break
        x2 = x1 - f1 * (x1 - x0) / denom
        f2 = f(x2)
        err = abs(x2 - x1)
        history.append((k, x0, x1, x2, f2, err))

        stop = False
        if max_iter is not None and k >= max_iter: stop = True
        if epsilon  is not None and err < epsilon:  stop = True
        if k >= 200: stop = True
        if stop: break
        x0, f0 = x1, f1
        x1, f1 = x2, f2

    n = len(history)
    display(Markdown(f"### Kết quả ({n} vòng lặp)"))
    cols = ["$k$", "$x_{k-1}$", "$x_k$", "$x_{k+1}$", "$f(x_{k+1})$", "$\\|\\Delta\\|$"]
    seps = [":---:"]*6
    rows = []
    for (k_, a_, b_, c_, fc_, er_) in history:
        rows.append([f"${k_}$", f"${a_:.6f}$", f"${b_:.6f}$",
                     f"${c_:.6f}$", f"${fc_:.4e}$", f"${er_:.4e}$"])
    header = "| " + " | ".join(cols) + " |"
    sep    = "| " + " | ".join(seps) + " |"
    lines  = [header, sep]
    for r in rows: lines.append("| " + " | ".join(r) + " |")
    display(Markdown("\n".join(lines)))

    c_star = history[-1][3]
    er_final = history[-1][5]
    display(Markdown(f"**Nghiệm xấp xỉ:** $x^* \\approx {c_star:.10f}$"))
    display(Markdown(f"**Sai số cuối:** $\\Delta = {er_final:.4e}$"))
    display(Math(f"f(x^*) = {f(c_star):.6e} \\approx 0"))
    return c_star

# ═══════════════════════════════════════════════════════════════════
# NHẬP DỮ LIỆU CỦA BẠN VÀO ĐÂY
# ═══════════════════════════════════════════════════════════════════
f = lambda x: x**3 - x - 2

a, b = 1.0, 2.0
# ═══════════════════════════════════════════════════════════════════

day_cung(f, a, b, max_iter=None, epsilon=1e-8)





# --- CODE FROM NOTEBOOK: scripts\CHƯƠNG 2 GIẢI PHƯƠNG TRÌNH PHI TUYẾN 1 CHIỀU\Giải Đa Thức Toàn Tập.ipynb ---


import numpy as np
from IPython.display import display, Math, Markdown

def format_poly(coeffs):
    n = len(coeffs) - 1
    terms = []
    for i, c in enumerate(coeffs):
        if abs(c) < 1e-10: continue
        deg = n - i
        sign = " + " if c > 0 else " - "
        c_abs = abs(c)
        c_str = f"{c_abs:.4f}" if abs(c_abs - 1.0) > 1e-10 or deg == 0 else ""
        if deg == 0: terms.append(f"{sign}{c_abs:.4f}")
        elif deg == 1: terms.append(f"{sign}{c_str}x")
        else: terms.append(f"{sign}{c_str}x^{deg}")
    res = "".join(terms).lstrip(" + ")
    if res.startswith("- "): res = "-" + res[2:]
    return res if res else "0"

def Polynomial_Solver_Full(coeffs_input, epsilon=1e-4):
    P = np.array(coeffs_input, dtype=float)
    display(Markdown("## ❖ TÌM TẤT CẢ NGHIỆM ĐA THỨC (CÁCH LY + NEWTON)"))
    display(Math(f"P(x) = {format_poly(P)} = 0"))
    
    # 1. TÌM KHOẢNG CÁCH LY (Sturm)
    display(Markdown("### 1. Phân tách khoảng cách ly nghiệm bằng định lý Sturm"))
    sturm_seq = [np.poly1d(P), np.polyder(np.poly1d(P))]
    while True:
        P_prev, P_curr = sturm_seq[-2], sturm_seq[-1]
        if P_curr.order == 0 and abs(P_curr.coeffs[0]) < 1e-10:
            sturm_seq.pop()
            break
        quot, rem = np.polydiv(P_prev, P_curr)
        P_next = np.poly1d(-rem.coeffs)
        if P_next.order == 0 and abs(P_next.coeffs[0]) < 1e-10: break
        sturm_seq.append(P_next)
        
    def count_sign_chànges(x_val):
        signs = [np.sign(p(x_val)) for p in sturm_seq if abs(p(x_val)) > 1e-10]
        return sum(1 for i in range(len(signs)-1) if signs[i]*signs[i+1] < 0)

    R = 1 + np.max(np.abs(P[1:])) / abs(P[0])
    step, start, end = 1.0, -np.ceil(R), np.ceil(R)
    
    intervals = []
    curr = start
    while curr <= end:
        a, b = curr, curr + step
        num_roots = count_sign_chànges(a) - count_sign_chànges(b)
        if num_roots == 1: intervals.append((a, b))
        elif num_roots > 1: # Chia nhỏ khoảng
            mid = (a + b) / 2.0
            if count_sign_chànges(a) - count_sign_chànges(mid) == 1: intervals.append((a, mid))
            if count_sign_chànges(mid) - count_sign_chànges(b) == 1: intervals.append((mid, b))
        curr += step
        
    for i, (a, b) in enumerate(intervals):
        display(Markdown(f"- Khoảng nghiệm thứ {i+1}: $x \in [{a:.4f}, {b:.4f}]$"))
        
    # 2. PHƯƠNG PHÁP NEWTON
    f = np.poly1d(P)
    df = np.polyder(f)
    d2f = np.polyder(df)
    
    for i, (a, b) in enumerate(intervals):
        display(Markdown(f"\n### 2.{i+1}. Giải nghiệm trong khoảng $[{a:.4f}, {b:.4f}]$ bằng Tiếp tuyến (Newton)"))
        x0 = a if f(a)*d2f(a) > 0 else b
        
        history = [x0]
        x_k = x0
        k = 0
        while True:
            k += 1
            x_new = x_k - f(x_k)/df(x_k)
            err = abs(x_new - x_k)
            history.append(x_new)
            if err < epsilon:
                break
            if k > 50:
                display(Markdown("Chưa hội tụ!"))
                break
            x_k = x_new
            
        display(Markdown(f"- **Tổng số lần lặp:** {k}"))
        display(Markdown(f"- **Sai số cuối cùng:** $\Delta = {err:.6e} \le \epsilon = {epsilon}$"))
        
        display(Markdown("- **Chi tiết các xấp xỉ:**"))
        if len(history) <= 5:
            for idx, val in enumerate(history):
                display(Math(f"x_{{{idx}}} = {val:.6f}"))
        else:
            display(Math(f"x_{{0}} = {history[0]:.6f} \\quad \\text{{(Xấp xỉ đầu)}}"))
            display(Math(f"x_{{1}} = {history[1]:.6f}"))
            display(Math(f"x_{{2}} = {history[2]:.6f}"))
            display(Markdown("$\\dots$"))
            display(Math(f"x_{{{k-2}}} = {history[-3]:.6f}"))
            display(Math(f"x_{{{k-1}}} = {history[-2]:.6f}"))
            display(Math(f"x_{{{k}}} = {history[-1]:.6f} \\quad \\text{{(Xấp xỉ cuối)}}"))
            
        # Kiểm tra lại nghiệm
        val_check = f(history[-1])
        display(Markdown("- **Kiểm tra nghiệm:**"))
        display(Math(f"P(x_{{{k}}}) = {val_check:.6e} \\approx 0 \\quad \\Rightarrow \\text{{Nghiệm hợp lệ!}}"))

# ========================================================
# NHẬP HỆ SỐ ĐA THỨC CỦA BẠN VÀO ĐÂY
# P(x) = a_n * x^n + a_{n-1} * x^{n-1} + ... + a_0
# Ví dụ: P(x) = 1*x^5 - 3*x^4 + 2*x^3 + 5*x^2 - x - 7

# ═══════════════════════════════════════════════════════════════════
# NHẬP DỮ LIỆU CỦA BẠN VÀO ĐÂY
# ═══════════════════════════════════════════════════════════════════
# He so da thuc theo thu tu tu bac cao nhat: [a_n, a_{n-1}, ..., a_1, a_0]
# Vi du: P(x) = x^5 - 2x^4 - 5x^3 + 4x^2 + 6x - 3
P_coeffs = [1.0, -2.0, -5.0, 4.0, 6.0, -3.0]
# ═══════════════════════════════════════════════════════════════════

Polynomial_Solver_Full(P_coeffs, epsilon=1e-6)





# --- CODE FROM NOTEBOOK: scripts\CHƯƠNG 2 GIẢI PHƯƠNG TRÌNH PHI TUYẾN 1 CHIỀU\Lặp đơn (1 chiều).ipynb ---


import numpy as np
from IPython.display import display, Math, Markdown

def lap_don_1d(g, x0, max_iter=None, epsilon=None):
    # Phương pháp Lap don 1 chieu (Fixed-Point Iteration)
    # g: hàm lặp g(x) sao cho x = g(x) tương đương f(x) = 0
    # x0: xấp xỉ khởi đầu
    # max_iter: số vòng lặp cố định
    # epsilon: sai so |x_{k+1} - x_k|
    display(Markdown("## ❖ PHƯƠNG PHÁP LẶP ĐƠN 1 CHIỀU"))
    display(Math(r"x_{k+1} = g(x_k)"))

    history = [(0, float(x0), None)]
    x_k = float(x0)
    k = 0
    while True:
        k += 1
        x_new = g(x_k)
        err   = abs(x_new - x_k)
        history.append((k, x_new, err))

        stop = False
        if max_iter is not None and k >= max_iter: stop = True
        if epsilon  is not None and err < epsilon:  stop = True
        if k >= 200: stop = True
        if stop: break
        x_k = x_new

    n = len(history) - 1
    display(Markdown(f"### Kết quả ({n} vòng lặp)"))
    cols = ["$k$", "$x_k$", "$\\|x_{k+1}-x_k\\|$"]
    seps = [":---:"]*3
    rows = []
    for (k_, x_, er_) in history:
        er_str = f"${er_:.4e}$" if er_ is not None else "—"
        rows.append([f"${k_}$", f"${x_:.10f}$", er_str])
    header = "| " + " | ".join(cols) + " |"
    sep    = "| " + " | ".join(seps) + " |"
    lines  = [header, sep]
    m = len(rows)
    for r in rows: lines.append("| " + " | ".join(r) + " |")
    display(Markdown("\n".join(lines)))

    x_star = history[-1][1]
    display(Markdown(f"**Nghiệm xấp xỉ:** $x^* \\approx {x_star:.10f}$"))
    return x_star

# ═══════════════════════════════════════════════════════════════════
# NHẬP DỮ LIỆU CỦA BẠN VÀO ĐÂY
# ═══════════════════════════════════════════════════════════════════
# Vi du: x^3 - x - 2 = 0  =>  x = (x+2)^(1/3)
g = lambda x: (x + 2) ** (1.0/3)

x0 = 1.5          # xấp xỉ khởi đầu
# ═══════════════════════════════════════════════════════════════════

lap_don_1d(g, x0, max_iter=None, epsilon=1e-6)





# --- CODE FROM NOTEBOOK: scripts\CHƯƠNG 2 GIẢI PHƯƠNG TRÌNH PHI TUYẾN 1 CHIỀU\So sánh các phương pháp (Lý thuyết).ipynb ---


from IPython.display import Markdown, display

md = [
    "## ❖ SO SÁNH ƯU NHƯỢC ĐIỂM CỦA CÁC PHƯƠNG PHÁP GIẢI GẦN ĐÚNG PHƯƠNG TRÌNH $f(x) = 0$",
    "",
    "| Phương pháp | Cấp hội tụ | Ưu điểm (Nên dùng khi nào?) | Nhược điểm (Khi nào thất bại?) |",
    "| :--- | :--- | :--- | :--- |",
    "| **1. Chia đôi (Bisection)** | Tuyến tính ($p=1$) | - Đơn giản, vô cùng dễ lập trình.<br>- Chắc chắn hội tụ 100% nếu xác định được khoảng $[a, b]$ chứa nghiệm (sao cho $f(a)f(b)<0$).<br>- Tính toán và kiểm soát sai số rất trực quan. | - Tốc độ hội tụ **rất chậm**.<br>- Cần phải biết trước khoảng cách ly nghiệm.<br>- Sẽ **thất bại** nếu nghiệm là nghiệm kép hoặc đồ thị chỉ tiếp xúc với trục hoành (vì không có sự đổi dấu). |",
    "| **2. Dây cung (Secant)** | $p \\approx 1.618$ | - Tốc độ hội tụ khá nhanh (nhanh hơn Chia đôi).<br>- Điểm mạnh lớn nhất là **không cần phải tính công thức đạo hàm $f'(x)$** như phương pháp Newton. | - Tốc độ hội tụ vẫn chậm hơn Newton.<br>- Đòi hỏi phải chọn 2 giá trị xấp xỉ khởi đầu $x_0, x_1$ đủ gần với nghiệm.<br>- Có thể bị phân kỳ nếu đồ thị hàm số biến thiên quá phức tạp. |",
    "| **3. Tiếp tuyến (Newton-Raphson)** | Bậc 2 ($p=2$) | - Tốc độ hội tụ **cực kỳ nhanh** (số lượng chữ số chính xác tăng gấp đôi sau mỗi bước lặp). | - Bắt buộc phải tính được công thức đạo hàm bậc 1 $f'(x)$.<br>- Phương pháp sẽ **thất bại ngay lập tức** (chia cho 0) nếu tại bước lặp nào đó có tiếp tuyến nằm ngang ($f'(x_k) = 0$).<br>- Đòi hỏi giá trị khởi đầu $x_0$ phải nằm trong lân cận rất gần với nghiệm. |",
    "| **4. Lặp đơn (Fixed Point)** | Tuyến tính | - Công thức lặp $x_{k+1} = g(x_k)$ tự nhiên, dễ code.<br>- Không cần tính đạo hàm (nếu không cần kiểm tra điều kiện).<br>- Có thể tổng quát hóa áp dụng cho cả hệ phương trình phi tuyến. | - Điều kiện để hội tụ vô cùng khắt khe: Bắt buộc $|g'(x)| < 1$ trong lân cận nghiệm (nếu $\\ge 1$ sẽ bị phân kỳ đẩy ra xa).<br>- Tốc độ hội tụ bị phụ thuộc vào hằng số Lipschitz $q$, nếu $q$ sát 1 thì hội tụ cực kỳ chậm.<br>- Phải mất công biến đổi phương trình $f(x)=0$ thành dạng $x = g(x)$ thích hợp. |",
    "",
    "---",
    "*Ghi chú: Nội dung trên là bảng so sánh chuẩn chỉ nhất, bạn có thể bê nguyên văn vào giấy thi tự luận để lấy điểm tuyệt đối câu phân tích lý thuyết.*"
]

display(Markdown('\n'.join(md)))








# --- CODE FROM NOTEBOOK: scripts\CHƯƠNG 2 GIẢI PHƯƠNG TRÌNH PHI TUYẾN 1 CHIỀU\Tiếp tuyến (Newton).ipynb ---


import numpy as np
from IPython.display import display, Math, Markdown

def tiep_tuyen(f, df, x0, max_iter=None, epsilon=None):
    # Phương pháp Tiep tuyen (Newton-Raphson)
    # f: ham f(x)
    # df: đạo hàm f'(x)
    # x0: xấp xỉ khởi đầu
    # max_iter: số vòng lặp cố định
    # epsilon: sai so |x_{k+1} - x_k|
    display(Markdown("## ❖ PHƯƠNG PHÁP TIẾP TUYẾN (NEWTON-RAPHSON)"))
    display(Math(r"x_{k+1} = x_k - \frac{f(x_k)}{f'(x_k)}"))

    history = [(0, float(x0), f(float(x0)), None)]
    x_k = float(x0)
    k = 0
    while True:
        k += 1
        fk  = f(x_k)
        dfk = df(x_k)
        if abs(dfk) < 1e-14:
            display(Markdown("⚠️ **Cảnh báo:** f'(x_k) xap xi 0 - tiếp tuyến nằm ngang!"))
            break
        x_new = x_k - fk / dfk
        err   = abs(x_new - x_k)
        history.append((k, x_new, f(x_new), err))

        stop = False
        if max_iter is not None and k >= max_iter: stop = True
        if epsilon  is not None and err < epsilon:  stop = True
        if k >= 200: stop = True
        if stop: break
        x_k = x_new

    n = len(history) - 1
    display(Markdown(f"### Kết quả ({n} vòng lặp)"))
    cols = ["$k$", "$x_k$", "$f(x_k)$", "$\\|x_{k+1}-x_k\\|$"]
    seps = [":---:"]*4
    rows = []
    for (k_, x_, fx_, er_) in history:
        er_str = f"${er_:.4e}$" if er_ is not None else "—"
        rows.append([f"${k_}$", f"${x_:.10f}$", f"${fx_:.4e}$", er_str])
    header = "| " + " | ".join(cols) + " |"
    sep    = "| " + " | ".join(seps) + " |"
    lines  = [header, sep]
    m = len(rows)
    for r in rows: lines.append("| " + " | ".join(r) + " |")
    display(Markdown("\n".join(lines)))

    x_star = history[-1][1]
    display(Markdown(f"**Nghiệm xấp xỉ:** $x^* \\approx {x_star:.10f}$"))
    display(Math(f"f(x^*) = {f(x_star):.6e} \\approx 0"))
    return x_star

# ═══════════════════════════════════════════════════════════════════
# NHẬP DỮ LIỆU CỦA BẠN VÀO ĐÂY
# ═══════════════════════════════════════════════════════════════════
f  = lambda x: x**3 - x - 2
df = lambda x: 3*x**2 - 1

x0 = 2.0         # xấp xỉ khởi đầu
# ═══════════════════════════════════════════════════════════════════

tiep_tuyen(f, df, x0, max_iter=None, epsilon=1e-10)





# --- CODE FROM NOTEBOOK: scripts\CHƯƠNG 3 GIẢI HỆ PHƯƠNG TRÌNH PHI TUYẾN NHIỀU CHIỀU\Lặp đơn nhiều chiều.ipynb ---


import numpy as np
from IPython.display import display, Math, Markdown

def _vec_latex(v, p=6):
    inner = " \\\\ ".join([f"{x:.{p}f}" for x in v])
    return f"\\begin{{bmatrix}} {inner} \\end{{bmatrix}}^T"

def lap_don_nhieu_chieu(G, x0, max_iter=None, epsilon=None):
    # Phương pháp Lap don nhieu chieu: x = G(x)
    # G: ham vector G: R^n -> R^n
    # x0: vector xấp xỉ khởi đầu (list hoac ndarray)
    # max_iter: số vòng lặp cố định
    # epsilon: sai so ||x_{k+1} - x_k||_inf
    display(Markdown("## ❖ PHƯƠNG PHÁP LẶP ĐƠN NHIỀU CHIỀU"))
    display(Math(r"x^{(k+1)} = G(x^{(k)})"))

    x_k = np.array(x0, dtype=float)
    display(Math(f"x^{{(0)}} = {_vec_latex(x_k)}"))

    history = [x_k.copy()]
    k = 0
    while True:
        k += 1
        x_new = np.array(G(x_k), dtype=float)
        err   = np.linalg.norm(x_new - x_k, np.inf)
        history.append(x_new.copy())

        stop = False
        if max_iter is not None and k >= max_iter: stop = True
        if epsilon  is not None and err < epsilon:  stop = True
        if k >= 200: stop = True
        if stop: break
        x_k = x_new

    n = len(history) - 1
    display(Markdown(f"### Kết quả ({n} vòng lặp)"))

    for i, v in enumerate(history):
        display(Math(f"x^{{({i})}} = {_vec_latex(v)}"))

    err_final = np.linalg.norm(history[-1] - history[-2], np.inf)
    display(Markdown(f"**Sai số cuối:** $\\|x^{{({n})}} - x^{{({n-1})}}\\|_{{\\infty}} = {err_final:.4e}$"))
    return history[-1]

# ═══════════════════════════════════════════════════════════════════
# NHẬP DỮ LIỆU CỦA BẠN VÀO ĐÂY
# ═══════════════════════════════════════════════════════════════════
# Vi du: giai hệ phi tuyến:
#   x1 = cos(x2) / 2
#   x2 = (sin(x1) + 1) / 3
def G(x):
    return [np.cos(x[1]) / 2.0,
            (np.sin(x[0]) + 1) / 3.0]

x0 = [0.5, 0.5]   # xấp xỉ khởi đầu
# ═══════════════════════════════════════════════════════════════════

lap_don_nhieu_chieu(G, x0, max_iter=None, epsilon=1e-6)





# --- CODE FROM NOTEBOOK: scripts\CHƯƠNG 3 GIẢI HỆ PHƯƠNG TRÌNH PHI TUYẾN NHIỀU CHIỀU\Newton nhiều chiều.ipynb ---


import numpy as np
from IPython.display import display, Math, Markdown

def _vec_latex(v, p=6):
    inner = " \\\\ ".join([f"{x:.{p}f}" for x in v])
    return f"\\begin{{bmatrix}} {inner} \\end{{bmatrix}}^T"

def _mat_latex(M, p=6):
    rows = " \\\\ ".join([" & ".join([f"{x:.{p}f}" for x in row]) for row in M])
    return f"\\begin{{bmatrix}} {rows} \\end{{bmatrix}}"

def newton_nhieu_chieu(F, J, x0, max_iter=None, epsilon=None):
    # Phương pháp Newton nhieu chieu
    # F: ham vector F: R^n -> R^n (can tim nghiem F(x)=0)
    # J: ham Jacobian J(x) tra ve ma trận n x n
    # x0: vector xấp xỉ khởi đầu
    # max_iter: số vòng lặp cố định
    # epsilon: sai so ||x_{k+1} - x_k||_inf
    display(Markdown("## ❖ PHƯƠNG PHÁP NEWTON NHIỀU CHIỀU"))
    display(Math(r"x^{(k+1)} = x^{(k)} - J(x^{(k)})^{-1} F(x^{(k)})"))

    x_k = np.array(x0, dtype=float)
    display(Math(f"x^{{(0)}} = {_vec_latex(x_k)}"))

    history = [x_k.copy()]
    k = 0
    while True:
        k += 1
        Fk = np.array(F(x_k), dtype=float)
        Jk = np.array(J(x_k), dtype=float)

        display(Markdown(f"#### Bước lặp $k = {k}$"))
        display(Math(f"F(x^{{({k-1})}}) = {_vec_latex(Fk)}"))
        display(Math(f"J(x^{{({k-1})}}) = {_mat_latex(Jk)}"))

        try:
            delta = np.linalg.solve(Jk, -Fk)
        except np.linalg.LinAlgError:
            display(Markdown("⚠️ **Cảnh báo:** Jacobian suy biến!"))
            break

        x_new = x_k + delta
        err   = np.linalg.norm(delta, np.inf)
        display(Math(f"x^{{({k})}} = {_vec_latex(x_new)}"))
        display(Markdown(f"Sai số: $\\|\\Delta x\\|_{{\\infty}} = {err:.4e}$"))

        history.append(x_new.copy())

        stop = False
        if max_iter is not None and k >= max_iter: stop = True
        if epsilon  is not None and err < epsilon:  stop = True
        if k >= 100: stop = True
        if stop: break
        x_k = x_new

    n = len(history) - 1
    display(Markdown(f"### Kết quả ({n} vòng lặp)"))
    x_star = history[-1]
    display(Math(f"x^* = {_vec_latex(x_star)}"))
    Fstar = np.array(F(x_star), dtype=float)
    display(Markdown("**Kiểm tra nghiệm:**"))
    display(Math(f"F(x^*) = {_vec_latex(Fstar)} \\approx 0"))
    return x_star

# ═══════════════════════════════════════════════════════════════════
# NHẬP DỮ LIỆU CỦA BẠN VÀO ĐÂY
# ═══════════════════════════════════════════════════════════════════
# Vi du: giai hệ phi tuyến F(x) = 0
#   x1^2 + x2^2 - 1 = 0
#   x1 - x2^2       = 0
def F(x):
    return [x[0]**2 + x[1]**2 - 1,
            x[0]   - x[1]**2]

def J(x):
    return [[2*x[0], 2*x[1]],
            [1,     -2*x[1]]]

x0 = [0.8, 0.6]   # xấp xỉ khởi đầu
# ═══════════════════════════════════════════════════════════════════

newton_nhieu_chieu(F, J, x0, max_iter=None, epsilon=1e-8)





# --- CODE FROM NOTEBOOK: scripts\CHƯƠNG 4 GIẢI HỆ ĐẠI SỐ TUYẾN TÍNH & TÌM MA TRẬN NGHỊCH ĐẢO\LU có Pivoting.ipynb ---


import numpy as np
from IPython.display import display, Math, Markdown

def _mat(M, p=4):
    if hasattr(M[0], "__len__"):
        rows = " \\\\ ".join([" & ".join([f"{x:.{p}f}" for x in row]) for row in M])
        return f"\\begin{{bmatrix}} {rows} \\end{{bmatrix}}"
    inner = " \\\\ ".join([f"{x:.{p}f}" for x in M])
    return f"\\begin{{bmatrix}} {inner} \\end{{bmatrix}}^T"

def LU_Pivoting(A_input, b_input=None):
    # Phân tách LU voi chon pivot rieng phan (PA = LU)
    # A_input: ma trận vuong n x n
    # b_input: ve phai (tuy chon) de giai he Ax = b
    A = np.array(A_input, dtype=float)
    n = A.shape[0]
    display(Markdown("## ❖ PHÂN TÁCH LU CÓ HOÁN VỊ ($PA = LU$)"))
    display(Math(f"A = {_mat(A)}"))

    P = np.eye(n)
    L = np.zeros((n, n))
    U = A.copy()

    for k in range(n - 1):
        # Chon pivot
        max_row = k + np.argmax(np.abs(U[k:, k]))
        if max_row != k:
            U[[k, max_row], :] = U[[max_row, k], :]
            P[[k, max_row], :] = P[[max_row, k], :]
            if k > 0:
                L[[k, max_row], :k] = L[[max_row, k], :k]
            display(Markdown(f"Hoán vị hàng {k+1} va hàng {max_row+1}"))

        for i in range(k + 1, n):
            if abs(U[k, k]) < 1e-14: continue
            m = U[i, k] / U[k, k]
            L[i, k] = m
            U[i, :] -= m * U[k, :]
        L[k, k] = 1.0

    L[n-1, n-1] = 1.0

    display(Markdown("### Kết quả phân tách"))
    display(Math(f"P = {_mat(P)}"))
    display(Math(f"L = {_mat(L)}"))
    display(Math(f"U = {_mat(U)}"))
    display(Markdown("**Kiem tra $PA = LU$:**"))
    display(Math(f"PA = {_mat(P @ A_input)}"))
    display(Math(f"LU = {_mat(L @ U)}"))

    if b_input is not None:
        b = np.array(b_input, dtype=float).flatten()
        pb = P @ b
        # Ly = Pb
        display(Markdown("#### Giải $Ly = Pb$"))
        y = np.zeros(n)
        for i in range(n):
            y[i] = pb[i] - sum(L[i, j]*y[j] for j in range(i))
            display(Math(f"y_{{{i+1}}} = {y[i]:.6f}"))
        # Ux = y
        display(Markdown("#### Giải $Ux = y$"))
        x = np.zeros(n)
        for i in range(n - 1, -1, -1):
            x[i] = (y[i] - sum(U[i, j]*x[j] for j in range(i + 1, n))) / U[i, i]
            display(Math(f"x_{{{i+1}}} = {x[i]:.6f}"))
        display(Markdown("**Kiem tra $Ax$:**"))
        display(Math(f"Ax = {_mat(np.array(A_input) @ x)} \\approx b = {_mat(b)}"))
        return L, U, P, x
    return L, U, P

# ═══════════════════════════════════════════════════════════════════
# NHẬP DỮ LIỆU CỦA BẠN VÀO ĐÂY
# ═══════════════════════════════════════════════════════════════════
A = np.array([
    [2.0, 1.0,  1.0],
    [4.0, 3.0,  3.0],
    [8.0, 7.0,  9.0]
])

b = np.array([1.0, 1.0, -1.0])   # bo qua neu chi can phan tach
# ═══════════════════════════════════════════════════════════════════

LU_Pivoting(A, b)








# --- CODE FROM NOTEBOOK: scripts\CHƯƠNG 4 GIẢI HỆ ĐẠI SỐ TUYẾN TÍNH & TÌM MA TRẬN NGHỊCH ĐẢO\Lặp đơn (Hệ phương trình).ipynb ---


import numpy as np
from IPython.display import display, Math, Markdown

def _mat(M, p=4):
    if hasattr(M[0], "__len__"):
        rows = " \\\\ ".join([" & ".join([f"{x:.{p}f}" for x in row]) for row in M])
        return f"\\begin{{bmatrix}} {rows} \\end{{bmatrix}}"
    inner = " \\\\ ".join([f"{x:.{p}f}" for x in M])
    return f"\\begin{{bmatrix}} {inner} \\end{{bmatrix}}^T"

def lap_don_he(B_input, d_input, X0_input=None, epsilon=1e-6, p_norm=np.inf):
    B = np.array(B_input, dtype=float)
    d = np.array(d_input, dtype=float).flatten()
    n = len(d)
    
    if X0_input is None:
        X_k = np.zeros(n)
    else:
        X_k = np.array(X0_input, dtype=float).flatten()
        
    display(Markdown("## ❖ PHƯƠNG PHÁP LẶP ĐƠN (HỆ PHƯƠNG TRÌNH $X = BX + d$)"))
    display(Math(f"B = {_mat(B)} \\quad d = {_mat(d)}"))
    
    q = np.linalg.norm(B, p_norm)
    display(Markdown("### 1. Kiểm tra hội tụ"))
    display(Math(f"\\text{{Chuẩn }} p={p_norm} \\text{{ của B: }} q = {q:.4f}"))
    if q < 1:
        display(Markdown("=> $q < 1$, phương pháp lặp **hội tụ**."))
    else:
        display(Markdown("=> ⚠️ **Cảnh báo:** $q \\ge 1$, chưa chắc hội tụ."))
        
    display(Markdown("### 2. Bảng lặp"))
    
    cols = ["$k$"] + [f"$x_{i+1}$" for i in range(n)] + ["$||X_k - X_{k-1}||$"]
    header = "| " + " | ".join(cols) + " |"
    sep = "| " + " | ".join([":---:"] * len(cols)) + " |"
    lines = [header, sep]
    
    k = 0
    X_prev = None
    
    while True:
        if k > 0:
            diff = np.linalg.norm(X_k - X_prev, p_norm)
            row = [f"${k}$"] + [f"${xi:.6f}$" for xi in X_k] + [f"${diff:.4e}$"]
            lines.append("| " + " | ".join(row) + " |")
            
            # Sai số hậu nghiệm
            err = (q / (1 - q)) * diff if q < 1 else diff
            
            if err < epsilon or k > 200:
                display(Markdown("\n".join(lines)))
                display(Markdown("### 3. Kết luận"))
                display(Markdown(f"Hội tụ tại bước $k = {k}$."))
                display(Math(f"X^* \\approx {_mat(X_k, 6)}"))
                display(Markdown(f"**Sai số hậu nghiệm:** $\\Delta = {err:.4e} \\le {epsilon}$"))
                break
        else:
            row = [f"${k}$"] + [f"${xi:.6f}$" for xi in X_k] + ["-"]
            lines.append("| " + " | ".join(row) + " |")
            
        X_prev = X_k.copy()
        X_k = B @ X_k + d
        k += 1

# ═══════════════════════════════════════════════════════════════════
# NHẬP DỮ LIỆU CỦA BẠN VÀO ĐÂY
# ═══════════════════════════════════════════════════════════════════
# Vi du: Ax = b, viet lai thanh x = Bx + d
# A = I - C voi C la ma trận he so va d la ve phai
A = np.array([
    [10.0, 1.0,  2.0],
    [ 1.0, 10.0, 3.0],
    [ 2.0,  3.0, 10.0]
], dtype=float)

b = np.array([7.0, 8.0, 9.0], dtype=float)
n = len(b)
I = np.eye(n)

# Bien doi ve dang x = Bx + d
B = I - A / np.diag(A)[:, None]
d = b / np.diag(A)
# ═══════════════════════════════════════════════════════════════════

lap_don_he(B, d, np.zeros(n), epsilon=1e-6)





# --- CODE FROM NOTEBOOK: scripts\CHƯƠNG 4 GIẢI HỆ ĐẠI SỐ TUYẾN TÍNH & TÌM MA TRẬN NGHỊCH ĐẢO\Nghịch đảo bằng Cholesky.ipynb ---


import numpy as np
from IPython.display import display, Math, Markdown

def _mat(M, p=4):
    if hasattr(M[0], "__len__"):
        rows = " \\\\ ".join([" & ".join([f"{x:.{p}f}" for x in row]) for row in M])
        return f"\\begin{{bmatrix}} {rows} \\end{{bmatrix}}"
    inner = " \\\\ ".join([f"{x:.{p}f}" for x in M])
    return f"\\begin{{bmatrix}} {inner} \\end{{bmatrix}}^T"

def nghich_dao_Cholesky(A_input):
    # Tim nghich dao A^-1 qua phan tach Cholesky (A = LL^T)
    # Giai LL^T * X = I cột theo cột
    A = np.array(A_input, dtype=float)
    n = A.shape[0]
    display(Markdown("## ❖ TÌM MA TRẬN NGHỊCH ĐẢO $A^{-1}$ QUA CHOLESKY"))
    display(Math(f"A = {_mat(A)}"))

    # Phân tách Cholesky
    L = np.zeros((n, n))
    for i in range(n):
        s = sum(L[i, k]**2 for k in range(i))
        val = A[i, i] - s
        if val <= 0:
            display(Markdown("⚠️ **Cảnh báo:** Không xác định dương — khong the dung Cholesky!"))
            return None
        L[i, i] = np.sqrt(val)
        for j in range(i + 1, n):
            L[j, i] = (A[j, i] - sum(L[j, k]*L[i, k] for k in range(i))) / L[i, i]

    display(Math(f"L = {_mat(L)}"))

    # Giai LL^T x_j = e_j cho moi cot j
    X = np.zeros((n, n))
    for j in range(n):
        e = np.zeros(n); e[j] = 1.0
        # Ly = e
        y = np.zeros(n)
        for i in range(n):
            y[i] = (e[i] - sum(L[i, k]*y[k] for k in range(i))) / L[i, i]
        # L^T x = y
        x = np.zeros(n)
        for i in range(n - 1, -1, -1):
            x[i] = (y[i] - sum(L[k, i]*x[k] for k in range(i + 1, n))) / L[i, i]
        X[:, j] = x

    display(Markdown("### Kết quả"))
    display(Math(f"A^{{-1}} = {_mat(X)}"))
    display(Markdown("**Kiem tra $A \\cdot A^{{-1}}$:**"))
    display(Math(f"A A^{{-1}} = {_mat(A @ X)}"))
    return X

# ═══════════════════════════════════════════════════════════════════
# NHẬP DỮ LIỆU CỦA BẠN VÀO ĐÂY
# ═══════════════════════════════════════════════════════════════════
A = np.array([
    [4.0,  2.0,  2.0],
    [2.0,  5.0,  3.0],
    [2.0,  3.0, 10.0]
])
# ═══════════════════════════════════════════════════════════════════

nghich_dao_Cholesky(A)








# --- CODE FROM NOTEBOOK: scripts\CHƯƠNG 4 GIẢI HỆ ĐẠI SỐ TUYẾN TÍNH & TÌM MA TRẬN NGHỊCH ĐẢO\Nghịch đảo bằng Lặp Jacobi  Gauss-Seidel.ipynb ---


import numpy as np
from IPython.display import Markdown, display, Math

def Inverse_Gauss_Seidel(A_input, epsilon=None, max_iter=50):
    def matrix_to_latex(M, precision=4):
        rows = " \\\\ ".join([" & ".join([f"{x:.{precision}f}" for x in row]) for row in M])
        return f"\\begin{{bmatrix}} {rows} \\end{{bmatrix}}"

    A = np.array(A_input, dtype=float)
    n = A.shape[0]
    I = np.eye(n)
    
    display(Markdown("## ❖ TÌM MA TRẬN NGHỊCH ĐẢO BẰNG PHƯƠNG PHÁP LẶP GAUSS-SEIDEL"))
    display(Math(f"A = {matrix_to_latex(A)}"))
    
    # Check chéo trội
    dom = True
    for i in range(n):
        if abs(A[i, i]) <= sum(abs(A[i, j]) for j in range(n) if j != i):
            dom = False
    if not dom:
        display(Markdown("⚠️ **Lưu ý:** Ma trận $A$ không có tính chéo trội hàng chặt ngặt. Hãy đảm bảo bạn đã biến đổi nó (nhân $A^T$) trước khi đưa vào hàm hoặc chấp nhận rủi ro thuật toán có thể phân kỳ!"))
    
    # Khởi tạo ma trận X
    X_k = np.zeros((n, n))
    history = [X_k.copy()]
    
    k = 0
    while True:
        k += 1
        X_new = X_k.copy()
        
        # Cập nhật Gauss-Seidel cột theo cột
        for col in range(n):
            for i in range(n):
                sum_val = I[i, col]
                for j in range(n):
                    if j != i:
                        sum_val -= A[i, j] * X_new[j, col]
                X_new[i, col] = sum_val / A[i, i]
                
        err = np.linalg.norm(X_new - X_k, np.inf)
        history.append(X_new.copy())
        
        if epsilon is not None and err < epsilon:
            break
        if max_iter is not None and k >= max_iter:
            break
        X_k = X_new

    display(Markdown(f"### Kết quả tính toán (Tổng số vòng lặp: {k})"))
    if epsilon is not None:
        display(Markdown(f"- **Đánh giá sai số:** $\\Delta = {err:.6e} \\le \\epsilon = {epsilon}$"))
        
    # In giá trị trung gian
    mid_idx = k // 2
    display(Markdown(f"- **Giá trị trung gian tại bước lặp {mid_idx}:**"))
    display(Math(f"A^{{-1}}_{{({mid_idx})}} = {matrix_to_latex(history[mid_idx], 5)}"))
    
    # In kết quả cuối
    display(Markdown(f"- **Kết quả xấp xỉ cuối cùng (bước {k}):**"))
    display(Math(f"A^{{-1}}_{{({k})}} = {matrix_to_latex(history[-1], 5)}"))
    
    # Kiểm tra nghiệm
    check_matrix = A @ history[-1]
    display(Markdown(f"### Kiểm tra nghiệm"))
    display(Markdown(f"Tính tích $A \\times A^{{-1}}_{{({k})}}$ để kiểm tra độ chính xác (kỳ vọng xấp xỉ ma trận đơn vị $I$):"))
    display(Math(f"A \\cdot A^{{-1}} \\approx {matrix_to_latex(check_matrix, 4)}"))
    
    err_I = np.linalg.norm(check_matrix - I, np.inf)
    if err_I < 1e-2:
        display(Markdown(f"**Nhận xét:** Tích $A \cdot A^{{-1}}$ rất sát với ma trận đơn vị $I$ (sai số cực đại: {err_I:.4e}). Thuật toán hoạt động chính xác!"))
    else:
        display(Markdown(f"**Nhận xét:** Sai số còn lớn (sai số cực đại: {err_I:.4e}). Nghịch đảo chưa đạt độ chính xác cao."))

# ========================================================
# NHẬP MA TRẬN A CẦN TÌM NGHỊCH ĐẢO VÀO ĐÂY
# Lưu ý: Nếu ma trận không chéo trội, thuật toán có thể phân kỳ

# ═══════════════════════════════════════════════════════════════════
# NHẬP DỮ LIỆU CỦA BẠN VÀO ĐÂY
# ═══════════════════════════════════════════════════════════════════
A = np.array([
    [10.0, 1.0,  2.0],
    [ 1.0, 10.0, 3.0],
    [ 2.0,  3.0, 10.0]
], dtype=float)
# ═══════════════════════════════════════════════════════════════════

Inverse_Gauss_Seidel(A, epsilon=1e-6)



Inverse_Gauss_Seidel(A, max_iter=4)







# --- CODE FROM NOTEBOOK: scripts\CHƯƠNG 4 GIẢI HỆ ĐẠI SỐ TUYẾN TÍNH & TÌM MA TRẬN NGHỊCH ĐẢO\Phân tách Cholesky.ipynb ---


import numpy as np
from IPython.display import display, Math, Markdown

def _mat(M, p=4):
    if hasattr(M[0], "__len__"):
        rows = " \\\\ ".join([" & ".join([f"{x:.{p}f}" for x in row]) for row in M])
        return f"\\begin{{bmatrix}} {rows} \\end{{bmatrix}}"
    inner = " \\\\ ".join([f"{x:.{p}f}" for x in M])
    return f"\\begin{{bmatrix}} {inner} \\end{{bmatrix}}^T"

def phan_tach_Cholesky(A_input):
    # Phân tách Cholesky: A = L * L^T (A phai doi xung xac dinh duong)
    A = np.array(A_input, dtype=float)
    n = A.shape[0]
    display(Markdown("## ❖ PHÂN TÁCH CHOLESKY ($A = L L^T$)"))
    display(Math(f"A = {_mat(A)}"))

    L = np.zeros((n, n))
    for i in range(n):
        # Tinh duong cheo
        s = sum(L[i, k]**2 for k in range(i))
        val = A[i, i] - s
        if val <= 0:
            display(Markdown(f"⚠️ **Cảnh báo:** $A_{{{i+1},{i+1}}} - \\sum l^2 = {val:.4f} \\leq 0$ — ma trận khong xac dinh duong!"))
            return None
        L[i, i] = np.sqrt(val)
        display(Math(f"l_{{{i+1},{i+1}}} = \\sqrt{{A_{{{i+1},{i+1}}} - \\sum_{{k<{i+1}}} l_{{ik}}^2}} = \\sqrt{{{val:.4f}}} = {L[i,i]:.4f}"))

        # Tinh phan duoi duong cheo
        for j in range(i + 1, n):
            s2 = sum(L[j, k] * L[i, k] for k in range(i))
            L[j, i] = (A[j, i] - s2) / L[i, i]
            display(Math(f"l_{{{j+1},{i+1}}} = \\frac{{A_{{{j+1},{i+1}}} - \\sum_{{k}} l_{{jk}}l_{{ik}}}}{{{L[i,i]:.4f}}} = {L[j,i]:.4f}"))

    display(Markdown("### Kết quả"))
    display(Math(f"L = {_mat(L)}"))
    display(Markdown("**Kiểm tra:** $L \\cdot L^T$:"))
    display(Math(f"L L^T = {_mat(L @ L.T)}"))
    return L

def giai_he_Cholesky(A_input, b_input):
    # Giai Ax = b qua Cholesky: Ly = b, L^T x = y
    A = np.array(A_input, dtype=float)
    b = np.array(b_input, dtype=float).flatten()
    n = len(b)
    L = phan_tach_Cholesky(A)
    if L is None: return None

    # Ly = b
    display(Markdown("#### Giải $Ly = b$"))
    y = np.zeros(n)
    for i in range(n):
        y[i] = (b[i] - sum(L[i, j]*y[j] for j in range(i))) / L[i, i]
        display(Math(f"y_{{{i+1}}} = {y[i]:.6f}"))

    # L^T x = y
    display(Markdown("#### Giải $L^T x = y$"))
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - sum(L[j, i]*x[j] for j in range(i + 1, n))) / L[i, i]
        display(Math(f"x_{{{i+1}}} = {x[i]:.6f}"))

    display(Markdown("**Kiểm tra:** $Ax$:"))
    display(Math(f"Ax = {_mat(A @ x)} \\approx b = {_mat(b)}"))
    return x

# ═══════════════════════════════════════════════════════════════════
# NHẬP DỮ LIỆU CỦA BẠN VÀO ĐÂY
# ═══════════════════════════════════════════════════════════════════
# A phai doi xung xac dinh duong
A = np.array([
    [4.0,  12.0, -16.0],
    [12.0, 37.0, -43.0],
    [-16.0, -43.0, 98.0]
])

b = np.array([1.0, 0.0, 0.0])
# ═══════════════════════════════════════════════════════════════════

# Chi phan tach:
# phan_tach_Cholesky(A)

# Hoac giai he Ax = b:
giai_he_Cholesky(A, b)





# --- CODE FROM NOTEBOOK: scripts\CHƯƠNG 4 GIẢI HỆ ĐẠI SỐ TUYẾN TÍNH & TÌM MA TRẬN NGHỊCH ĐẢO\Phân tách LU.ipynb ---


import numpy as np
from IPython.display import display, Math, Markdown

def _mat(M, p=4):
    if hasattr(M[0], "__len__"):
        rows = " \\\\ ".join([" & ".join([f"{x:.{p}f}" for x in row]) for row in M])
        return f"\\begin{{bmatrix}} {rows} \\end{{bmatrix}}"
    inner = " \\\\ ".join([f"{x:.{p}f}" for x in M])
    return f"\\begin{{bmatrix}} {inner} \\end{{bmatrix}}^T"

def phan_tach_LU(A_input):
    # Phân tách LU khong hoán vi: A = L * U
    # A_input: ma trận vuong n x n
    A = np.array(A_input, dtype=float)
    n = A.shape[0]
    display(Markdown("## ❖ PHÂN TÁCH LU (Gaussian Elimination)"))
    display(Math(f"A = {_mat(A)}"))
    display(Math(r"A = L \cdot U"))

    L = np.eye(n)
    U = A.copy()

    for k in range(n - 1):
        display(Markdown(f"#### Khử cột $k = {k+1}$"))
        if abs(U[k, k]) < 1e-14:
            display(Markdown(f"⚠️ **Cảnh báo:** Phan tu pivot $U_{{{k+1},{k+1}}} = 0$ — ma trận suy biến!"))
            return None, None
        for i in range(k + 1, n):
            m = U[i, k] / U[k, k]
            L[i, k] = m
            U[i, :] -= m * U[k, :]
            display(Math(f"l_{{{i+1},{k+1}}} = \\frac{{U_{{{i+1},{k+1}}}}}{{U_{{{k+1},{k+1}}}}} = \\frac{{{U[i,k] + m*U[k,k]:.4f}}}{{{U[k,k]+0:.4f}}} = {m:.4f}"))
        display(Math(f"U \\leftarrow {_mat(U)}"))

    display(Markdown("### Kết quả"))
    display(Math(f"L = {_mat(L)}"))
    display(Math(f"U = {_mat(U)}"))
    display(Markdown("**Kiểm tra:** $L \\cdot U$:"))
    display(Math(f"L \\cdot U = {_mat(L @ U)}"))
    return L, U

def giai_he_LU(A_input, b_input):
    # Giai Ax = b qua phan tach LU: Ly = b, Ux = y
    A = np.array(A_input, dtype=float)
    b = np.array(b_input, dtype=float).flatten()
    n = len(b)
    L, U = phan_tach_LU(A)
    if L is None: return None

    # Giai Ly = b (thay the tien)
    display(Markdown("#### Giải $Ly = b$ (thay thế tiến)"))
    y = np.zeros(n)
    for i in range(n):
        y[i] = b[i] - sum(L[i, j] * y[j] for j in range(i))
        display(Math(f"y_{{{i+1}}} = {y[i]:.6f}"))

    # Giai Ux = y (thay the lui)
    display(Markdown("#### Giải $Ux = y$ (thay thế lùi)"))
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - sum(U[i, j] * x[j] for j in range(i + 1, n))) / U[i, i]
        display(Math(f"x_{{{i+1}}} = {x[i]:.6f}"))

    display(Markdown("**Kiểm tra:** $Ax$:"))
    display(Math(f"Ax = {_mat(A @ x)} \\approx b = {_mat(b)}"))
    return x

# ═══════════════════════════════════════════════════════════════════
# NHẬP DỮ LIỆU CỦA BẠN VÀO ĐÂY
# ═══════════════════════════════════════════════════════════════════
A = np.array([
    [2.0, 1.0,  1.0],
    [4.0, -6.0, 0.0],
    [-2.0, 7.0, 2.0]
])

b = np.array([5.0, -2.0, 9.0])
# ═══════════════════════════════════════════════════════════════════

# Chi phan tach LU:
# phan_tach_LU(A)

# Hoac giai he Ax = b:
giai_he_LU(A, b)





# --- CODE FROM NOTEBOOK: scripts\CHƯƠNG 4 GIẢI HỆ ĐẠI SỐ TUYẾN TÍNH & TÌM MA TRẬN NGHỊCH ĐẢO\Viền quanh.ipynb ---


import numpy as np
from IPython.display import display, Math, Markdown

def _mat(M, p=4):
    if hasattr(M[0], "__len__"):
        rows = " \\\\ ".join([" & ".join([f"{x:.{p}f}" for x in row]) for row in M])
        return f"\\begin{{bmatrix}} {rows} \\end{{bmatrix}}"
    inner = " \\\\ ".join([f"{x:.{p}f}" for x in M])
    return f"\\begin{{bmatrix}} {inner} \\end{{bmatrix}}^T"

def vien_quanh(A_input):
    # Phương pháp Vien quanh de tinh A^-1 theo từng bước tang kich thuoc
    # A_input: ma trận vuong n x n
    A = np.array(A_input, dtype=float)
    n = A.shape[0]
    display(Markdown("## ❖ PHƯƠNG PHÁP VIỀN QUANH (Bordering Method)"))
    display(Math(f"A = {_mat(A)}"))
    display(Markdown("Xây dựng $A_k^{-1}$ tu $A_1^{-1}$ len $A_n^{-1}$ theo từng bước."))

    # A_1^-1
    if abs(A[0, 0]) < 1e-14:
        display(Markdown("⚠️ **Cảnh báo:** A[0,0] = 0"))
        return None
    Ak_inv = np.array([[1.0 / A[0, 0]]])
    display(Math(f"A_1^{{-1}} = {_mat(Ak_inv)}"))

    for k in range(1, n):
        # Phần mở rộng
        a_new = A[:k, k]         # cot k moi (phan tren)
        b_new = A[k, :k]         # hàng k moi (phan trai)
        alpha = A[k, k]          # phan tu goc duoi-phai

        u = Ak_inv @ a_new
        v = b_new @ Ak_inv

        delta = alpha - b_new @ u
        if abs(delta) < 1e-14:
            display(Markdown(f"⚠️ **Cảnh báo:** delta = {delta:.4e} xap xi 0 tai buoc k={k+1}!"))
            return None

        # Công thức viền quanh
        A_new_inv = np.zeros((k + 1, k + 1))
        A_new_inv[:k, :k] = Ak_inv + np.outer(u, v) / delta
        A_new_inv[:k, k]  = -u / delta
        A_new_inv[k, :k]  = -v / delta
        A_new_inv[k, k]   = 1.0 / delta

        Ak_inv = A_new_inv
        display(Markdown(f"**Buoc k = {k+1}:** $\\delta_{{k+1}} = {delta:.4f}$"))
        display(Math(f"A_{{{k+1}}}^{{-1}} = {_mat(Ak_inv)}"))

    display(Markdown("### Kết quả cuối cùng"))
    display(Math(f"A^{{-1}} = {_mat(Ak_inv)}"))
    display(Markdown("**Kiem tra $A \\cdot A^{{-1}}$:**"))
    display(Math(f"A A^{{-1}} = {_mat(A @ Ak_inv)}"))
    return Ak_inv

# ═══════════════════════════════════════════════════════════════════
# NHẬP DỮ LIỆU CỦA BẠN VÀO ĐÂY
# ═══════════════════════════════════════════════════════════════════
A = np.array([
    [3.0, 1.0, 2.0],
    [1.0, 4.0, 1.0],
    [2.0, 1.0, 5.0]
])
# ═══════════════════════════════════════════════════════════════════

vien_quanh(A)





# --- CODE FROM NOTEBOOK: scripts\CHƯƠNG 4 GIẢI HỆ ĐẠI SỐ TUYẾN TÍNH & TÌM MA TRẬN NGHỊCH ĐẢO\Lặp Gauss-Seidel\Lặp Gauss-Seidel (Ax=B).ipynb ---


import numpy as np
from IPython.display import Markdown, display

def Gauss_Seidel_Ax_B(A_input, b_input, max_iter=None, epsilon=None, x0=None):
    def matrix_to_latex(M, precision=4):
        if not isinstance(M, np.ndarray): return str(M)
        elif M.ndim == 1:
            inner = " \\\\ ".join([f"{x:.{precision}f}" for x in M])
            return f"\\begin{{bmatrix}} {inner} \\end{{bmatrix}}"
        else:
            rows = " \\\\ ".join([" & ".join([f"{x:.{precision}f}" for x in row]) for row in M])
            return f"\\begin{{bmatrix}} {rows} \\end{{bmatrix}}"

    A = np.array(A_input, dtype=float)
    b = np.array(b_input, dtype=float).flatten()
    n = len(b)
    
    if x0 is None:
        X_k = np.zeros(n)
    else:
        X_k = np.array(x0, dtype=float)
        
    md = []
    md.append("## ❖ PHƯƠNG PHÁP LẶP GAUSS-SEIDEL (DẠNG $Ax = b$)")
    md.append("---\n")
    md.append("> **📝 HƯỚNG DẪN TRÌNH BÀY BÀI THI:**")
    md.append("> - **Bước 1:** Đưa hệ về dạng $x = Bx + d$ bằng cách rút $x_i$ từ phương trình thứ $i$. Tính $||B||_\\infty$.")
    md.append("> - **Bước 2:** Viết công thức lặp Gauss-Seidel dạng khai triển.")
    md.append("> - **Bước 3:** Kẻ bảng quá trình lặp và ghi số liệu.")
    md.append("> - **Bước 4:** Kết luận nghiệm và sai số nếu được yêu cầu.")
    
    # Biến đổi Ax=b thành x=Bx+d
    D = np.diag(np.diag(A))
    L = np.tril(A, -1)
    U = np.triu(A, 1)
    
    # B = -D^-1 (L + U)
    D_inv = np.linalg.inv(D)
    B = -D_inv @ (L + U)
    d = D_inv @ b
    
    md.append("\n### I. RÚT X VÀ KIỂM TRA ĐIỀU KIỆN HỘI TỤ")
    md.append(f"Hệ tương đương với dạng $x = Bx + d$, với:")
    md.append(f"$$ B = {matrix_to_latex(B, precision=4)} $$")
    md.append(f"$$ d = {matrix_to_latex(d, precision=4)} $$")
    
    norm_B = np.linalg.norm(B, np.inf)
    md.append(f"Chuẩn vô cùng của ma trận $B$: $||B||_\\infty = {norm_B:.4f}$")
    if norm_B < 1:
        md.append(f"Vì $||B||_\\infty < 1$, phương pháp lặp chắc chắn hội tụ.")
    else:
        md.append(f"**Cảnh báo:** $||B||_\\infty \\ge 1$, phương pháp chưa chắc hội tụ.")

    md.append("\n### II. CÔNG THỨC LẶP GAUSS-SEIDEL (KHAI TRIỂN)")
    
    for i in range(n):
        terms = []
        for j in range(n):
            val = B[i, j]
            if abs(val) < 1e-10: continue
            
            sign = " + " if val > 0 else " - "
            if j < i:
                terms.append(f"{sign}{abs(val):.4f} x_{{{j+1}}}^{{(k+1)}}")
            else:
                terms.append(f"{sign}{abs(val):.4f} x_{{{j+1}}}^{{(k)}}")
        
        formula = "".join(terms).lstrip(" + ")
        d_sign = f" + {d[i]:.4f}" if d[i] >= 0 else f" - {abs(d[i]):.4f}"
        md.append(f"- $x_{{{i+1}}}^{{(k+1)}} = {formula}{d_sign}$")
        
    md.append("\n---\n### III. BẢNG QUÁ TRÌNH LẶP")
    
    header = "| $k$ | " + " | ".join([f"$x_{{{i+1}}}$" for i in range(n)]) + " | Sai số $||x^{(k)} - x^{(k-1)}||_\\infty$ |"
    md.append(header)
    md.append("|---" * (n + 2) + "|")
    
    row0 = f"| 0 | " + " | ".join([f"{x:.5f}" for x in X_k]) + " | - |"
    md.append(row0)
    
    k = 1
    max_safe_iters = max_iter if max_iter is not None else 100
    
    while True:
        X_new = np.copy(X_k)
        for i in range(n):
            s1 = sum(B[i][j] * X_new[j] for j in range(i))
            s2 = sum(B[i][j] * X_k[j] for j in range(i, n))
            X_new[i] = s1 + s2 + d[i]
            
        sai_so = np.linalg.norm(X_new - X_k, np.inf)
        row = f"| {k} | " + " | ".join([f"{x:.5f}" for x in X_new]) + f" | {sai_so:.5f} |"
        md.append(row)
        X_k = X_new
        
        stop_eps = (epsilon is not None) and (sai_so <= epsilon)
        stop_iter = (max_iter is not None) and (k >= max_iter)
        if stop_eps or stop_iter or k >= max_safe_iters:
            break
        k += 1
        
    md.append("\n---\n### IV. KẾT LUẬN")
    md.append(f"Hệ dừng lại tại bước lặp $k = {k}$. Nghiệm gần đúng là:")
    md.append(f"$$ x^{{({k})}} = {matrix_to_latex(X_k, precision=5)} $$")
    
    display(Markdown('\n'.join(md)))

# Ma trận cung cầu A (Kích thước 10x10)

# ═══════════════════════════════════════════════════════════════════
# NHẬP DỮ LIỆU CỦA BẠN VÀO ĐÂY
# ═══════════════════════════════════════════════════════════════════

# ═══════════════════════════════════════════════════════════════════
# NHẬP DỮ LIỆU CỦA BẠN VÀO ĐÂY
# ═══════════════════════════════════════════════════════════════════

# ═══════════════════════════════════════════════════════════════════
# NHẬP DỮ LIỆU CỦA BẠN VÀO ĐÂY
# ═══════════════════════════════════════════════════════════════════
A = np.array([
    [10.0, 1.0,  2.0],
    [ 1.0, 10.0, 3.0],
    [ 2.0,  3.0, 10.0]
], dtype=float)

b = np.array([7.0, 8.0, 9.0], dtype=float)
# ═══════════════════════════════════════════════════════════════════

Gauss_Seidel_Ax_B(A, b, max_iter=None, epsilon=1e-6)








# --- CODE FROM NOTEBOOK: scripts\CHƯƠNG 4 GIẢI HỆ ĐẠI SỐ TUYẾN TÍNH & TÌM MA TRẬN NGHỊCH ĐẢO\Lặp Gauss-Seidel\Lặp Gauss-Seidel (x=Bx+d).ipynb ---


import numpy as np
from IPython.display import Markdown, display, Math

def Gauss_Seidel_Bd(B_input, d_input, max_iter=None, epsilon=None, x0=None):
    def matrix_to_latex(M, precision=4):
        if not isinstance(M, np.ndarray): return str(M)
        elif M.ndim == 1:
            inner = " \\\\ ".join([f"{x:.{precision}f}" for x in M])
            return f"\\begin{{bmatrix}} {inner} \\end{{bmatrix}}^T"
        else:
            rows = " \\\\ ".join([" & ".join([f"{x:.{precision}f}" for x in row]) for row in M])
            return f"\\begin{{bmatrix}} {rows} \\end{{bmatrix}}"

    B = np.array(B_input, dtype=float)
    d = np.array(d_input, dtype=float).flatten()
    n = len(d)
    
    if x0 is None:
        x_k = np.zeros(n)
    else:
        x_k = np.array(x0, dtype=float).flatten()
        
    display(Markdown("## ❖ PHƯƠNG PHÁP LẶP GAUSS-SEIDEL CHO HỆ $x = Bx + d$"))
    display(Math(f"B = {matrix_to_latex(B)}, \\quad d = {matrix_to_latex(d)}"))
    
    history = [x_k.copy()]
    
    k = 0
    while True:
        k += 1
        x_new = x_k.copy()
        for i in range(n):
            sum_val = d[i]
            for j in range(n):
                sum_val += B[i][j] * x_new[j]
            x_new[i] = sum_val
            
        err = np.linalg.norm(x_new - x_k, np.inf)
        history.append(x_new.copy())
        
        if max_iter is not None and k >= max_iter:
            break
        if epsilon is not None and err < epsilon:
            break
        if k >= 100:
            display(Markdown(f"**Cảnh báo:** Thuật toán chưa hội tụ sau {k} vòng lặp."))
            break
            
        x_k = x_new
        
    # IN KẾT QUẢ ĐÃ ĐƯỢC TỐI ƯU TRÌNH BÀY
    display(Markdown(f"### Kết quả tính toán (Tổng số vòng lặp: {k})"))
    
    for idx, val in enumerate(history):
        display(Math(f"x^{({idx})} = {matrix_to_latex(val)}"))
    if epsilon is not None:
        display(Math(f"\\|x^{{({k})}} - x^{{({k-1})}}\\|_\\infty = {err:.6e} < \\epsilon = {epsilon}"))

# DỮ LIỆU ĐỀ BÀI
C = np.array([
    [0.1588, 0.0064, 0.0025, 0.0304, 0.0014, 0.0083, 0.1594],
    [0.0057, 0.2645, 0.0436, 0.0099, 0.0083, 0.0201, 0.3413],
    [0.0264, 0.1506, 0.3557, 0.0139, 0.0142, 0.0070, 0.0236],
    [0.3299, 0.0565, 0.0495, 0.3636, 0.0204, 0.0483, 0.0649],
    [0.0089, 0.0081, 0.0333, 0.0295, 0.3412, 0.0237, 0.0020],
    [0.1190, 0.0901, 0.0996, 0.1260, 0.1722, 0.2368, 0.3369],
    [0.0063, 0.0126, 0.0196, 0.0098, 0.0064, 0.0132, 0.0012]
], dtype=float)

d = np.array([74000, 56000, 10500, 25000, 17500, 196000, 5000], dtype=float)

# Lặp Gauss-Seidel tìm lượng sản phẩm cần thiết
Gauss_Seidel_Bd(C, d, max_iter=None, epsilon=1e-4)








# --- CODE FROM NOTEBOOK: scripts\CHƯƠNG 4 GIẢI HỆ ĐẠI SỐ TUYẾN TÍNH & TÌM MA TRẬN NGHỊCH ĐẢO\Lặp Gauss-Seidel\Lặp Gauss-Seidel (Đổi dòng tạo chéo trội).ipynb ---


import numpy as np
import itertools
from IPython.display import Markdown, display

def Check_And_Permute_Dominant(A, b):
    n = A.shape[0]
    for perm in itertools.permutations(range(n)):
        A_perm = A[list(perm), :]
        b_perm = b[list(perm)]
        
        is_dominant = True
        for i in range(n):
            if np.abs(A_perm[i, i]) <= np.sum(np.abs(A_perm[i])) - np.abs(A_perm[i, i]):
                is_dominant = False
                break
        if is_dominant:
            return True, A_perm, b_perm, perm
    return False, A, b, None

def Gauss_Seidel_Ax_B_Permute(A_input, b_input, max_iter=None, epsilon=None, x0=None):
    def matrix_to_latex(M, precision=4):
        if not isinstance(M, np.ndarray): return str(M)
        elif M.ndim == 1:
            inner = " \\\\ ".join([f"{x:.{precision}f}" for x in M])
            return f"\\begin{{bmatrix}} {inner} \\end{{bmatrix}}"
        else:
            rows = " \\\\ ".join([" & ".join([f"{x:.{precision}f}" for x in row]) for row in M])
            return f"\\begin{{bmatrix}} {rows} \\end{{bmatrix}}"

    A_origin = np.array(A_input, dtype=float)
    b_origin = np.array(b_input, dtype=float).flatten()
    n = len(b_origin)
    
    if x0 is None: X_k = np.zeros(n)
    else: X_k = np.array(x0, dtype=float)
        
    md = []
    md.append("## ❖ GAUSS-SEIDEL (CÓ TỰ ĐỘNG ĐỔI DÒNG TẠO CHÉO TRỘI)")
    md.append("---\n")
    
    md.append("### I. TỰ ĐỘNG KIỂM TRA VÀ ĐỔI DÒNG")
    md.append("Hệ ban đầu:")
    md.append(f"$$ A_{{ban\\_dau}} = {matrix_to_latex(A_origin, 2)} \\quad b_{{ban\\_dau}} = {matrix_to_latex(b_origin, 2)} $$\n")
    
    is_dom, A, b, perm = Check_And_Permute_Dominant(A_origin, b_origin)
    
    if is_dom and perm != tuple(range(n)):
        md.append(f"**✅ ĐÃ ĐỔI DÒNG THÀNH CÔNG!** Thứ tự các hàng mới: {perm}")
        md.append(f"$$ A = {matrix_to_latex(A, 2)} \\quad b = {matrix_to_latex(b, 2)} $$\n")
        md.append("Ma trận A mới đã **chéo trội hàng ngặt**, đảm bảo Gauss-Seidel hội tụ.")
    elif is_dom:
        md.append("**✅ Hợp lệ:** Ma trận ban đầu đã chéo trội hàng ngặt sẵn, không cần đổi dòng.")
        A, b = A_origin, b_origin
    else:
        md.append("**⚠️ Cảnh báo:** Đã thử mọi hoán vị nhưng không thể tạo ra ma trận chéo trội hàng ngặt.")
        A, b = A_origin, b_origin

    # Biến đổi Ax=b thành x=Bx+d
    D = np.diag(np.diag(A))
    L = np.tril(A, -1)
    U = np.triu(A, 1)
    D_inv = np.linalg.inv(D)
    B = -D_inv @ (L + U)
    d = D_inv @ b
    
    md.append("\n### II. RÚT X VÀ BIẾN ĐỔI THÀNH DẠNG x = Bx + d")
    md.append(f"$$ B = {matrix_to_latex(B, precision=4)} \\quad d = {matrix_to_latex(d, precision=4)} $$")
    
    norm_B = np.linalg.norm(B, np.inf)
    md.append(f"- **Chuẩn vô cùng của B:** $q = ||B||_\\infty = {norm_B:.4f}$")
    
    md.append("\n---\n### III. BẢNG QUÁ TRÌNH LẶP")
    
    header = "| $k$ | " + " | ".join([f"$x_{{{i+1}}}$" for i in range(n)]) + " | Sai số $||x^{(k)} - x^{(k-1)}||_\\infty$ |"
    md.append(header)
    md.append("|---" * (n + 2) + "|")
    
    row0 = f"| 0 | " + " | ".join([f"{x:.5f}" for x in X_k]) + " | - |"
    md.append(row0)
    
    k = 1
    max_safe_iters = max_iter if max_iter is not None else 100
    
    while True:
        X_new = np.copy(X_k)
        for i in range(n):
            s1 = sum(B[i][j] * X_new[j] for j in range(i))
            s2 = sum(B[i][j] * X_k[j] for j in range(i, n))
            X_new[i] = s1 + s2 + d[i]
            
        sai_so = np.linalg.norm(X_new - X_k, np.inf)
        row = f"| {k} | " + " | ".join([f"{x:.5f}" for x in X_new]) + f" | {sai_so:.5f} |"
        md.append(row)
        X_k = X_new
        
        stop_eps = (epsilon is not None) and (sai_so <= epsilon)
        stop_iter = (max_iter is not None) and (k >= max_iter)
        if stop_eps or stop_iter or k >= max_safe_iters:
            break
        k += 1
        
    md.append("\n---\n### IV. KẾT LUẬN")
    md.append(f"Hệ dừng lại tại bước lặp $k = {k}$. Nghiệm gần đúng là:")
    md.append(f"$$ x^{{({k})}} = {matrix_to_latex(X_k, precision=5)} $$")
    
    display(Markdown('\n'.join(md)))

# Ma trận hệ số A (Cố tình để lộn xộn để test tự động đổi dòng)

# ═══════════════════════════════════════════════════════════════════
# NHẬP DỮ LIỆU CỦA BẠN VÀO ĐÂY
# ═══════════════════════════════════════════════════════════════════
A = np.array([
    [ 2.0, 10.0,  1.0],
    [10.0,  1.0,  2.0],
    [ 1.0,  2.0, 10.0]
], dtype=float)

b = np.array([13.0, 13.0, 13.0], dtype=float)
# ═══════════════════════════════════════════════════════════════════

Gauss_Seidel_Ax_B_Permute(A, b, max_iter=None, epsilon=1e-6)








# --- CODE FROM NOTEBOOK: scripts\CHƯƠNG 4 GIẢI HỆ ĐẠI SỐ TUYẾN TÍNH & TÌM MA TRẬN NGHỊCH ĐẢO\Lặp Jacobi - Lặp Đơn\Lặp Jacobi (Ax=b).ipynb ---


import numpy as np
from IPython.display import display, Math, Markdown

def matrix_to_latex(M, precision=4):
    if not isinstance(M, np.ndarray): return str(M)
    elif M.ndim == 1:
        inner = " \\\\ ".join([f"{x:.{precision}f}" for x in M])
        return f"\\begin{{bmatrix}} {inner} \\end{{bmatrix}}^T"
    else:
        rows = " \\\\ ".join([" & ".join([f"{x:.{precision}f}" for x in row]) for row in M])
        return f"\\begin{{bmatrix}} {rows} \\end{{bmatrix}}"

def Jacobi_Ax_b(A_input, b_input, x0_input=None, num_iters=None, epsilon=None):
    A = np.array(A_input, dtype=float)
    b = np.array(b_input, dtype=float).flatten()
    n = len(b)
    
    if x0_input is None: x_k = np.zeros(n)
    else: x_k = np.array(x0_input, dtype=float).flatten()
    
    md = []
    md.append("## ❖ PHƯƠNG PHÁP LẶP JACOBI (Giải hệ $Ax = b$)")
    md.append("---\n")
    
    md.append("### I. CHÉO TRỘI VÀ BIẾN ĐỔI")
    md.append(f"$$ A = {matrix_to_latex(A)} $$")
    
    # Kiểm tra chéo trội hàng
    is_diagonally_dominant = True
    for i in range(n):
        if np.abs(A[i, i]) <= np.sum(np.abs(A[i])) - np.abs(A[i, i]):
            is_diagonally_dominant = False
            break
            
    if is_diagonally_dominant:
        md.append("- **Đánh giá:** Ma trận A là ma trận **chéo trội hàng ngặt**. Thuật toán Jacobi **chắc chắn hội tụ**!")
    else:
        md.append("- **Cảnh báo:** Ma trận A **KHÔNG** chéo trội hàng ngặt. Thuật toán có thể phân kỳ.")

    # Biến đổi
    D = np.diag(np.diag(A))
    L_plus_U = A - D
    D_inv = np.linalg.inv(D)
    B = -D_inv @ L_plus_U
    d = D_inv @ b
    
    md.append("Chuyển hệ phương trình về dạng $x = Bx + d$ với $B = -D^{-1}(L+U)$ và $d = D^{-1}b$:")
    md.append(f"$$ B = {matrix_to_latex(B)} $$")
    md.append(f"$$ d = {matrix_to_latex(d)} $$\n")
    
    q = np.linalg.norm(B, np.inf)
    md.append(f"- **Chuẩn vô cùng của B:** $q = ||B||_\\infty = {q:.5f}$")
    
    md.append("\n---\n### II. BẢNG QUÁ TRÌNH LẶP")
    
    table = ["| $k$ | " + " | ".join([f"$x_{i+1}$" for i in range(n)]) + " | Sai số $||x^{(k)} - x^{(k-1)}||_\\infty$ |",
             "|---|" + "|".join(["---"] * n) + "|---|"]
             
    history = [x_k.copy()]
    k = 0
    while True:
        if k == 0:
            row_str = " | ".join([f"{v:.5f}" for v in x_k])
            table.append(f"| {k} | {row_str} | - |")
        else:
            diff = np.linalg.norm(history[k] - history[k-1], np.inf)
            row_str = " | ".join([f"{v:.5f}" for v in x_k])
            table.append(f"| {k} | {row_str} | {diff:.5f} |")
            
            stop_eps = (epsilon is not None) and (diff <= epsilon or (q/(1-q))*diff <= epsilon if q < 1 else False)
            stop_iter = (num_iters is not None) and (k >= num_iters)
            if stop_eps or stop_iter:
                break
                
        # Lặp Jacobi thực chất là lặp đơn trên dạng x = Bx+d
        x_next = B @ x_k + d
        history.append(x_next.copy())
        x_k = x_next
        k += 1
        
    md.extend(table)
    
    md.append("\n---\n### III. KẾT LUẬN")
    md.append(f"Hệ dừng lại tại bước lặp $k = {k}$. Nghiệm gần đúng là:")
    md.append(f"$$ X^{{({k})}} \\approx {matrix_to_latex(x_k, precision=5)} $$")
    
    diff_final = np.linalg.norm(history[-1] - history[-2], np.inf)
    if q < 1:
        sai_so_hau_nghiem = (q / (1 - q)) * diff_final
        md.append(f"**Sai số hậu nghiệm:** $\\frac{{q}}{{1-q}} ||x^{{({k})}} - x^{{({k-1})}}||_\\infty = {sai_so_hau_nghiem:.5e}$")
    else:
        md.append(f"**Sai số thực tế (khoảng cách 2 bước cuối):** $||x^{{({k})}} - x^{{({k-1})}}||_\\infty = {diff_final:.5e}$")
        
    display(Markdown('\n'.join(md)))

# Ma trận cung cầu A (Kích thước 10x10)

# ═══════════════════════════════════════════════════════════════════
# NHẬP DỮ LIỆU CỦA BẠN VÀO ĐÂY
# ═══════════════════════════════════════════════════════════════════
A = np.array([
    [10.0, 1.0,  2.0],
    [ 1.0, 10.0, 3.0],
    [ 2.0,  3.0, 10.0]
], dtype=float)

b = np.array([7.0, 8.0, 9.0], dtype=float)
# ═══════════════════════════════════════════════════════════════════

Jacobi_Ax_b(A, b, num_iters=100, epsilon=1e-6)








# --- CODE FROM NOTEBOOK: scripts\CHƯƠNG 4 GIẢI HỆ ĐẠI SỐ TUYẾN TÍNH & TÌM MA TRẬN NGHỊCH ĐẢO\Lặp Jacobi - Lặp Đơn\Lặp Jacobi (Đổi dòng tạo chéo trội).ipynb ---


import numpy as np
import itertools
from IPython.display import display, Math, Markdown

def matrix_to_latex(M, precision=4):
    if not isinstance(M, np.ndarray): return str(M)
    elif M.ndim == 1:
        inner = " \\\\ ".join([f"{x:.{precision}f}" for x in M])
        return f"\\begin{{bmatrix}} {inner} \\end{{bmatrix}}^T"
    else:
        rows = " \\\\ ".join([" & ".join([f"{x:.{precision}f}" for x in row]) for row in M])
        return f"\\begin{{bmatrix}} {rows} \\end{{bmatrix}}"

def Check_And_Permute_Dominant(A, b):
    n = A.shape[0]
    for perm in itertools.permutations(range(n)):
        A_perm = A[list(perm), :]
        b_perm = b[list(perm)]
        
        is_dominant = True
        for i in range(n):
            if np.abs(A_perm[i, i]) <= np.sum(np.abs(A_perm[i])) - np.abs(A_perm[i, i]):
                is_dominant = False
                break
        if is_dominant:
            return True, A_perm, b_perm, perm
    return False, A, b, None

def Jacobi_Ax_b_Permute(A_input, b_input, x0_input=None, num_iters=None, epsilon=None):
    A_origin = np.array(A_input, dtype=float)
    b_origin = np.array(b_input, dtype=float).flatten()
    n = len(b_origin)
    
    if x0_input is None: x_k = np.zeros(n)
    else: x_k = np.array(x0_input, dtype=float).flatten()
    
    md = []
    md.append("## ❖ LẶP JACOBI (CÓ TỰ ĐỘNG ĐỔI DÒNG TẠO CHÉO TRỘI)")
    md.append("---\n")
    
    md.append("### I. TỰ ĐỘNG KIỂM TRA VÀ ĐỔI DÒNG")
    md.append("Hệ ban đầu:")
    md.append(f"$$ A_{{ban\\_dau}} = {matrix_to_latex(A_origin)} \\quad b_{{ban\\_dau}} = {matrix_to_latex(b_origin)} $$\n")
    
    is_dom, A, b, perm = Check_And_Permute_Dominant(A_origin, b_origin)
    
    if is_dom and perm != tuple(range(n)):
        md.append(f"**✅ ĐÃ ĐỔI DÒNG THÀNH CÔNG!** Thứ tự các hàng mới: {perm}")
        md.append(f"$$ A = {matrix_to_latex(A)} \\quad b = {matrix_to_latex(b)} $$\n")
        md.append("Ma trận A mới đã **chéo trội hàng ngặt**, đảm bảo Jacobi hội tụ.")
    elif is_dom:
        md.append("**✅ Hợp lệ:** Ma trận ban đầu đã chéo trội hàng ngặt sẵn, không cần đổi dòng.")
        A, b = A_origin, b_origin
    else:
        md.append("**⚠️ Cảnh báo:** Đã thử mọi hoán vị nhưng không thể tạo ra ma trận chéo trội hàng ngặt. Thuật toán có thể phân kỳ.")
        A, b = A_origin, b_origin

    # Biến đổi
    D = np.diag(np.diag(A))
    L_plus_U = A - D
    D_inv = np.linalg.inv(D)
    B = -D_inv @ L_plus_U
    d = D_inv @ b
    
    md.append("\n---\n### II. BIẾN ĐỔI x = Bx + d")
    md.append(f"$$ B = -D^{{-1}}(L+U) = {matrix_to_latex(B)} $$")
    md.append(f"$$ d = D^{{-1}}b = {matrix_to_latex(d)} $$\n")
    
    q = np.linalg.norm(B, np.inf)
    md.append(f"- **Chuẩn vô cùng của B:** $q = ||B||_\\infty = {q:.5f}$")
    
    md.append("\n---\n### III. BẢNG QUÁ TRÌNH LẶP JACOBI")
    
    table = ["| $k$ | " + " | ".join([f"$x_{i+1}$" for i in range(n)]) + " | Sai số $||x^{(k)} - x^{(k-1)}||_\\infty$ |",
             "|---|" + "|".join(["---"] * n) + "|---|"]
             
    history = [x_k.copy()]
    k = 0
    while True:
        if k == 0:
            row_str = " | ".join([f"{v:.5f}" for v in x_k])
            table.append(f"| {k} | {row_str} | - |")
        else:
            diff = np.linalg.norm(history[k] - history[k-1], np.inf)
            row_str = " | ".join([f"{v:.5f}" for v in x_k])
            table.append(f"| {k} | {row_str} | {diff:.5f} |")
            
            stop_eps = (epsilon is not None) and (diff <= epsilon or (q/(1-q))*diff <= epsilon if q < 1 else False)
            stop_iter = (num_iters is not None) and (k >= num_iters)
            if stop_eps or stop_iter:
                break
                
        x_next = B @ x_k + d
        history.append(x_next.copy())
        x_k = x_next
        k += 1
        
    md.extend(table)
    
    md.append("\n---\n### IV. KẾT LUẬN")
    md.append(f"Hệ dừng lại tại bước lặp $k = {k}$. Nghiệm gần đúng là:")
    md.append(f"$$ X^{{({k})}} \\approx {matrix_to_latex(x_k, precision=5)} $$")
    
    diff_final = np.linalg.norm(history[-1] - history[-2], np.inf)
    if q < 1:
        sai_so_hau_nghiem = (q / (1 - q)) * diff_final
        md.append(f"**Sai số hậu nghiệm:** $\\frac{{q}}{{1-q}} ||x^{{({k})}} - x^{{({k-1})}}||_\\infty = {sai_so_hau_nghiem:.5e}$")
    else:
        md.append(f"**Sai số thực tế:** $||x^{{({k})}} - x^{{({k-1})}}||_\\infty = {diff_final:.5e}$")
        
    display(Markdown('\n'.join(md)))

# ═══════════════════════════════════════════════════════════════════
# NHẬP DỮ LIỆU CỦA BẠN VÀO ĐÂY
# ═══════════════════════════════════════════════════════════════════
A = np.array([
    [ 2.0, 10.0,  1.0],
    [10.0,  1.0,  2.0],
    [ 1.0,  2.0, 10.0]
], dtype=float)

b = np.array([13.0, 13.0, 13.0], dtype=float)
# ═══════════════════════════════════════════════════════════════════

Jacobi_Ax_b_Permute(A, b, num_iters=100, epsilon=1e-6)





# --- CODE FROM NOTEBOOK: scripts\CHƯƠNG 4 GIẢI HỆ ĐẠI SỐ TUYẾN TÍNH & TÌM MA TRẬN NGHỊCH ĐẢO\Lặp Jacobi - Lặp Đơn\Lặp Đơn (x=Bx+d).ipynb ---


import numpy as np
from IPython.display import display, Math, Markdown

def Lap_Don_x_Bx_d(B_input, d_input, x0_input=None, num_iters=None, epsilon=None):
    def matrix_to_latex(M, precision=4):
        if not isinstance(M, np.ndarray): return str(M)
        elif M.ndim == 1:
            inner = " \\\\ ".join([f"{x:.{precision}f}" for x in M])
            return f"\\begin{{bmatrix}} {inner} \\end{{bmatrix}}^T"
        else:
            rows = " \\\\ ".join([" & ".join([f"{x:.{precision}f}" for x in row]) for row in M])
            return f"\\begin{{bmatrix}} {rows} \\end{{bmatrix}}"

    B = np.array(B_input, dtype=float)
    d = np.array(d_input, dtype=float).flatten()
    n = len(d)
    
    if x0_input is None:
        X_k = np.zeros(n)
    else:
        X_k = np.array(x0_input, dtype=float).flatten()
        
    display(Markdown("## ❖ PHƯƠNG PHÁP LẶP ĐƠN CHO HỆ $x = Bx + d$"))
    display(Math(f"B = {matrix_to_latex(B)}, \\quad d = {matrix_to_latex(d)}"))
    
    history = [X_k.copy()]
    
    k = 0
    while True:
        k += 1
        X_new = B @ X_k + d
        err = np.linalg.norm(X_new - X_k, np.inf)
        history.append(X_new.copy())
        
        if num_iters is not None and k >= num_iters:
            break
        if epsilon is not None and err < epsilon:
            break
        if k >= 100:
            display(Markdown(f"**Cảnh báo:** Thuật toán chưa hội tụ sau {k} vòng lặp."))
            break
            
        X_k = X_new
        
    # IN KẾT QUẢ ĐÃ ĐƯỢC TỐI ƯU TRÌNH BÀY
    display(Markdown(f"### Kết quả tính toán (Tổng số vòng lặp: {k})"))
    
    for idx, val in enumerate(history):
        display(Math(f"x^{({idx})} = {matrix_to_latex(val)}"))
    if epsilon is not None:
        display(Math(f"\\|x^{{({k})}} - x^{{({k-1})}}\\|_\\infty = {err:.6e} < \\epsilon = {epsilon}"))

# DỮ LIỆU ĐỀ BÀI
C = np.array([
    [0.1588, 0.0064, 0.0025, 0.0304, 0.0014, 0.0083, 0.1594],
    [0.0057, 0.2645, 0.0436, 0.0099, 0.0083, 0.0201, 0.3413],
    [0.0264, 0.1506, 0.3557, 0.0139, 0.0142, 0.0070, 0.0236],
    [0.3299, 0.0565, 0.0495, 0.3636, 0.0204, 0.0483, 0.0649],
    [0.0089, 0.0081, 0.0333, 0.0295, 0.3412, 0.0237, 0.0020],
    [0.1190, 0.0901, 0.0996, 0.1260, 0.1722, 0.2368, 0.3369],
    [0.0063, 0.0126, 0.0196, 0.0098, 0.0064, 0.0132, 0.0012]
], dtype=float)

d = np.array([74000, 56000, 10500, 25000, 17500, 196000, 5000], dtype=float)

# Lặp Đơn tìm lượng sản phẩm cần thiết
Lap_Don_x_Bx_d(C, d, num_iters=None, epsilon=1e-4)








# --- CODE FROM NOTEBOOK: scripts\CHƯƠNG 5 GIÁ TRỊ RIÊNG VÀ VECTOR RIÊNG CỦA MA TRẬN\Giá trị kỳ dị SVD (Lớn nhất).ipynb ---


import numpy as np
from IPython.display import display, Math, Markdown

def SVD_Reduced(A_input, num_components=None, v0_input=None, num_iters=1000, tol=1e-10):
    def matrix_to_latex(M, precision=4):
        if not isinstance(M, np.ndarray): return str(M)
        elif M.ndim == 1:
            inner = " \\\\ ".join([f"{x:.{precision}f}" for x in M])
            return f"\\begin{{bmatrix}} {inner} \\end{{bmatrix}}^T"
        else:
            rows = " \\\\ ".join([" & ".join([f"{x:.{precision}f}" for x in row]) for row in M])
            return f"\\begin{{bmatrix}} {rows} \\end{{bmatrix}}"

    def power_method_L2(B, v0, num_iters, tol):
        v = v0.copy()
        lam_prev = 0
        for i in range(num_iters):
            y_new = B @ v
            lam_rayleigh = v.T @ y_new
            norm_y = np.linalg.norm(y_new, 2)
            if norm_y == 0: return 0, v
            v_new = y_new / norm_y
            
            idx = np.argmax(np.abs(v_new))
            if v_new[idx] < 0: v_new = -v_new
                
            if np.abs(lam_rayleigh - lam_prev) < tol:
                v = v_new
                lam_prev = lam_rayleigh
                break
            v = v_new
            lam_prev = lam_rayleigh
        return lam_prev, v

    # Phần 1: Ghi chú lý thuyết Phương pháp Xuống thàng
    theory_md = [
        "## ❖ KHAI TRIỂN KỲ DỊ SVD BẰNG PHƯƠNG PHÁP XUỐNG THANG (DEFLATION)",
        "",
        "**Ý tưởng của phương pháp Xuống thàng:**",
        "Sau khi đã tìm được trị riêng trội lớn nhất $\\lambda_1$ và véctơ riêng tương ứng $v_1$ của ma trận $A$. "
        "Để tìm được trị riêng lớn thứ hai, ta cần 'khử' (triệt tiêu) ảnh hưởng của $\\lambda_1$ bằng cách tạo ra một ma trận mới:",
        "$$ A_1 = A - \\lambda_1 v_1 x^T $$",
        "(với $x$ là véctơ sao cho $x^T v_1 = 1$). Mọi trị riêng của $A_1$ đều giống $A$, ngoại trừ $\\lambda_1$ đã bị ép về 0. "
        "Do đó, khi áp dụng tiếp phương pháp Lũy thừa lên $A_1$, thuật toán sẽ hội tụ về trị riêng lớn thứ hai $\\lambda_2$ của $A$. "
        "Quá trình này lặp lại để tìm các trị riêng tiếp theo."
    ]
    display(Markdown('\n'.join(theory_md)))
    
    A = np.array(A_input, dtype=float)
    n, m = A.shape
    
    display(Math(f"A = {matrix_to_latex(A, precision=4)}"))

    A_k = A.copy()
    rank = min(n, m)
    if num_components is not None:
        rank = min(rank, num_components)
    
    if v0_input is None: v0_base = np.ones(m) / np.sqrt(m)
    else: v0_base = np.array(v0_input, dtype=float).flatten()
    
    U_cols = []
    S_vals = []
    V_cols = []
    
    approx_formula_terms = []
    
    for k in range(1, rank + 1):
        display(Markdown(f"\n### --- BƯỚC {k} ---"))
        B_k = A_k.T @ A_k
        lam, v = power_method_L2(B_k, v0_base, num_iters, tol)
        
        if lam < 1e-10:
            display(Markdown(f"⚠️ **Dừng thuật toán:** Giá trị riêng cực đại tiếp theo xấp xỉ 0."))
            break
            
        sigma = np.sqrt(lam)
        u = (A_k @ v) / sigma
        
        U_cols.append(u)
        S_vals.append(sigma)
        V_cols.append(v)
        
        display(Markdown(f"- **Giá trị kỳ dị lớn nhất (hiện tại):** $\\sigma_{k} = \\sqrt{{\\lambda_{k}}} \\approx {sigma:.4f}$"))
        display(Markdown(f"- **Vector kỳ dị phải:**"))
        display(Math(f"v_{k} = {matrix_to_latex(v, precision=4)}"))
        display(Markdown(f"- **Vector kỳ dị trái:**"))
        display(Math(f"u_{k} = \\frac{{A_{k} v_{k}}}{{\\sigma_{k}}} = {matrix_to_latex(u, precision=4)}"))
        
        approx_formula_terms.append(f"\\sigma_{k} u_{k} v_{k}^T")
        
        A_next = A_k - sigma * np.outer(u, v)
        A_k = A_next
        
    display(Markdown("\n### ❖ TỔNG KẾT VÀ XẤP XỈ MA TRẬN A"))
    approx_formula = "A \\approx " + " + ".join(approx_formula_terms)
    display(Math(approx_formula))

# DỮ LIỆU ĐỀ BÀI

# ═══════════════════════════════════════════════════════════════════
# NHẬP DỮ LIỆU CỦA BẠN VÀO ĐÂY
# ═══════════════════════════════════════════════════════════════════
A = np.array([
    [3.0, 2.0, 1.0],
    [1.0, 4.0, 2.0],
    [2.0, 1.0, 5.0]
], dtype=float)
# ═══════════════════════════════════════════════════════════════════

# num_components: so luong gia tri ky di can tinh (None = tinh het)
SVD_Reduced(A, num_components=2)








# --- CODE FROM NOTEBOOK: scripts\CHƯƠNG 5 GIÁ TRỊ RIÊNG VÀ VECTOR RIÊNG CỦA MA TRẬN\Khoảng cách ly nghiệm đa thức.ipynb ---


import numpy as np
from IPython.display import display, Math, Markdown

def format_poly(coeffs):
    n = len(coeffs) - 1
    terms = []
    for i, c in enumerate(coeffs):
        if abs(c) < 1e-10: continue
        deg = n - i
        sign = " + " if c > 0 else " - "
        c_abs = abs(c)
        c_str = f"{c_abs:.4f}" if abs(c_abs - 1.0) > 1e-10 or deg == 0 else ""
        
        if deg == 0: terms.append(f"{sign}{c_abs:.4f}")
        elif deg == 1: terms.append(f"{sign}{c_str}x")
        else: terms.append(f"{sign}{c_str}x^{deg}")
        
    res = "".join(terms).lstrip(" + ")
    if res.startswith("- "): res = "-" + res[2:]
    return res if res else "0"

def Polynomial_Root_Isolation(coeffs_input):
    # coeffs_input là mảng hệ số đa thức, từ bậc cao nhất đến bậc 0
    # Ví dụ: x^3 - 2x + 1 => [1, 0, -2, 1]
    P = np.array(coeffs_input, dtype=float)
    n = len(P) - 1
    
    display(Markdown("## ❖ TÌM KHOẢNG CÁCH LY NGHIỆM CỦA ĐA THỨC"))
    display(Markdown("Sử dụng **Định lý Sturm** để đếm số nghiệm thực phân biệt trong khoảng [a, b]."))
    
    poly_str = format_poly(P)
    display(Math(f"P(x) = {poly_str}"))
    
    # Chuỗi Sturm
    sturm_seq = [np.poly1d(P)]
    P_deriv = np.polyder(sturm_seq[0])
    sturm_seq.append(P_deriv)
    
    md = ["### 1. Xây dựng chuỗi Sturm"]
    md.append(f"- $P_0(x) = P(x) = {format_poly(sturm_seq[0].coeffs)}$")
    md.append(f"- $P_1(x) = P'(x) = {format_poly(sturm_seq[1].coeffs)}$")
    
    while True:
        P_prev = sturm_seq[-2]
        P_curr = sturm_seq[-1]
        
        if P_curr.order == 0 and abs(P_curr.coeffs[0]) < 1e-10:
            sturm_seq.pop() # Loại bỏ đa thức 0
            break
            
        # Chia đa thức
        quot, rem = np.polydiv(P_prev, P_curr)
        # P_{i+1} = - phần dư
        P_next = np.poly1d(-rem.coeffs)
        
        if P_next.order == 0 and abs(P_next.coeffs[0]) < 1e-10:
            break
            
        sturm_seq.append(P_next)
        idx = len(sturm_seq) - 1
        md.append(f"- $P_{idx}(x) = - \\text{{dư}}(P_{idx-2}, P_{idx-1}) = {format_poly(P_next.coeffs)}$")
        
    display(Markdown('\n'.join(md)))
    
    def count_sign_changes(x_val):
        signs = []
        for p in sturm_seq:
            val = p(x_val)
            if abs(val) > 1e-10:
                signs.append(np.sign(val))
        changes = 0
        for i in range(len(signs)-1):
            if signs[i] * signs[i+1] < 0:
                changes += 1
        return changes

    # Giới hạn nghiệm theo tiêu chuẩn Cauchy
    a_n = P[0]
    A_max = np.max(np.abs(P[1:]))
    R = 1 + A_max / abs(a_n)
    
    display(Markdown("### 2. Đánh giá giới hạn nghiệm và quét tìm khoảng"))
    display(Math(f"R = 1 + \\frac{{\\max |a_k|}}{{|a_n|}} = 1 + \\frac{{{A_max:.4f}}}{{{abs(a_n):.4f}}} = {R:.4f}"))
    display(Markdown(f"Tất cả các nghiệm thực đều nằm trong khoảng $[-R, R] = [{-R:.4f}, {R:.4f}]$.\n"))
    
    intervals = []
    # Quét từ -R đến R với bước 1.0 (có thể tinh chỉnh bước quét nếu cần)
    step = 1.0
    start = -np.ceil(R)
    end = np.ceil(R)
    
    curr = start
    while curr < end:
        a = curr
        b = curr + step
        
        V_a = count_sign_changes(a)
        V_b = count_sign_changes(b)
        
        num_roots = V_a - V_b
        if num_roots == 1:
            intervals.append((a, b))
        elif num_roots > 1:
            # Nếu có >1 nghiệm trong khoảng này, chia nhỏ ra để tìm chính xác khoảng cách ly 1 nghiệm
            mid = (a + b) / 2.0
            V_mid = count_sign_changes(mid)
            if V_a - V_mid == 1: intervals.append((a, mid))
            if V_mid - V_b == 1: intervals.append((mid, b))
            
        curr += step
        
    display(Markdown("**Kết luận các khoảng cách ly nghiệm:**"))
    for i, (a, b) in enumerate(intervals):
        display(Markdown(f"- Khoảng cách ly nghiệm thứ {i+1}: $x_{i+1} \\in [{a:.4f}, {b:.4f}]$"))

# DỮ LIỆU ĐỀ BÀI (Câu 3)
# Đặc trưng đa thức của A^T A (bạn có thể lấy kết quả từ hàm Danielevski đưa vào đây)
# Ví dụ: P(lambda) = lambda^3 - 5*lambda^2 + 6*lambda
coeffs = [1.0, -5.0, 6.0, 0.0]
Polynomial_Root_Isolation(coeffs)

# ═══════════════════════════════════════════════════════════════════
# NHẬP DỮ LIỆU CỦA BẠN VÀO ĐÂY
# ═══════════════════════════════════════════════════════════════════
# He so da thuc tu bac cao nhat: a_n, ..., a_1, a_0
# Vi du: P(x) = x^3 - 6x^2 + 11x - 6
P_coeffs = [1.0, -6.0, 11.0, -6.0]
# ═══════════════════════════════════════════════════════════════════

Polynomial_Root_Isolation(P_coeffs)





# --- CODE FROM NOTEBOOK: scripts\CHƯƠNG 5 GIÁ TRỊ RIÊNG VÀ VECTOR RIÊNG CỦA MA TRẬN\Lý thuyết Nén Ảnh (SVD - PCA).ipynb ---


from IPython.display import Markdown, display

md = [
    "## ❖ SƠ LƯỢC ỨNG DỤNG TÌM GIÁ TRỊ RIÊNG TRONG NÉN VÀ GỠ NÉN ẢNH SỐ",
    "",
    "Mỗi bức ảnh kỹ thuật số (ảnh xám) về bản chất được lưu trữ dưới dạng một ma trận số $A$ kích thước $M \\times N$, trong đó mỗi phần tử đại diện cho cường độ sáng của một pixel.",
    "",
    "Thay vì lưu trữ toàn bộ $M \\times N$ pixel, ta có thể ứng dụng **Phân tích Giá trị Kỳ dị (SVD) / Giá trị riêng** để nén ảnh thông qua các bước sau:",
    "",
    "**1. Phân tích SVD:**",
    "Ma trận ảnh $A$ được phân tích thành: $A = U \\Sigma V^T$",
    "Với $\\Sigma$ là ma trận đường chéo chứa các **giá trị kỳ dị $\\sigma_i$** (chính là căn bậc hai của các giá trị riêng của $A^T A$) được sắp xếp giảm dần từ lớn đến bé.",
    "",
    "**2. Nguyên lý Nén ảnh:**",
    "Thực tế, phần lớn lượng thông tin thị giác của bức ảnh (đường nét, hình khối chính) được gói gọn trong một số ít các **giá trị kỳ dị (trị riêng) lớn nhất**. Các trị riêng nhỏ chỉ mang thông tin nhiễu hoặc các chi tiết rất vụn vặt.",
    "Do đó, để nén ảnh, ta chỉ cần **giữ lại $k$ trị riêng lớn nhất** đầu tiên (với $k \\ll \\min(M,N)$) và cắt bỏ hoàn toàn các trị riêng còn lại.",
    "",
    "**3. Lưu trữ (Nén):**",
    "Ta chỉ lưu trữ $k$ giá trị $\\sigma_i$ lớn nhất, cùng với $k$ véctơ kỳ dị (véctơ riêng) tương ứng $u_i$ và $v_i$. Số lượng dữ liệu phải lưu lúc này chỉ là $k \\times (M + N + 1)$, nhỏ hơn rất nhiều so với $M \\times N$ của ma trận gốc.",
    "",
    "**4. Gỡ nén (Khôi phục):**",
    "Khi mở file, máy tính sẽ phục hồi bức ảnh bằng phép tính ma trận đơn giản:",
    "$$ A_{xấp_xỉ} = \\sum_{i=1}^k \\sigma_i \\cdot u_i \\cdot v_i^T $$",
    "Ảnh được phục hồi $A_{xấp_xỉ}$ sẽ gần như giống hệt ảnh gốc về mặt thị giác người nhìn, nhưng dung lượng file đã giảm đi đáng kể."
]

display(Markdown('\n'.join(md)))








# --- CODE FROM NOTEBOOK: scripts\CHƯƠNG 5 GIÁ TRỊ RIÊNG VÀ VECTOR RIÊNG CỦA MA TRẬN\Phương pháp Danielevski.ipynb ---


import numpy as np
from IPython.display import display, Math, Markdown

def _mat(M, p=4):
    if hasattr(M[0], "__len__"):
        rows = " \\\\ ".join([" & ".join([f"{x:.{p}f}" for x in row]) for row in M])
        return f"\\begin{{bmatrix}} {rows} \\end{{bmatrix}}"
    inner = " \\\\ ".join([f"{x:.{p}f}" for x in M])
    return f"\\begin{{bmatrix}} {inner} \\end{{bmatrix}}^T"

def Danielevski(A_input):
    A = np.array(A_input, dtype=float)
    n = A.shape[0]
    
    display(Markdown("## ❖ PHƯƠNG PHÁP DANIELEVSKI (TÌM ĐA THỨC ĐẶC TRƯNG)"))
    display(Math(f"A = {_mat(A)}"))
    
    P = A.copy()
    display(Markdown("### 1. Quá trình khử lặp"))
    
    for k in range(n - 1, 0, -1):
        if abs(P[k, k-1]) < 1e-12:
            display(Markdown(f"⚠️ **Lỗi:** $p_{{{k+1},{k}}} \\approx 0$, cần hoán vị khối! (Chưa hỗ trợ hoán vị trong script này)"))
            return None
            
        M = np.eye(n)
        M_inv = np.eye(n)
        
        # Xây dựng M_k
        M[k-1, :] = -P[k, :] / P[k, k-1]
        M[k-1, k-1] = 1.0 / P[k, k-1]
        
        # Xây dựng M_k^-1
        M_inv[k-1, :] = P[k, :]
        
        display(Markdown(f"**Bước $k = {k}$ (khử cột {k}):**"))
        display(Math(f"M_{{{k}}} = {_mat(M)} \\quad M_{{{k}}}^{{-1}} = {_mat(M_inv)}"))
        
        P = M @ P @ M_inv
        display(Math(f"A_{{{k-1}}} = M_{{{k}}} A_{{{k}}} M_{{{k}}}^{{-1}} = {_mat(P)}"))
        
    display(Markdown("### 2. Kết luận đa thức đặc trưng"))
    display(Markdown("Đa thức đặc trưng $P(\\lambda) = |A - \\lambda I|$ được cho bởi hàng đầu tiên của ma trận dạng Frobenius:"))
    
    # P(lambda) = (-1)^n * (lambda^n - p1*lambda^{n-1} - p2*lambda^{n-2} ... - pn)
    terms = []
    for i in range(n):
        coef = P[0, i]
        power = n - 1 - i
        sign = "+" if coef >= 0 else "-"
        terms.append(f"{sign} {abs(coef):.4f} \\lambda^{power}")
        
    poly = f"P(\\lambda) = (-1)^{n} \\left( \\lambda^{n} {' '.join(terms)} \\right)"
    display(Math(poly))
    return P

# ═══════════════════════════════════════════════════════════════════
# NHẬP DỮ LIỆU CỦA BẠN VÀO ĐÂY
# ═══════════════════════════════════════════════════════════════════
A = np.array([
    [1.0, 2.0, 3.0],
    [4.0, 5.0, 6.0],
    [7.0, 8.0, 10.0]
], dtype=float)
# ═══════════════════════════════════════════════════════════════════

Danielevski(A)








# --- CODE FROM NOTEBOOK: scripts\CHƯƠNG 5 GIÁ TRỊ RIÊNG VÀ VECTOR RIÊNG CỦA MA TRẬN\Phương pháp Lũy thừa.ipynb ---


import numpy as np
from IPython.display import display, Math, Markdown

def Power_Method_L2(A_input, x0_input=None, tol=1e-5, max_iter=100):
    def matrix_to_latex(M, precision=4):
        if not isinstance(M, np.ndarray): return str(M)
        elif M.ndim == 1:
            inner = " \\\\ ".join([f"{x:.{precision}f}" for x in M])
            return f"\\begin{{bmatrix}} {inner} \\end{{bmatrix}}^T"
        else:
            rows = " \\\\ ".join([" & ".join([f"{x:.{precision}f}" for x in row]) for row in M])
            return f"\\begin{{bmatrix}} {rows} \\end{{bmatrix}}"

    A = np.array(A_input, dtype=float)
    n = A.shape[0]
    
    if x0_input is None:
        x_k = np.ones(n)
    else:
        x_k = np.array(x0_input, dtype=float).flatten()
        
    x_k = x_k / np.linalg.norm(x_k, 2)
    
    display(Markdown("## ❖ TÌM TRỊ RIÊNG TRỘI BẰNG PHƯƠNG PHÁP LŨY THỪA"))
    display(Math(f"A = {matrix_to_latex(A)}"))
    
    lam_prev = 0
    history_lam = []
    history_v = [x_k.copy()]
    
    k = 0
    while True:
        k += 1
        y_new = A @ x_k
        lam_rayleigh = x_k.T @ y_new
        
        norm_y = np.linalg.norm(y_new, 2)
        if norm_y == 0:
            break
            
        v_new = y_new / norm_y
        idx = np.argmax(np.abs(v_new))
        if v_new[idx] < 0:
            v_new = -v_new
            
        err = np.abs(lam_rayleigh - lam_prev)
        history_lam.append(lam_rayleigh)
        history_v.append(v_new.copy())
        
        if err < tol:
            break
        if k >= max_iter:
            display(Markdown(f"**Cảnh báo:** Thuật toán chưa hội tụ sau {k} vòng lặp."))
            break
            
        x_k = v_new
        lam_prev = lam_rayleigh
        
    display(Markdown(f"### Kết quả tính toán (Tổng số vòng lặp: {k})"))
    display(Markdown(f"- **Đánh giá sai số:** $\\Delta = |\\lambda_{{{k}}} - \\lambda_{{{k-1}}}| = {err:.6e} \\le \\epsilon = {tol}$"))
    
    # In 3 xấp xỉ đầu và 3 xấp xỉ cuối
    display(Markdown("### Chi tiết các xấp xỉ Trị riêng $\\lambda$ và Véctơ riêng $v$:"))
    
    for idx in range(len(history_lam)):
        display(Math(f"\\lambda_{{idx+1}} = {history_lam[idx]:.5f}, \\quad v_{{idx+1}} = {matrix_to_latex(history_v[idx+1])}"))

    # Kiểm tra
    check_v = A @ history_v[-1]
    lam_v = history_lam[-1] * history_v[-1]
    display(Markdown("### Kiểm tra nghiệm"))
    display(Markdown(f"Kiểm tra định nghĩa $A \\cdot v \\approx \\lambda \\cdot v$:"))
    display(Math(f"A \\cdot v_k = {matrix_to_latex(check_v)}"))
    display(Math(f"\\lambda_k \\cdot v_k = {matrix_to_latex(lam_v)}"))
    
# ========================================================
# NHẬP MA TRẬN A CỦA BẠN VÀO ĐÂY

# ═══════════════════════════════════════════════════════════════════
# NHẬP DỮ LIỆU CỦA BẠN VÀO ĐÂY
# ═══════════════════════════════════════════════════════════════════
A = np.array([
    [4.0, 1.0, 1.0],
    [1.0, 5.0, 1.0],
    [1.0, 1.0, 6.0]
], dtype=float)
# ═══════════════════════════════════════════════════════════════════

Power_Method_L2(A, tol=1e-6)








# --- CODE FROM NOTEBOOK: scripts\CHƯƠNG 5 GIÁ TRỊ RIÊNG VÀ VECTOR RIÊNG CỦA MA TRẬN\Phương pháp Xuống thang.ipynb ---


import numpy as np
from IPython.display import display, Math, Markdown

def _mat(M, p=4):
    if hasattr(M[0], "__len__"):
        rows = " \\\\ ".join([" & ".join([f"{x:.{p}f}" for x in row]) for row in M])
        return f"\\begin{{bmatrix}} {rows} \\end{{bmatrix}}"
    inner = " \\\\ ".join([f"{x:.{p}f}" for x in M])
    return f"\\begin{{bmatrix}} {inner} \\end{{bmatrix}}^T"

def Power_Method_L2_Silent(A_input, x0_input=None, tol=1e-5, max_iter=100):
    A = np.array(A_input, dtype=float)
    n = A.shape[0]
    if x0_input is None: x0 = np.ones(n)
    else: x0 = np.array(x0_input, dtype=float)
    
    x = x0 / np.linalg.norm(x0, 2)
    lam_prev = 0
    for k in range(max_iter):
        y = A @ x
        lam = np.dot(x, y)
        x_new = y / np.linalg.norm(y, 2)
        if abs(lam - lam_prev) < tol:
            return lam, x_new
        lam_prev = lam
        x = x_new
    return lam, x

def Deflation_L2(A_input, max_iter=50):
    A = np.array(A_input, dtype=float)
    n = A.shape[0]
    
    display(Markdown("## ❖ PHƯƠNG PHÁP XUỐNG THANG (TÌM TRỊ RIÊNG THỨ HAI)"))
    display(Math(f"A = {_mat(A)}"))
    
    # 1. Tìm trị riêng trội nhất của A
    display(Markdown("### 1. Tìm trị riêng trội nhất $\\lambda_1$ của $A$ bằng pp Lũy thừa"))
    lam1, v1 = Power_Method_L2_Silent(A)
    display(Math(f"\\lambda_1 = {lam1:.6f}"))
    display(Math(f"v_1 = {_mat(v1)}"))
    
    # 2. Xây dựng ma trận xuống thang A1
    display(Markdown("### 2. Xây dựng ma trận xuống thang $A_1$"))
    display(Markdown("Theo công thức Hotelling, chọn véctơ phụ $x = v_1$ (do $v_1$ đã chuẩn hóa chuẩn 2)."))
    
    A1 = A - lam1 * np.outer(v1, v1)
    
    display(Math(f"A_1 = A - \\lambda_1 v_1 v_1^T = {_mat(A1)}"))
    
    # 3. Tìm trị riêng trội nhất của A1
    display(Markdown("### 3. Tìm trị riêng trội nhất $\\lambda_2$ của $A_1$"))
    lam2, v2_tilde = Power_Method_L2_Silent(A1)
    
    display(Math(f"\\lambda_2 = {lam2:.6f}"))
    display(Math(f"\\tilde{{v}}_2 = {_mat(v2_tilde)}"))
    
    # 4. Tìm véctơ riêng thực sự của A
    display(Markdown("### 4. Phục hồi véctơ riêng $v_2$ của $A$"))
    c = np.dot(v1, v2_tilde)
    v2_unnorm = v2_tilde + (lam2 / (lam1 - lam2)) * c * v1
    v2 = v2_unnorm / np.linalg.norm(v2_unnorm, 2)
    
    display(Math(f"v_2 = {_mat(v2)}"))

# ═══════════════════════════════════════════════════════════════════
# NHẬP DỮ LIỆU CỦA BẠN VÀO ĐÂY
# ═══════════════════════════════════════════════════════════════════
A = np.array([
    [4.0, 1.0, 1.0],
    [1.0, 5.0, 1.0],
    [1.0, 1.0, 6.0]
], dtype=float)
# ═══════════════════════════════════════════════════════════════════

Deflation_L2(A)








# --- CODE FROM NOTEBOOK: scripts\CHƯƠNG 5 GIÁ TRỊ RIÊNG VÀ VECTOR RIÊNG CỦA MA TRẬN\Số điều kiện Cond(A).ipynb ---


import numpy as np
from IPython.display import display, Math, Markdown

def _mat(M, p=4):
    if hasattr(M[0], "__len__"):
        rows = " \\\\ ".join([" & ".join([f"{x:.{p}f}" for x in row]) for row in M])
        return f"\\begin{{bmatrix}} {rows} \\end{{bmatrix}}"
    inner = " \\\\ ".join([f"{x:.{p}f}" for x in M])
    return f"\\begin{{bmatrix}} {inner} \\end{{bmatrix}}^T"

def Cond_Number(A_input):
    A = np.array(A_input, dtype=float)
    display(Markdown("## ❖ TÍNH SỐ ĐIỀU KIỆN CỦA MA TRẬN $Cond(A)_2$"))
    display(Math(f"A = {_mat(A)}"))
    
    display(Markdown("### 1. Tìm các trị riêng của $A^T A$"))
    ATA = A.T @ A
    display(Math(f"A^T A = {_mat(ATA)}"))
    
    eigvals, _ = np.linalg.eigh(ATA)
    eigvals = np.sort(eigvals)[::-1]  # giam dan
    
    S = np.sqrt(np.maximum(eigvals, 0))
    display(Math(f"\\text{{Giá trị kỳ dị: }} \\sigma = {_mat(S)}"))
    
    sigma_max = S[0]
    sigma_min = S[-1]
    
    display(Markdown("### 2. Kết luận"))
    display(Math(f"\\sigma_{{max}} = {sigma_max:.5f} \\quad \\sigma_{{min}} = {sigma_min:.5f}"))
    
    if sigma_min < 1e-12:
        display(Markdown("⚠️ **Cảnh báo:** $\\sigma_{min} \\approx 0$, ma trận $A$ suy biến. $Cond(A) = \\infty$"))
    else:
        cond = sigma_max / sigma_min
        display(Math(f"Cond(A)_2 = \\frac{{\\sigma_{{max}}}}{{\\sigma_{{min}}}} = {cond:.5f}"))

# ═══════════════════════════════════════════════════════════════════
# NHẬP DỮ LIỆU CỦA BẠN VÀO ĐÂY
# ═══════════════════════════════════════════════════════════════════
A = np.array([
    [4.0, 1.0],
    [3.0, 1.0]
], dtype=float)
# ═══════════════════════════════════════════════════════════════════

Cond_Number(A)


