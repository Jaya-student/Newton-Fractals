def f(x):
    return x**2 - 4*x - 10

def bisection_method(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        raise ValueError("The Bisection Method requires that "
                         "f(a) and f(b) have opposite signs.")
    for _ in range(max_iter):
        c = (a + b) / 2
        fc = f(c)

        if abs(fc) < tol or (b - a) / 2 < tol:
            return c

        if f(a) * fc < 0:
            b = c
        else:
            a = c
    return c

root = bisection_method(f, -2.0, 0.0, tol=1e-4)
print(f"Root: {root}")
