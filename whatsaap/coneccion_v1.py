#librerias 
import pyodbc 
import pandas as pd
import pyautogui, webbrowser
from time import sleep 

#region Variables
query = 'SELECT Movil FROM xls.LineasRayogas WHERE  Valor IS NULL'
celular = '3176655253'
url = 'https://web.whatsapp.com/send?phone=+57'
tiempoMsj = 6
RepetirMsj = 2
mensaje = 'Prueba api whastapp rayogas area TI DATOS'


#Se hace la conexión
conexionString ='DRIVER={SQL Server};SERVER=192.168.0.139\BODEGA;DATABASE=DataStage;UID=odbc;PWD=Odbc.2019'
try:
    conexion = pyodbc.connect(conexionString)
    print('Exito')
except: 
    print('Error')

#abrir la conexión 
cursor = conexion.cursor()

# Llamado la base de Datos
cursor.execute (query)
for row in cursor:
    #webbrowser.open(url+row)
    #sleep(tiempoMsj)

    ##Ciclo para enviar mensaje 
    #for i in range(RepetirMsj):
    #    pyautogui.typewrite(mensaje)
    #    pyautogui.press('enter')
    print(row)   
    
#abri el whatsaap   
webbrowser.open(url+celular)

#tiempo de espera para enviar mensaje el tienpo no puede ser menor de 6 segundos 
sleep(tiempoMsj)

#Ciclo para enviar mensaje 
for i in range(RepetirMsj):
    pyautogui.typewrite(mensaje)
    pyautogui.press('enter')

