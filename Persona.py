import math
from datetime import datetime, date, time, timedelta
import calendar
from Texto import Texto

#Clase Principal llamada Persona, esta contiene el método Main que dirige todo el proyecto.
#Le dejo mi alma a este proyecto.

class Persona():

	listPersona = {"Documento  ":["Documento ","Nombre ","Fecha de Nacimiento"]} # Resolver lo más pronto posible lo de los datos ficticios.
	contrasenas = {"Contrasena","Rol de Usuario"}
	_hoy = datetime.now
	_documento
	_nombre
	_fechaNac
	_idiom
	_rol
	_contrasena

	def __init__(self):
		Texto.setIdiom()
		
		
		if(contrasena[])


	if()
		Texto.selIdiom()# Este es el inicializador del método persona que recibe el idioma en que la persona desea ver la aplicación. Si la elección es válido para luego a los métodos para registrar el usuario y posteriormente clasificarlo.
		idiom=input()

		if _idiom==1:
			#Mostrar textos para Entrada de Persona en español.
			self.registrarPersona()
			self.clasificar()
			pass
		else if _idiom==2:
			#Mostrar textos para Entrada de Persona en inglés.
			self.registrarPersona()
			self.clasificarPersona()
			pass
		else:
			Texto.datoInvalido()

			

	@staticmethod
	def registrarPersona():

		_documento=input();
		if (type(_documento)==(int)):
			_nombre=input()
			if(type(_nombre)==(str)):
				_fechaNac=input(Fecha de Nacimiento!) #Aquí no sé como hacer el intro para la fecha de Nacimiento.
				if(type(_fechaNac)==(date)):
					listPersona[0]=(_documento,_nombre,_fechaNac)
				else:
					Texto.datoInvalido()
			else:
				Texto.datoInvalido()
		else:
			Texto.datoInvalido()


	@staticmethod
	def clasificarPersona():

		#Texto para presentar al usuario sobre que rol tomar.
		print("Si usted es un")


	
    if __name__ == "__main__":

     	Persona().run()






		
