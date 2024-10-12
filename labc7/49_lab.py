# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 19:39:35 2024

@author: Thanh Thanh
"""
def ktra_so_chan_am(n):
    return n<0 and n%2==0
n=int(input("Nhap so: "))
if __name__=="__main__":
    print(ktra_so_chan_am(n))
    

