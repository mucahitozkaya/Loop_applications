# -*- coding: utf-8 -*-
"""
Created on Mon May  3 19:38:44 2021

@author: hpp
"""
#%% Tahmin
import random

sayi = random.randint(1,400)
can = int(input('Kaç hak istersiniz? = '))
hak = can
sayac = 0

while hak > 0:
    hak -= 1
    sayac += 1
    tahmin = int(input('Tahmin: '))
    
    if sayi == tahmin:
        print(f'Tebrikler {sayac}. defada bildiniz. Toplam puanınız: {100 - (100/can) * (sayac-1) }')
        break
    elif sayi > tahmin:
        print('yukarı')
    else:
        print('aşağı')
    if hak == 0:
        print(f'hakkınız bitti. Tutulan sayı : {sayi}')     
        
#%% Asal Sayı Bulma
        
sayi = int(input('sayı: '))
asalmi = True

if sayi == 1:
    asalmi = False

for i in range(2,sayi):
    if (sayi % i == 0):
        asalmi = False
        break
if asalmi:
    print(sayi,'Sayısı Asaldır')
else:
    print(sayi,'Sayısı Asal Değildir')
    
    
#%%Faktoriyel
    
sayi = int(input('Faktöriyelini öğrenmek istediğiniz sayıyı giriniz : '))
sonuc = 1
for i in range(1,sayi+1):
    sonuc *= i
print(f'{sayi} sayısının faktöreyli : {sonuc}')
    
    
    
    
    
    