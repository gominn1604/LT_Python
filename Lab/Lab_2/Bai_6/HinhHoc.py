class HinhHoc:
    def __init__(self, canh: float) -> None:
        self._canh = canh

    @property
    def canh(self):
        return self._canh

    @canh.setter
    def canh(self, canh: float):
        self._canh = canh

    def DienTich(self):
        pass

    def __str__(self) -> str:
        return f"Hinh "