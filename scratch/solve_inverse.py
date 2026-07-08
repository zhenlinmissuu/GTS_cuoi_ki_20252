import numpy as np

A_orig = np.array([
    [11, 22, -13, 24, 15, -26, 17, 28],
    [22, 233, 24, 35, 26, 37, 28, -39],
    [33, -24, 35, -26, 37, 28, -39, 20],
    [14, 45, 26, 47, 38, 49, 40, -41],
    [-55, 16, 57, 28, 59, 30, -51, 42],
    [46, 27, -48, 39, 40, 61, 42, 73],
    [27, -58, 29, 70, -21, 42, 23, 34],
    [38, 59, 60, -71, 82, -93, 24, 15]
], dtype=float)

a = 200
A = A_orig.copy()
for i in range(8):
    A[i, i] += a

n = A.shape[0]
eps = 1e-4

def solve_gs(A, b, eps=1e-4, max_iter=100):
    n = A.shape[0]
    x = np.zeros(n)
    history = [x.copy()]
    for k in range(max_iter):
        x_new = x.copy()
        for i in range(n):
            s1 = sum(A[i, j] * x_new[j] for j in range(i))
            s2 = sum(A[i, j] * x[j] for j in range(i+1, n))
            x_new[i] = (b[i] - s1 - s2) / A[i, i]
        history.append(x_new.copy())
        if np.linalg.norm(x_new - x, np.inf) < eps:
            break
        x = x_new
    return history

X_inv_cols = []
histories = []
for j in range(n):
    b = np.zeros(n)
    b[j] = 1.0
    hist = solve_gs(A, b, eps)
    histories.append(hist)
    X_inv_cols.append(hist[-1])

X_inv = np.column_stack(X_inv_cols)

with open("scratch/inverse_output.txt", "w", encoding="utf-8") as f:
    f.write("=== MA TRAN NGHICH DAO A^-1 ===\n")
    np.savetxt(f, X_inv, fmt="%.6f")
    
    f.write("\n=== CAC BUOC LAP CUA COT 1 ===\n")
    for idx, x in enumerate(histories[0]):
        f.write(f"Step {idx}: {np.array2string(x, precision=6, separator=', ')}\n")

    f.write("\n=== SO BUOC LAP CUA TUNG COT ===\n")
    for j in range(n):
        f.write(f"Col {j+1}: {len(histories[j])-1} steps\n")
        
    f.write("\n=== KIEM TRA A * A^-1 ===\n")
    I_check = A @ X_inv
    np.savetxt(f, I_check, fmt="%.4f")
    f.write(f"Sai lech max: {np.linalg.norm(I_check - np.eye(n), np.inf):.2e}\n")
