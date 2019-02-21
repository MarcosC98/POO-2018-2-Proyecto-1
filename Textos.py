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
			self.entradaFechaNac = ""+"\n"+"Ingrese su fecha de Nacimiento (dd/mm/aaaa): "
			self.selecOpcion = ""+"\n"+"Ingrese el número de la acción a realizar:"+"\n"+" "+"\n"+"  1.Adquirir Lápida."+"\n"+"  2.Escribir Memoria "+"\n"+"  3.Leer Lápida "+"\n"+"  4.Ingresar con otro perfil "+"\n"+"  5.Salir "+"\n"+""+"\n"+"Tu Seleccion: "
			self.ingresoEpitafio = ""+"\n"+"Ingrese el epitafio que desea en su lapida: "
			self.crearContrasena = ""+"\n"+"Ingrese la contraseña que usará en su cuenta: "
			self.ingresoUbicacion = ""+"\n"+"Ingrese la úbicación de su lápida: "
			self.selecPrivacidad = ""+"\n"+"Ingrese 0 si desea que su lápida sea privada"+"\n"+"Ingrese 1 si desea que sea pública (Recomendado) "
			self.lapidaOcupada = ""+"\n"+"Esta ubicación ya se encuentra ocupada, selecciona una distinta por favor."
			self.ubicacionInvalida = ""+"\n"+"Ingresa una ubicación valida."
			self.noNumerico = ""+"\n"+"Ingrese un número por favor."
			self.contrasenaInvalida = ""+"\n"+"Ingrese una contraseña válida."
			self.lapidaAntesCreada = ""+"\n"+"Ya tienes una lapida creada."
			self.propLapDejarMemoria = ""+"\n"+"Ingrese el documento de la persona propietaria de la lapida donde va a dejar la memoria: "
			self.lapidaPrivada = ""+"\n"+"Esta lápida es privada. No puedes leer/escribir memorias."
			self.noDescripcion = ""+"\n"+"No puede haber una Memoria sin descripción."
			self.noDocumentoLap = ""+"\n"+"No hay ninguna persona con ese documento que tenga una lapida."
			self.exit = ""+"\n"+"El programa ha finalizado."
			self.ingMemoria = ""+"\n"+"Ingrese la descripcion de la memoria por favor: "
			self.lapidaInvalida = ""+"\n"+"No hay ninguna persona con ese documento que tenga una lapida."
			self.ingresoPropietario = ""+"\n"+"Ingrese el documento de la persona propietaria de la lapida que desea leer: "
			self.noLapida = ""+"\n"+"No hay ninguna persona con ese documento que tenga una lapida."
			self.modOrClient = ""+"\n"+"¿Desea ingresar a su perfil de moderador o cliente?"+"\n"+"   1.Moderador"+"\n"+"   2.Cliente"+"\n"+"   3.Ingreso con otro Documento."
			self.selecMenu = ""+"\n"+"Ingrese el número de la acción a realizar:"+"\n"+""+"\n"+"   1.Registrar nuevo moderador"+"\n"+"   2.Borrar memoria."+"\n"+"   3.Registrar defunción de un cliente."+"\n"+"   4.Cambiar contraseña."+"\n"+"   5.Ver numero total de clientes."+"\n"+"   6.Ver numero total de moderadores."+"\n"+"   7.Ver numero total de visitantes"+"\n"+"   8.Ingresar con otro perfil."+"\n"+"   9.Salir." 
			self.ingresoContrasena = ""+"\n"+"Por favor ingrese su contraseña: "
			self.docModerador = ""+"\n"+"Ingrese el documento del Moderador: "
			self.nombreModerador = ""+"\n"+"Ingrese el nombre del Moderador: "
			self.fnModerador = ""+"\n"+"Ingrese la Fecha de Nacimiento del Moderador (dd/mm/aaaa): "
			self.contrasenaModerador = ""+"\n"+"Ingrese su contraseña como Moderador: "
			self.existeMod = ""+"\n"+"Ya existe un Moderador con este documento."
			self.documentoLapida = ""+"\n"+"Ingrese el documento de la persona la cual posee la lapida donde está la memoria que desea eliminar "
			self.noDuenoLapida = ""+"\n"+"No hay ninguna persona con ese documento que posea una lapida"
			self.lapPrivSinMemoria = ""+"\n"+"Esta lápida es privada y no tiene Memorias."
			self.sinMemoria = ""+"\n"+"Esta lápida no tiene Memorias."
			self.eliminarMemoria = ""+"\n"+"Ingrese el numero de la memoria que desea eliminar "
			self.noPosicionMemoria = ""+"\n"+"No existe una memoria en la posición: "
			self.documentoClienteFallecido = ""+"\n"+"Ingrese el documento del Cliente fallecido: "
			self.clienteNoLapida = ""+"\n"+"No hay ninguna persona con ese documento que posea una lapida."
			self.fechaDefuncion = ""+"\n"+"Ingrese la fecha de defunción de el cliente en formado (dd/mm/aaaa):"
			self.yaDifunto = ""+"\n"+"Este cliente ya tiene una fecha de defunción registrada."
			self.textNuevaContraseña = ""+"\n"+"Su Nueva Contraseña es: "
			self.total = ""+"\n"+"En total hay: "
			self.clientes = ""+"\n"+" Clientes."
			self.mods = ""+"\n"+" Moderadores."
			self.visit = ""+"\n"+" Visitantes."
			self.contrasenaIncorrecta = ""+"\n"+"La contraseña es incorrecta."
			self.perfilVisitante = ""+"\n"+"TIPO DE PERFIL: VISITANTE"
			self.nombre = "Nombre: "
			self.documento = "Documento: "
			self.fechaNac = "Fecha de Nacimiento: "
			self.propLapidaLeer= ""+"\n"+"Ingrese el documento de la persona propietaria de la lapida que desea leer."
			self.noDuenoLapida = ""+"\n"+"No hay ninguna persona con ese documento que tenga una lapida"
				
		else:
			self.datoInvalido = ""+"\n"+"El dato ingresado es inválido."
			self.introDoc = ""+"\n"+"Please enter you id number: "
			self.noRegistra = ""+"\n"+"There isn't any registered account with that id number."
			self.seleccionUno = ""+"\n"+"If you want to try again with another document, enter 0."+"\n"+"If you want to create a new account with this document, enter 1."+"\n"+""
			self.entradaNombre = ""+"\n"+"Enter your complete name: "
			self.entradaFechaNac = ""+"\n"+"Enter your Birth day (dd/mm/yyyy): "
			self.selecOpcion = ""+"\n"+"Choose one of the follow options: "+"\n"+" "+"\n"+"  1.Purchase a tombstone."+"\n"+"  2.Write Memory "+"\n"+"  3.Read tombstone "+"\n"+"  4.Enter with another profile "+"\n"+"  5.Game Over "+"\n"+""+"\n"+"Your Selection: "
			self.ingresoEpitafio = ""+"\n"+"Write the sentence of your Epitaph: "
			self.crearContrasena = ""+"\n"+"Enter a password for your account: "
			self.ingresoUbicacion = ""+"\n"+"Enter the location of your tombstone: "
			self.selecPrivacidad = ""+"\n"+"Type 0 if you want your tombstone to be private"+"\n"+"Type 1 if you want a public tombstone (Recommended) "
			self.lapidaOcupada = ""+"\n"+"This location is already occupied, select a different one please."
			self.ubicacionInvalida = ""+"\n"+"Ingresa una ubicación valida."#Traducir
			self.noNumerico = ""+"\n"+"Ingrese un número por favor."#Traducir
			self.contrasenaInvalida = ""+"\n"+"Ingrese una contraseña válida."#Traducir
			self.lapidaAntesCreada = ""+"\n"+"You already have a tombstone created."
			self.propLapDejarMemoria = ""+"\n"+"Enter the document of the person who owns the tombstone where you will leave the memory: "
			self.lapidaPrivada = ""+"\n"+"This tombstone is private. You can not read / write memories."
			self.noDescripcion = ""+"\n"+"No puede haber una Memoria sin descripción."#Traducir
			self.noDocumentoLap = ""+"\n"+"No hay ninguna persona con ese documento que tenga una lapida." #Traducir
			self.exit = ""+"\n"+"El programa ha finalizado." #Traducir
			self.ingMemoria = ""+"\n"+"Enter the description of the memory please: "
			self.lapidaInvalida = ""+"\n"+"There is no person with that document who has a tombstone."
			self.ingresoPropietario = ""+"\n"+"Enter the document of the person who owns the tombstone you want to read: "
			self.noLapida = ""+"\n"+"There is no person with that document who has a tombstone."
			self.modOrClient = ""+"\n"+"¿Desea ingresar a su perfil de moderador o cliente?"+"\n"+"   1.Moderador"+"\n"+"   2.Cliente"+"\n"+"   3.Ingreso con otro Documento." #Traducir
			self.selecMenu = ""+"\n"+"Choose one of the follow options: "+"\n"+""+"\n"+"   1.Register a new Moderator."+"\n"+"   2.Delete Memory."+"\n"+"   3.Record the death of a client."+"\n"+"   4.Cambiar contraseña."+"\n"+"   5.See amount of clients."+"\n"+"   6.See amount of moderators."+"\n"+"   7.See amount of visitors"+"\n"+"   8.Enter with other profile."+"\n"+"   9.Game Over." 
			self.ingresoContrasena = ""+"\n"+"Por favor ingrese su contraseña: " #Traducir
			self.docModerador = ""+"\n"+"Ingrese el documento del Moderador: " #Traducir
			self.nombreModerador = ""+"\n"+"Ingrese el nombre del Moderador: "#Traducir
			self.fnModerador = ""+"\n"+"Ingrese la Fecha de Nacimiento del Moderador (dd/mm/aaaa): "#Traducir
			self.contrasenaModerador = ""+"\n"+"Ingrese una contraseña para Moderador: "#Traducir
			self.existeMod = ""+"\n"+"Ya existe un Moderador con este documento." #Traducir
			self.documentoLapida = ""+"\n"+"Ingrese el documento de la persona la cual posee la lapida donde está la memoria que desea eliminar " #Traducir
			self.noDuenoLapida = ""+"\n"+"No hay ninguna persona con ese documento que posea una lapida" #Traducir
			self.lapPrivSinMemoria = ""+"\n"+"Esta lápida es privada y no tiene Memorias."#Traducir
			self.sinMemoria = ""+"\n"+"Esta lápida no tiene Memorias."#Traducir
			self.eliminarMemoria = ""+"\n"+"Ingrese el numero de la memoria que desea eliminar "#Traducir
			self.noPosicionMemoria = ""+"\n"+"No existe una memoria en la posición: "#Traducir
			self.documentoClienteFallecido = ""+"\n"+"Ingrese el documento del Cliente fallecido: "#Traducir
			self.clienteNoLapida = ""+"\n"+"No hay ninguna persona con ese documento que posea una lapida."#Traducir
			self.fechaDefuncion = ""+"\n"+"Ingrese la fecha de defunción de el cliente en formado (dd/mm/aaaa):"#Traducir
			self.yaDifunto = ""+"\n"+"Este cliente ya tiene una fecha de defunción registrada."#Traducir
			self.textNuevaContraseña = ""+"\n"+"Su Nueva Contraseña es: "#Traducir
			self.total = ""+"\n"+"There are in total: "#Traducir
			self.clientes = ""+"\n"+" Clients."
			self.mods = ""+"\n"+" Moderators."
			self.visit = ""+"\n"+" Visitors."
			self.contrasenaIncorrecta = ""+"\n"+"La contraseña es incorrecta."#Traducir
			self.perfilVisitante = ""+"\n"+"TIPO DE PERFIL: VISITANTE"
			self.nombre = "Name: "
			self.documento = "Document: "
			self.fechaNac = "Date of Birth: "
			self.propLapidaLeer = ""+"\n"+"Ingrese el documento de la persona propietaria de la lapida que desea leer."#Traducir
			self.noDuenoLapida = ""+"\n"+"No hay ninguna persona con ese documento que tenga una lapida"#Traducir






