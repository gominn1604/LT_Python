from HinhHoc import HinhHoc

class HinhChuNhat(HinhHoc):
    def __init__(self, canh: float, chieuRong: float) -> None:
        super().__init__(canh)
        self._chieuRong = chieuRong

    @property 
    def chieuDai(self):
        return self.canh

    @property
    def chieuRong(self):
        return self._chieuRong

    def __str__(self) -> str:
        return super().__str__() + f"chu nhat co cd: {self.chieuDai}, cr: {self.chieuRong}"

    @property
    def DienTich(self):
        return float(self.chieuDai) * float(self.chieuRong)