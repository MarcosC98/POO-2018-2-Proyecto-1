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
			self.datoInvalido = ""+"\n"+"El dato ingresado es inválido."
			self.introDoc = ""+"\n"+"Por favor ingrese su documento: "
			self.noRegistra = ""+"\n"+"Su número de identidad no se encuentra registrado."
			self.seleccionUno = ""+"\n"+"Si desea intentar nuevamente con otro documento ingrese 0."+"\n"+"Si desea crear una cuenta nueva con este documento ingrese 1."+"\n"+""
			self.entradaNombre = ""+"\n"+"Ingrese su nombre completo: "
			self.entradaFechaNac = ""+"\n"+"Ingrese su fecha de Nacimiento: "
			self.selecOpcion = ""+"\n"+"Ingrese el número de la acción a realizar:"+"\n"+" "+"\n"+"  1.Adquirir Lápida."+"\n"+"  2.Escribir Memoria "+"\n"+"  3.Leer Lápida "+"\n"+"  4.Ingresar con otro perfil "+"\n"+"  5.Salir "
			self.ingresoEpitafio = ""+"\n"+"Ingrese el epitafio que desea en su lapida: "
			self.ingresoContrasena = ""+"\n"+"Ingrese la contraseña que usará en su cuenta: "
			self.ingresoUbicacion = ""+"\n"+"Ingrese la úbicación de su lápida: "
			self.selecPrivacidad = ""+"\n"+"Ingrese 0 si desea que su lápida sea privada"+"\n"+"Ingrese 1 si desea que sea pública (Recomendado) "
			self.lapidaOcupada = ""+"\n"+"Esta ubicación ya se encuentra ocupada, selecciona una distinta por favor."
			self.lapidaAntesCreada = ""+"\n"+"Ya tienes una lapida creada."
			self.propietarioLap = ""+"\n"+"Ingrese el documento de la persona propietaria de la lapida donde va a dejar la memoria: "
			self.lapidaPrivada = ""+"\n"+"Esta lápida es privada. No puedes leer/escribir memorias."
			self.ingMemoria = ""+"\n"+"Ingrese la descripcion de la memoria por favor: "
			self.lapidaInvalida = ""+"\n"+"No hay ninguna persona con ese documento que tenga una lapida."
			self.ingresoPropietario = ""+"\n"+"Ingrese el documento de la persona propietaria de la lapida que desea leer: "
			self.noLapida = ""+"\n"+"No hay ninguna persona con ese documento que tenga una lapida."

			
		else:
			self.datoInvalido = ""+"\n"+"El dato ingresado es inválido."
			self.introDoc = ""+"\n"+"Please enter you id number: "
			self.noRegistra = ""+"\n"+"There isn't any registered account with that id number."
			self.seleccionUno = ""+"\n"+"If you want to try again with another document, enter 0."+"\n"+"If you want to create a new account with this document, enter 1."+"\n"+""
			self.entradaNombre = ""+"\n"+"Enter your complete name: "
			self.entradaFechaNac = ""+"\n"+"Enter your Birth day: "
			self.selecOpcion = ""+"\n"+"Choose one of the follow options: "+"\n"+" "+"\n"+"  1.Purchase a tombstone."+"\n"+"  2.Write Memory "+"\n"+"  3.Read tombstone "+"\n"+"  4.Enter with another profile "+"\n"+"  5.Game Over "
			self.ingresoEpitafio = ""+"\n"+"Write the sentence of your Epitaph: "
			self.ingresoContrasena = ""+"\n"+"Enter the password of your account: "
			self.ingresoUbicacion = ""+"\n"+"Enter the location of your tombstone: "
			self.selecPrivacidad = ""+"\n"+"Type 0 if you want your tombstone to be private"+"\n"+"Type 1 if you want a public tombstone (Recommended) "
			self.lapidaOcupada = ""+"\n"+"This location is already occupied, select a different one please."
			self.lapidaAntesCreada = ""+"\n"+"You already have a tombstone created."
			self.propietarioLap = ""+"\n"+"Enter the document of the person who owns the tombstone where you will leave the memory: "
			self.lapidaPrivada = ""+"\n"+"This tombstone is private. You can not read / write memories."
			self.ingMemoria = ""+"\n"+"Enter the description of the memory please: "
			self.lapidaInvalida = ""+"\n"+"There is no person with that document who has a tombstone."
			self.ingresoPropietario = ""+"\n"+"Enter the document of the person who owns the tombstone you want to read: "
			self.noLapida = ""+"\n"+"There is no person with that document who has a tombstone."







