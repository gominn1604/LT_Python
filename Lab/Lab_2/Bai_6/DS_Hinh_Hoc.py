from LoaiHinh import LoaiHinh
from HinhHoc import HinhHoc
from HinhVuong import HinhVuong
from HinhChuNhat import HinhChuNhat
from HinhTron import HinhTron

class DanhSachHinhHoc:
    def __init__(self) -> None:
        self.dshh = []

    def themHinh(self, hinh: HinhHoc):
        self.dshh.append(hinh)

    def xuat(self):
        for hinh in self.dshh:
            print(hinh)
    
    def docTuFile(self, filename: str):
        f = open(filename, "r", encoding="utf8")
        lines = f.readlines()
        for line in lines:
            hh = line.split(",")
            if (int(hh[0]) == LoaiHinh.HinhVuong.value):
                hv = HinhVuong(float(hh[1]))
                self.themHinh(hv)
            elif (int(hh[0]) == LoaiHinh.HinhTron.value):
                ht = HinhTron(float(hh[1]))
                self.themHinh(ht)
            elif (int(hh[0]) == LoaiHinh.HinhChuNhat.value):
                hcn = HinhChuNhat(float(hh[1]), float(hh[2]))
                self.themHinh(hcn)
        return self.dshh
        
    def timHinhCoDienTichLonNhat(self) -> list:
        max = 0
        for hh in self.dshh:
            if float(hh.DienTich) > float(max):
                max = hh.DienTich 
        print("Danh sach cac hinh co dien tich lon nhat la:")
        return [ hh for hh in self.dshh if hh.DienTich == max]  

    def timHinhCoDienTichNhoNhat(self) -> list:
        min = self.dshh[1].DienTich
        for hh in self.dshh:
            if float(hh.DienTich) < float(min):
                min = hh.DienTich
        print("Danh sach cac hinh hoc co dien tich nho nhat la: ")
        return [hh for hh in self.dshh if hh.DienTich == min]
    
    def timHinhCoDienTichLonNhatTheoLoai(self, loaihinh: LoaiHinh):
        result = HinhHoc(0)
        max = 0
        if loaihinh.value == loaihinh.HinhTron.value:
            for hh in self.dshh:
                if hh.DienTich > max and isinstance(hh, HinhTron):
                    result = hh
        elif loaihinh.value == loaihinh.HinhVuong.value:
            for hh in self.dshh:
                if hh.DienTich > max and isinstance(hh, HinhVuong):
                    result = hh
        elif loaihinh.value == loaihinh.HinhChuNhat.value:
            for hh in self.dshh:
                if hh.DienTich > max and isinstance(hh, HinhChuNhat):
                    result = hh
        return print(result)

    def sapXepTheoDienTich(self):
        return sorted(self.dshh, key=lambda x:x.DienTich, reverse=True)

    def demSoLuongHinh(self, loaihinh: LoaiHinh):
        result = []
        if loaihinh.value == loaihinh.HinhVuong.value:
            result = [hh for hh in self.dshh if isinstance(hh, HinhVuong)]
        if loaihinh.value == loaihinh.HinhTron.value:
            result = [hh for hh in self.dshh if isinstance(hh, HinhTron)]
        if loaihinh.value == loaihinh.HinhChuNhat.value:
            result = [hh for hh in self.dshh if isinstance(hh, HinhChuNhat)]
        print(f"Co {len(result)} {loaihinh.name}")

    def tinhTongDienTich(self):
        sum = 0
        for hh in self.dshh:
            sum += hh.DienTich
        print(f"Tong dien tich cac hinh la: {sum}")

    def timViTriCuaHinh(self, h: HinhHoc):
        for i in range(len(self.dshh)):
            if (isinstance(self.dshh[i], HinhChuNhat)):
                if self.dshh[i].chieuDai == h.chieuDai and self.dshh[i].chieuRong == h.chieuRong:
                    return i
            elif ((isinstance(self.dshh[i], HinhTron) and LoaiHinh.HinhTron.name == HinhTron) or (isinstance(self.dshh[i], HinhVuong)) and LoaiHinh.HinhVuong.name == HinhVuong):
                if self.dshh[i].canh == h.canh:
                    return i
        return -1

dshh = DanhSachHinhHoc()
dshh.docTuFile("F:\Study\Year4_Semester1\LT_Python\Lab\Lab_2\Bai_6\hinhhoc.txt")
dshh.xuat()

def xuat(dshh):
    for hh in dshh:
        print(hh)

kq = dshh.timHinhCoDienTichLonNhat()
xuat(kq)
xuat(dshh.timHinhCoDienTichNhoNhat())
dshh.timHinhCoDienTichLonNhatTheoLoai(LoaiHinh.HinhTron)
xuat(dshh.sapXepTheoDienTich())
dshh.demSoLuongHinh(LoaiHinh.HinhTron)
dshh.tinhTongDienTich()
print(dshh.timViTriCuaHinh(HinhVuong(8)))

