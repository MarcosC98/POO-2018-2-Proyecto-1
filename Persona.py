class Persona:
	personas_totales = []

	def __init__(self,nombre,documento,fechaNac):
		self._nombre = nombre
		self._documento = documento
		self._fechaNac = fechaNac
		Persona.personas_totales.append(self)

	def imprimirDatosPersona(self):
		print(""+"\n"+"TIPO DE PERFIL: VISITANTE"+"\n"+"")
		print("Nombre: " + self._nombre)
		print("Documento: " + self._documento)
		print("Fecha de Nacimiento: " + self._fechaNac)

	def getNombre(self):
		return self._nombre

	def getDocumento(self):
		return self._documento

	def getFechaNac(self):
		return self._fechaNac

if __name__ == '__main__':
	from Moderador import Moderador
	from Cliente import Cliente
	from Persona import Persona
	from Lapida import Lapida
	from Ubicacion import Ubicacion
	from Memoria import Memoria
	from Textos import Texto

	p1 = Persona("David","1090514247","23/02/1999")
	u1 = Ubicacion("1")
	l1 = Lapida(p1,False,u1)

	Moderador("Marcos","1090514246","23/02/1998","123")
	Cliente("David","1090514247","23/02/1999","456",l1)
	Moderador("David","1090514247","23/02/1999","789")

	Texto.presentacion()

	while True:
		_idiom = input("Su Selección / Your Selection: ")
		if _idiom =="1":
			t = Texto(_idiom)
			break
		elif _idiom =="2":
			t = Texto(_idiom)
			break
		else:
			print(""+"\n"+"El dato ingresado es inválido. / The entered data is invalid."+"\n"+"")
	

	while True:
		d = input(t.introDoc)
		m = Moderador.buscarModerador(d)
		c = Cliente.buscarCliente(d)
		if m is None and c is None:
			print(t.noRegistra)

			while True:
				print (t.seleccionUno)
				e = input()
				if e == "1":
					print(t.entradaNombre)
					nombre = input()
					print(t.entradaFechaNac) 
					fechaNac = input()
					v = Persona(nombre,d,fechaNac)
					v.imprimirDatosPersona()
					while True:
						print(t.selecOpcion) 
						ac = input()
						if ac == "1":
							if Cliente.comprobarDocumentoCliente(d) is None:
								print("///////////////////////////////////////////CREACION DE LAPIDA///////////////////////////////////////////") #Dejo este print porque me parece que hace el texto más legible.
								print(t.ingresoEpitafio)
								ep = input()
								print(t.ingresoContrasena)
								contra = input()
								while True:
									print(t.ingresoUbicacion)
									u = input()
									if Ubicacion.revisarDisponibilidadUbicacion(u):
										ub = Ubicacion(u)
										while True:
											print(t.selecPrivacidad)
											p = input()
											if p == "0":
												la = Lapida(v,True,ub,ep)
												cl = Cliente(nombre,d,fechaNac,contra,la)
												Lapida.leerLapida(la)
												break
											if p == "1":
												la = Lapida(v,False,ub,ep)
												cl = Cliente(nombre,d,fechaNac,contra,la)
												Lapida.leerLapida(la)
												break
											print(t.datoInvalido)
										break
									else:
										print(t.lapidaOcupada)
							else:
								print(t.lapidaAntesCreada)
						if ac == "2":
							print(""+"\n"+"///////////////////////////////////////////CREACION DE MEMORIA///////////////////////////////////////////"+"\n"+"") #Nuevamente los dejo porque me parece que son puntos de referencia en el código.
							while True:
								print(t.propietarioLap)
								l = Lapida.buscarLapida(input())
								if l is not None:
									if l.getPrivacidad():
										print(t.lapidaPrivada)
										break
									else:
										print(t.ingMemoria)
										de = input()
										me = Memoria(v,de,l)
										l.memorias.append(me)
										me.imprimirDatosMemoria()
										break
								else:
									print(t.lapidaInvalida)

						if ac == "3":
							while True:
								print(t.ingresoPropietario)
								l = Lapida.buscarLapida(input())
								if l is not None:
									l.leerLapida()
									break
								else:
									print(t.noLapida)
						if ac == "4":
							e = "0"
							break

						if ac == "5":
							print("aca va el sys exit")
							break

				if e == "0":
					break

				else:
					print("Ingrese un numero valido por favor")

		else:
			if m is not None and c is not None:
				while True:
					print("Desea ingresar a su perfil de moderador o cliente ? 1.Moderador 2.Cliente ")
					e = input()
					if e == "1":
						while True:
							print("Ingrese la contraseña de este perfil ")
							c = input()
							if c == m.getContrasenaModerador():
								m.imprimirDatosModerador()
								while True:
									print("Ingrese el número de la acción a realizar: 1.Registrar nuevo moderador 2.Borrar memoria 3.Registrar defunción de un cliente 4.Cambiar contraseña 5.Ver numero total de clientes 6.Ver numero total de moderadores 7.Ver numero total de visitantes 8.Ingresar con otro perfil 9.Salir  " )
									ac = input()
									if ac == "1":
										while True:
											print("Ingrese el documento de el nuevo moderador ")
											documento = input()
											if Moderador.comprobarDocumentoModerador(documento) is None:
												print("Ingrese el nombre completo de el nuevo moderador ")
												nombre = input()			
												print("Ingrese la fecha de nacimiento de el nuevo moderador en el formato dd/mm/aaaa ")					
												fechaNac = input()
												print("Ingrese la contraseña de la cuenta de el nuevo moderador ")
												contrasena = input()
												mod = Moderador(nombre,documento,fechaNac,contrasena)
												print("NUEVO MODERADOR CREADO:  ----------------------------------")
												Moderador.imprimirDatosModerador(mod)
												break
											else:
												print("Ya existe un moderador registrado con este documento")
							else:
								print("La contraseña es incorrecta")





"""
		else: 
			if m is not None and c is not None:
				perfil = input("¿Desea ingresar como moderador o como cliente? 1.Moderador 2.Cliente ")
				contra = input("Ingrese contraseña para este perfil: ")
				if perfil == "1":
					if contra == m.getContrasenaModerador():
						m.imprimirDatosModerador()
						break
				if perfil == "2":
					if contra == c.getContrasenaCliente():
						c.imprimirDatosCliente()
						break
			elif m is not None:
				contra = input("Ingrese contraseña para este perfi: ")
				if contra == m.getContrasenaModerador():
					m.imprimirDatosModerador()
					break
			else:
				contra = input("Ingrese contraseña para este perfil: ")
				if contra == c.getContrasenaCliente():
					c.imprimirDatosCliente()
					break
"""