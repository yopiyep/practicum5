N, K, M = map(int, input().split())
x1 = abs(M - K) - 1
x2 = N - abs(M - K) - 1
i = min(x1, x2)
if i >= 0:
    print(i)
else:
    print(max(x1, x2))