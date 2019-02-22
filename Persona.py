from Textos import Texto
from Lapida import Lapida
class Persona:
    personas_totales = []

    def __init__(self,nombre,documento,fechaNac):
        self._nombre = nombre
        self._documento = documento
        self._fechaNac = fechaNac
        Persona.personas_totales.append(self)

    def imprimirDatosPersona(self,t):
        print("--------------------------------------------------------------------------------------------")
        print(t.perfilVisitante)
        print(t.nombre + self._nombre)
        print(t.documento + self._documento)
        print(t.fechaNac + self._fechaNac)
        print("--------------------------------------------------------------------------------------------")

    def getNombre(self):
        return self._nombre

    def getDocumento(self):
        return self._documento

    def getFechaNac(self):
        return self._fechaNac

    def verLapida(t):
        while True:
            print(t.propLapidaLeer)
            l = Lapida.buscarLapida(input())
            if l is not None:
                l.leerLapida()
                break
            else:
                print(t.noDuenoLapida)

    def escribirMemoria(t,v):
        from Memoria import Memoria
        print(""+"\n"+"///////////////////////////////////////////CREACION DE MEMORIA///////////////////////////////////////////"+"\n"+"") #Nuevamente los dejo porque me parece que son puntos de referencia en el código.
        while True:
            print(t.propLapDejarMemoria)
            l = Lapida.buscarLapida(input())
            if l is not None:
                if l.getPrivacidad():
                    print(t.lapidaPrivada)
                    break
                else:
                    while True:
                        print(t.ingMemoria)
                        de = input()
                        if de is not "":
                            me = Memoria(v,de,l)
                            l.memorias.append(me)
                            me.imprimirDatosMemoria()
                            break
                        else:
                            print(t.noDescripcion)
                    break
            else:
                print(t.noDocumentoLap)

    def borrarMemoria(t,c):
        l = c.getLapida()
        if l.getPrivacidad():
            print(t.lapPrivSinMemoria)
        else:
            if len(l.memorias) == 0:
                print(t.sinMemoria)
            else:
                l.imprimirMemorias()
                while True:
                    print(t.eliminarMemoria)
                    i = input()#FALLA SI INPUT ES VACÍO
                    if len(l.memorias) >= int(i):
                        l.borrarMemoria(i) #CONTROL PARA QUE ALGUIEN NO PONGA LETRAS O NÚMEROS INVALIDOS
                        break
                    else:
                        print(t.noPosicionMemoria + i)

    def accionesModerador(t,m):
        from Cliente import Cliente
        from Moderador import Moderador
        from Ubicacion import Ubicacion
        while True:
            print(t.ingresoContrasena)
            c = input()
            if c == m.getContrasenaModerador():
                m.imprimirDatosModerador()
                while True:
                    print(t.selecMenu)
                    ac = input()
                    if ac == "1":
                        while True:
                            documento = input(t.docModerador)
                            if documento.isdigit():
                                if Moderador.comprobarDocumentoModerador(documento) is None:
                                    while True:
                                        print(t.nombreModerador)
                                        nombre = input()  
                                        print(t.fnModerador)                           
                                        fechaNac = input()
                                        print(t.contrasenaModerador)
                                        contrasena = input()
                                        if nombre is not "" and fechaNac is not "" and contrasena is not "":
                                            mod = Moderador(nombre,documento,fechaNac,contrasena)
                                            print("-------------------------------------NUEVO MODERADOR CREADO-------------------------------------")
                                            Moderador.imprimirDatosModerador(mod)
                                            break
                                        else:
                                            print("Por favor ingrese la información completa ")
                                    break
                                else:
                                    print(t.existeMod)
                            else:
                                print(t.noNumerico)

                    elif ac == "2":
                        while True:
                            print(t.nombre)
                            a = input()
                            c = Cliente.buscarCliente(a)
                            if c is None:
                                print(t.noDuenoLapida)
                            else:
                                Persona.borrarMemoria(t,c)
                                break

                    elif ac == "3":
                        while True:
                            print(t.documentoClienteFallecido)
                            a = input()
                            c = Cliente.buscarCliente(a)
                            if c is None:
                                print(t.clienteNoLapida)
                            else:
                                l = c.getLapida()
                                if l.getFechaDef() is "":
                                    while True:
                                        print("Ingrese la fecha de defunción")
                                        fd = input()
                                        if fd is not "":
                                            l.setFechaDef(fd)
                                            print("Se registró la defunción del cliente")
                                            break
                                        else:
                                            print("La fecha de defuncion no puede estar vacía")
                                    break
                                else:
                                    print(t.yaDifunto)
                                    break

                    elif ac == "4":
                        while True:
                            print(t.crearContrasena)
                            a = input()
                            if a is not "":
                                m.setContrasena(a)
                                print(t.textNuevaContraseña + a)
                                break
                            else:
                                print("La contraseña no puede estar vacía ")
                    
                    elif ac == "5":
                        print(t.total + str(len(Cliente.clientes_totales)) + t.clientes)
                        for c in Cliente.clientes_totales:
                            c.imprimirDatosCliente()
                            c.imprimirDatosLapida()

                    elif ac == "6":
                        print(t.total + str(len(Moderador.moderadores_totales)) + t.mods)
                        for m in Moderador.moderadores_totales:
                            m.imprimirDatosModerador()

                    elif ac == "7":
                        visitantes = len(Persona.personas_totales) - len(Cliente.clientes_totales) - len(Moderador.moderadores_totales)
                        print(t.total + str(visitantes) + t.visit)
                        for v in Persona.personas_totales:
                            if v.getDocumento() in Moderador.documentos_moderadores or v.getDocumento() in Cliente.documentos_clientes:
                                pass
                            else:
                                v.imprimirDatosPersona()

                    elif ac == "8":
                        break

                    elif ac == "9":
                        print("Las ubicaciones ocupadas son : ")
                        for u in Ubicacion.indices_usados:
                            print(u)

                    elif ac == "10":
                        sys.exit()
                        pass

                    else:
                        print(t.datoInvalido)
                break

            else:
                print(t.contrasenaIncorrecta)

    def accionesCliente(t,c):
        from Cliente import Cliente
        from Moderador import Moderador
        from Ubicacion import Ubicacion
        while True:
            print(t.ingresoContrasena)
            contra = input()
            if c.getContrasenaCliente() == contra:
                c.imprimirDatosCliente()
                lapida = c.getLapida()
                lapida.leerLapida()
                while True:
                    ac = input("Ingrese el número de la acción a realizar 1.Cambiar epitafio 2.Cambiar ubicación 3.Cambiar contraseña 4.Ingresar Memoria 5.Leer Lapida 6.Eliminar memoria de mi lapida 7.Cambiar privacidad 8.Ingresar con un perfil distinto 9. Salir")
                    if ac == "1":
                        epitafio = input("Ingrese el nuevo epitafio ")
                        lapida.setEpitafio(epitafio)
                        print("Su epitafio es " + epitafio)
                    elif ac == "2":
                        while True:
                            ubicacion = input("Ingrese su nueva ubicación")
                            if ubicacion.isdigit():
                                while True:
                                    if int(ubicacion) <= 50 and not 0:
                                        if Ubicacion.revisarDisponibilidadUbicacion(ubicacion):
                                            ubi = Ubicacion(ubicacion)
                                            lapida.setUbicacion(ubi)
                                            print("Su nueva ubicación es en " + ubicacion)
                                            break                                                 
                                        else:
                                            print("Esta ubicación no está disponible")
                                    else:
                                        print("Debe ingresar un numero entre 1 y 50")
                                        break
                                break
                            else:
                                print("Por favor ingrese un numero")
                    elif ac == "3":
                        print(t.crearContrasena)
                        a = input()
                        c.setContrasena(a)
                        print(t.textNuevaContraseña + a)
                    elif ac == "4":
                        Persona.escribirMemoria(t,c)
                    elif ac == "5":
                        Persona.verLapida(t)
                    elif ac == "6":
                        Persona.borrarMemoria(t,c)
                    elif ac == "7":
                        if lapida.getPrivacidad():
                            lapida.setPrivacidad(False)
                            print("Ahora su lapida es publica")
                        else:
                            lapida.setPrivacidad(True)
                            print("Ahora su lapida es privada")
                    elif ac == "8":
                        break
                    elif ac == "9":
                        sys.exit()
                    else:
                        print("Ingrese un numero valido por favor")
                break
            else:
                print("La contraseña es incorrecta")



