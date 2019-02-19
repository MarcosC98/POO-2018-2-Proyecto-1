from Persona import Persona
class Visitante(Persona):
	visitantes_totales = 0

	def __init__(self,nombre,fechaNac):
		super().__init__(nombre,fechaNac)
		Visitante.visitantes_totales = visitantes_totales+1
