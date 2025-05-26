def login(pin_correcto):
    intentos = 3
    pin_ingresado = int(input("Ingresá tu PIN: "))
    while pin_ingresado != pin_correcto and intentos > 1:
        intentos -= 1
        print("PIN incorrecto. Intentos restantes:", intentos)
        pin_ingresado = int(input("Ingresá tu PIN: "))
    if pin_ingresado == pin_correcto:
        return True
    else:
        print("Cuenta bloqueada.")
        return False

def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Cambiar PIN")
    print("5. Salir")
    opcion = int(input("Elegí una opción: "))
    return opcion

def consultar_saldo(saldo):
    print("Tu saldo actual es:", saldo)
    return saldo

def depositar(saldo):
    monto = int(input("¿Cuánto querés depositar?: "))
    if monto > 0:
        saldo += monto
        print("Depósito exitoso. Nuevo saldo:", saldo)
    else:
        print("Monto inválido.")
    return saldo

def retirar(saldo):
    monto = int(input("¿Cuánto querés retirar?: "))
    if monto > 0 and monto <= saldo:
        saldo -= monto
        print("Retiro exitoso. Nuevo saldo:", saldo)
    else:
        print("Fondos insuficientes o monto inválido.")
    return saldo

def cambiar_pin(pin_actual):
    viejo = int(input("Ingresá el PIN actual: "))
    if viejo == pin_actual:
        nuevo = int(input("Nuevo PIN: "))
        confirmado = int(input("Confirmá el nuevo PIN: "))
        if nuevo == confirmado:
            print("PIN cambiado con éxito.")
            return nuevo
        else:
            print("Los PINs no coinciden.")
            return pin_actual
    else:
        print("PIN incorrecto.")
        return pin_actual

# Programa principal
def cajero():
    pin = 1234
    saldo = 10000
    sesion_activa = login(pin)
    
    while sesion_activa:
        opcion = mostrar_menu()
        if opcion == 1:
            saldo = consultar_saldo(saldo)
        elif opcion == 2:
            saldo = depositar(saldo)
        elif opcion == 3:
            saldo = retirar(saldo)
        elif opcion == 4:
            pin = cambiar_pin(pin)
        elif opcion == 5:
            print("Gracias por usar el cajero.")
            sesion_activa = False
        else:
            print("Opción inválida.")

cajero()

			
			
