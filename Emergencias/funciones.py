import json
from composite import ArchivoSAMUR, Documento, Carpeta


def agregar_documento_a_carpeta(carpeta, documento):
    if isinstance(carpeta, Carpeta):
        carpeta.agregar_documento(documento)
    else:
        print("No se puede agregar a un elemento que no es una carpeta.")


def eliminar_documento_de_carpeta(carpeta, nombre_documento):
    documento = carpeta.obtener_documento(nombre_documento)
    if documento:
        carpeta.eliminar_documento(documento)
    else:
        print(f"No se encontró el documento '{nombre_documento}'.")


def buscar_documento_por_nombre(carpeta, nombre_documento):
    return carpeta.obtener_documento(nombre_documento)


def buscar_elemento_por_nombre(elemento, nombre):
    if isinstance(elemento, list):
        for item in elemento:
            resultado = buscar_elemento_por_nombre(item, nombre)
            if resultado:
                return resultado
    elif isinstance(elemento, ArchivoSAMUR) and elemento.obtener_nombre() == nombre:
        return elemento
    return None


def mostrar_menu():
    print("1. Mostrar JSON")
    print("2. Agregar elemento")
    print("3. Eliminar elemento")
    print("4. Salir")


def agregar_elemento(estructura):
    ruta = input(
        "Ingrese la ruta donde desea agregar el elemento (por ejemplo, 'Mis documentos/Carpeta1'): ")
    nombres = ruta.split("/")
    carpeta_actual = estructura

    for nombre in nombres[:-1]:
        elemento = buscar_elemento_por_nombre(
            carpeta_actual.contenido, nombre)
        if isinstance(elemento, Carpeta):
            carpeta_actual = elemento
        else:
            print(f"No se encontró la carpeta '{
                  nombre}' o no es una carpeta válida.")
            return

    nombre_elemento = nombres[-1]
    tipo = input(
        "Ingrese el tipo del nuevo elemento ('documento' o 'carpeta'): ")
    if tipo == 'documento':
        tamaño = input("Ingrese el tamaño del nuevo documento: ")
        nuevo_documento = Documento(nombre_elemento, tipo, tamaño)
        agregar_documento_a_carpeta(carpeta_actual, nuevo_documento)
    elif tipo == 'carpeta':
        nueva_carpeta = Carpeta(nombre_elemento)
        agregar_documento_a_carpeta(carpeta_actual, nueva_carpeta)
    else:
        print("Tipo de elemento inválido.")


def eliminar_elemento(carpeta):
    nombre = input("Ingrese el nombre del elemento a eliminar: ")
    eliminar_documento_de_carpeta(carpeta, nombre)


def guardar_json(nombre_archivo, estructura):
    with open(nombre_archivo, 'w') as archivo_salida:
        json.dump(estructura.__dict__, archivo_salida, indent=4)


nombre_archivo = "Emergencias/data/prueba.json"

try:
    with open("Emergencias/data/prueba.json", 'r') as archivo_entrada:
        data = json.load(archivo_entrada)
        nombre_carpeta = data.get('nombre', 'Documentos')
        estructura = Carpeta(nombre_carpeta)
        contenido = data.get('contenido', [])
        for elemento in contenido:
            if elemento['tipo'] == 'carpeta':
                carpeta = Carpeta(elemento['nombre'])
                estructura.agregar_documento(carpeta)
            elif elemento['tipo'] == 'documento':
                documento = Documento(elemento['nombre'], elemento['tipo'], elemento['tamaño'])
                estructura.agregar_documento(documento)
except FileNotFoundError:
    estructura = Carpeta('Documentos')


def main():
    while True:
        mostrar_menu()
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
             print(json.dumps(estructura.to_json(), indent=4))
        elif opcion == 2:
            agregar_elemento(estructura)
            guardar_json(nombre_archivo, estructura)
        elif opcion == 3:
            eliminar_elemento(estructura)
            guardar_json(nombre_archivo, estructura)
        elif opcion == 4:
            break
        else:
            print("Opción inválida.")

    guardar_json(nombre_archivo, estructura)


if __name__ == '__main__':
    main()
