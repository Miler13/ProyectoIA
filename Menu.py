
from consolemenu import *
from consolemenu.items import *


def action(name):
    print("\nHello from action {}!!!\n".format(name))
    Screen().input('Press [Enter] to continue')
def sumas(a):
    print("hollaaa"+ a)
    Screen().input('Press [Enter] to continue')
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
    menu.append_item(FunctionItem("especialidad   4", sumas, args=['fouiir']))

    # Show the menu
    menu.start()
    menu.join()


if __name__ == "__main__":
    main()
