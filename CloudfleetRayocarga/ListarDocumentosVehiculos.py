import requests
import json

# URL base del servicio REST
base_url = "https://fleet.cloudfleet.com/api/v1/vehicles/documents/"

# Token de autorización
token = ""

# Headers de la petición
headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/json",
}

# Inicializar la página en 1
page = 1

# Inicializar una lista para almacenar todas las respuestas
all_data = []

while True:
    # Agregar el parámetro de página a la URL
    url = f"{base_url}?page={page}"

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
with open("ListarDocumentosVehiculos.json", "w") as file:
    json.dump(all_data, file, indent=4)