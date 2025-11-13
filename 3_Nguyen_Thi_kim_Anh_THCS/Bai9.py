so_kwh = float(input("Nhập số kwh điện tiêu thụ: "))
if so_kwh <= 50:
    tien_dien = so_kwh * 1.678
elif so_kwh <= 100:
    tien_dien = 50 * 1.678 + (so_kwh - 50) * 1.734
else:
    tien_dien = 50 * 1.678 + 50 * 1.734 + (so_kwh - 100) * 2.014
    print("TIền điện phải trả lad:", round(tien_dien, 2), "vnd")