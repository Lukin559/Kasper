def f(n, k):
    if n in [0, 1, 2]:
        return 1
    else:
        return f(n - 1, k) + f(n - 2, k) * k


hours, warms = [int(i) for i in input().split()]
print(f(hours, warms))
