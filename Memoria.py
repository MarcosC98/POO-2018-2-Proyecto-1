import datetime
class Memoria:
	memorias_totales = []
	id = 0
	
	def __init__(self,autor,descripcion,lapida):
		self._autor = autor
		self._descripcion = descripcion
		self._lapida = lapida
		self._fechaPub =  str(datetime.datetime.now())

	def imprimirDatosMemoria(self):
		print("Memoria de " + self._lapida._persona.getNombre())
		print(self._descripcion)
		print("Escrito en : " + self._fechaPub + " por " + self._autor.getNombre())
		print("-------------------------------------------------------------------------------------------------------------------------------------------------------")
		
