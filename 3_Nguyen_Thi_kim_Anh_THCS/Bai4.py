tien_vnd = float(input("Nhập số tiền (vnd): "))
ty_gia_usd = 24.500
tien_usd = tien_vnd / ty_gia_usd
print("Số tiền sau khi đổi là:", round(tien_usd, 2), "usd")