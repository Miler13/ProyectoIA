import os
class ColaPrioridad:
    def __init__(self):
        self.cola = []

    def pushInsercion(self, elem):
        if len(self.cola) == 0:
            self.cola.append(elem)
        else:
            val = len(self.cola)-1
            flag = True;
            while val >= 0 and flag:
                nodo = self.cola[val]
                if nodo.fHCantidadDeMantariasRestantes > elem.fHCantidadDeMantariasRestantes:
                    val -= 1
                else:
                    self.cola.insert(val+1, elem)
                    flag = False

            if(val==-1 and flag):
                self.cola.insert(0, elem)

    def returnCola(self):
        return self.cola

    def popCola(self):
        if(len(self.cola)>=0):
            a = self.cola[0]
            del self.cola[0]
            return a
    def estaVacia(self):
        if len(self.cola) == 0:
            return True
        else:
            return False

class ColaPrioridadNivel:
    def __init__(self):
        self.cola = []

    def pushInsercion(self, elem):
        if len(self.cola) == 0:
            self.cola.append(elem)
        else:
            val = len(self.cola)-1
            flag = True;
            while val >= 0 and flag:
                nodo = self.cola[val]
                if nodo.nivel > elem.nivel:
                    val -= 1
                else:
                    self.cola.insert(val+1, elem)
                    flag = False

            if(val==-1 and flag):
                self.cola.insert(0, elem)

    def returnCola(self):
        return self.cola

    def popCola(self):
        if(len(self.cola)>=0):
            a = self.cola[0]
            del self.cola[0]
            return a
    def estaVacia(self):
        if len(self.cola) == 0:
            return True
        else:
            return False

class Materia:
    def __init__(self, nombreMateria, fHCantidadDeMantariasRestantes, nivel, nombrePadre=None):
        self.nombreMateria = nombreMateria
        self.fHCantidadDeMantariasRestantes = fHCantidadDeMantariasRestantes
        self.ListaNodosHijos = []
        self.nombrePadre = nombrePadre
        self.nivel = nivel

    def agregarNodo(self, Objeto):
        if self.nombreMateria == Objeto.nombrePadre:
            self.ListaNodosHijos.append(Objeto)
        else:
            self.verificarLista(self.ListaNodosHijos, Objeto, True)

    def verificarLista(self, listaNodos, Objeto, bandera):
        val=len(listaNodos)
        if len(listaNodos)> 0 and bandera:
            indice = 0
            while indice < len(listaNodos):
                arbol = listaNodos[indice]
                indice += 1
                if arbol.nombreMateria == Objeto.nombrePadre:
                    arbol.ListaNodosHijos.append(Objeto)
                    bandera = False
                    return bandera
            i = 0
            while i < len(listaNodos) and bandera:
                arbolNodo = listaNodos[i]
                bandera = self.verificarLista(arbolNodo.ListaNodosHijos, Objeto, bandera);
                i+=1
                if bandera== False:
                    return bandera
        return bandera

listaPrioridadNivel=ColaPrioridadNivel()

def busquedaAvara(x,y,colaDePrioridad):
    i=0
    VALOR=len(x.ListaNodosHijos)
    while i<len(x.ListaNodosHijos):
        obj=x.ListaNodosHijos[i]
        colaDePrioridad.pushInsercion(obj)
        i+=1
    if(not colaDePrioridad.estaVacia()):
        elemento=colaDePrioridad.popCola()
        listaPrioridadNivel.pushInsercion(elemento)
        y+="\n"+elemento.nombreMateria
        if(elemento.fHCantidadDeMantariasRestantes)==0:
            return y
        else:
            y=busquedaAvara(elemento,y,colaDePrioridad)
            return y
    else:
        return "No existe ruta posible"

def menu():
    os.system('cls')  # NOTA para windows tienes que cambiar clear por cls
    print(" Selecciona una especialidad en informatica")
    print("\t1 - Inteligencia Artificial")
    print("\t2 - Redes")
    print("\t3 - Teoria de computacion")
    print("\t4 - Base de datos")
    print("\t5 - Desarrollo e ingenieria de Software")
    print("\t9 - salir")


