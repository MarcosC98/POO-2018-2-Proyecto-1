from Persona import Persona
class Visitante(Persona):
	visitantes_totales = []

	def __init__(self,nombre,fechaNac):
		super().__init__(nombre,fechaNac)
