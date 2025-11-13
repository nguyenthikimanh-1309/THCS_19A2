luong_co_ban = float(input("Nhập lương cơ bản: "))
so_ngay_cong = int(input("Nhập số ngày công trong tháng: "))
luong_1_ngay = luong_co_ban
luong_thang = luong_1_ngay * so_ngay_cong
if so_ngay_cong >= 22:
    luong_thang += luong_thang * 0.1
elif so_ngay_cong < 22:
    luong_thang -= luong_thang * 0.05
    print("Lương tháng phải trả là:", round(luong_thang, 2), "vnd")
