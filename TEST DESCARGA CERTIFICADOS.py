from turtle import width
import pyautogui as pg, webbrowser as wb, time as tm, pandas as pd, os as os

data = pd.read_csv("Resultados7K.csv", encoding= 'unicode_escape')
data_dict = data.to_dict('list')
dorsales = data_dict['dorsales']
mensajes = data_dict['mensaje']
combo = zip(dorsales, mensajes)
first = True

for dorsales, mensaje in combo:
    #wb.open("https://sportmaniacs.com/es/races/trail-rinconada-2023-la-ruta-de-la-garnacha/64c99df5-97e8-48f2-97bb-0d12ac1f1123/results/athlete/"+dorsales+"/results")
    wb.open("https://sportmaniacs.com/es/races/trail-rinconada-2023-la-ruta-de-la-garnacha/64c99df5-97e8-48f2-97bb-0d12ac1f1123/results/athlete/"+dorsales+"/results")
    tm.sleep(2)
    if first:
        first = False
    tm.sleep(3)
    #pg.click()
    #pg.hotkey('ctrl', 'v')
    #tm.sleep(8)
    pg.press('tab', 16)
    pg.press('enter')
    tm.sleep(7)
    pg.hotkey('ctrl', 'w')
    print("descargado",dorsales)