# conexión de Python con SQL Server
import pyodbc 
import pandas as pd

#se crea variable para guardar la conexión de sql
server = '192.168.0.139\BODEGA'
dataBase = 'DataStage'
userName = 'odbc'
password = 'Odbc.2019'
#conexionString = 'DRIVER={{SQL Server}};SERVER={server};DATABASE={dataBase};Trusted_Connection=yes;'
#conexionString ='DRIVER={SQL Server};SERVER={server};DATABASE={dataBase};UID={userName};PWD={password}'
conexionString ='DRIVER={SQL Server};SERVER=192.168.0.139\BODEGA;DATABASE=DataStage;UID=odbc;PWD=Odbc.2019'

#Se hace la conexión
try:
    conexion = pyodbc.connect(conexionString)
    print('Exito')
except: 
    print('Error')

#se crea varia  para abrir la conexión 
cursor = conexion.cursor()

# Llamamos la base de Datos
query_Claro = "SELECT  Movil FROM xls.LineasRayogas WHERE  Valor IS NULL"
df_tablas = pd.read_sql(query_Claro,conexion)
df_tablas.info()
df_tablas.sample(3)

#se importa libreria para abri el whatsaap    

import pyautogui, webbrowser
from time import sleep

url= 'https://web.whatsapp.com/send?phone=+57'
celular = '3176655253'

#webbrowser.open('https://web.whatsapp.com/send?phone=+57'+celular)
webbrowser.open(url+celular)

sleep(10)

for i in range(2):
    pyautogui.typewrite('Prueba api whastapp rayogas area TI DATOS ingeniero Jesus Vargas')
    pyautogui.press('enter')
    