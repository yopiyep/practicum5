a, b, c = map(int, input().split())
max_val = max(a, b, c)
min_val = min(a, b, c)
mid_val = a + b + c - max_val - min_val
print(max_val, mid_val, min_val)