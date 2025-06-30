Algoritmo CajeroAutomatico
	// Declaración de listas y variables
	Definir Lista_DNI, Lista_nombre, Lista_saldo, Lista_PIN, Lista_extracciones Como Real
	Definir contador, ejecucion, sesionActiva, correcto, indice, peticion, DNI, PIN, opcion, monto, respuesta Como Entero
	Definir nombre Como Cadena
	// Inicialización de listas con dos usuarios de ejemplo
	Dimensionar Lista_DNI(100)
	Dimensionar Lista_nombre(100)
	Dimensionar Lista_saldo(100)
	Dimensionar Lista_PIN(100)
	Dimensionar Lista_extracciones(100)
	Lista_DNI[1] <- 43459748
	Lista_DNI[2] <- 46208734
	Lista_nombre[1] <- 'Tobias'
	Lista_nombre[2] <- 'Lucia'
	Lista_saldo[1] <- 20000
	Lista_saldo[2] <- 3000
	Lista_PIN[1] <- 1234
	Lista_PIN[2] <- 5678
	Lista_extracciones[1] <- 0
	Lista_extracciones[2] <- 0
	contador <- 2
	ejecucion <- 1
	Mientras ejecucion=1 Hacer
		// BLOQUE DE LOGIN
		correcto <- 0
		Mientras correcto=0 Hacer
			Escribir '================================='
			Escribir 'Ingrese su número de documento: '
			Leer DNI
			// Buscar DNI
			indice <- 0
			Para i<-1 Hasta contador Hacer
				Si Lista_DNI[i]=DNI Entonces
					indice <- i
				FinSi
			FinPara
			Si indice=0 Entonces
				Escribir 'Su número de documento no está registrado. ¿Desea registrarse? (1=si 2=no)'
				Leer respuesta
				Si respuesta=1 Entonces
					contador <- contador+1
					Lista_DNI[contador] <- DNI
					Escribir 'Ingrese su nombre: '
					Leer nombre
					Lista_nombre[contador] <- nombre
					Escribir 'Genere su PIN: '
					Leer PIN
					Lista_PIN[contador] <- PIN
					Lista_saldo[contador] <- 0
					Lista_extracciones[contador] <- 0
					indice <- contador
				SiNo
					Escribir 'Debe ingresar un usuario válido.'
				FinSi
			FinSi
			Si indice<>0 Entonces
				Escribir 'Bienvenido/a ', Lista_nombre[indice]
				Escribir 'Ingrese su PIN: '
				Leer PIN
				Si PIN=Lista_PIN[indice] Entonces
					Escribir 'Clave correcta'
					correcto <- 1
				SiNo
					Escribir 'Clave incorrecta. - Reiniciando...'
				FinSi
			FinSi
		FinMientras
		// MENÚ PRINCIPAL DEL CAJERO
		sesionActiva <- 1
		Mientras sesionActiva=1 Hacer
			Escribir 'Cajero automático'
			Escribir '1- Agregar dinero'
			Escribir '2- Retirar dinero'
			Escribir '3- Mostrar dinero disponible'
			Escribir '4- Cerrar sesión'
			Escribir '5- Salir'
			Leer opcion
			Según opcion Hacer
				1:
					Escribir 'Ingrese el monto a agregar:'
					Leer monto
					Si monto>0 Entonces
						Lista_saldo[indice] <- Lista_saldo[indice]+monto
						Escribir 'Saldo actual: ', Lista_saldo[indice]
					SiNo
						Escribir 'Monto inválido.'
					FinSi
				2:
					Si Lista_extracciones[indice]>=3 Entonces
						Escribir 'Límite de extracciones alcanzado.'
					SiNo
						Escribir 'Ingrese el monto a retirar:'
						Leer monto
						Si monto>0 Y monto<=Lista_saldo[indice] Entonces
							Lista_saldo[indice] <- Lista_saldo[indice]-monto
							Lista_extracciones[indice] <- Lista_extracciones[indice]+1
							Escribir 'Dinero retirado. Saldo actual: ', Lista_saldo[indice]
						SiNo
							Escribir 'Monto inválido o saldo insuficiente.'
						FinSi
					FinSi
				3:
					Escribir 'El dinero disponible es: ', Lista_saldo[indice]
				4:
					Escribir 'Cerrando sesión...'
					sesionActiva <- 0
				5:
					Escribir 'Saliendo...'
					sesionActiva <- 0
					ejecucion <- 0
				De Otro Modo:
					Escribir 'Opción inválida.'
			FinSegún
		FinMientras
	FinMientras
FinAlgoritmo
