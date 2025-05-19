saldo = 10000
pin_correcto = "1234"

def iniciar_sesion():
    intentos = 3
    while intentos <= 3:
        pin = input("Ingrese su PIN: ")
        if pin == pin_correcto:
            print("Acceso concedido.")
            return True
        else:
            intentos -= 1
            print(f"PIN incorrecto. Te quedan {intentos} intento(s).")
    print("Demasiados intentos fallidos. Tarjeta bloqueada.")
    return False

def ver_saldo():
    print(f"Tu saldo actual es: ${saldo}")

def depositar():
    global saldo
    monto = float(input("Ingrese el monto a depositar: "))
    if monto > 0:
        saldo += monto
        print(f"Depósito exitoso. Nuevo saldo: ${saldo}")
    else:
        print("El monto debe ser mayor que cero.")

def retirar():
    global saldo
    monto = float(input("Ingrese el monto a retirar: "))
    if monto <= saldo and monto > 0:
        saldo -= monto
        print(f"Retiro exitoso. Nuevo saldo: ${saldo}")
    else:
        print("Fondos insuficientes o monto inválido.")

def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Ver saldo")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            ver_saldo()
        elif opcion == "2":
            depositar()
        elif opcion == "3":
            retirar()
        elif opcion == "4":
            print("Gracias por usar el cajero.")
            activo = False
        else:
            print("Opción inválida.")

# Programa principal
if iniciar_sesion():
    menu()

			
			
