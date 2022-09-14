
from PhanSo import PhanSo


class DanhSachPS:
    def __init__(self) -> None:
        self.dsps = []
    
    def themPS(self, ps: PhanSo):
        self.dsps.append(ps)

    def xuat(self):
        for ps in self.dsps:
            print(ps)

    def laPhanSoDuong(self, ps: PhanSo):
        if (ps.tuSo > 0 and ps.mauSo > 0) or (ps.tuSo < 0 and ps.mauSo < 0):
            return True
        return False

    def docTuFile(self):
        filename = "F:\Study\Year4_Semester1\LT_Python\Lab\Lab_2\Bai_4\phanso.txt"
        f = open(filename, "r")
        for x in f:
            s = x.split(",")
            ps = PhanSo(int(s[0]), int(s[1]))
            dsps.themPS(ps)

    def demSoPSAmTrongMang(self):
        count = 0
        for ps in self.dsps:
            if(self.laPhanSoDuong(ps)):
                pass
            else:
                count += 1
        return count

    def chiaPhanSo(self, ps: PhanSo):
        return ps.tuSo / ps.mauSo

    def timPSDuongNhoNhat(self):
        min = 0
        result = PhanSo()
        for ps in self.dsps:
            if(self.laPhanSoDuong(ps)):
                min = self.chiaPhanSo(ps)
                result = ps
                break
        for ps in self.dsps:
            if (self.laPhanSoDuong(ps) and self.chiaPhanSo(ps) < min):
                min = self.chiaPhanSo(ps)
                result = ps
        return result

    def timPSDuongNhoNhat_2(self):
        min  = PhanSo(1_000_000_000)
        for ps in self.dsps:
            if ps > 0 and ps < min:
                min = ps
        return min

    def laPhanSoGiongNhau(self, ps1: PhanSo, ps2: PhanSo):
        return (ps1.tuSo == ps2.tuSo and ps1.mauSo == ps2.mauSo)
        
    def timVTPhanSo(self, phanso: PhanSo):
        vt = []
        for i in range(len(self.dsps)):
            if(self.laPhanSoGiongNhau(self.dsps[i], phanso)):
                vt.append(i)
        return vt

    def timVTPhanSo_2(self, ps: PhanSo):
        vt = []
        for i in range(len(self.dsps)):
            if (self.dsps[i] == ps):
                vt.append(i)
        return vt

    def mangPhanSoAm(self):
        return [ps for ps in self.dsps if not self.laPhanSoDuong(ps)]

    def tongPhanSoAm(self):
        sum = PhanSo()
        sum.tuSo = 0
        sum.mauSo = 1
        for i in range(len(self.mangPhanSoAm())):
            sum = sum.__add__(self.mangPhanSoAm()[i])
        return sum

    def tongPhanSoAm_2(self):
        sum = PhanSo(0, 1)
        for ps in self.dsps:
            if ps < 0:
                print(ps)
                sum+=ps
        return sum

    def xoaPSXTrongMang(self, phanso: PhanSo()):
        for i in range(len(self.dsps)):
            if self.timVTPhanSo(phanso):
                del self.dsps[i]

    def xoaPSXTrongMang_2(self, phanso: PhanSo()):
        for ps in self.dsps:
            if ps == phanso:
                self.dsps.remove(ps)

    def xoaPSCoTuLaX(self, tuso: int):
        for ps in self.dsps:
            if (ps.tuSo == tuso):
                self.dsps.remove(ps)

dsps = DanhSachPS()

dsps.docTuFile()
dsps.xuat()
ps = PhanSo(1,2)


# print(f"Tong cac phan so am trong mang la: {dsps.tongPhanSoAm()}")
# print(f"Tong cac phan so am trong mang la: {dsps.tongPhanSoAm_2()}")
# print(f"Cac vi tri xuat hien cua phan so trong mang la: {dsps.timVTPhanSo(ps)}")
# print(f"Cac vi tri xuat hien cua phan so trong mang la: {dsps.timVTPhanSo_2(ps)}")
# print("Phan so duong nho nhat la: ")
# print(dsps.timPSDuongNhoNhat())
# print(dsps.timPSDuongNhoNhat_2())


# dsps.xoaPSXTrongMang(ps)
dsps.xoaPSXTrongMang_2(ps)
print(f"Danh sach mang phan so sau khi xoa phan so {ps}")
dsps.xuat()

# dsps.xoaPSCoTuLaX(2)
# print(f"Danh sach mang phan so sau khi xoa la: ")
# dsps.xuat()