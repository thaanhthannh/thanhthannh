# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 21:36:42 2024

@author: Thanh Thanh
"""
import math
#Can bậc x của n
def can_bac_n(x,n):
    return x ** (1/n)
#Đảo số
# chuỗi số (vẫn giữ lại số 0 phía trước)
def dao_so(n):
    return str(n)[::-1]\
# không giữ lại số 0
def dao_so_(n):
    return int(str(n)[::-1])
#cách 3 số đảo
def dao(n):
    dao=0
    while n>0:
        dao=dao*10+n%10
        n//=10
    return dao
#Số chính phương
def ktra_chinhphuong(n):
    return int(math.sqrt(n))**2 == n
#Số nguyên tố
def ktra_nguyento(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i ==0:
            return False
    return True
# Tích các số lẻ
def tichsole(n):
    tich = 1
    for i in str(n):
        if int(i) % 2 !=0:
            tich *=int(i)
    return tich
# Tổng các số nguyên tố nhỏ hơn n
def tongnguyentonhohonn(n):
    tong_ngto =0
    for i in range(2,n):
        if ktra_nguyento(i):
            tong_ngto +=i
    return tong_ngto
# Tổng các số chính phương nhỏ hơn n
def tongchinhphuong(n):
    tong_cp =0
    for i in range(1, int(math.sqrt(n)) +1):
        tong_cp += i**i

    return tong_cp
# Tổng ước số dương của n
def tonguoc(n):
    tong =0
    for i in range(1,n+1):
        if n%1 ==0:
            tong += i
    return tong







if __name__=='__main__':
    print(can_bac_n(8, 3))
    print(dao_so(123450))
    print(dao(123450))
    print(ktra_chinhphuong(2))
    print(ktra_nguyento(4))
    print(tichsole(3))
    print(tongnguyentonhohonn(7))
    print(tongchinhphuong(9))
    print(tonguoc(12))

 