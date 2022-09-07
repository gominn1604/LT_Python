from cmath import phase


class PhanSo:
    def __init__(self, tu: int, mau: int) -> None:
        self.__tu = tu
        self.__mau = mau
    
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
        return PhanSo(tu, mau)

    def __str__(self) -> str:
        return(f"{self.__tu}/{self.__mau}")

    def __add__(self, other):
        tuA = self.__tu
        mauA = self.__mau
        tuB = other.__tu
        mauB = other.__mau
        tuA = tuA * mauB
        tuB = tuB * mauA
        mauA = mauA* mauB
        return PhanSo((tuA+tuB), mauA).rutGon()

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

a = PhanSo(2, 3)
b = PhanSo(3, 5)


print(f"{a} + {b} = {a.__add__(b)}")
print(f"{a} - {b} = {a.__sub__(b)}")
print(f"{a} * {b} = {a.__mul__(b)}")
print(f"{a} / {b} = {a.__truediv__(b)}")




