import numpy as np

def khu_gauss(A, b):
    """
    Phương pháp Khử Gauss với xoay vòng một phần (Partial Pivoting).
    Trả về (nghiệm, lịch_sử_bước_làm, thông_báo).
    """
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    n = len(b)
    
    if A.shape[0] != A.shape[1] or A.shape[0] != n:
        return None, [], "Lỗi: Ma trận không vuông hoặc kích thước b không khớp."
        
    history = []
    
    # Ma trận mở rộng
    Aug = np.hstack((A, b.reshape(-1, 1)))
    history.append(("Ma trận mở rộng ban đầu", Aug.copy()))
    
    for i in range(n):
        # Partial Pivoting
        max_row = i + np.argmax(abs(Aug[i:, i]))
        if Aug[max_row, i] == 0:
            return None, history, "Lỗi: Ma trận suy biến (det = 0)."
            
        if max_row != i:
            Aug[[i, max_row]] = Aug[[max_row, i]]
            history.append((f"Đổi chỗ hàng {i+1} và hàng {max_row+1}", Aug.copy()))
            
        # Khử các hàng dưới
        for j in range(i+1, n):
            factor = Aug[j, i] / Aug[i, i]
            Aug[j, i:] -= factor * Aug[i, i:]
            if factor != 0:
                history.append((f"L_{j+1} = L_{j+1} - ({factor:.4f})*L_{i+1}", Aug.copy()))
                
    # Thế ngược (Back substitution)
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (Aug[i, -1] - np.dot(Aug[i, i+1:n], x[i+1:n])) / Aug[i, i]
        
    return x.tolist(), history, "Giải hệ thành công bằng phương pháp Khử Gauss."

def jacobi(A, b, x0=None, tol=1e-5, max_iter=50):
    """
    Phương pháp lặp Jacobi.
    """
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    n = len(b)
    
    if x0 is None:
        x0 = np.zeros(n)
    else:
        x0 = np.array(x0, dtype=float)
        
    # Kiểm tra đường chéo có số 0
    if any(np.diag(A) == 0):
        return None, [], "Lỗi: Các phần tử trên đường chéo chính phải khác 0."
        
    history = []
    x = x0.copy()
    
    for i in range(1, max_iter + 1):
        x_new = np.zeros(n)
        for j in range(n):
            s = sum(A[j, k] * x[k] for k in range(n) if k != j)
            x_new[j] = (b[j] - s) / A[j, j]
            
        error = np.linalg.norm(x_new - x, ord=np.inf)
        
        row = {"Lần lặp": i}
        for idx in range(n):
            row[f"x_{idx+1}"] = x_new[idx]
        row["Sai số"] = error
        history.append(row)
        
        if error < tol:
            return x_new.tolist(), history, f"Hội tụ sau {i} vòng lặp."
            
        x = x_new
        
    return x.tolist(), history, f"Đạt số lần lặp tối đa ({max_iter}) nhưng chưa hội tụ."

def gauss_seidel(A, b, x0=None, tol=1e-5, max_iter=50):
    """
    Phương pháp lặp Gauss-Seidel.
    """
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    n = len(b)
    
    if x0 is None:
        x0 = np.zeros(n)
    else:
        x0 = np.array(x0, dtype=float)
        
    if any(np.diag(A) == 0):
        return None, [], "Lỗi: Các phần tử trên đường chéo chính phải khác 0."
        
    history = []
    x = x0.copy()
    
    for i in range(1, max_iter + 1):
        x_old = x.copy()
        for j in range(n):
            s1 = sum(A[j, k] * x[k] for k in range(j))
            s2 = sum(A[j, k] * x_old[k] for k in range(j + 1, n))
            x[j] = (b[j] - s1 - s2) / A[j, j]
            
        error = np.linalg.norm(x - x_old, ord=np.inf)
        
        row = {"Lần lặp": i}
        for idx in range(n):
            row[f"x_{idx+1}"] = x[idx]
        row["Sai số"] = error
        history.append(row)
        
        if error < tol:
            return x.tolist(), history, f"Hội tụ sau {i} vòng lặp."
            
    return x.tolist(), history, f"Đạt số lần lặp tối đa ({max_iter}) nhưng chưa hội tụ."
