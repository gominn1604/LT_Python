import math
import msvcrt
from os import system
import os

list = [1, 2, 3, 4, 5, 8, 9, 12, 15, 18, 21, 25, 30, 35, 37, 41, 21]


def CheckPerfectSquare(m):
    n = int(math.sqrt(m))
    return n * n == m


def CheckFibo(m):
    return CheckPerfectSquare(5 * m * m + 4) or CheckPerfectSquare(5 * m * m - 4)


def isOdd(i):
    return True if i % 2 != 0 else False


def SoLeKhongChiaHetCho5(list):
    sb = ""
    for i in list:
        if i % 5 != 0 and i % 2 != 0:
            sb = sb + str(i) + " "
    print(sb)


def XuatTatCaSoFibonacci(list):
    sb = ""
    for i in list:
        if CheckFibo(i) == True:
            sb = sb + str(i) + " "
    print(sb)

def isPrimeNum(lNumber):
    if(lNumber<2):
        return False
    squareRoot = int(math.sqrt(lNumber))
    for value in range(2, squareRoot+1):
        if(lNumber % value == 0):
            return False
    return True

def TimSoNguyenToLonNhat(list):
    result = []
    for i in list:
        if isPrimeNum(i):
            result.append(i)
    print(max(result))

def TimSoFibonacciBeNhat(list):
    result = []
    for i in list:
        if CheckFibo(i) == True:
            result.append(i)
    print(min(result))

def TinhTrungBinhCacSoLe(list):
    result = []
    sum = 0
    for i in list:
        if isOdd(i):
            result.append(i)
    print(f"Danh sách các số lẻ: {result}")
    for i in result:
        sum+=i
    print(sum/len(result))

def TichSoLeKhongChiaHetCho3(list):
    result = []
    mul = 1
    for i in list:
        if isOdd(i) and i %3 != 0:
            result.append(i)
    print(f"Danh sách các số lẻ không chia hết cho 3: {result}")
    for i in result:
        mul*=i
    print(mul)

def Swap(list, x, y):
    list[x], list[y] = list[y], list[x]

def Rev(list):
    print("Mảng sau khi đổi: ", list[::-1])

def TimSoLonThuNhi(list):
    maxst = max(list[0], list[1])
    maxnd = max(list[0], list[1])
    
    for i in range(2, len(list)):
        if list[i] > maxst:
            maxnd = maxst
            maxst = list[i]
        elif (list[i]>maxnd) and (maxst > list[i]):
            maxnd=list[i]
            
    print(f"Số lớn thứ nhì trong mảng là: {maxnd}")

def TongCacChuSo(n):
    total = 0
    while (n>0):
        total = total + n%10
        n = int(n/10)
    return total

def TongCacSo(list):
    sum = 0
    for i in list:
        sum += TongCacChuSo(i)
        
    print(f"Tổng các chữ số của tất cả các số trong danh sách là: {sum}")

def DemSoLanXuatHien(list, n):
    if(n in list):
        print(f"Số lần xuất hiện của {n} trong mảng là: ",list.count(n))
    else:
        print('Không tồn tại phần tử trong mảng!')

def XuatSoXuatHienNLan(list, n):
    result = []
    for i in list:
        if list.count(i) == n and i not in result:
            result.append(i)
    print(f"Số xuất hiện {n} lần trong mảng là: {result}")

def XuatHienNhieuNhat(list):
    b = []
    c = []
    for i in range(len(list)-1):
        b.append(list.count(list[i]))
        
    for i in range(len(b)-1):
        if b[i] == max(b):
            c.append(list[i])
            
    print(f"Số xuất hiện nhiều lần nhất trong danh sách là: ",c[0])

