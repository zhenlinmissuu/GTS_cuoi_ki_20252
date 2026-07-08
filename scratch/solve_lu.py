import numpy as np
import scipy.linalg as la

C = np.array([
    [0.1588, 0.0064, 0.0025, 0.0304, 0.0014, 0.0083, 0.1594],
    [0.0057, 0.2645, 0.0436, 0.0099, 0.0083, 0.0201, 0.3413],
    [0.0264, 0.1506, 0.3557, 0.0139, 0.0142, 0.0070, 0.0236],
    [0.3299, 0.0565, 0.0495, 0.3636, 0.0204, 0.0483, 0.0649],
    [0.0089, 0.0081, 0.0333, 0.0295, 0.3412, 0.0237, 0.0020],
    [0.1190, 0.0901, 0.0996, 0.1260, 0.1722, 0.2368, 0.3369],
    [0.0063, 0.0126, 0.0196, 0.0098, 0.0064, 0.0132, 0.0012]
])

d = np.array([74000, 56000, 10500, 25000, 17500, 196000, 5000])

A = np.eye(7) - C
# Let's perform LU decomposition without pivoting first to see if it is stable (usually it is because A is diagonally dominant or has positive diagonal and non-positive off-diagonal, i.e., an M-matrix).
# Let's check if LU without pivoting exists.
# We can do it manually or via scipy.
# LU decomposition A = L * U (where L has 1s on diagonal)
# Since A is an M-matrix, LU without pivoting is stable. Let's do it using scipy's lu but check if P is identity.
P, L, U = la.lu(A)
print("Is P identity?", np.allclose(P, np.eye(7)))

# Let's compute LU without pivoting manually to be absolutely sure:
def lu_no_pivot(A):
    n = A.shape[0]
    L = np.eye(n)
    U = A.copy()
    for k in range(n):
        for i in range(k+1, n):
            factor = U[i, k] / U[k, k]
            L[i, k] = factor
            U[i, k:] -= factor * U[k, k:]
    return L, U

L_np, U_np = lu_no_pivot(A)
print("\nL_np:")
print(np.round(L_np, 5))
print("\nU_np:")
print(np.round(U_np, 5))

# Solve LY = d
Y = la.solve_triangular(L_np, d, lower=True)
print("\nY:")
print(np.round(Y, 5))

# Solve UX = Y
X = la.solve_triangular(U_np, Y, lower=False)
print("\nX:")
print(np.round(X, 5))
