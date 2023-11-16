"""Izveidojiet Python programmu, kas atkarībā no pašreizējās 
stundas izvada atbilstošu sveicienu, izmantojot if priekšrakstu.
 (labrīt<12, labdien<18, labvakar - parējais)"""

#Kaut kas import
import datetime


#Mainīgie
sobrid=datetime.datetime.now()
laiks=sobrid.hour

#Ja tagad ir pulkstens tik, tad saka to
if laiks<12:
    print("Labrīt")

elif laiks<18:
    print("Labdien")

#Ja nav viens no tiem, tad saka to
else:
    print("Labvakar") 

