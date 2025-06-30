import random

# 

# FUNCIONES

def ingreso(sumar, total):
# sumar plata al saldo
    return total + sumar

def ingresarDinero():
    sumar = ""
    while sumar == "":
        print("=================================")
        print("Dinero que va a ingresar: ")
        sumar = (input(">>> "))            
        sumar=validacion(sumar)

    while sumar <= 0:
        print("Error, ingrese un saldo válido")
        sumar = int(input(">>> "))
    saldo = ingreso(sumar, Lista_saldo[indice])
    Lista_saldo[indice]=saldo
    print("Saldo actual:", Lista_saldo[indice])
    print("Proceso exitoso")
    print("=================================")

def extraccion():
    print("=================================")
    print(f"Extracciones realizadas: {Lista_extracciones[indice]}")
    if Lista_extracciones[indice] >= 3:
        print("Límite de 3 extracciones alcanzado.")
    else:
        restar = ""
        while restar == "":
            print("=================================")
            print("Dinero que va a extraer: ")
            restar = (input(">>> "))            
            restar=validacion(restar)
        # Se asegura de no extraer negativos
        while restar<0:
            print("Debe ingresar un numero positivo. Intentelo nuevamente.")
            restar = int(input("Dinero que va a retirar\n>>> "))
        if restar > Lista_saldo[indice]:
            # Se asegura de no extraer más de su saldo
            print("Saldo insuficiente")
        else:
            Lista_saldo[indice] = egreso(restar, Lista_saldo[indice])
            Lista_nro_de_movimiento_Egresos.append(contador)
            Lista_egresos.append(restar)
            Lista_extracciones[indice] += 1
            print("Dinero retirado")
            print("Saldo actual:", Lista_saldo[indice])
            print("Extracciones restantes: ", 3 - Lista_extracciones[indice])
            print("Proceso exitoso")
    print("=================================")

def mostrarSaldo():
    print("=================================")
    print("El dinero disponible es:", Lista_saldo[indice])
    print("=================================")

def egreso(restar, total):
# descontar plata del saldo
    return total - restar

def cerrarSesion(sesionActiva):
    print("=================================")
    print("Cerrando sesión... .")  
    print("=================================")
    sesionActiva=False
    return sesionActiva

def terminar(ejecucion):
    print("=================================")
    print("Saliendo...")
    print("=================================")
    ejecucion=False
    return ejecucion

def ordenamientoPorDNI():
    ordenada = True
    while ordenada:
        ordenada = False
        for i in range(len(Lista_DNI) - 1):
            if Lista_DNI[i] > Lista_DNI[i + 1]:
                # Intercambiar DNI
                aux = Lista_DNI[i]
                Lista_DNI[i] = Lista_DNI[i + 1]
                Lista_DNI[i + 1] = aux

                # Intercambiar nombre
                aux = Lista_nombre[i]
                Lista_nombre[i] = Lista_nombre[i + 1]
                Lista_nombre[i + 1] = aux

                # Intercambiar saldo
                aux = Lista_saldo[i]
                Lista_saldo[i] = Lista_saldo[i + 1]
                Lista_saldo[i + 1] = aux

                # Intercambiar PIN
                aux = Lista_PIN[i]
                Lista_PIN[i] = Lista_PIN[i + 1]
                Lista_PIN[i + 1] = aux

                ordenada = True

def busquedaEnLista(lista_DNI,DNI):
# buscar el dni en la lista de los dni
    izq=0
    der=len(Lista_DNI)-1
    pos=-1

    while izq <= der and pos ==-1:
        centro=(izq + der)//2
        if lista_DNI[centro]==DNI:
            pos=centro
        elif lista_DNI[centro]< DNI:    
            izq=centro+1
        else:
            der= centro-1

    return pos

def agregarsuario(DNI,indice):
    Lista_DNI.append(DNI)
    nuevoNombre=input("Ingrese su nombre: ")
    nuevoPIN = ""
    while nuevoPIN == "":
        nuevoPIN = (input("Genere su Pin: "))            
        nuevoPIN=validacion(nuevoPIN)
    Lista_PIN.append(nuevoPIN)
    Lista_nombre.append(nuevoNombre)
    Lista_saldo.append(0)
    Lista_extracciones.append(0)
    indice = len(Lista_DNI)-1
    ordenamientoPorDNI()

def validacion(informacion):
    while informacion == "":
        informacion= input("No puede estar vacío. Intente nuevamente: ")
    else:
        es_numero = True
        i = 0
        while i < len(informacion):
            if informacion[i] < '0' or informacion[i] > '9':
                es_numero = False
            i = i + 1

        if es_numero:
            informacion = int(informacion)
        else:
            print("Debe ingresar solo números positivos. Intente nuevamente: ")
            informacion = ""  # fuerza a repetir
    return informacion

# Listas y contadores
Lista_DNI = [43459748,46208734]
Lista_nombre=["Tobias","Lucia"]
Lista_saldo=[20000, 3000]
Lista_PIN = [1234,5678]
Lista_egresos = []
Lista_ingresos = []
Lista_nro_de_movimiento_Ingresos = []
Lista_nro_de_movimiento_Egresos = []
Lista_extracciones = [0 for i in Lista_DNI]
contador = 0

# sistema de ejecucion
ejecucion=True
while ejecucion:
    # LOGIN
    correcto = False
    while not correcto:
        print("=================================")
        DNI = ""
        while DNI == "":
            DNI = input("Ingrese su número de documento: ")
            DNI=validacion(DNI)

        posicionBusqueda=busquedaEnLista(Lista_DNI,DNI)
        indice=posicionBusqueda
        if posicionBusqueda==-1:
            guardardni = ""
            while guardardni == "":
                guardardni = (input("Su numero de documento no se encuentra registrado ¿Quiere registrarse?(1=si 2=no)"))            
                guardardni=validacion(guardardni)
            if guardardni==1:
                agregarsuario(DNI,indice)
        else:
            print("Bienvenido/a",Lista_nombre[indice] )
            print("=================================")
            # print(Lista_PIN,Lista_nombre)
            verificacion = ""
            while verificacion == "":
                print("=================================")
                print("Ingrese su PIN: ")
                verificacion = (input(">>> "))            
                verificacion=validacion(verificacion)
            if verificacion == Lista_PIN[indice]:
                print("Clave correcta")
                print("=================================")
                print("Bienvenido/a", "...", Lista_nombre[indice], "...")
                print("=================================")
                correcto = True
            else:
                print("Clave incorrecta. - Reiniciando.....")


    # MENÚ PRINCIPAL
    peticion = 0
    sesionActiva= True

    while peticion != 5 and sesionActiva:
        print("Cajero automático\n")
        print("\tMenú\n")
        print("1- Agregar dinero")
        print("2- Retirar dinero")
        print("3- Mostrar dinero disponible")
        print("4- Cerrar sesión")
        print("5- Salir")
        
        peticion = ""
        while peticion == "":
            print("=================================")
            peticion = (input(">>> "))            
            peticion=validacion(peticion)

        if peticion == 1:
            ingresarDinero()

        elif peticion == 2:
            extraccion()

        elif peticion == 3:
            mostrarSaldo()
        
        elif peticion == 4:
            sesionActiva = cerrarSesion(sesionActiva)

        elif peticion == 5:
            ejecucion = terminar(ejecucion)

        elif peticion == -1:
            print("=================================")
            print("Usuarios registrados: ", Lista_DNI)
            print("Claves registradas: ", Lista_PIN)
            print("=================================")

        else:
            print("Debe ingresar una función válida")


