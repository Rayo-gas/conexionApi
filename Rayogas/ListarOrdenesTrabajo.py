import requests
import json
#import pandas as pd

# URL base del servicio REST
base_url = "https://fleet.cloudfleet.com/api/v2/work-orders/"

# Token de autorización
token = "1mT6Lny.R38_jSB5iTHtmUKD2d6RdOXQZDD8HLzg4"

# Headers de la petición
headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/json",
}

# Inicializar la página en 1
page = 1

# Inicializar la fecha inicial
FechaIni = "2024-03-01"

# Inicializar la fecha Final
FechaFin = "2024-06-24"

# Inicializar una lista para almacenar todas las respuestas
all_data = []

while True:
    # Agregar el parámetro de página a la URL
    url = f"{base_url}?page={page}&startDateFrom={FechaIni}T00:00:00&startDateTo={FechaFin}T00:00:00"

    # Realizar la petición GET
    response = requests.get(url, headers=headers)

    # Verificar que la petición fue exitosa
    if response.status_code == 200:
        # Convertir la respuesta a JSON
        data = response.json()

        # Verificar si el mensaje de error está en la respuesta
        if "error" in data and data["error"]["message"] == "No Vehicles found with the specified filters":
            break

        # Agregar la respuesta a la lista
        all_data.append(data)

        # Incrementar la página
        page += 1
    else:
        print(f"Error: {response.status_code}")
        break

# Guardar todas las respuestas en un archivo .json
with open("ListarOrdenesTrabajo.json", "w") as file:
    json.dump(all_data, file, indent=4)
    