from Persona import Persona
class Moderador(Persona):
	moderadores_totales = []

	def __init__(self,nombre,documento,fechaNac,contrasena):
		super().__init__(nombre,documento,fechaNac)
		self._contrasena = contrasena
		Moderador.moderadores_totales.append(self)

	def buscarModerador(documento):
		for m in Moderador.moderadores_totales:
			if m._documento == documento:
				return m
				break
		return("No hay ningun moderador registrado con ese documento")		

	def getContrasenaModerador(self):
		return self._contrasena

	def getNombre(self):
		return self._nombre

	def imprimirDatosModerador(self):
		print("TIPO DE PERFIL: MODERADOR")
		print("Nombre: " + self._nombre)
		print("Documento: " + self._documento)
		print("Fecha de Nacimiento: " + self._fechaNac)