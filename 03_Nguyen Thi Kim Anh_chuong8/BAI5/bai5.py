n = int(input("Nhap n: "))
S1 = 0
for i in range(1, n+1):
    S1 += i
S2 = 0
for i in range(1, n, 2):
    S2 += i * (i + 1)
S3 = 0
for i in range(1, n+1):
    S3 += ((-1)**(i+1)) * (1/i)
S4 = 0
for k in range(0, n+1):
    S4 += k / (k + 2)
print("S1 =", S1)
print("S2 =", S2)
print("S3 =", S3)
print("S4 =", S4)
