class Persona:
	personas_totales = []

	def __init__(self,nombre,documento,fechaNac):
		self._nombre = nombre
		self._documento = documento
		self._fechaNac = fechaNac
		Persona.personas_totales.append(self)

if __name__ == '__main__':
	from Moderador import Moderador
	from Cliente import Cliente
	from Persona import Persona
	from Lapida import Lapida
	from Ubicacion import Ubicacion

	p1 = Persona("David","1090514247","23/02/1999")
	u1 = Ubicacion("1")
	l1 = Lapida(p1,False,u1)

	Moderador("Marcos","1090514246","23/02/1998","123")
	Cliente("David","1090514247","23/02/1999","456",l1)


	a = input("¿Ya se encuentra registrado en la base de datos de el cementerio ? 1.Si 2.No ")
	if a == "1":
		d = input("Ingrese su numero de documento por favor ")
		while True:
			b = input("¿Se encuentra registrado como moderador o como cliente ? 1.Cliente 2.Moderador ")
			if b=="2":
				m = Moderador.buscarModerador(d)
				x = input("Ingrese su contraseña por favor ")
				if x == m.getContrasenaModerador():
					m.imprimirDatosModerador()
				break
			elif b=="1":
				c = Cliente.buscarCliente(d)
				x = input("Ingrese su contraseña por favor ")
				if x == c.getContrasenaCliente():
					c.imprimirDatosCliente()
					c.imprimirDatosLapida()
				break
			else:
				print("Ingrese una opción valida")