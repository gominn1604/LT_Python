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
            if (hh[0].upper() =="HV"):
                hv = HinhVuong(float(hh[1]))
                self.themHinh(hv)
            elif (hh[0].upper() == "HT"):
                ht = HinhTron(float(hh[1]))
                self.themHinh(ht)
            elif (hh[0].upper() == "HCN"):
                hcn = HinhChuNhat(float(hh[1]), float(hh[2]))
                self.themHinh(hcn)
        return self.dshh
        
    def timHinhCoDienTichLonNhat(self) -> list:
        max = 0
        result = DanhSachHinhHoc()
        for hh in self.dshh:
            if hh.DienTich() > float(max):
                max = hh.DienTich()
        for hh in self.dshh:
            if hh.DienTich() == float(max):
                result.append(hh)     
        return result

dshh = DanhSachHinhHoc()
dshh.docTuFile("F:\Study\Year4_Semester1\LT_Python\Lab\Lab_2\Bai_6\hinhhoc.txt")
dshh.xuat()
kq = dshh.timHinhCoDienTichLonNhat()
for hh in kq:
    print(hh)