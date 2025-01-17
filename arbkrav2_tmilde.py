# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 16:16:13 2025

@author: tfm
"""

print('\n'"*** Oppgave 1 ***")

alder = int(input('Hvilket år er du født? ') )
print("Din alder i løpet av 2024 vil være: ",2024-alder)



print('\n'"*** Oppgave 2 ***")
import math
antall_elever = int(input('Skriv inn antall elever:' ))
print("Det må kjøpes inn ",math.ceil(antall_elever/4)," pizzaer til klassefesten")



""" Oppgave 3 """
print('\n'"*** Oppgave 3 ***")
import numpy as np
v_grad = float(input('Skriv inn gradtallet:' ))
v_rad = v_grad*np.pi/180
print("Radiantallet til vinkel gradtallet ",v_grad, "er: ",round(v_rad,3))



""" Oppg 4 """
import pprint as pp

print('\n'"*** Oppgave 4a ***")
countrydict={"England":["London", 8.982],
             "Danmark":["København", 1.8],
             "Norge":["Oslo", 1.1],
             "Sverige":["Stockholm", 1.3]
             }

print('\n'"*** Oppgave 4b ***")
chkcountry = input('Skriv inn land:' )
if chkcountry in countrydict.keys():
       countryinfo=countrydict[chkcountry]
       print(countryinfo[0],"er hovedstaden med",countryinfo[1],"mill. innbyggere")       
       

print('\n'"*** Oppgave 4c ***")
print("Legg til nytt land med info")
newcountry = input('Skriv inn land:' )
if newcountry not in countrydict.keys():
    newcapital = input('Skriv inn hovedstad:' )
    newpeople = input('Skriv inn antall innbyggere:' )
countrydict[newcountry] = [newcapital,newpeople]

print('\n'"Innhold av oppdatert dictionary:")
pp.pprint(countrydict)


""" Oppg 5 """
print('\n'"*** Oppgave 5 ***")
varA, varB = input("Sett inn 2 variabler til en rettvinklet trekant og halvsirkel med mellomrom her: ").split()
varA, varB = [int(varA), int(varB)]
print('\n'"Rettvinklet trekant:")
print("Areal er",(varA*varB)/2)
print("Omkrets er",round(varA + varB + (math.sqrt(varA**2 + varB**2)),3))

print('\n'"Halvsirkel:")
print("Areal er",round((math.pi * varA**2),2))
print("Omkrets er",round((2 * math.pi * varA),2))


""" Oppg 6 """

print('\n'"*** Oppgave 6 ***")
import numpy as np
import matplotlib.pyplot as plt

def f ( x ):
    return -x **2 - 5

xa = np.linspace ( -10 , 10 , 200)
plt.close ("all")
plt.figure (1 , figsize =(12 , 9))
plt.plot ( xa, f( xa ) )
plt.show ()





