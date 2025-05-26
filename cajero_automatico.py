# import time as nya
# import os


saldo = 100
#funcion ingresar usuario con el pin

#funcion de ingresar un usario
def ingresarDinero():
	return
#funcion de ingresar plata
#funcion de retirar plata
#funcion de recuperar pin 

peticion=0

while peticion !=4:
	
	print()
	print()
	print("Cajero automatico\n\n")

	print("\t Menu\n")
	print("1- Agregar dinero")
	print("2- Retirar dinero")
	print("3- Mostrar dinero disponible")
	print("4- Salir\n")

	peticion = int(input(">>> "))
	print()
	print()


	if peticion==1:
		
		print("""=================================""")
		print("Dinero que vas a ingresar")
		sumar = float(input(">>> "))
	
		saldo = sumar + saldo
	
		print(saldo)
		
		print("""=================================""")
		
	elif peticion==2:
			
			print("""=================================""")
			restar = float(input("Dinero que vas a retirar\n>>> "))
			
			print()
			if restar>saldo:
				print("Insuficiente dinero")
				
			else:
				saldo = restar - saldo
				
				print("Dinero retirado")
			print("""=================================""")
			
			
	elif peticion==3:
				print("""=================================""")
				print("El dinero disponible es:", saldo)
				print("""=================================""")
				
	elif peticion==4:
			print("""=================================""")
			print("Okey, saliendo...")
			print("""=================================""")
	else:
		print("ingrese una accion valida")
			
			
			