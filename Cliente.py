from Persona import Persona
class Cliente(Persona):
	clientes_totales = []
	documentos_clientes = []

	def __init__(self,nombre,documento,fechaNac,contrasena,lapida):
		super().__init__(nombre,documento,fechaNac)
		self._contrasena =  contrasena
		self.lapida = lapida
		Cliente.documentos_clientes.append(documento)
		Cliente.clientes_totales.append(self)

	def comprobarDocumentoCliente(documento):
		for d in Cliente.documentos_clientes:
			if d == documento:
				return True
				break

	def buscarCliente(documento):
		for c in Cliente.clientes_totales:
			if c._documento == documento:
				return c

	def getContrasenaCliente(self):
		return self._contrasena

	def imprimirDatosCliente(self):
		print("TIPO DE PERFIL: CLIENTE")
		print("Nombre: " + self._nombre)
		print("Documento: " + self._documento)
		print("Fecha de Nacimiento: " + self._fechaNac)

	def imprimirDatosLapida(self):
		print("DATOS LAPIDA: ")
		l = self.lapida
		if l.getPrivacidad():
			print("Su lapida es privada")
		else:
			print("Su lapida es publica")
		u = l.getUbicacion()
		print("Su lapida se encuentra en la posición " +  u.getIndice())
		if l.getEpitafio() == "":
			print("No tiene ningún epitafio")
		else:
			print("Epitafio: " + l.getEpitafio)
		if l.getFechaDef() =="":
			print("No tiene fecha de defunción")
		else:
			print("Fecha de defunción = " + l.getFechaDef())