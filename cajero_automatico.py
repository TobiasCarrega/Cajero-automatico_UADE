
import random

# 

# FUNCIONES

def ingreso(sumar, total):
# sumar plata al saldo
    return total + sumar

def ingresarDinero():
    print("=================================")
    print("Dinero que va a ingresar: ")
    sumar = int(input(">>> "))
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
        restar = int(input("Dinero que va a retirar\n>>> "))
        print()
        if restar > Lista_saldo[indice]:
            print("Saldo insuficiente")
        else:
            Lista_saldo[indice] = egreso(restar, Lista_saldo)
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

def cerrarSesion():
    print("=================================")
    print("Cerrando sesión... .")  
    print("=================================")
    sesionActiva=False

def terminar():
    print("=================================")
    print("Saliendo...")
    print("=================================")
    ejecucion=False

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
    nuevoPIN=int(input("Ingrese su Pin: "))
    Lista_PIN.append(nuevoPIN)
    Lista_nombre.append(nuevoNombre)
    Lista_saldo.append(0)
    Lista_extracciones.append(0)
    indice = len(Lista_DNI)-1
    ordenamientoPorDNI()

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
        DNI = 0
        while DNI == 0:
            DNI = int(input("Ingrese su número de documento: "))
        while DNI != int(DNI):
            print("Debe ingresar solo números. Intente nuevamente.")
        ordenamientoPorDNI() #Se asegura estar ordenada
        posicionBusqueda = busquedaEnLista(Lista_DNI, DNI)
        indice = posicionBusqueda
        if posicionBusqueda==-1:
            guardardni=int(input("Su numero de documento no se encuentra registrado ¿Quiere registrarse?(1 = si 2 = no)"))
            if guardardni==1:
                agregarsuario(DNI,indice)
        else:
            print("Bienvenido/a",Lista_nombre[indice] )
            print("=================================")
            verificacion = int(input("Ingrese su pin: "))
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
        
        peticion = int(input(">>> "))
        print()

        if peticion == 1:
            ingresarDinero()

        elif peticion == 2:
            extraccion()

        elif peticion == 3:
            mostrarSaldo()
        
        elif peticion == 4:
            cerrarSesion()

        elif peticion == 5:
            terminar()

        elif peticion == -1:
            print("=================================")
            print("Usuarios registrados: ", Lista_DNI)
            print("Claves registradas: ", Lista_PIN)
            print("=================================")

        else:
            print("Debe ingresar una función válida")
			
			
