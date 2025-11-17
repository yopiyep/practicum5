n = int(input())
g = n // 493
r = n % 493
s = r // 29
k = r % 29
if g > 0:
    print(f"{g} галлсона")
if s > 0:
    print(f"{s} сиклей")
if k > 0:
    print(f"{k} кнатов")