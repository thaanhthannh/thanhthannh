# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 19:50:30 2024

@author: Thanh Thanh
"""
def ktra_so_am_duong(so):
    if so<0 and so%2!=0:
        return -1
    elif so>0 and so%2==0:
        return 1
    else:
        return 0
so=int(input("Nhap so: "))
if __name__=="__main__":
    print(ktra_so_am_duong(so))
