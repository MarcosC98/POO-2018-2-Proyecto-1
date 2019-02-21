class Persona:
    personas_totales = []

    def __init__(self,nombre,documento,fechaNac):
        self._nombre = nombre
        self._documento = documento
        self._fechaNac = fechaNac
        Persona.personas_totales.append(self)

    def imprimirDatosPersona(self):
        print("--------------------------------------------------------------------------------------------")
        print("TIPO DE PERFIL: VISITANTE")
        print("Nombre: " + self._nombre)
        print("Documento: " + self._documento)
        print("Fecha de Nacimiento: " + self._fechaNac)
        print("----------------------------------------------------------------------------------------------")

    def getNombre(self):
        return self._nombre

    def getDocumento(self):
        return self._documento

    def getFechaNac(self):
        return self._fechaNac

    def verLapida():
        from Lapida import Lapida
        while True:
            l = Lapida.buscarLapida(input("Ingrese el documento de la persona propietaria de la lapida que desea leer "))
            if l is not None:
                l.leerLapida()
                break
            else:
                print("No hay ninguna persona con ese documento que tenga una lapida")


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
                        print(t.entradaNombre)
                        nombre = input() #//CONTROL PARA QUE SOLO INGRESEN LETRAS 
                        print(t.entradaFechaNac)
                        fechaNac = input() #//CONTROL PARA QUE INGRESEN UNA FECHA VALIDA
                        v = Persona(nombre,d,fechaNac)
                        v.imprimirDatosPersona()
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
                                                u = input()#//CONTROL PARA QUE SOLO INGRESEN NUMEROS
                                                if u.isdigit():
                                                    if u is not "":
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
                                                        print(t.ubicacionInvalida)
                                                    break
                                                else:
                                                    print(t.noNumerico)
                                            break
                                        else:
                                            print(t.contrasenaInvalida)
                                else:
                                    print(t.lapidaAntesCreada)
                            elif ac == "2":
                                print(""+"\n"+"///////////////////////////////////////////CREACION DE MEMORIA///////////////////////////////////////////"+"\n"+"") #Nuevamente los dejo porque me parece que son puntos de referencia en el código.
                                while True:
                                    print(t.propietarioLap)
                                    l = Lapida.buscarLapida(input())
                                    if l is not None:
                                        if l.getPrivacidad():
                                            print(t.lapidaPrivada)
                                            break
                                        else:
                                            while True:
                                                print(t.lapidaPrivada)
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

                            elif ac == "3":
                                Persona.verLapida()

                            elif ac == "4":
                                e = "0"
                                break

                            elif ac == "5":
                                print(t.exit)
                                sys.exit()

                            else:
                                print(t.datoInvalido)

                    if e == "0":
                        break

                    else:
                        print(t.datoInvalido)

            else:
                if m is not None and c is not None:
                    while True:
                        print(t.modOrClient)
                        e = input()
                        if e == "1":
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
                                                        print(t.nombreModerador)
                                                        nombre = input()  
                                                        print(t.fnModerador)                           
                                                        fechaNac = input()
                                                        print(t.contrasenaModerador)
                                                        contrasena = input()
                                                        mod = Moderador(nombre,documento,fechaNac,contrasena)
                                                        print("-------------------------------------NUEVO MODERADOR CREADO-------------------------------------")
                                                        Moderador.imprimirDatosModerador(mod)
                                                        break
                                                    else:
                                                        print(t.existeMod)
                                                else:
                                                    print(t.noNumerico)

                                        elif ac == "2":
                                            while True:
                                                a = input("Ingrese el documento de la persona la cual posee la lapida donde está la memoria que desea eliminar ")
                                                c = Cliente.buscarCliente(a)
                                                if c is None:
                                                    print("No hay ninguna persona con ese documento que posea una lapida")
                                                else:
                                                    l = c.getLapida()
                                                    if l.getPrivacidad():
                                                        print("Esta lapida es privada, no tiene ninguna memoria")
                                                        break
                                                    else:
                                                        if len(l.memorias) == 0:
                                                            print("Esta lapida no tiene ninguna memoria")
                                                            break
                                                        else:
                                                            l.imprimirMemorias()
                                                            while True:
                                                                i = input("Ingrese el numero de la memoria que desea eliminar ")#FALLA SI INPUT ES VACÍO
                                                                if len(l.memorias) >= int(i):
                                                                    l.borrarMemoria(i) #CONTROL PARA QUE ALGUIEN NO PONGA LETRAS O NÚMEROS INVALIDOS
                                                                    break
                                                                else:
                                                                    print("No existe una memoria en la posición " + i)
                                                            break
                                        elif ac == "3":
                                            while True:
                                                a = input("Ingrese el documento de el cliente que ha fallecido ")
                                                c = Cliente.buscarCliente(a)
                                                if c is None:
                                                    print("No hay ninguna persona con ese documento que posea una lapida")
                                                else:
                                                    l = c.getLapida()
                                                    if l.getFechaDef() is "":
                                                        fd = input("Ingrese la fecha de defunción de el cliente en formado dd/mm/aaaa ")
                                                        l.setFechaDef(fd)
                                                        break
                                                    else:
                                                        print("Este cliente ya tiene una fecha de defunción registrada ")
                                                        break

                                        elif ac == "4":
                                            print(t.crearContrasena)
                                            a = input()
                                            m.setContrasena(a)
                                            print("Su nueva contraseña es: " + a)
                                        
                                        elif ac == "5":
                                            print("En total hay " + str(len(Cliente.clientes_totales)) + " clientes")
                                            for c in Cliente.clientes_totales:
                                                c.imprimirDatosCliente()
                                                c.imprimirDatosLapida()

                                        elif ac == "6":
                                            print("En total hay " + str(len(Moderador.moderadores_totales)) + " moderadores")
                                            for m in Moderador.moderadores_totales:
                                                m.imprimirDatosModerador()

                                        elif ac == "7":
                                            visitantes = len(Persona.personas_totales) - len(Cliente.clientes_totales) - len(Moderador.moderadores_totales)
                                            print("En total hay " + str(visitantes) + " visitantes")
                                            for v in Persona.personas_totales:
                                                if v.getDocumento() in Moderador.documentos_moderadores or v.getDocumento() in Cliente.documentos_clientes:
                                                    pass
                                                else:
                                                    v.imprimirDatosPersona()

                                        elif ac == "8":
                                            e = "3"
                                            break

                                        elif ac == "9":
                                            sys.exit()
                                            pass

                                        else:
                                            print("Ingrese un numero valido por favor ")
                                    break

                                else:
                                    print("La contraseña es incorrecta")

                        elif e == "2":
                            #CLIENTE
                            pass

                        elif e == "3":
                            break
                        else:
                            print(t.datoInvalido)
        else:
            print("Por favor ingrese un número ")







"""
        else: 
            if m is not None and c is not None:
                perfil = input("¿Desea ingresar como moderador o como cliente? 1.Moderador 2.Cliente ")
                contra = input("Ingrese contraseña para este perfil: ")
                if perfil == "1":
                    if contra == m.getContrasenaModerador():
                        m.imprimirDatosModerador()
                        break
                if perfil == "2":
                    if contra == c.getContrasenaCliente():
                        c.imprimirDatosCliente()
                        break
            elif m is not None:
                contra = input("Ingrese contraseña para este perfi: ")
                if contra == m.getContrasenaModerador():
                    m.imprimirDatosModerador()
                    break
            else:
                contra = input("Ingrese contraseña para este perfil: ")
                if contra == c.getContrasenaCliente():
                    c.imprimirDatosCliente()
                    break
"""