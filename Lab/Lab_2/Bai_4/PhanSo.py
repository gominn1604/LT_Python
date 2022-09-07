from cmath import phase


class PhanSo:
    def __init__(self) -> None:
        self.__tu = 0
        self.__mau = 1

    @property
    def tuSo(self):
        return self.__tu

    @tuSo.setter
    def tuSo(self, tuso):
        self.__tu = tuso

    @property
    def mauSo(self):
        return self.__mau

    @mauSo.setter
    def mauSo(self, mauso):
        if mauso != 0:
            self.__mau = mauso
        else:
            print("Mau so khong hop le")
        
    def UCLN(self):
        a = self.__tu
        b = self.__mau
        r = a % b
        while r != 0:
            a = b
            b = r
            r = a % b
        ucln = b
        return ucln

    def rutGon(self) -> None:
        ucln = self.UCLN()
        tu = self.__tu / ucln
        mau = self.__mau / ucln
        ps = PhanSo()
        ps.tuSo = tu
        ps.mauSo = mau
        return ps

    def __str__(self) -> str:
        return(f"{self.__tu}/{self.__mau}")

    def __add__(self, other):
        tuA = self.tuSo
        mauA = self.mauSo
        tuB = other.tuSo
        mauB = other.mauSo  
        ps = PhanSo()
        ps.tuSo = tuA * mauB + tuB * mauA
        ps.mauSo = mauA * mauB
        return ps.rutGon()

    def __sub__(self, other):
        tuA = self.__tu
        mauA = self.__mau
        tuB = other.__tu
        mauB = other.__mau
        tuA = tuA * mauB
        tuB = tuB * mauA
        mauA = mauA* mauB
        return PhanSo((tuA-tuB), mauA).rutGon()

    def __mul__(self, other):
        tuA = self.__tu
        mauA = self.__mau
        tuB = other.__tu
        mauB = other.__mau
        tuA = tuA * tuB
        mauA = mauA * mauB
        return PhanSo(tuA, mauA).rutGon()

    def __truediv__(self, other):
        tuA = self.__tu
        mauA = self.__mau
        tuB = other.__mau
        mauB = other.__tu
        tuA = tuA * tuB
        mauA = mauA * mauB
        return PhanSo(tuA, mauA).rutGon()

ps1 = PhanSo()
ps2 = PhanSo()

ps1.tuSo = 1
ps2.tuSo = -2
ps2.mauSo = 3
ps1.mauSo = 2

# print(f"{ps1} + {ps2} = {ps1.__add__(ps2)}")
# # print(f"{a} - {b} = {a.__sub__(b)}")
# # print(f"{a} * {b} = {a.__mul__(b)}")
# # print(f"{a} / {b} = {a.__truediv__(b)}")



