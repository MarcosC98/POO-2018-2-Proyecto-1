import datetime
class Memoria:
	memorias_totales = []
	id = 0
	
	def __init__(self,autor,descripcion,lapida):
		self.autor = autor
		self._descripcion = descripcion
		self.lapida = lapida
		self._fechaPub =  str(datetime.datetime.now())

	def imprimirDatosMemoria(self):
		print("Memoria de " + self.lapida._persona.getNombre())
		print(self._descripcion)
		print("Escrito en : " + self._fechaPub + " por " + self.autor.getNombre())
		print("-------------------------------------------------------------------------------------------------------------------------------------------------------")
		