while True:
    # Mostramos el menu
    menu()
    # solicituamos una opción al usuario
    opcionMenu = input("inserta un numero valor >> ")
    if opcionMenu == "1":
        # elemento raiz
        raiz = Materia("Ingenieria Informatica", 25, 0)
        materiaB1 = Materia("Algebra I", 7, 1, "Ingenieria Informatica")
        # Demas materias del semestre 1 semestre
        materiaA1 = Materia("Introduccion a la programacion", 24, 1, "Ingenieria Informatica")
        materiaC1 = Materia("Calculo I", 24, 1, "Ingenieria Informatica")
        materiaD1 = Materia("Ingles I", 24, 1, "Ingenieria Informatica")
        materiaE1 = Materia("Fisica", 24, 1, "Ingenieria Informatica")
        #

        materiaC2 = Materia("Algebra II", 6, 2, "Algebra I")
        # Demas materias del semestre 2 semestre
        materiaA2 = Materia("Elementos de programacion y Estructura de datos", 9, 2, "Introduccion a la programacion")
        materiaB2 = Materia("Programacion", 29, 2, "Introduccion a la programacion")
        materiaD2 = Materia("Calculo II", 29, 2, "Calculo I")
        materiaE2 = Materia("Ingles II", 29, 2, "Ingles I")
        materiaF2 = Materia("Arquitectura por computadoras I", 29, 2, "Fisica")
        #

        materiaC3 = Materia("Logica", 5, 3, "Algebra II")
        # Demas materias del semestre 3 semestre
        materiaA3 = Materia("Metodos y tecnicas de programacion", 30, 3,
                            "Elementos de programacion y Estructura de datos")
        materiaB3 = Materia("Teoria de grafos", 30, 3, "Programacion")
        materiaD3 = Materia("Calculo Numerico", 30, 3, "Calculo II")
        materiaE3 = Materia("Organizacion y metodos", 30, 3, "Ingles II")
        materiaF3 = Materia("Arquitectura por computadoras II", 30, 3, "Arquitectura por computadoras I")
        #

        materiaC4 = Materia("Programacion Funcional", 4, 4, "Logica")
        # Demas materias del semestre 4 semestre
        materiaA4 = Materia("Sistemas de Informacion I", 18, 4, "Metodos y tecnicas de programacion")
        materiaB4 = Materia("Algoritmos Avanzados", 18, 4, "Teoria de grafos")
        materiaC4 = Materia("Programacion Funcional", 18, 4, "Logica")
        materiaD4 = Materia("Probabilidad y estadistica", 18, 4, "Calculo Numerico")
        materiaE4 = Materia("Taller de programacion de bajo nivel", 18, 4, "Arquitectura por computadoras II")
        materiaF4 = Materia("Base de Datos", 18, 4, "Organizacion y metodos")
        #

        materiaC5 = Materia("Inteligencia Artificial I", 3, 5, "Programacion Funcional")
        # Demas materias del semestre 4 semestre
        materiaA5 = Materia("Sistemas de Informacion II", 19, 5, "Sistemas de Informacion I")
        materiaB5 = Materia("Graficacion por computacion", 19, 5, "Algoritmos Avanzados")
        materiaD5 = Materia("Taller de Sistemas operativo", 19, 5, "Taller de programacion de bajo nivel")
        materiaE5 = Materia("Teoria de automatas y lenguajes formales", 19, 5, "Taller de programacion de bajo nivel")
        materiaF5 = Materia("Base de Datos II", 19, 5, "Base de Datos")
        #
        materiaC6 = Materia("Inteligencia Artificial II", 2, 6, "Inteligencia Artificial I")
        # Demas materias del semestre 4 semestre
        materiaA6 = Materia("Ingenieria de Software", 19, 6, "Sistemas de Informacion II")
        materiaB6 = Materia("Programacion web", 19, 6, "Graficacion por computacion")
        materiaD6 = Materia("Redes de computadoras", 19, 6, "Taller de Sistemas operativo")
        materiaE6 = Materia("Estructura y semantica de lenguajes de programacion", 19, 6,
                            "Teoria de automatas y lenguajes formales")
        materiaF6 = Materia("Taller de base de Datos", 19, 6, "Base de Datos II")
        #

        materiaC7 = Materia("Interacion Humano computador", 1, 7, "Inteligencia Artificial II")
        # Demas materias del semestre 4 semestre
        materiaA7 = Materia("Taller de Ingeniera de software", 20, 7, "Ingenieria de Software")
        materiaB7 = Materia("Arquitectura de software", 20, 7, "Programacion web")
        materiaD7 = Materia("Tecnologia y redes avanzadas", 20, 7, "Redes de computadoras")
        materiaE7 = Materia("Electiva Teoria de computacion", 20, 7,
                            "Estructura y semantica de lenguajes de programacion")
        materiaF7 = Materia("Electiva base de Datos", 20, 7, "Taller de base de Datos")
        #
        materiaC8 = Materia("Electiva Inteligencia Artificial", 0, 8, "Interacion Humano computador")
        # Demas materias del semestre 8 semestre
        materiaA8 = Materia("Taller de grado", 21, 8, "Taller de Ingeniera de software")
        materiaB8 = Materia("Evaluacion y auditoria de sistemas", 21, 8, "Arquitectura de software")
        materiaD8 = Materia("Electiva de redes", 21, 8, "Tecnologia y redes avanzadas")
        materiaE8 = Materia("Electiva Teoria de computacion II", 21, 8, "Electiva Teoria de computacion")
        materiaF8 = Materia("Electiva base de Datos II", 21, 8, "Electiva base de Datos")
        #
        materiaA9 = Materia("Modalidad de titulacion", 21, 9, "Taller de grado")

        raiz.agregarNodo(materiaB1)
        raiz.agregarNodo(materiaA1)
        # Agregar  las demas ameteria
        raiz.agregarNodo(materiaC1)
        raiz.agregarNodo(materiaD1)
        raiz.agregarNodo(materiaE1)

        raiz.agregarNodo(materiaC2)
        raiz.agregarNodo(materiaA2)
        raiz.agregarNodo(materiaB2)
        # Agregar  las demas ameteria
        raiz.agregarNodo(materiaD2)
        raiz.agregarNodo(materiaE2)
        raiz.agregarNodo(materiaF2)

        raiz.agregarNodo(materiaC3)
        raiz.agregarNodo(materiaA3)
        raiz.agregarNodo(materiaB3)
        # Agregar  las demas ameteria
        raiz.agregarNodo(materiaD3)
        raiz.agregarNodo(materiaE3)
        raiz.agregarNodo(materiaF3)

        raiz.agregarNodo(materiaC4)
        raiz.agregarNodo(materiaA4)
        raiz.agregarNodo(materiaB4)
        # Agregar  las demas ameteria
        raiz.agregarNodo(materiaD4)
        raiz.agregarNodo(materiaE4)
        raiz.agregarNodo(materiaF4)

        raiz.agregarNodo(materiaC5)
        raiz.agregarNodo(materiaA5)
        raiz.agregarNodo(materiaB5)
        # Agregar  las demas ameteria
        raiz.agregarNodo(materiaD5)
        raiz.agregarNodo(materiaE5)
        raiz.agregarNodo(materiaF5)

        raiz.agregarNodo(materiaC6)
        raiz.agregarNodo(materiaA6)
        raiz.agregarNodo(materiaB6)
        # Agregar  las demas ameteria
        raiz.agregarNodo(materiaD6)
        raiz.agregarNodo(materiaE6)
        raiz.agregarNodo(materiaF6)

        raiz.agregarNodo(materiaC7)
        raiz.agregarNodo(materiaA7)
        raiz.agregarNodo(materiaB7)
        # Agregar  las demas ameteria
        raiz.agregarNodo(materiaD7)
        raiz.agregarNodo(materiaE7)
        raiz.agregarNodo(materiaF7)

        raiz.agregarNodo(materiaC8)
        raiz.agregarNodo(materiaA8)
        raiz.agregarNodo(materiaB8)
        # Agregar  las demas ameteria
        raiz.agregarNodo(materiaD8)
        raiz.agregarNodo(materiaE8)
        raiz.agregarNodo(materiaF8)

        raiz.agregarNodo(materiaA9)

        colaDePrioridad = ColaPrioridad()
        camino = "Ingenieria Informatica"
        camino += busquedaAvara(raiz, "", colaDePrioridad)
        j = 0
        x = listaPrioridadNivel.popCola()
        semestreX = "Semestre " + str(x.nivel)
        print(semestreX)
        print(x.nombreMateria)
        while j < len(listaPrioridadNivel.cola):
            y = listaPrioridadNivel.popCola()
            semestreY = "Semestre " + str(y.nivel)
            if not semestreX == semestreY:
                print(semestreY)
                semestreX = semestreY
            print(y.nombreMateria)
        #==================================================================
        #print("")
        #print(camino)
        input("pulsa una tecla para continuar")

    elif opcionMenu == "2":
        print("")
        input("Has pulsado la opción 2...\npulsa una tecla para continuar")
    elif opcionMenu == "3":
        print("")
        input("Has pulsado la opción 3...\npulsa una tecla para continuar")
    elif opcionMenu == "4":
        print("")
        input("Has pulsado la opción 4...\npulsa una tecla para continuar")
    elif opcionMenu == "5":
        # elemento raiz
        raiz = Materia("Ingenieria Informatica", 49, 0)
        # Desarrolo de software
        materiaA1 = Materia("Introduccion a la programacion", 15, 1, "Ingenieria Informatica")
        # Demas materias del semestre 1 semestre
        materiaB1 = Materia("Algebra I", 16, 1, "Ingenieria Informatica")
        materiaC1 = Materia("Calculo I", 16, 1, "Ingenieria Informatica")
        materiaD1 = Materia("Ingles I", 16, 1, "Ingenieria Informatica")
        materiaE1 = Materia("Fisica", 16, 1, "Ingenieria Informatica")
        #

        materiaA2 = Materia("Elementos de programacion y Estructura de datos", 14, 2, "Introduccion a la programacion")
        materiaB2 = Materia("Programacion", 13, 2, "Introduccion a la programacion")
        # Demas materias del semestre 2 semestre
        materiaC2 = Materia("Algebra II", 17, 2, "Algebra I")
        materiaD2 = Materia("Calculo II", 17, 2, "Calculo I")
        materiaE2 = Materia("Ingles II", 17, 2, "Ingles I")
        materiaF2 = Materia("Arquitectura por computadoras I", 16, 2, "Fisica")
        #

        materiaA3 = Materia("Metodos y tecnicas de programacion", 12, 3,
                            "Elementos de programacion y Estructura de datos")
        materiaB3 = Materia("Teoria de grafos", 11, 3, "Programacion")
        # Demas materias del semestre 3 semestre
        materiaC3 = Materia("Logica", 18, 3, "Algebra II")
        materiaD3 = Materia("Calculo Numerico", 18, 3, "Calculo II")
        materiaE3 = Materia("Organizacion y metodos", 18, 3, "Ingles II")
        materiaF3 = Materia("Arquitectura por computadoras II", 18, 3, "Arquitectura por computadoras I")
        #

        materiaA4 = Materia("Sistemas de Informacion I", 10, 4, "Metodos y tecnicas de programacion")
        materiaB4 = Materia("Algoritmos Avanzados", 9, 4, "Teoria de grafos")
        # Demas materias del semestre 4 semestre
        materiaC4 = Materia("Programacion Funcional", 19, 4, "Logica")
        materiaD4 = Materia("Probabilidad y estadistica", 19, 4, "Calculo Numerico")
        materiaE4 = Materia("Taller de programacion de bajo nivel", 19, 4, "Arquitectura por computadoras II")
        materiaF4 = Materia("Base de Datos", 19, 4, "Organizacion y metodos")
        #

        materiaA5 = Materia("Sistemas de Informacion II", 8, 5, "Sistemas de Informacion I")
        materiaB5 = Materia("Graficacion por computacion", 7, 5, "Algoritmos Avanzados")
        # Demas materias del semestre 5 semestre
        materiaC5 = Materia("Inteligencia Artificial I", 20, 5, "Programacion Funcional")
        materiaD5 = Materia("Taller de Sistemas operativo", 20, 5, "Taller de programacion de bajo nivel")
        materiaE5 = Materia("Teoria de automatas y lenguajes formales", 20, 5, "Taller de programacion de bajo nivel")
        materiaF5 = Materia("Base de Datos II", 20, 5, "Base de Datos")
        #

        materiaA6 = Materia("Ingenieria de Software", 6, 6, "Sistemas de Informacion II")
        materiaB6 = Materia("Programacion web", 5, 6, "Graficacion por computacion")
        # Demas materias del semestre 6 semestre
        materiaC6 = Materia("Inteligencia Artificial II", 21, 6, "Inteligencia Artificial I")
        materiaD6 = Materia("Redes de computadoras", 21, 6, "Taller de Sistemas operativo")
        materiaE6 = Materia("Estructura y semantica de lenguajes de programacion", 21, 6,
                            "Teoria de automatas y lenguajes formales")
        materiaF6 = Materia("Taller de base de Datos", 21, 6, "Base de Datos II")
        #

        materiaA7 = Materia("Taller de Ingeniera de software", 4, 7, "Ingenieria de Software")
        materiaB7 = Materia("Arquitectura de software", 3, 7, "Programacion web")
        # Demas materias del semestre 4 semestre
        materiaC7 = Materia("Interacion Humano computador", 22, 7, "Inteligencia Artificial II")
        materiaD7 = Materia("Tecnologia y redes avanzadas", 22, 7, "Redes de computadoras")
        materiaE7 = Materia("Electiva Teoria de computacion", 22, 7,
                            "Estructura y semantica de lenguajes de programacion")
        materiaF7 = Materia("Electiva base de Datos", 22, 7, "Taller de base de Datos")
        #
        materiaA8 = Materia("Taller de grado", 2, 8, "Taller de Ingeniera de software")
        materiaB8 = Materia("Evaluacion y auditoria de sistemas", 1, 8, "Arquitectura de software")
        # Demas materias del semestre 4 semestre
        materiaC8 = Materia("Electiva Inteligenci Artificial", 23, 8, "Interacion Humano computador")
        materiaD8 = Materia("Electiva de redes", 23, 8, "Tecnologia y redes avanzadas")
        materiaE8 = Materia("Electiva Teoria de computacion II", 23, 8, "Electiva Teoria de computacion")
        materiaF8 = Materia("Electiva base de Datos II", 23, 8, "Electiva base de Datos")
        #
        materiaA9 = Materia("Modalidad de titulacion", 0, 9, "Taller de grado")

        raiz.agregarNodo(materiaA1)
        # Agregar  las demas ameteria
        raiz.agregarNodo(materiaB1)
        raiz.agregarNodo(materiaC1)
        raiz.agregarNodo(materiaD1)
        raiz.agregarNodo(materiaE1)

        raiz.agregarNodo(materiaA2)
        raiz.agregarNodo(materiaB2)
        # Agregar  las demas ameteria
        raiz.agregarNodo(materiaC2)
        raiz.agregarNodo(materiaD2)
        raiz.agregarNodo(materiaE2)
        raiz.agregarNodo(materiaF2)

        raiz.agregarNodo(materiaA3)
        raiz.agregarNodo(materiaB3)
        # Agregar  las demas ameteria
        raiz.agregarNodo(materiaC3)
        raiz.agregarNodo(materiaD3)
        raiz.agregarNodo(materiaE3)
        raiz.agregarNodo(materiaF3)

        raiz.agregarNodo(materiaA4)
        raiz.agregarNodo(materiaB4)
        # Agregar  las demas ameteria
        raiz.agregarNodo(materiaC4)
        raiz.agregarNodo(materiaD4)
        raiz.agregarNodo(materiaE4)
        raiz.agregarNodo(materiaF4)

        raiz.agregarNodo(materiaA5)
        raiz.agregarNodo(materiaB5)
        # Agregar  las demas ameteria
        raiz.agregarNodo(materiaC5)
        raiz.agregarNodo(materiaD5)
        raiz.agregarNodo(materiaE5)
        raiz.agregarNodo(materiaF5)

        raiz.agregarNodo(materiaA6)
        raiz.agregarNodo(materiaB6)
        # Agregar  las demas ameteria
        raiz.agregarNodo(materiaC6)
        raiz.agregarNodo(materiaD6)
        raiz.agregarNodo(materiaE6)
        raiz.agregarNodo(materiaF6)

        raiz.agregarNodo(materiaA7)
        raiz.agregarNodo(materiaB7)
        # Agregar  las demas ameteria
        raiz.agregarNodo(materiaC7)
        raiz.agregarNodo(materiaD7)
        raiz.agregarNodo(materiaE7)
        raiz.agregarNodo(materiaF7)

        raiz.agregarNodo(materiaA8)
        raiz.agregarNodo(materiaB8)
        # Agregar  las demas ameteria
        raiz.agregarNodo(materiaC8)
        raiz.agregarNodo(materiaD8)
        raiz.agregarNodo(materiaE8)
        raiz.agregarNodo(materiaF8)

        raiz.agregarNodo(materiaA9)

        colaDePrioridad = ColaPrioridad()
        camino = "Ingenieria Informatica"
        camino += busquedaAvara(raiz, "", colaDePrioridad)

        j=0
        x = listaPrioridadNivel.popCola()
        semestreX="Semestre " + str(x.nivel)
        print(semestreX)
        print(x.nombreMateria)
        while j<len(listaPrioridadNivel.cola):
            y=listaPrioridadNivel.popCola()
            semestreY="Semestre " + str(y.nivel)
            if  not semestreX==semestreY:
                print(semestreY)
                semestreX=semestreY
            print(y.nombreMateria)

        #print("Por niveles")
        #print(camino)

        print("")
        input("Has pulsado la opción 5...\npulsa una tecla para continuar")
    elif opcionMenu == "9":
        break
    else:
        print("")
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")



