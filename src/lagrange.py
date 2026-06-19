def lagrange_interpolation(x, y, t):
    n = len(x)
    p= 0.0
    for i in range(n):
        L = 1.0
        for j in range(n):
            if i != j:
                L *= (t - x[j]) / (x[i] - x[j])
        p += y[i] * L       
    return p
#example:
t=[2,3,8]
x=[1,3,5,7,8]
y=[2,1,5,3,9]
for j in t:
    y2=lagrange_interpolation(x, y, j)
    print(f"value at {j} = {y2}")
