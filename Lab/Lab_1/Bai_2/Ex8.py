from math import sqrt


def ptBac2(a, b, c):
    x1 = 0
    x2 = 0
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Phương trình vô nghiệm")
    elif delta == 0:
        print(f"Phương trình có nghiệm kép x1=x2={-(b/(2*a))}")
    else:
        x1 = (-(b) + sqrt(delta))/(2*a)
        x2 = (-(b) - sqrt(delta))/(2*a)
        print(f"Phương trình có 2 nghiệm phân biệt x1 = {x1}, x2 = {x2}")


a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
while True:
    if a == 0 and b == 0:
        print("Một trong hai hệ số a, b phải khác 0")
        a = float(input("Nhập lại hệ số a: "))
        b = float(input("Nhập lại hệ số b: "))
    else:
        break

c = float(input("Nhập hệ số c: "))

ptBac2(a, b, c)
