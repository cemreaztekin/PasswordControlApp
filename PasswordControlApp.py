# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 19:11:16 2022

@author: user
"""
sifre = input("Lütfen şifrenizi giriniz")
sifreUzunluk = len(sifre)
buyukHarfSayi=0
kucukHarfSayi=0
rakam=0
ozelKarakter=0
guclulukSkoru=0
kontrol=True

buyukHarfListe = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',  'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 
                  'V', 'W', 'X', 'Y', 'Z']   
                
kucukHarfListe = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',  'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 
                  'v', 'w', 'x', 'y', 'z']  

rakamListe = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']

ozelKarakterListe = ['(' , ')' , '*' , '+' , ',' , '-' , '.']

#sifre uzunluk kontrolu 
if (sifreUzunluk<4):
        print("Geçersiz Şifre")
        print("Şifre çok kısa")
        kontrol=False
        
elif (sifreUzunluk>8):
        print("Geçersiz Şifre")
        print("Şifre en fazla 8 karakter olabilir")
        kontrol=False

#sifre uzunluk doğrulandıysa --> degisken degerlerinin bulunması    
if (kontrol == True):
    for i in buyukHarfListe:
        for j in sifre:
            if i==j:               
                buyukHarfSayi+=1  
    for i in kucukHarfListe:
        for j in sifre:
            if i==j:                
                kucukHarfSayi+=1  
    for i in rakamListe:
        for j in sifre:
            if i==j:
                rakam+=1 
    for i in ozelKarakterListe:
        for j in sifre:
            if i==j:
                ozelKarakter+=1 

#sifre uzunluk doğrulandıysa --> 'gecerli sifre' sartlarının kontolu
if (kontrol==True):
    if(kucukHarfSayi<1):
        print("Geçersiz Şifre")
        print("Şifre en az bir küçük harf içermeli")
        kontrol=False
       
    if(buyukHarfSayi<1):
        print("Geçersiz Şifre")
        print("Şifre en az bir büyük harf içermeli")
        kontrol=False
      
    if(rakam<1):
        print("Geçersiz Şifre")
        print("Şifre en az bir rakam içermeli")
        kontrol=False
       
    if(ozelKarakter<1):
        print("Geçersiz Şifre")
        print("Şifre izin verilen özel karakterlerden en az birini içermeli")
        kontrol=False
        
    if (sifreUzunluk != (buyukHarfSayi+kucukHarfSayi+rakam+ozelKarakter)):
        print("Geçersiz Şifre")
        print("Şifre yalnızca sayı, harf ve izin verilen özel karakterlerden oluşmalı" )
        kontrol = False 

#'gecerli sifre' sartları saglandiysa --> sifre gucluluk kontrolu ve mesajın verilmesi
if (kontrol==True):  
    guclulukSkoru = 3 * (kucukHarfSayi+1) * 5 * (buyukHarfSayi+1) *  2 * (rakam+1) * 4 * (ozelKarakter+1)-120
    if(guclulukSkoru<2000):
        print("Geçerli Şifre")
        print("Çok Zayıf Şifre")
    elif(guclulukSkoru >= 2000 and guclulukSkoru<4000):
        print("Geçerli Şifre")
        print("Zayıf Şifre")
    elif (guclulukSkoru >= 4000 and guclulukSkoru<6000):
        print("Geçerli Şifre")
        print("Ortalama Şifre")     
    elif (guclulukSkoru >= 6000 and guclulukSkoru<9000):
        print("Geçerli Şifre")
        print("Güçlü Şifre")
    elif (guclulukSkoru >= 9000):
        print("Geçerli Şifre")
        print("Çok Güçlü Şifre") 
        
        
        
 
