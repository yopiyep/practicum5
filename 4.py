n = int(input())
last = n % 10
last_two = n % 100
if 11 <= last_two <= 14:
    print(f"{n} попугаев")
elif last == 1:
    print(f"{n} попугай")
elif 2 <= last <= 4:
    print(f"{n} попугая")
else:
    print(f"{n} попугаев")
