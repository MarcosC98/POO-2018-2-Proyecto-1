class Persona:
	personas_totales = []

	def __init__(self,nombre,documento,fechaNac):
		self._nombre = nombre
		self._documento = documento
		self._fechaNac = fechaNac
		Persona.personas_totales.append(self)

	def imprimirDatosPersona(self):
		print("TIPO DE PERFIL: VISITANTE")
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

	p1 = Persona("David","1090514247","23/02/1999")
	u1 = Ubicacion("1")
	l1 = Lapida(p1,False,u1)

	Moderador("Marcos","1090514246","23/02/1998","123")
	Cliente("David","1090514247","23/02/1999","456",l1)
	Moderador("David","1090514247","23/02/1999","789")

	while True:
		d = input("Ingrese su numero de documento por favor: ")
		m = Moderador.buscarModerador(d)
		c = Cliente.buscarCliente(d)
		if m is None and c is None:
			print("No hay ninguna cuenta registrada con ese documento.")
			while True:
				e = input("Si desea intentar nuevamente con otro documento ingrese 0, si desea crear una cuenta nueva con este documento ingrese 1 ")
				if e == "1":
					nombre = input("Ingrese su nombre completo: ")
					fechaNac = input("Ingrese su fecha de nacimiento en formato dd/mm/aaaa: ")
					v = Persona(nombre,d,fechaNac)
					v.imprimirDatosPersona()
					while True:
						ac = input("Ingrese el número de la acción a realizar: 1.Adquirir Lápida 2.Escribir Memoria 3.Leer Lápida 4.Ingresar con otro perfil 5.Salir ")
						if ac == "1":
							if Cliente.comprobarDocumentoCliente(d) is None:
								print("CREACION DE LAPIDA///////////////////////////////////////////////////////////////")
								ep = input("Ingrese el epitafio que desea en su lapida ")
								contra = input("Ingrese la contraseña que usará en su cuenta ")
								while True:
									u = input("Ingrese la úbicación de su lápida ")
									if Ubicacion.revisarDisponibilidadUbicacion(u):
										ub = Ubicacion(u)
										while True:
											p = input("Ingrese 0 si desea que su lápida sea privada, 1 si desea que sea pública ")
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
											print("Ingrese un numero valido por favor")
										break
									else:
										print("Esta ubicación ya se encuentra ocupada, selecciona una distinta por favor")
							else:
								print("Ya tienes una lapida creada")
						if ac == "2":
							print("CREACION DE MEMORIA/////////////////////////////////////////////////////////////")
							while True:
								l = Lapida.buscarLapida(input("Ingrese el documento de la persona propietaria de la lapida donde va a dejar la memoria "))
								if l is not None:
									if l.getPrivacidad():
										print("Esta lápida es privada. No puedes leer/escribir memorias.")
										break
									else:
										de = input("Ingrese la descripcion de la memoria por favor ")
										me = Memoria(v,de,l)
										l.memorias.append(me)
										me.imprimirDatosMemoria()
										break
								else:
									print("No hay ninguna persona con ese documento que tenga una lapida")

						if ac == "3":
							while True:
								l = Lapida.buscarLapida(input("Ingrese el documento de la persona propietaria de la lapida que desea leer "))
								if l is not None:
									l.leerLapida()
									break
								else:
									print("No hay ninguna persona con ese documento que tenga una lapida")
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
					e = input("Desea ingresar a su perfil de moderador o cliente ? 1.Moderador 2.Cliente ")
					if e == "1":
						while True:
							c = input("Ingrese la contraseña de este perfil ")
							if c == m.getContrasenaModerador():
								m.imprimirDatosModerador()
								while True:
									ac = input("Ingrese el número de la acción a realizar: 1.Registrar nuevo moderador 2.Borrar memoria 3.Registrar defunción de un cliente 4.Cambiar contraseña 5.Ver numero total de clientes 6.Ver numero total de moderadores 7.Ver numero total de visitantes 8.Ingresar con otro perfil 9.Salir  " )
									if ac == "1":
										while True:
											documento = input("Ingrese el documento de el nuevo moderador ")
											if Moderador.comprobarDocumentoModerador(documento) is None:
												nombre = input("Ingrese el nombre completo de el nuevo moderador ")								
												fechaNac = input("Ingrese la fecha de nacimiento de el nuevo moderador en el formato dd/mm/aaaa ")
												contrasena = input("Ingrese la contraseña de la cuenta de el nuevo moderador ")
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