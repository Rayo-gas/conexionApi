# conexión de Python con SQL Server
import pyodbc 
import pandas as pd

#se crean variables para guardar la conexion de sql
server = '192.168.0.139\BODEGA'
dataBase = 'DataStage'
userName = 'odbc'
password = 'Odbc.2019'
#conexionString = 'DRIVER={{SQL Server}};SERVER={server};DATABASE={dataBase};Trusted_Connection=yes;'
#conexionString ='DRIVER={{SQL Server}};SERVER={server};DATABASE={dataBase};UID={userName};PWD={password}'
conexionString ='DRIVER={SQL Server};SERVER=192.168.0.139\BODEGA;DATABASE=DataStage;UID=odbc;PWD=Odbc.2019'

#Se crea cadena de conexion

try:
    conexion = pyodbc.connect(conexionString)
    print('Exito')
except: 
    print('Error')
    

import pyautogui, webbrowser
from time import sleep
Numero = '+573164916409'
 
webbrowser.open('https://web.whatsapp.com/send?phone=+573164916409')
#webbrowser.open('https://web.whatsapp.com/send??gruop=TIC Rayogas')
 
sleep(10)
 
for i in range(2):
    pyautogui.typewrite('Ok, prueba api whastapp Chucho TI')
    pyautogui.press('enter')