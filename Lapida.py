import ubicacion
class Lapida:
	lapidas_totales = []#Lista con todas las lápidas generadas	


	def __init__(self,idCliente,nombreCliente,fechaNac,fechaDef=0,epitafio="",privacidad,idUbicacion): #Constructor de clase lapida
		self _fechaDef = fechaDef	#fecha defuncion, se inicia en 0 ya que un cliente puede tener una lapida sin haber fallecido
		self _epitafio = epitafio	#epitafio. En el constructor se inicia vacío ya que hay lapidas sin epitafios
		self _privacidad = privacidad	#Es un boolean con true = privada y false = publica
		self _idCliente = idCliente	#Se asocia al cliente con su ID
		self _nombrecli = nombreCliente		#Se guarda tambien el nombre del cliente
		self _fechaNac = fechaNac 	#Se guarda la fecha de nacimiento del cliente
		self _idUbicacion = idUbicacion	#Se asocia la ubicación con su ID
		self _moderadores = moderadores [] 	#Se genera lista para que guarde cada moderador que realice algún cambio
		self _memorias = memorias[]	#Se genera la lista que guarde las memorias que sean dejadas en la lapida
		Lapida.lapidas_totales.append(self)		#Se envía la lápida generada a la lista de todas las lapidas

	def modificarEpitafio(self):			#Método para modificar el epitafio
		e = input("Ingrese el epitafio")	
		self._epitafio = e

	@staticmethod
	def leerLapida(self):													#Método para leer la información de la lápida
		print("Nombre = " + self._nombrecli)								
		print("Identificación = " + self._idCliente)						
		if self._epitafio != "":											#Se comprueba que el epitafio no esté vacío
			print("Epitafio = " + self._epitafio)
		print("Fechad de nacimiento = " + self._fechaNac)
		if self._fechaDef != 0:												#Se comprueba que ya esté la fecha de defunción
			print("Fecha de defunción" + self._fechaDef)
		print("Ubicacion = " + self._idUbicacion)
		if self._privacidad False:											#Se comprueba que la privacidad sea pública y se recorre un arreglo imprimiendo todas las memorias				
			print("Memorias: ")
			for m in memorias[]:
				print("* " + m)
		else:
			print("Esta lápida es privada. No puedes leer las memorias.")

	def modificarUbicacion(self):										
			u = input("Ingrese el ID de la nueva ubicación")
			if ubicacion.revisarDisponibilidadUbicacion(u):					#Se llama al método de la clase ubicacion.py donde se revisa si la ubicacion está disponible(retorna true or false dependiendo)
				ubicacion.indices_usados.remove(self._idUbicacion)			#Se remueve el indice que solía estar ocupado de la lista de indices usados
				ubicacion.indices_usados.append(u)							#Se agrega el nuevo indice
				self._idUbicacion = u
			else:															#Si el método retorna False, el ID ya está siendo usado(Ya está ocupada la ubicación)
				print("Esta ubicación ya está ocupada")

	def modificarPrivacidad(self):
		p = input("Ingrese 1 para hacer de la lapida privada, 2 para que sea pública")
		if p == 1:
			self._privacidad = True
		else:
			self._privacidad = False




	
