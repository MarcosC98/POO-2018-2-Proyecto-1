from Persona import Persona
class Moderador(Persona):
	moderadores_totales = []
	documentos_moderadores = []

	def __init__(self,nombre,documento,fechaNac,contrasena):
		super().__init__(nombre,documento,fechaNac)
		self._contrasena = contrasena
		Moderador.moderadores_totales.append(self)
		Moderador.documentos_moderadores.append(documento)

	def buscarModerador(documento):
		for m in Moderador.moderadores_totales:
			if m._documento == documento:
				return m
				break

	def comprobarDocumentoModerador(documento):
		for d in Moderador.documentos_moderadores:
			if d == documento:
				return True
				break

	def getContrasenaModerador(self):
		return self._contrasena


	def imprimirDatosModerador(self):
		print("TIPO DE PERFIL: MODERADOR")
		print("Nombre: " + self._nombre)
		print("Documento: " + self._documento)
		print("Fecha de Nacimiento: " + self._fechaNac)
