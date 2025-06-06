import random

# FUNCIONES
def ingreso(sumar, total):
    return total + sumar

def egreso(restar, total):
    return total - restar

# Listas y contadores
Lista_usuarios = []
Lista_claves = []
Lista_egresos = []
Lista_ingresos = []
Lista_nro_de_movimiento_Ingresos = []
Lista_nro_de_movimiento_Egresos = []
contador = 0
# LOGIN
correcto = False

while not correcto:
    print("=================================")
    Usuario = input("Ingrese su usuario: ")
    Lista_usuarios.append(Usuario)
    clave = random.randint(1000, 9999)
    print("Tu clave es:", clave)
    print("=================================")
    verificacion = int(input("Ingrese la clave generada: "))

    if verificacion == clave:
        print("Clave correcta")
        Lista_claves.append(clave)
        print("=================================")
        print("BIENVENIDO", "...", Usuario, "...")
        print("=================================")
        correcto = True
    else:
        print("Clave incorrecta. Se generará una nueva clave...\n - Reiniciando.....")
        Lista_claves.append(0000)

# Saldo inicial aleatorio
saldo = random.randint(0, 50000)

# MENÚ PRINCIPAL
peticion = 0

while peticion != 5:
    print("Cajero automático\n")
    print("\tMenú\n")
    print("1- Agregar dinero")
    print("2- Retirar dinero")
    print("3- Mostrar dinero disponible")
    print("4- Historial de Ingresos/Egresos")
    print("5- Salir")
    
    print("-1- Visualizar historial de registros ***REQUIERE PERMISOS DE ADMINISTRADOR***")

    peticion = int(input(">>> "))
    print()

    if peticion == 1:
        print("=================================")
        print("Dinero que vas a ingresar")
        sumar = float(input(">>> "))
        saldo = ingreso(sumar, saldo)
        contador += 1
        Lista_nro_de_movimiento_Ingresos.append(contador)
        Lista_ingresos.append(sumar)
        
        print("Saldo actual:", saldo)
        print("Proceso exitoso")
        print("=================================")

    elif peticion == 2:
        print("=================================")
        restar = float(input("Dinero que vas a retirar\n>>> "))
        print()
        if restar > saldo:
            print("Insuficiente dinero")
        else:
            saldo = egreso(restar, saldo)
            contador += 1
            Lista_nro_de_movimiento_Egresos.append(contador)
            Lista_egresos.append(restar)
            print("Dinero retirado")
            print("Saldo actual:", saldo)
            print("Proceso exitoso")
        print("=================================")

    elif peticion == 3:
        print("=================================")
        print("El dinero disponible es:", saldo)
        print("=================================")
    
    elif peticion == 4:
        print("=================================")
        print("Ingresando al Historial")
        print("=================================")
        print("Movimiento de Ingresos//> ",Lista_ingresos)
        print("   ID CORRESPONDIENTE///>",Lista_nro_de_movimiento_Ingresos) 
        print("Movimiento de Egresos///>",Lista_egresos)
        print("   ID CORRESPONDIENTE///>",Lista_nro_de_movimiento_Egresos)
        print("=================================")
        

    elif peticion == 5:
        print("=================================")
        print("Okey, saliendo...")
        print("=================================")

    elif peticion == -1:
        print("=================================")
        print("Usuarios registrados:", Lista_usuarios)
        print("Claves registradas:", Lista_claves)
        print("=================================")

       


