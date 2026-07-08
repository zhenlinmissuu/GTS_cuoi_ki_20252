import numpy as np

def power_method(B, num_iters=1000, tol=1e-10):
    n = B.shape[0]
    # Initialize with a vector of ones (or random)
    v = np.ones(n)
    v = v / np.linalg.norm(v)
    lam_prev = 0
    for i in range(num_iters):
        v_new = B @ v
        lam = np.linalg.norm(v_new)
        if lam == 0:
            return 0, v
        v_new = v_new / lam
        
        # Rayleight quotient is more accurate and handles sign
        lam_rayleigh = v_new.T @ B @ v_new
        
        if np.abs(lam_rayleigh - lam_prev) < tol:
            # Check sign
            v = v_new
            break
        v = v_new
        lam_prev = lam_rayleigh
        
    return lam_rayleigh, v

def solve_svd():
    A = np.array([
        [3, 3, 7],
        [3, 9, 10],
        [8, 4, 6],
        [2, 10, 9]
    ], dtype=float)
    
    print("## TÌM PHÂN TÍCH SVD RÚT GỌN BẰNG LŨY THỪA VÀ XUỐNG THANG")
    print("\nMa trận ban đầu $A_1 = A$:")
    print("```text\n" + str(np.round(A, 4)) + "\n```")
    
    A_k = A.copy()
    rank = A.shape[1]
    
    U_cols = []
    S_vals = []
    V_cols = []
    
    for k in range(1, rank + 1):
        print(f"\n### Bước {k}:")
        # Compute B_k = A_k^T * A_k
        B_k = A_k.T @ A_k
        
        # Power method
        lam, v = power_method(B_k)
        
        if lam < 1e-10:
            print(f"Giá trị riêng cực đại của $A_{k}^T A_{k}$ xấp xỉ 0. Dừng thuật toán.")
            break
            
        sigma = np.sqrt(lam)
        
        # Enforce consistent sign for v (e.g. first non-zero element is positive)
        idx = np.argmax(np.abs(v))
        if v[idx] < 0:
            v = -v
            
        u = (A_k @ v) / sigma
        
        U_cols.append(u)
        S_vals.append(sigma)
        V_cols.append(v)
        
        print(f"- Trị riêng lớn nhất $\\lambda_{k} = {lam:.4f}$")
        print(f"- Giá trị kỳ dị $\\sigma_{k} = {sigma:.4f}$")
        print(f"- Véctơ kỳ dị phải $v_{k} = {np.round(v, 4).tolist()}$")
        print(f"- Véctơ kỳ dị trái $u_{k} = \\frac{{A_{k} v_{k}}}{{\\sigma_{k}}} = {np.round(u, 4).tolist()}$")
        
        # Deflation
        A_next = A_k - sigma * np.outer(u, v)
        print(f"\nMa trận sau khi xuống thang $A_{{{k+1}}} = A_{k} - \\sigma_{k} u_{k} v_{k}^T$:")
        print("```text\n" + str(np.round(A_next, 4)) + "\n```")
        
        A_k = A_next
        
    print("\n### Kết luận phân tích SVD rút gọn $A = U \\Sigma V^T$:")
    U = np.column_stack(U_cols)
    S = np.diag(S_vals)
    V = np.column_stack(V_cols)
    
    print("Ma trận $U$:")
    print("```text\n" + str(np.round(U, 4)) + "\n```")
    print("Ma trận $\\Sigma$:")
    print("```text\n" + str(np.round(S, 4)) + "\n```")
    print("Ma trận $V$:")
    print("```text\n" + str(np.round(V, 4)) + "\n```")
    print("Ma trận $V^T$:")
    print("```text\n" + str(np.round(V.T, 4)) + "\n```")
    
    # Verify
    A_reconstructed = U @ S @ V.T
    err = np.linalg.norm(A - A_reconstructed)
    print(f"\nKiểm tra $||A - U \\Sigma V^T||_F = {err:.2e}")

solve_svd()
