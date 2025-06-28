import random

# Mejorar el lexico
# 

# FUNCIONES

def ingreso(sumar, total):
# sumar plata al saldo
    return total + sumar

def ingresarDinero():
    print("=================================")
    print("Dinero que vas a ingresar")
    sumar = int(input(">>> "))
    saldo = ingreso(sumar, Lista_saldo[indice])
    Lista_saldo[indice]=saldo
    print("Saldo actual:", Lista_saldo[indice])
    print("Proceso exitoso")
    print("=================================")

def extraccion():
    print("=================================")
    restar = int(input("Dinero que vas a retirar\n>>> "))
    print()
    if restar > saldo:
        print("Saldo insuficiente")
    else:
        saldo = egreso(restar, saldo)
        Lista_nro_de_movimiento_Egresos.append(contador)
        Lista_egresos.append(restar)
        print("Dinero retirado")
        print("Saldo actual:", saldo)
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
    print("Okey, saliendo...")
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
    nuevoNombre=input("igrese su nombre: ")
    nuevoPIN=int(input("igrese su Pin: "))
    Lista_PIN.append(nuevoPIN)
    Lista_nombre.append(nuevoNombre)
    Lista_saldo.append(0)
    indice = len(Lista_DNI)-1
    ordenamientoPorDNI()

# Listas y contadores
Lista_DNI = [43459748,46208734]
Lista_nombre=["Tobias","lucia"]
Lista_saldo=[20000, 3000]
Lista_PIN = [1234,5678]
Lista_egresos = []
Lista_ingresos = []
Lista_nro_de_movimiento_Ingresos = []
Lista_nro_de_movimiento_Egresos = []
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
        posicionBusqueda=busquedaEnLista(Lista_DNI,DNI)
        indice=posicionBusqueda
        if posicionBusqueda==-1:
            guardardni=int(input("Su numero de documento no se encuentra registrado ¿Quiere registrarse?(1=si 2=no)"))
            if guardardni==1:
                agregarsuario(DNI,indice)
        else:
            print("bienvenido",Lista_nombre[indice] )
            print("=================================")
            verificacion = int(input("Ingrese su pin: "))
            if verificacion == Lista_PIN[indice]:
                print("Clave correcta")
                print("=================================")
                print("BIENVENIDO", "...", Lista_nombre[indice], "...")
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
            print("Usuarios registrados:", Lista_DNI)
            print("Claves registradas:", Lista_PIN)
            print("=================================")

        else:
            print("Debe ingresar una funcion valida")


