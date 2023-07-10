from dinhnghia import KhachHang
import datetime

class BangTinhTienThueXe:
    list_nguoi_thue = []
    def taobang(self):
            Stt = int(input("nhap Stt: "))
            HoDem = str(input("nhap ten: "))
            Ten = str(input("nhap ten: "))
            NoiDuLich = str(input("nhap noi Du Lich"))
            def taongay():
                  ngay = input("dd/mm/yyyy: ")
                  ngay = ngay.split("/")
                  d = datetime.datetime(int(ngay[2]),int(ngay[1]),int(ngay[0]))
                  d1 = d.strftime("%d/%m/%Y")
                  return d, d1
            NgayDi = taongay()
            d,d1 = NgayDi
            NgayVe = taongay()
            b, b1 = NgayVe
            SoNgay = int((b-d).days)
            DonGia = int(input("nhap gia tien: "))
            ThanhTien = DonGia*SoNgay
            custumer = KhachHang(Stt, HoDem, Ten, NoiDuLich,NgayDi,NgayVe,SoNgay,DonGia,ThanhTien)
            self.list_nguoi_thue.append(custumer)

BangTinhTienThueXe.taobang()