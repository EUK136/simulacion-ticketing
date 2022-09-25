import json
import os
from getpass import getpass

print("Bienvenido al sistema Ticketing")

#Función menú login
def menuLogin():
    print("Menú de inicio")
    print("1. Login")
    print("2. Registro de usuario")
    print("3. Salir")
    opcion = input("Seleccionar opción: ")

    opcionesValidas = ("1", "2", "3")
    if opcion in opcionesValidas:
        return opcion
    else:
        print("-> Opción no valida")


#Función para mostrar el menú de usuario
def menu():
    print("Menú de usuario")
    print("1. Añadir recinto")
    print("2. Añadir asistente")
    print("3. Mostrar lista de recintos")
    print("4. Mostrar lista de asistentes")
    print("5. Eliminar recinto")
    print("6. Eliminar asistente")
    print("7. Estadistica de recinto")
    print("8. Cerrar sesión")
    opcion = input("Seleccionar opción: ")

    opcionesValidas = ("1", "2", "3", "4", "5", "6", "7", "8")
    if opcion in opcionesValidas:
        return opcion
    else:
        print("-> Opción no valida")

#Función login
def login():
    try:
        with open("login.json", "r") as f:
            js = json.load(f)

            nombreUsuario = input("Introduce nombre de usuario: ")
            contraseñaUsuario = getpass("Introduce contraseña")

            if nombreUsuario in js:
                if js[nombreUsuario] == contraseñaUsuario:
                    print("Login correcto")
                    return 1
            else:
                print("Usuario o contraseña no validos")

    except:
        print("Error al hacer login")

#Función registro
def registro():
    if os.path.exists("login.json") == True:
        with open("login.json", "r") as f:
            js = json.load(f)
            nombreUsuario = input("Introduce nombre de usuario: ")

            if nombreUsuario in js:
                print("No se puede registrar ese usuario")
            else:
                contraseñaUsuario = getpass("Introduce contraseña")
                data = {nombreUsuario: contraseñaUsuario}
                with open("login.json", "w") as f:
                    js.update(data)
                    json.dump(js, f)
                    print("-> Usuario creado correctamente")
    else:
        nombreUsuario = input("Indica nombre de usuario: ")
        contraseñaUsuario = getpass("Introduce contraseña: ")
        data = {nombreUsuario: contraseñaUsuario}

        with open("login.json", "w") as f:
            json.dump(data, f)
            print("-> Usuario creado correctamente")


#Función añadir recinto
def anadirRecinto():
    if os.path.exists("recintos.json") == True:
        try:
            with open("recintos.json", "r") as f:
                js = json.load(f)
                nombreRecinto = input("Indica el nombre del recinto: ").lower()

                if nombreRecinto in js:
                    print("-> Recinto ya en la aplicación")
                else:
                    aforoRecinto = input("Indica el aforo maximo: ")
                    aforoRecinto = int(aforoRecinto)
                    data = {nombreRecinto: {"aforo": aforoRecinto, "asistentes":[]}}

                    with open("recintos.json", "w") as f:
                        js.update(data)
                        json.dump(js, f)
                        print("-> Añadido correctamente")
        except:
            print("-> Aforo invalido, introduce solo numeros")
    else:
        nombreRecinto = input("Indica el nombre del recinto: ").lower()
        aforoRecinto = input("Indica el aforo maximo: ")
        aforoRecinto = int(aforoRecinto)
        data = {nombreRecinto: {"aforo": aforoRecinto, "asistentes":[]}}

        with open("recintos.json", "w") as f:
            json.dump(data, f)
            print("-> Añadido correctamente")


#Función añadir asistente
def anadirAsistente():
    try:
        with open("recintos.json", "r") as f:
            js = json.load(f)
            nombreRecinto = input("Indicar nombre del recinto: ")

            if nombreRecinto in js:
                ocupacion = len(js[nombreRecinto]["asistentes"])
                aforoMaximo = js[nombreRecinto]["aforo"]

                if ocupacion < aforoMaximo:
                    nombreAsistente = input("Nombre asistente: ").lower()
                    listaAsistentes = js[nombreRecinto]["asistentes"]
                    listaAsistentes.append(nombreAsistente)
                    data = {nombreRecinto: {"aforo": js[nombreRecinto]["aforo"], "asistentes": listaAsistentes}}

                    with open("recintos.json", "w") as f:
                        js.update(data)
                        json.dump(js, f)
                        print("-> Asistente añadido correctamente")
                else:
                    print("-> Aforo al maximo, no se puede añadir mas asistentes")
            else:
                print("-> Recinto no encontrado")

    except:
        print("Error al ejecutar el comando")

