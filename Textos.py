from Persona import Persona
class Texto:

	@staticmethod
	def presentacion():
		print("")
		print("")
		print("                                                           Bienvenido a Beyond's Memories")# Hay que expandir la presentación aquí para cuestiones de presentación y demás pero es pulimento, lo dejaré para despues.
		print("                                                            Welcome to Beyond's Memories")
		print("")
		print("         Por favor seleccione el idioma de su preferencia")
		print("         Please select your favorite langueage")
		print("")
		print("                     1. Español")
		print("                     2. English")
		print("")
		print("")
		print("")


	def introduccion(idiom):
		if(idiom==1):
			print("")
			print("")
			print("Behind Memories es una iniciativa para que las personas sean recordadas hasta el final de los tiempos.")
			print("")
			print("")
		else:
			print("")
			print("")
			print("Behind Memories is a initiative for record the memories of the people untill the end of the time.")
			print("")
			print("")


	def __init__(self,idiom):

		if idiom=="1":
			self.introDoc = ""+"\n"+"Por favor ingrese su documento: "
			self.noRegistra = ""+"\n"+"Su número de identidad no se encuentra registrado."
			self.seleccionUno = ""+"\n"+"Si desea intentar nuevamente con otro documento ingrese 0."+"\n"+"Si desea crear una cuenta nueva con este documento ingrese 1."+"\n"+""
			self.entradaNombre = ""+"\n"+"Ingrese su nombre completo: "
			self.entradaFechaNac = ""+"\n"+"Ingrese su fecha de Nacimiento: "
			self.metodo = ""+"\n"+""
			self.metodo = ""+"\n"+""
			self.metodo = ""+"\n"+""
			self.metodo = ""+"\n"+""
			self.metodo = ""+"\n"+""
			self.metodo = ""+"\n"+""
			self.metodo = ""+"\n"+""
			self.metodo = ""+"\n"+""
			self.metodo = ""+"\n"+""
			self.metodo = ""+"\n"+""
			self.metodo = ""+"\n"+""
			self.metodo = ""+"\n"+""
			self.metodo = ""+"\n"+""
			self.metodo = ""+"\n"+""
			
		else:
			self.introDoc = ""+"\n"+"Please enter you id number: "
			self.noRegistra = ""+"\n"+"There isn't any registered account with that id number."
			self.seleccionUno = ""+"\n"+"If you want to try again with another document, enter 0."+"\n"+"If you want to create a new account with this document, enter 1."+"\n"+""
			self.entradaNombre = ""+"\n"+"Enter your complete name: "
			self.entradaFechaNac = ""+"\n"+""
			self.metodo = ""+"\n"+""







