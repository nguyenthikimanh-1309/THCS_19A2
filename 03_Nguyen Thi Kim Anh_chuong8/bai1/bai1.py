import math

n = int(input("Nhập số n: "))

can = int(math.sqrt(n))

if can * can == n:
    print(n, "là số chính phương")
else:
    print(n, "KHÔNG phải số chính phương")