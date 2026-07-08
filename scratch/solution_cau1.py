import numpy as np

def P(x):
    return x**5 - 20*x**4 - 15*x**3 + 8*x**2 + 2*x + 2002

def dP(x):
    return 5*x**4 - 80*x**3 - 45*x**2 + 16*x + 2

def newton_method(x0, eps=1e-5, max_iter=100):
    iterations = []
    x = x0
    iterations.append(x)
    for k in range(max_iter):
        fx = P(x)
        dfx = dP(x)
        if abs(dfx) < 1e-12:
            break
        x_new = x - fx / dfx
        iterations.append(x_new)
        if abs(x_new - x) < eps:
            break
        x = x_new
    return iterations

# Let's find for each interval:
# Interval 1: [-5, -3] -> x0 = -4.0
# Interval 2: [3, 4] -> x0 = 3.5
# Interval 3: [20, 21] -> x0 = 20.5

eps = 1e-5
roots_info = {}
for name, x0 in [("Root 1", -4.0), ("Root 2", 3.5), ("Root 3", 20.5)]:
    iters = newton_method(x0, eps)
    roots_info[name] = iters

for name, iters in roots_info.items():
    print(f"=== {name} (x0 = {iters[0]}) ===")
    print(f"Total iterations: {len(iters)-1}")
    print(f"First 3 approximations:")
    for i in range(min(3, len(iters))):
        print(f"  x_{i} = {iters[i]:.9f}")
    print(f"Last 3 approximations:")
    last_idx = len(iters)
    for i in range(max(0, last_idx-3), last_idx):
        print(f"  x_{i} = {iters[i]:.9f}")
    final_val = iters[-1]
    print(f"Final root: {final_val:.9f}")
    print(f"Check P(x_final) = {P(final_val):.2e}")
    print(f"Estimated error: {abs(iters[-1] - iters[-2]):.2e}" if len(iters) > 1 else "N/A")
    print()
