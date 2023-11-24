import json

ruta_json = 'Emergencias/data/prueba.json'

def cargar_json(ruta):
    try:
        with open(ruta, 'r') as archivo:
            data = json.load(archivo)
        return data
    except FileNotFoundError:
        print(f"El archivo en la ruta '{ruta}' no fue encontrado.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error al decodificar JSON en '{ruta}': {e}")
        return None

def mostrar_contenido_json(ruta):
    datos_json = cargar_json(ruta)
    if datos_json:
        print(json.dumps(datos_json, indent=4, ensure_ascii=False))

mostrar_contenido_json(ruta_json)