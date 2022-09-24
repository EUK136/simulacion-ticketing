import json

userName = input("Hola ¿Puedes indicarnos tu nombre?: ")

#Función para mostrar el menú de usuario
def menu():
    print(f"Menu de usuario - {userName}")
    print("1. Añadir recinto")
    print("2. Añadir asistente")
    print("3. Mostrar lista de recintos")
    print("4. Mostrar lista de asistentes")
    print("5. Eliminar recinto")
    print("6. Eliminar asistente")
    print("7. Estadistica de recinto")
    print("8. Salir")
    opcion = input("Seleccionar opción: ")

    opcionesValidas = ("1", "2", "3", "4", "5", "6", "7", "8")
    if opcion in opcionesValidas:
        return opcion
    else:
        print("-> Opción no valida")

#Función añadir recinto
def anadirRecinto():
    nombreRecinto = input("Indica el nombre del recinto: ")
    aforoRecinto = input("Indica el aforo maximo: ")

    try:
        aforoRecinto = int(aforoRecinto)
        data = {nombreRecinto: {"aforo": aforoRecinto, "asistentes":[]}}

        with open("recintos.json", "r") as f:
            js = json.load(f)

        with open("recintos.json", "w") as f:
            js.update(data)
            json.dump(js, f)
            print("Añadido correctamente")
    except:
        print("Valor de aforo invalido")

#Función añadir asistente -> TODO acabar la función
def anadirAsistente():
    nombreRecinto = input("Indicar nombre del recinto: ")
    nombreAsistente = input("Nombre asistente: ")
    
    try:
        with open("recintos.json", "r") as f:
            js = json.load(f)
            listaAsistentes = js[nombreRecinto]["asistentes"]
            listaAsistentes.append(nombreAsistente)
            data = {nombreRecinto: {"aforo": js[nombreRecinto]["aforo"], "asistentes": listaAsistentes}}

        with open("recintos.json", "w") as f:
            js.update(data)
            json.dump(js, f)
            print("Asistente añadido correctamente")

    except:
        print("Error al ejecutar el comando")

#Función eliminar asistente
def eliminarAsistente():
    nombreRecinto = input("Indica el nombre del recinto: ")
    nombreAsistente = input("Indica el nombre del asistente: ")

    try:
        with open("recintos.json", "r") as f:
            js = json.load(f)
            listaAsistentes = js[nombreRecinto]["asistentes"]

            if nombreAsistente in listaAsistentes:
                listaAsistentes.remove(nombreAsistente)
                data = {nombreRecinto: {"aforo": js[nombreRecinto]["aforo"], "asistentes": listaAsistentes}}

                with open("recintos.json", "w") as f:
                    js.update(data)
                    json.dump(js, f)
                    print("Asistente elimnado correctamente")
            else:
                print("No se encuentra al asistente")
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
            print(f"El aforo maximo del {nombreRecinto} es {aforoMaximo}, los asistentes actuales son {ocupacion} lo que es el " + "{:.2f}".format(porcentaje) + "% del aforo total")
        else:
            print("No se encuentra el recinto")
    except:
        print("Error al ejecutar el comando")


#Ciclo de la aplicación
while True:
    opcionUsuario = menu()
    
    if opcionUsuario == "8":
        print("Cerrando....")
        break
    elif opcionUsuario == "1":
        anadirRecinto()
    elif opcionUsuario == "2":
        anadirAsistente()
    elif opcionUsuario == "6":
        eliminarAsistente()
    elif opcionUsuario == "7":
        estadisticas()