#Función mostrar lista recintos
def listaRecintos():
    try:
        with open("recintos.json", "r") as f:
            js = json.load(f)

            print("-> Listado recintos: ")
            for x in js:
                print(x)
    except:
        print("Error al ejecutar el comando")

#Función mostrar asistentes
def listaAsistentes():
    try:
        with open("recintos.json", "r") as f:
            js = json.load(f)

            for key, value in js.items():
                asistentes = value["asistentes"]
                print(f"{key} -> {asistentes}")
    except:
        print("Error al ejecutar el comando")

#Función eliminar recinto:
def eliminarRecinto():
    try:
        with open("recintos.json", "r") as f:
            js = json.load(f)
            nombreRecinto = input("Indica el nombre del recinto: ")

            if nombreRecinto in js:
                opcion = input(f"¿Esta seguro de eliminar el recinto {nombreRecinto}? Esto eliminara la lista de asistentes, si - no: ")

                if opcion == "si":
                    js.pop(nombreRecinto, "No se encuentra")
                    with open("recintos.json", "w") as f:
                        js.update(js)
                        json.dump(js, f)
                        print("-> Recinto eliminado correctamente")
                elif opcion == "no":
                    return
                else:
                    print("-> Opcion no valida")
    except:
        print("Error al ejecutar el comando")

#Función eliminar asistente
def eliminarAsistente():
    try:
        with open("recintos.json", "r") as f:
            js = json.load(f)
            nombreRecinto = input("Indica el nombre del recinto: ")

            if nombreRecinto in js:
                nombreAsistente = input("Indica el nombre del asistente: ")
                listaAsistentes = js[nombreRecinto]["asistentes"]

                if nombreAsistente in listaAsistentes:
                    listaAsistentes.remove(nombreAsistente)
                    data = {nombreRecinto: {"aforo": js[nombreRecinto]["aforo"], "asistentes": listaAsistentes}}

                    with open("recintos.json", "w") as f:
                        js.update(data)
                        json.dump(js, f)
                        print("-> Asistente eliminado correctamente")
                else:
                    print("-> No se encuentra al asistente")
            else:
                print("-> Recinto no encontrado")
    except:
        print("Error al ejecutar el comando")

#Función estadisticas recinto
def estadisticas():
    nombreRecinto = input("Indica el nombre del recinto: ")
    
    try:
        with open("recintos.json", "r") as f:
            js = json.load(f)
        
        if nombreRecinto in js:
            ocupacion = len(js[nombreRecinto]["asistentes"])
            aforoMaximo = js[nombreRecinto]["aforo"]
            porcentaje = (ocupacion/js[nombreRecinto]["aforo"])*100
            restantes = aforoMaximo - ocupacion
            print(f"El aforo máximo del {nombreRecinto} es {aforoMaximo}, los asistentes actuales son {ocupacion} lo que es el " + "{:.2f}".format(porcentaje) + f"% del aforo total, quedan {restantes} plazas libres")
        else:
            print("No se encuentra el recinto")
    except:
        print("Error al ejecutar el comando")



#Ciclo de la aplicación
while True:
    opcionUsuario = menuLogin()

    if opcionUsuario == "3":
        print("Cerrando....")
        break
    elif opcionUsuario == "1":
        loginOpcion = login()

        if loginOpcion == 1:
            while True:
                opcionUsuario = menu()

                if opcionUsuario == "8":
                    print("Saliendo....")
                    break
                elif opcionUsuario == "1":
                    anadirRecinto()
                elif opcionUsuario == "2":
                    anadirAsistente()
                elif opcionUsuario == "3":
                    listaRecintos()
                elif opcionUsuario == "4":
                    listaAsistentes()
                elif opcionUsuario == "5":
                    eliminarRecinto()
                elif opcionUsuario == "6":
                    eliminarAsistente()
                elif opcionUsuario == "7":
                    estadisticas()
                else:
                    print("Error en menú")
    elif opcionUsuario == "2":
        registro()
    else:
        print("Error en menú")