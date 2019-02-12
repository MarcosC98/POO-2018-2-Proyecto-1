class ubicacion:
	ubicaciones_disponibles=50
	ubicaciones_totales = []
	indices_usados = []
	def __init__(self,indice,idCliente=0):
		while indice is in indices_usados:
			print("Está ubicación está ocupada, ingrese una ubicación distinta")
			if indice is not in indices_usados:
				indices_usados.append(indice)
				self._indice = indice
				self._idCliente = idCliente
				break

	def revisarDisponibilidadUbicacion(u):
		if u is not in indices_usados:
			return True
		else:
			return False	
