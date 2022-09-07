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

    def timSvTheoTen(self, ten: str):
        return [ sv for sv in self.dssv if sv.hoTen.split(" ")[-1].lower() == ten.lower()]

    def timSvSinhTruocNgay(self, ngaySinh: datetime):
        return [ sv for sv in self.dssv if sv.ngaySinh < ngaySinh]


sv1 = SinhVien(1911136, "Nguyen Viet Duy Danh", datetime.strptime("21/12/2001", "%d/%m/%Y"))
sv2 = SinhVien(1914775, "Dinh Trong Dat", datetime.strptime("3/9/2001", "%d/%m/%Y"))
sv3 = SinhVien(1910152, "Truong Quang Tuan", datetime.strptime("24/2/2001", "%d/%m/%Y"))
sv4 = SinhVien(1914899, "Tran Minh Canh", datetime.strptime("5/6/2000", "%d/%m/%Y"))
sv5 = SinhVien(1911155, "Nguyen Anh Nhat Huy", datetime.strptime("15/7/2001", "%d/%m/%Y"))

dssv = DanhSachSV()

dssv.themSV(sv1)
dssv.themSV(sv2)
dssv.themSV(sv3)
dssv.themSV(sv4)
dssv.themSV(sv5)

kq1 = dssv.timSvTheoTen("Danh")
kq2 = dssv.timSvSinhTruocNgay(datetime.strptime("3/9/2001", "%d/%m/%Y"))


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
