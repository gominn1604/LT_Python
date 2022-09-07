from ast import Lambda
from datetime import datetime

from SinhVien import SinhVien

class DanhSachSV:
    def __init__(self) -> None:
        self.dssv = []

    def themSV(self, sv: SinhVien):
        self.dssv.append(sv)

    def xuat(self):
        for sv in self.dssv:
            print(sv)
    
    def timSVTheoMssv(self, mssv: int):
        return [ sv for sv in self.dssv if sv.mssv == mssv ]

    def timVTSvTheoMssv(self, mssv: int):
        for i in range(len(self.dssv)):
            if self.dssv[i].mssv == mssv:
                return i
        return -1

    def xoaSvTheoMssv(self, maSo: int) -> bool:
        vt = self.timVTSvTheoMssv(maSo)
        if vt != -1:
            del self.dssv[vt]
            return True
        else:
            return False

    def convertNS(self):
        for sv in self.dssv:
            sv.ngaySinh = datetime.strptime(sv.ngaySinh, "%d/%m/%Y") 

    def timSvTheoTen(self, ten: str):
        return [ sv for sv in self.dssv if sv.hoTen.split(" ")[-1].lower() == ten.lower()]

    def timSvSinhTruocNgay(self, ngaySinh: datetime):
        return [ sv for sv in self.dssv if sv.ngaySinh < ngaySinh]

    def docTuFile(self):
        fileName = "F:\Study\Year4_Semester1\LT_Python\Lab\Lab_2\Bai_2\dssv.txt"
        f = open(fileName, "r")
        for x in f:
            s = x.split(",")
            sv = SinhVien(s[0], s[1], datetime.strptime(s[2].strip(), "%d/%m/%Y"))
            dssv.themSV(sv)

    def sapXepSVTheoTen(self):
        self.dssv.sort(key=lambda x: x.hoTen.split(" ")[-1].lower(), reverse=False)

dssv = DanhSachSV()

dssv.docTuFile()
dssv.xuat()


kq1 = dssv.timSvTheoTen("Danh")
kq2 = dssv.timSvSinhTruocNgay(datetime.strptime("3/9/2001", "%d/%m/%Y"))
kq3 = dssv.sapXepSVTheoTen()
print("Xuat dssv theo ten")
dssv.xuat()


def xuat(dssv):
    if (len(dssv) == 0):
        print("Khong co sinh vien nao")
    else:
        for sv in dssv:
            print(sv)

print("Danh sach sinh vien co ten Danh la: ")
xuat(kq1)

print("Danh sach sinh vien sinh truoc ngay 3/9/2001 la: ")
xuat(kq2)
