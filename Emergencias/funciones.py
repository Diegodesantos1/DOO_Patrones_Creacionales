import json

from composite import Documento, Carpeta, Enlace
from proxy import Proxy


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


ruta_json = 'Emergencias/data/prueba.json'


def cargar_estructura_desde_json(ruta):
    datos_json = cargar_json(ruta)
    if datos_json:
        nombre = datos_json['nombre']
        tipo = datos_json['tipo']
        contenido = []

        for item in datos_json['contenido']:
            if item['tipo'] == 'documento':
                contenido.append(
                    Documento(item['nombre'], item['tipo'], item['tamaño']))
            elif item['tipo'] == 'carpeta':
                subcarpeta = cargar_estructura_desde_json_recursivo(item)
                contenido.append(
                    Carpeta(item['nombre'], item['tipo'], subcarpeta))
            elif item['tipo'] == 'enlace':
                contenido.append(
                    Enlace(item['nombre'], item['tipo'], item['url']))

        return Carpeta(nombre, tipo, contenido)
    else:
        return None


def cargar_estructura_desde_json_recursivo(data):
    contenido = []

    for item in data['contenido']:
        if item['tipo'] == 'documento':
            contenido.append(
                Documento(item['nombre'], item['tipo'], item['tamaño']))
        elif item['tipo'] == 'carpeta':
            subcarpeta = cargar_estructura_desde_json_recursivo(item)
            contenido.append(Carpeta(item['nombre'], item['tipo'], subcarpeta))
        elif item['tipo'] == 'enlace':
            contenido.append(Enlace(item['nombre'], item['tipo'], item['url']))

    return contenido


estructura = cargar_estructura_desde_json(ruta_json)


def guardar_json(nombre_archivo, estructura):
    try:
        estructura_serializable = estructura.to_dict()
        with open(nombre_archivo, 'w') as archivo_salida:
            json.dump(estructura_serializable, archivo_salida, indent=4)
        print(f"Guardado exitosamente en '{nombre_archivo}'.")

        return estructura
    except Exception as e:
        print(f"Error al guardar en '{nombre_archivo}': {e}")


def mostrar_contenido_json(ruta):
    datos_json = cargar_json(ruta)
    if datos_json:
        print(json.dumps(datos_json, indent=4, ensure_ascii=False))


def seleccionar_carpeta_por_ruta(carpeta_actual, ruta):
    carpetas = ruta.split('/')
    carpeta_temp = carpeta_actual

    if carpetas[0] != carpeta_temp.obtener_nombre():
        print(f"No se encontró la carpeta '{
              carpetas[0]}' como carpeta actual.")
        return None

    for nombre in carpetas[1:]:
        encontrado = False
        for contenido in carpeta_temp.contenido:
            if isinstance(contenido, Carpeta) and contenido.obtener_nombre() == nombre:
                carpeta_temp = contenido
                encontrado = True
                break

        if not encontrado:
            print(f"No se encontró la carpeta '{
                  nombre}' en la ruta proporcionada.")
            return None

    return carpeta_temp


ruta_json = 'Emergencias/data/prueba.json'


def mostrar_menu():
    print("1. Mostrar JSON")
    print("2. Agregar documento")
    print("3. Eliminar documento")
    print("4. Modificar documento")
    print("5. Agregar carpeta")
    print("6. Eliminar carpeta")
    print("7. Modificar carpeta")
    print("8. Agregar enlace")
    print("9. Eliminar enlace")
    print("10. Modificar enlace")
    print("11. Salir")




def main_base():
    while True:
        print("1. Mostrar JSON")
        print("2. Salir")
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            mostrar_contenido_json(ruta_json)
        elif opcion == 2:
            break
        else:
            print("Opción inválida.")



