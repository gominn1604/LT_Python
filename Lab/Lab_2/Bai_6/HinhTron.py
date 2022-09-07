from cmath import pi
from HinhHoc import HinhHoc

class HinhTron(HinhHoc):
    def __init__(self, canh: float) -> None:
        super().__init__(canh)

    @property
    def banKinh(self):
        return self.canh

    def __str__(self) -> str:
        return super().__str__() + f"tron co ban kinh {self.banKinh}"

    @property
    def DienTich(self):
        return pi * pow(int(self.banKinh), 2)