from Persona import Persona
class Texto:
#Por favor cualquier cosa que vean que requiere de texto, metanlo acá para generalizar todo.
	def __init__(self):
		pass

	@staticmethod
	def presentacion():
		if Persona.idiom()==1:
			print("")
			print("")
			print("Presentación de la aplicación") #Continuar aquí, colocar descripción del programa que hay en las diapositivas.
			print("")
			print("")
			print("¿Es ud usuario?")#Se espera que si es usuario tenga contraseña y pues que se pueda validar.
			print("")
			print("")
			print("Se determina el rol y ")
			print("")
			print("")

		else:




	@staticmethod
	def setIdiom():
		print("")
		print("")
		print("Bienvenido a Beyond's Memories")# Hay que expandir la presentación aquí para cuestiones de presentación y demás pero es pulimento, lo dejaré para despues.
		print("Welcome to Beyond's Memories")
		print("")
		print("Por favor seleccione el idioma de su preferencia")
		print("Please select your favorite langueage")
		print("")
		print("  1. Español")
		print("  2. English")
		print("")
		print("")

	@staticmethod
	def datoInvalido():#Todo este método es para imprimir cuando el usuario ingrese datos invalidos.
		if Persona.idiom()==1:
			print("")
		    print("El dato que usted ha ingresado es inválido, repita el proceso")
		    print("")
		else if Persona.idiom==2:
			print("")
			print("Data is invalid, repeat the process")
			print("")
		else:
			print("")
			print("El dato que usted ha ingresado es inválido, repita el proceso/Data is invalid, repeat the process")
			print("")





