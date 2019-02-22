class Ubicacion:
	indices_usados = []
	def __init__(self,indice):
		self._indice = indice
		Ubicacion.indices_usados.append(indice)
			
	def revisarDisponibilidadUbicacion(u):
		if u  not in Ubicacion.indices_usados:
			return True
		else:
			return False	

	def getIndice(self):
		return self._indice
