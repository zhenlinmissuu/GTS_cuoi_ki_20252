import numpy as np

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

# Simple iteration
# X^(k+1) = C X^(k) + d
# Initial guess X^(0) = d (standard for Leontief) or X^(0) = 0 vector.
# Let's test with X^(0) = d.
# Let's compute norms of C to see if it converges.
print("Norm 1 (column sum):", np.max(np.sum(np.abs(C), axis=0)))
print("Norm inf (row sum):", np.max(np.sum(np.abs(C), axis=1)))

X = d.copy()
# Let's run simple iteration until ||X^(k+1) - X^(k)||_1 < 1e-4
history = [X.copy()]
for step in range(1, 100):
    X_new = C.dot(X) + d
    history.append(X_new.copy())
    diff = np.linalg.norm(X_new - X, 1)
    X = X_new
    if diff < 1e-3:
        break

print(f"Converged in {len(history)-1} iterations.")
print("X^(0) (first 3):")
for i in range(min(5, len(history))):
    print(f"Iteration {i}:", history[i])

print("\nLast 3 iterations:")
for i in range(len(history)-3, len(history)):
    print(f"Iteration {i}:", history[i])

# Let's solve exactly
I = np.eye(7)
A = I - C
# LU decomposition of A
import scipy.linalg as la
P, L, U = la.lu(A)
print("\nExact solution:")
x_exact = la.solve(A, d)
print(x_exact)
