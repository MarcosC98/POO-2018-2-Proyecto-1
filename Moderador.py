class Moderador(Persona):

	listMods["Documento"]={"Nombre","fechaNac","Contraseña"}
	_contraseña

	def __init__ (self):
		pass

	def registrarMod(self,nombre,documento,fechaNac):

		if "_documento" in listClientes:
			print("Ud ya está inscrito como Moderador.")

		else:
			print("Por favor ingrese su Contraseña.")
			_contrasena = input()
			listMods[self._documento] = (self.nombre,self.fechaNac,self.contrasena)
			