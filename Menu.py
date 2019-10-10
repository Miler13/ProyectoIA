
from consolemenu import *
from consolemenu.items import *

from _graph.GraphPro import GraphPro as g
from time import time
import os




def action(name):
    print("\nHello from action {}!!!\n".format(name))
    Screen().input('Press [Enter] to continue')
def mostrar(a):
    os.system('clear')
    print("<--------Test Floyd-Warshall------->\n")

    weights = [0,1, 2, 3, 4, 5, 6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48]
    #graph = g.creategraph(6, .75, weights, directed=False)
    sources = [0, 0, 0, 0, 0, 1, 2, 3, 4, 5,   5,  6,  7,  8, 9,10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,20,21,22,23,24,25,26,27,28,29,30,31,32,33,33,34,35,36,37,38,39,40,41,46,47]
    targets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,15,16, 17, 18, 19, 20, 21, 22, 23, 24, 24, 25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,40,41,42,43,44,45,46,47,48,48]
    weights = [2, 2, 2, 2, 2, 2, 2, 2, 2, 3,   2, 2, 4, 4, 4, 4,  2, 2, 1, 1, 3, 3, 5, 5, 1, 1,1,2,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    graph = g(sources, targets, weights)

    graph.print_r()
    print('.........................')
    t = time()
    print(graph.floyd_warshall())
    elapsed = time() - t
    print("Time: ", elapsed)

    graph.draw()

def main():

    # Create the root menu
    menu = MultiSelectMenu("Proyecto IA", "Seleccione la el  destino",
                           epilogue_text=("porfavor seleccione  algun  destino "
                                          "puede  seleccionar  mas de una busqueda:  1,2,3   or   1-4   or   1,3-4"),
                           exit_option_text='Salir')  # Customize the exit text

    # Add all the items to the root menu
    menu.append_item(FunctionItem("especialidad   1", action, args=['one']))
    menu.append_item(FunctionItem("especialidad   2", action, args=['two']))
    menu.append_item(FunctionItem("especialidad   3", action, args=['three']))
    menu.append_item(FunctionItem("especialidad   4", mostrar, args=['fouiir']))

    # Show the menu
    menu.start()
    menu.join()


if __name__ == "__main__":
    main()
