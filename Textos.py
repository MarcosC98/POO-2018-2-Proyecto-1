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
		if(idiom=="1"):
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
			self.propLapElimMemoria =  ""+"\n"+"Ingrese el documento de la persona propietaria de la lapida donde va a eliminar la memoria: "
			self.lapidaPrivada = ""+"\n"+"Esta lápida es privada. No puedes leer/escribir memorias."
			self.noDescripcion = ""+"\n"+"No puede haber una Memoria sin descripción."
			self.noDocumentoLap = ""+"\n"+"No hay ninguna persona con ese documento que tenga una lapida."
			self.exit = ""+"\n"+"El programa ha finalizado."
			self.ingMemoria = ""+"\n"+"Ingrese la descripcion de la memoria por favor: "
			self.lapidaInvalida = ""+"\n"+"No hay ninguna persona con ese documento que tenga una lapida."
			self.ingresoPropietario = ""+"\n"+"Ingrese el documento de la persona propietaria de la lapida que desea leer: "
			self.noLapida = ""+"\n"+"No hay ninguna persona con ese documento que tenga una lapida."
			self.modOrClient = ""+"\n"+"¿Desea ingresar a su perfil de moderador o cliente?"+"\n"+"   1.Moderador"+"\n"+"   2.Cliente"+"\n"+"   3.Ingreso con otro Documento."
			self.selecMenu = ""+"\n"+"Ingrese el número de la acción a realizar:"+"\n"+""+"\n"+"   1.Registrar nuevo moderador"+"\n"+"   2.Borrar memoria."+"\n"+"   3.Registrar defunción de un cliente."+"\n"+"   4.Cambiar contraseña."+"\n"+"   5.Ver numero total de clientes."+"\n"+"   6.Ver numero total de moderadores."+"\n"+"   7.Ver numero total de visitantes"+"\n"+"   8.Ingresar con otro perfil."+"\n"+"   9.Revisar ubicaciones ocupadas. "+ "\n" + "   10.Salir."+"\n"+""+"\n"+"Su elección: "
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
			self.ingresoLapida = ""+"\n"+"Debe ingresar un numero entre 1 y 50. Por esto no se pudo completar la creación de lapida"
			self.ubicadas = ""+"\n""Las ubicaciones ocupadas son: "
			self.fnVacia = ""+"\n"+"Fecha de nacimiento no puede estar vacía."
			self.nombreVacio = ""+"\n"+"Nombre no puede estar vacio."
			self.selecTres = ""+"\n"+"Ingrese el número de la acción a realizar."+"\n"+""+"\n"+"   1.Cambiar epitafio."+"\n"+"   2.Cambiar ubicación."+"\n"+"   3.Cambiar contraseña."+"\n"+"   4.Ingresar Memoria."+"\n"+"   5.Leer Lapida."+"\n"+"   6.Eliminar memoria de mi lapida."+"\n"+"   7.Cambiar privacidad."+"\n"+"   8.Ingresar con un perfil distinto."+"\n"+"   9. Salir."
			self.nuevoEpitafio = ""+"\n"+"Ingrese el nuevo epitafio: "
			self.suEpitafio = ""+"\n"+"Su epitafio es: "
			self.nuevaUbicacion = ""+"\n"+"Ingrese su nueva ubicación: "
			self.suNUbicacion = ""+"\n"+"Su nueva ubicación es en: "
			self.ubicacionNoDisponible = ""+"\n"+"Esta ubicación no está disponible."
			self.indiceUbicacion = ""+"\n"+"Debe ingresar un numero entre 1 y 50"
			self.ingresoNumero = ""+"\n"+"Por favor ingrese un numero."
			self.lapidaPublica = ""+"\n"+"Ahora su lápida es publica."
			self.lapidaPrivada = ""+"\n"+"Ahora su lápida es privada."
			self.metodo = ""+"\n"+""
			self.metodo = ""+"\n"+""





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
			self.ubicacionInvalida = ""+"\n"+"Enter a valid location"
			self.noNumerico = ""+"\n"+"Enter a number please."
			self.contrasenaInvalida = ""+"\n"+"Enter a valid password."
			self.lapidaAntesCreada = ""+"\n"+"You already have a tombstone created."
			self.propLapDejarMemoria = ""+"\n"+"Enter the document of the person who owns the tombstone where you will leave the memory: "
			self.lapidaPrivada = ""+"\n"+"This tombstone is private. You can not read / write memories."
			self.noDescripcion = ""+"\n"+"There can not be a Memory without description."
			self.noDocumentoLap = ""+"\n"+"There is no person with that document who has a tombstone."
			self.exit = ""+"\n"+"The program has finished."
			self.ingMemoria = ""+"\n"+"Enter the description of the memory please: "
			self.lapidaInvalida = ""+"\n"+"There is no person with that document who has a tombstone."
			self.ingresoPropietario = ""+"\n"+"Enter the document of the person who owns the tombstone you want to read: "
			self.noLapida = ""+"\n"+"There is no person with that document who has a tombstone."
			self.modOrClient = ""+"\n"+"Do you want to enter your moderator or client profile?"+"\n"+"   1.Moderator."+"\n"+"   2.Client."+"\n"+"   3.Register with another document."
			self.selecMenu = ""+"\n"+"Choose one of the follow options: "+"\n"+""+"\n"+"   1.Register a new Moderator."+"\n"+"   2.Delete Memory."+"\n"+"   3.Record the death of a client."+"\n"+"   4.Change Password."+"\n"+"   5.See amount of clients."+"\n"+"   6.See amount of moderators."+"\n"+"   7.See amount of visitors"+"\n"+"   8.Enter with other profile."+"\n"+"   9.Review occupied locations.+"+"\n"+"   10.GameOver."+"\n"+""+"\n"+"Your Decision: "
			self.ingresoContrasena = ""+"\n"+"Please enter your password: " 
			self.docModerador = ""+"\n"+"Enter the Moderator's document: " 
			self.nombreModerador = ""+"\n"+"Enter the name of the Moderator: "
			self.fnModerador = ""+"\n"+"Enter the Date of Birth of the Moderator (dd/mm/yyyy): "
			self.contrasenaModerador = ""+"\n"+"Enter a password for Moderator: "
			self.existeMod = ""+"\n"+"There is already a Moderator with this document."
			self.documentoLapida = ""+"\n"+"Enter the document of the person who has the headstone where is the memory you want to delete: "
			self.noDuenoLapida = ""+"\n"+"There is no person with that document who has a tombstone."
			self.lapPrivSinMemoria = ""+"\n"+"This tombstone is private and has no memories."
			self.sinMemoria = ""+"\n"+"This tombstone has no Memories."
			self.eliminarMemoria = ""+"\n"+"Enter the number of the memory you want to delete:"
			self.noPosicionMemoria = ""+"\n"+"There is no memory in the position:"
			self.clienteNoLapida = ""+"\n"+"There is no person with that document who has a tombstone."
			self.fechaDefuncion = ""+"\n"+"Enter the customer's death date in the format (dd/mm/yyyy):"
			self.yaDifunto = ""+"\n"+"This client already has a registered death date."
			self.textNuevaContraseña = ""+"\n"+"Your New Password is:"
			self.clientes = ""+"\n"+" Clients."
			self.mods = ""+"\n"+" Moderators."
			self.visit = ""+"\n"+" Visitors."
			self.contrasenaIncorrecta = ""+"\n"+"Password is incorrect."
			self.perfilVisitante = ""+"\n"+"TYPE OF PROFILE: VISITOR"
			self.nombre = "Name: "
			self.documento = "Document: "
			self.fechaNac = "Date of Birth: "
			self.propLapidaLeer = ""+"\n"+"Enter the document of the person who owns the tombstone you wish to read."
			self.noDuenoLapida = ""+"\n"+"There is no person with that document that has a tombstone."
			self.ingresoLapida = ""+"\n"+"Debe ingresar un numero entre 1 y 50. Por esto no se pudo completar la creación de lapida" #Traducir
			self.ubicadas = ""+"\n"+"The occupied locations are: "
			self.fnVacia = ""+"\n"+"Date of birth can not be empty."
			self.nombreVacio = ""+"\n"+"Name can not be empty."
			self.selecTres = ""+"\n"+"Enter the number of the action to be done: "+"\n"+""+"\n"+"   1.Change epitaph."+"\n"+"   2.Change location."+"\n"+"   3.Change Password."+"\n"+"   4.Enter a Memory."+"\n"+"   5.Read Tombstone."+"\n"+"   6.Remove memory from my gravestone."+"\n"+"   7.Change Privacity."+"\n"+"   8.Login with a different profile."+"\n"+"   9. GameOver."
			self.nuevoEpitafio = ""+"\n"+"Enter the new epitaph: "
			self.suEpitafio = ""+"\n"+"Its epitaph is:"
			self.nuevaUbicacion = ""+"\n"+"Enter your new location:"
			self.suNUbicacion = ""+"\n"+"Your new location is in: "
			self.ubicacionNoDisponible = ""+"\n"+"This location is not available."
			self.indiceUbicacion = ""+"\n"+"You must enter a number between 1 and 50."
			self.ingresoNumero = ""+"\n"+"Please enter a number: "
			self.lapidaPublica = ""+"\n"+"Now his tombstone is public."
			self.lapidaPrivada = ""+"\n"+"Now his tombstone is private."






