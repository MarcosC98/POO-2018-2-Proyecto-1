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

    while True:
        d = input("Ingrese su numero de documento por favor: ") 
        if d.isdigit():
            m = Moderador.buscarModerador(d)
            c = Cliente.buscarCliente(d)
            if m is None and c is None:
                print("No hay ninguna cuenta registrada con ese documento.")
                while True:
                    e = input("Si desea intentar nuevamente con otro documento ingrese 0, si desea crear una cuenta nueva con este documento ingrese 1 ")
                    if e == "1":
                        nombre = input("Ingrese su nombre completo: ") #//CONTROL PARA QUE SOLO INGRESEN LETRAS 
                        fechaNac = input("Ingrese su fecha de nacimiento en formato dd/mm/aaaa: ") #//CONTROL PARA QUE INGRESEN UNA FECHA VALIDA
                        v = Persona(nombre,d,fechaNac)
                        v.imprimirDatosPersona()
                        while True:
                            ac = input("Ingrese el número de la acción a realizar: 1.Adquirir Lápida 2.Escribir Memoria 3.Leer Lápida 4.Ingresar con otro perfil 5.Salir ")
                            if ac == "1":
                                if Cliente.comprobarDocumentoCliente(d) is None:
                                    print("CREACION DE LAPIDA--------------------------------------------------------------------------------")
                                    ep = input("Ingrese el epitafio que desea en su lapida ")
                                    while True:
                                        contra = input("Ingrese la contraseña que usará en su cuenta ")
                                        if contra is not "":
                                            while True:
                                                u = input("Ingrese la úbicación de su lápida ")#//CONTROL PARA QUE SOLO INGRESEN NUMEROS
                                                if u.isdigit():
                                                    if u is not "":
                                                        if Ubicacion.revisarDisponibilidadUbicacion(u):
                                                            ub = Ubicacion(u)
                                                            while True:
                                                                p = input("Ingrese 0 si desea que su lápida sea privada, 1 si desea que sea pública ")
                                                                if p == "0":
                                                                    print("---------------------------------------------------------------------------------------------")
                                                                    la = Lapida(v,True,ub,ep)
                                                                    cl = Cliente(nombre,d,fechaNac,contra,la)
                                                                    Lapida.leerLapida(la)
                                                                    break
                                                                if p == "1":
                                                                    print("-------------------------------------------------------------------------------------------------------")
                                                                    la = Lapida(v,False,ub,ep)
                                                                    cl = Cliente(nombre,d,fechaNac,contra,la)
                                                                    Lapida.leerLapida(la)
                                                                    break
                                                                print("Ingrese una opción valida por favor")
                                                            break
                                                        
                                                        else:
                                                            print("Esta ubicación ya se encuentra ocupada, selecciona una distinta por favor")                                                   
                                                        break    
                                                    else:
                                                        print("Ingresa una ubicación valida ")
                                                    break
                                                else:
                                                    print("Ingrese un número por favor ")
                                            break
                                        else:
                                            print("Ingrese una contraseña válida ")
                                else:
                                    print("Ya tienes una lapida ")
                            elif ac == "2":
                                print("CREACION DE MEMORIA/////////////////////////////////////////////////////////////")
                                while True:
                                    l = Lapida.buscarLapida(input("Ingrese el documento de la persona propietaria de la lapida donde va a dejar la memoria "))
                                    if l is not None:
                                        if l.getPrivacidad():
                                            print("Esta lápida es privada. No puedes leer/escribir memorias.")
                                            break
                                        else:
                                            while True:
                                                de = input("Ingrese la descripcion de la memoria por favor ")
                                                if de is not "":
                                                    me = Memoria(v,de,l)
                                                    l.memorias.append(me)
                                                    me.imprimirDatosMemoria()
                                                    break
                                                else:
                                                    print("No puede haber una memoria sin descripcion")
                                            break
                                    else:
                                        print("No hay ninguna persona con ese documento que tenga una lapida")

                            elif ac == "3":
                                Persona.verLapida()

                            elif ac == "4":
                                e = "0"
                                break

                            elif ac == "5":
                                print("El programa ha finalizado ")
                                sys.exit()

                            else:
                                print("Ingrese un numero valido por favor")

                    if e == "0":
                        break

                    else:
                        print("Ingrese un numero valido por favor")

            else:
                if m is not None and c is not None:
                    while True:
                        e = input("Ingrese 1 para entrar a su perfil de moderador, 2 para su perfil de cliente, y 3 para ingresar con un documento distinto. ")
                        if e == "1":
                            while True:
                                c = input("Ingrese la contraseña de este perfil ")
                                if c == m.getContrasenaModerador():
                                    m.imprimirDatosModerador()
                                    while True:
                                        ac = input("Ingrese el número de la acción a realizar: 1.Registrar nuevo moderador 2.Borrar memoria 3.Registrar defunción de un cliente 4.Cambiar contraseña 5.Ver clientes totales 6.Ver moderadores totales 7.Ver visitantes totales 8.Ingresar con otro perfil 9.Salir  " )
                                        if ac == "1":
                                            while True:
                                                documento = input("Ingrese el documento de el nuevo moderador ")
                                                if documento.isdigit():
                                                    if Moderador.comprobarDocumentoModerador(documento) is None:
                                                        nombre = input("Ingrese el nombre completo de el nuevo moderador ")                             
                                                        fechaNac = input("Ingrese la fecha de nacimiento de el nuevo moderador en el formato dd/mm/aaaa ")
                                                        contrasena = input("Ingrese la contraseña de la cuenta de el nuevo moderador ")
                                                        mod = Moderador(nombre,documento,fechaNac,contrasena)
                                                        print("NUEVO MODERADOR CREADO:  ----------------------------------")
                                                        Moderador.imprimirDatosModerador(mod)
                                                        break
                                                    else:
                                                        print("Ya existe un moderador registrado con este documento")
                                                else:
                                                    print("Por favor ingrese un numero")

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
                                            a = input("Ingrese su nueva contraseña ")
                                            m.setContrasena(a)
                                            print("Su nueva contraseña es " + a)
                                        
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
                            print("Ingrese un numero valido por favor")
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