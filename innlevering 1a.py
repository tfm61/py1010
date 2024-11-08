# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 
@author: tarje milde
"""

""" Kost årlig bilhold El vs Bensin """

import sys

def calculate_car_cost(aarlig_km):
    fors_el = 5000
    fors_ben = 7500
    trafikk_avg = 8.38
    forbr_el = 0.2
    strompris = 2
    ben_forb_pris = 1
    bom_avg_el = 0.1
    bom_avg_ben = 0.3

    el_aar_kost = fors_el + ((forbr_el * strompris) + bom_avg_el) * \
        aarlig_km + (trafikk_avg * 365)

    ben_aar_kost = fors_ben + (ben_forb_pris + bom_avg_ben) * \
        aarlig_km + (trafikk_avg * 365)

    return el_aar_kost, ben_aar_kost


""" Main program """

aarlig_km = int(input("Legg inn antall km? "))

if aarlig_km < 1:
    raise ValueError("Antall km må være over 0")

el_aar_kost, ben_aar_kost = calculate_car_cost(aarlig_km)

print("Pris for ElBil     kr:  ", int(el_aar_kost))

print("Pris for BensinBil kr: ", int(ben_aar_kost))

sys.exit()