while True:
    system('CLS')
    print('Chọn chức năng muốn thực hiện: ')
    print('1: Xuất tất cả các số lẻ không chia hết cho 5')
    print('2: Xuất tất cả các số Fibonacci')
    print('3: Tìm số nguyên tố lớn nhất')
    print('4: Tìm số Fibonacci bé nhất')
    print('5: Tính trung bình các số lẻ')
    print('6: Tính tích các phần tử là số lẻ không chia hết cho 3 trong mảng')
    print('7: Đổi chỗ 2 phần tử của danh sách, đầu vào là 2 vị trí cần đổi chỗ')
    print('8: Đảo ngược trật tự các phần tử của danh sách')
    print('9: Xuất tất cả các số lớn thứ nhì của danh sách')
    print('10: Tính tổng các chữ số của tất cả các số trong danh sách')
    print('11: Đếm số lần xuất hiện của một số trong danh sách')
    print('12: Xuất các số xuất hiện n lần trong danh sách')
    print('13: Xuất các số xuất hiện nhiều lần nhất trong danh sách')
    print('0: Thoát chương trình')
    try:
        action = int(input("Nhập vào số của chức năng muốn chọn: "))
        if action == 0:
            break
        elif type(action) != int:
            print('Xin mời nhập lại')
            action = int(input())
            print('Chọn chức năng muốn thực hiện: ')
            print('1: Xuất tất cả các số lẻ không chia hết cho 5')
            print('2: Xuất tất cả các số Fibonacci')
            print('3: Tìm số nguyên tố lớn nhất')
            print('4: Tìm số Fibonacci bé nhất')
            print('5: Tính trung bình các số lẻ')
            print('6: Tính tích các phần tử là số lẻ không chia hết cho 3 trong mảng')
            print('7: Đổi chỗ 2 phần tử của danh sách, đầu vào là 2 vị trí cần đổi chỗ')
            print('8: Đảo ngược trật tự các phần tử của danh sách')
            print('9: Xuất tất cả các số lớn thứ nhì của danh sách')
            print('10: Tính tổng các chữ số của tất cả các số trong danh sách')
            print('11: Đếm số lần xuất hiện của một số trong danh sách')
            print('12: Xuất các số xuất hiện n lần trong danh sách')
            print('13: Xuất các số xuất hiện nhiều lần nhất trong danh sách')
            print('0: Thoát chương trình')
    except:
        print('Xin mời nhập lại')
        action = 0

    match action:
        case 1:
            system('CLS')
            print('===========================')
            print("Xuất tất cả các số lẻ không chia hết cho 5")
            print('===========================')
            SoLeKhongChiaHetCho5(list)
            print('===========================')
            msvcrt.getch()
        case 2:
            system('CLS')
            print('===========================')
            print("Xuất tất cả các số Fibonacci")
            print('===========================')
            XuatTatCaSoFibonacci(list)
            print('===========================')
            msvcrt.getch()
        case 3:
            system('CLS')
            print('===========================')
            print("Tìm số nguyên tố lớn nhất")
            print('===========================')
            TimSoNguyenToLonNhat(list)
            print('===========================')
            msvcrt.getch()
        case 4:
            system('CLS')
            print('===========================')
            print("Tìm số Fibonacci bé nhất")
            print('===========================')
            TimSoFibonacciBeNhat(list)
            print('===========================')
            msvcrt.getch()
        case 5:
            system('CLS')
            print('===========================')
            print("Tính trung bình các số lẻ")
            print('===========================')
            TinhTrungBinhCacSoLe(list)
            print('===========================')
            msvcrt.getch()
        case 6:
            system('CLS')
            print('===========================')
            print("Tính tích các phần tử là số lẻ không chia hết cho 3 trong mảng")
            print('===========================')
            TichSoLeKhongChiaHetCho3(list)
            print('===========================')
            msvcrt.getch()
        case 7:
            system('CLS')
            print('===========================')
            print("Đổi chỗ 2 phần tử của danh sách, đầu vào là 2 vị trí cần đổi chỗ")
            print('===========================')
            n1 = int(input("Nhập vào vị trí đầu tiên: "))
            n2 = int(input("Nhập vào vị trí cuối cùng: "))
            print('Mảng trước khi đổi: ', list)
            Swap(list, n1, n2)
            print('Mảng sau khi đổi: ', list)
            print('===========================')
            msvcrt.getch()
        case 8:
            system('CLS')
            print('===========================')
            print("Đảo ngược trật tự các phần tử của danh sách")
            print('===========================')
            print('Mảng trước khi đổi: ', list)
            Rev(list)
            print('===========================')
            msvcrt.getch()
        case 9:
            system('CLS')
            print('===========================')
            print("Xuất tất cả các số lớn thứ nhì của danh sách")
            print('===========================')
            print('Mảng hiện hành: ', list)
            TimSoLonThuNhi(list)
            print('===========================')
            msvcrt.getch()
        case 10:
            system('CLS')
            print('===========================')
            print("Tính tổng các chữ số của tất cả các số trong danh sách")
            print('===========================')
            print('Mảng hiện hành: ', list)
            TongCacSo(list)
            print('===========================')
            msvcrt.getch()
        case 11:
            system('CLS')
            print('===========================')
            print("Đếm số lần xuất hiện của một số trong danh sách")
            print('===========================')
            n= int(input("Nhập vào số n: "))
            print('Mảng hiện hành: ', list)
            DemSoLanXuatHien(list, n)
            print('===========================')
            msvcrt.getch()
        case 12:
            system('CLS')
            print('===========================')
            print("Xuất các số xuất hiện n lần trong danh sách")
            print('===========================')
            n = int(input("Nhập vào số n: "))
            print('Mảng hiện hành: ', list)
            XuatSoXuatHienNLan(list, n)
            print('===========================')
            msvcrt.getch()
        case 13:
            system('CLS')
            print('===========================')
            print("Xuất các số xuất hiện nhiều lần nhất trong danh sách")
            print('===========================')
            print('Mảng hiện hành: ', list)
            XuatHienNhieuNhat(list)
            print('===========================')
            msvcrt.getch()
