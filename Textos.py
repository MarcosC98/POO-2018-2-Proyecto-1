from Persona import Persona
class Texto:

	def __init__(self,idiom):

		if idiom=="1":
			self.introDoc = ""+"\n"+"Por favor ingrese su documento: "
			self.noRegistra = ""+"\n"+"Su número de identidad no se encuentra registrado."
			self.seleccionUno = ""+"\n"+"Si desea intentar nuevamente con otro documento ingrese 0."+"\n"+"Si desea crear una cuenta nueva con este documento ingrese 1."+"\n"+""

		else:
			self.introDoc = "Please enter you id number: "
			self.noRegistra = "There isn't any registered account with that id number."
			self.seleccionUno = "quibu"
			self.metodo = ""+"\n"+""


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

	@staticmethod
	def ingresoDocumento():
		if idiom==1:
			print("Ingrese su numero de documento por favor: ")
		else:
			print("Lo mismo pero en inglés: ")