if __name__ == '__main__':
    import sys
    from Moderador import Moderador
    from Cliente import Cliente
    from Persona import Persona
    from Lapida import Lapida
    from Ubicacion import Ubicacion
    from Memoria import Memoria
    from Textos import Texto
    
    m1 = Moderador("David","1090514247","23/02/1999","789")
    m3 = Moderador("Mario Aguilera","1010215392","13/06/1994","666")
    u1 = Ubicacion("1")
    l1 = Lapida(m1,False,u1)
    m2 = Moderador("Marcos","1090514246","23/02/1998","123")
    c1 = Cliente("David","1090514247","23/02/1999","456",l1)

    Texto.presentacion()
    while True:
        _idiom=input("Su Selección / Your Selection: ")
        if _idiom=="1":
            t=Texto(_idiom)
            break
        elif _idiom=="2":
            t=Texto(_idiom)
            break
        else:
            print(""+"\n"+"El dato ingresado es inválido. / The entered data is invalid."+"\n"+"")

    while True:
        print(t.introDoc)
        d = input() 
        if d.isdigit():
            m = Moderador.buscarModerador(d)
            c = Cliente.buscarCliente(d)
            if m is None and c is None:
                print(t.noRegistra)
                while True:
                    print (t.seleccionUno)
                    e = input()
                    if e == "1":  
                        while True:
                            print(t.entradaNombre)
                            nombre = input()
                            if nombre is not "":
                                while True:
                                    print(t.entradaFechaNac)
                                    fechaNac = input()
                                    if fechaNac is not "":
                                        v = Persona(nombre,d,fechaNac)
                                        v.imprimirDatosPersona(t)
                                        while True:
                                            print(t.selecOpcion)
                                            ac = input()
                                            if ac == "1":
                                                if Cliente.comprobarDocumentoCliente(d) is None:
                                                    print("///////////////////////////////////////////CREACION DE LAPIDA///////////////////////////////////////////") #Dejo este print porque me parece que hace el texto más legible.
                                                    print(t.ingresoEpitafio)
                                                    ep = input()
                                                    while True:
                                                        print(t.crearContrasena)
                                                        contra = input()
                                                        if contra is not "":
                                                            while True:
                                                                print(t.ingresoUbicacion)
                                                                u = input()
                                                                if u.isdigit():
                                                                    while True:
                                                                        if int(u) <= 50 and not 0:
                                                                            if Ubicacion.revisarDisponibilidadUbicacion(u):
                                                                                ub = Ubicacion(u)
                                                                                while True:
                                                                                    print(t.selecPrivacidad)
                                                                                    p = input()
                                                                                    if p == "0":
                                                                                        print("--------------------------------------------------------------------------------------------------------")
                                                                                        la = Lapida(v,True,ub,ep)
                                                                                        cl = Cliente(nombre,d,fechaNac,contra,la)
                                                                                        Lapida.leerLapida(la)
                                                                                        break
                                                                                    if p == "1":
                                                                                        print("--------------------------------------------------------------------------------------------------------")
                                                                                        la = Lapida(v,False,ub,ep)
                                                                                        cl = Cliente(nombre,d,fechaNac,contra,la)
                                                                                        Lapida.leerLapida(la)
                                                                                        break
                                                                                    print(t.datoInvalido)
                                                                                break
                                                                            
                                                                            else:
                                                                                print(t.lapidaOcupada)                                                   
                                                                            break
                                                                        else:
                                                                            print("Debe ingresar un numero entre 1 y 50. Por esto no se pudo completar la creación de lapida") 
                                                                            break
                                                                    break
                                                                else:
                                                                    print(t.noNumerico)
                                                            break
                                                        else:
                                                            print(t.contrasenaInvalida)
                                                else:
                                                    print(t.lapidaAntesCreada)
                                            elif ac == "2":
                                                Persona.escribirMemoria(t,v)

                                            elif ac == "3":
                                                Persona.verLapida(t)

                                            elif ac == "4":
                                                e = "0"
                                                break

                                            elif ac == "5":
                                                print(t.exit)
                                                sys.exit()

                                            else:
                                                print(t.datoInvalido)
                                        break
                                    else:
                                        print("Fecha de nacimiento no puede estar vacía")
                                break
                            else:
                                print("Nombre no puede estar vacio ")

                    if e == "0":
                        break

                    else:
                        print(t.datoInvalido)
            elif m is not None and c is not None:
                while True:
                    print(t.modOrClient)
                    e = input()
                    if e == "1":
                        Persona.accionesModerador(t,m)
                    elif e == "2":
                        Persona.accionesCliente(t,c)
                    elif e == "3":
                        break
                    else:
                        print(t.datoInvalido)
            elif m is not None and c is None:
                Persona.accionesModerador(t,m)
            elif m is None and c is not None:
                Persona.accionesCliente(t,c)             
        else:
            print(t.noNumerico)





