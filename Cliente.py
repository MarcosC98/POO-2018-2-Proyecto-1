from Persona import Persona
class Cliente(Persona):

	listClientes["Documento"]={"Nombre","fechaNac","Contraseña"}
	
	_contador=0


	def __init__(self):
		pass

	def registrarCliente(self,nombre,documento,fechaNac):

		if "_documento" in listClientes:
			print("Ud ya está inscrito como cliente.")

		else:
			print("Por favor ingrese su Contraseña.")
			_contrasena = input()
			listClientes[self._documento] = (self.nombre,self.fechaNac,self.contrasena)


		