from sys import settrace
from HinhHoc import HinhHoc

class HinhVuong(HinhHoc):
    def __init__(self, canh: float) -> None:
        super().__init__(canh)

    @property
    def canhHV(self):
        return self.canh

    def __str__(self) -> str:
        return super().__str__() + f"vuong co canh: {self.canhHV}"

    def DienTich(self):
        return pow(self.canhHV, 2)