def main(estructura):
    carpeta_actual = estructura
    while True:
        mostrar_menu()
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            mostrar_contenido_json(ruta_json)
        elif opcion == 2:
            ruta = input(
                "Ingrese la ruta de la carpeta (p.ej., 'Documentos'): ")
            carpeta_para_documento = seleccionar_carpeta_por_ruta(
                carpeta_actual, ruta)
            if carpeta_para_documento:
                nombre = input("Ingrese el nombre del documento: ")
                tipo = "documento"
                tamaño = input("Ingrese el tamaño del documento: ")
                documento = Documento(nombre, tipo, tamaño)
                carpeta_para_documento.agregar_documento(documento)
                guardar_json(ruta_json, estructura)
        elif opcion == 3:
            ruta = input(
                "Ingrese la ruta de la carpeta (p.ej., 'Documentos'): ")
            carpeta_para_eliminar = seleccionar_carpeta_por_ruta(
                carpeta_actual, ruta)
            if carpeta_para_eliminar:
                nombre_documento = input(
                    "Ingrese el nombre del documento a eliminar: ")
                carpeta_para_eliminar.eliminar_documento(nombre_documento)
                guardar_json(ruta_json, estructura)
        elif opcion == 4:
            ruta = input(
                "Ingrese la ruta de la carpeta (p.ej., 'Documentos'): ")
            carpeta_para_modificar = seleccionar_carpeta_por_ruta(
                carpeta_actual, ruta)
            if carpeta_para_modificar:
                nombre_documento = input(
                    "Ingrese el nombre del documento a modificar: ")
                atributo = input(
                    "Ingrese el atributo a modificar (nombre, tamaño): ")
                nuevo_valor = input(
                    f"Ingrese el nuevo valor para '{atributo}': ")
                carpeta_para_modificar.modificar_documento(
                    nombre_documento, atributo, nuevo_valor)
                guardar_json(ruta_json, estructura)
        elif opcion == 5:
            ruta = input(
                "Ingrese la ruta de la carpeta (p.ej., 'Documentos'): ")
            carpeta_para_carpeta = seleccionar_carpeta_por_ruta(
                carpeta_actual, ruta)
            if carpeta_para_carpeta:
                nombre = input("Ingrese el nombre de la carpeta: ")
                tipo = "carpeta"
                contenido = []
                carpeta = Carpeta(nombre, tipo, contenido)
                carpeta_para_carpeta.agregar_documento(carpeta)
                guardar_json(ruta_json, estructura)
        elif opcion == 6:
            ruta = input(
                "Ingrese la ruta de la carpeta (p.ej., 'Documentos'): ")
            carpeta_para_eliminar = seleccionar_carpeta_por_ruta(
                carpeta_actual, ruta)
            if carpeta_para_eliminar:
                nombre_documento = input(
                    "Ingrese el nombre de la carpeta a eliminar: ")
                carpeta_para_eliminar.eliminar_carpeta(nombre_documento)
                guardar_json(ruta_json, estructura)
        elif opcion == 7:
            ruta = input(
                "Ingrese la ruta de la carpeta (p.ej., 'Documentos'): ")
            carpeta_para_modificar = seleccionar_carpeta_por_ruta(
                carpeta_actual, ruta)
            if carpeta_para_modificar:
                nombre_carpeta = input(
                    "Ingrese el nombre de la carpeta a modificar: ")
                nombre = "nombre"
                nuevo_valor = input(f"Ingrese el nuevo valor para el '{
                                    nombre}' de la carpeta: ")
                carpeta_para_modificar.modificar_carpeta(
                    nombre_carpeta, nombre, nuevo_valor)
                guardar_json(ruta_json, estructura)
        elif opcion == 8:
            ruta = input(
                "Ingrese la ruta de la carpeta (p.ej., 'Documentos'): ")
            carpeta_para_enlace = seleccionar_carpeta_por_ruta(
                carpeta_actual, ruta)
            if carpeta_para_enlace:
                nombre = input("Ingrese el nombre del enlace: ")
                tipo = "enlace"
                url = input("Ingrese la url del enlace: ")
                enlace = Enlace(nombre, tipo, url)
                carpeta_para_enlace.agregar_enlace(enlace)
                guardar_json(ruta_json, estructura)
        elif opcion == 9:
            ruta = input(
                "Ingrese la ruta de la carpeta (p.ej., 'Documentos'): ")
            carpeta_para_eliminar = seleccionar_carpeta_por_ruta(
                carpeta_actual, ruta)
            if carpeta_para_eliminar:
                nombre_documento = input(
                    "Ingrese el nombre del enlace a eliminar: ")
                carpeta_para_eliminar.eliminar_enlace(nombre_documento)
                guardar_json(ruta_json, estructura)
        elif opcion == 10:
            ruta = input(
                "Ingrese la ruta de la carpeta (p.ej., 'Documentos'): ")
            carpeta_para_modificar = seleccionar_carpeta_por_ruta(
                carpeta_actual, ruta)
            if carpeta_para_modificar:
                nombre_enlace = input(
                    "Ingrese el nombre del enlace a modificar: ")
                atributo = input(
                    "Ingrese el atributo a modificar (nombre, url): ")
                nuevo_valor = input(
                    f"Ingrese el nuevo valor para '{atributo}': ")
                carpeta_para_modificar.modificar_enlace(
                    nombre_enlace, atributo, nuevo_valor)
                guardar_json(ruta_json, estructura)
        elif opcion == 11:
            if estructura:
                guardar_json(ruta_json, estructura)
            break
        else:
            print("Opción inválida.")

    return estructura



def main_proxy():
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    usuario_real = Proxy(estructura, usuario, contraseña)

    if usuario_real.obtener_usuario() == "admin" and usuario_real.obtener_contraseña() == "admin":
        print("Acceso autorizado como admin.")
        main(estructura)
    else:
        print("Acceso autorizado, con permisos limitados.")
        main_base()


if __name__ == "__main__":
    main_proxy()