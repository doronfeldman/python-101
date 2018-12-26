from util import printer


def learn():
    printer.print_code('def re_asign_list(list_of_stuff):\n'
                       '\tlist_of_stuff = []\n')

    def re_asign_list(list_of_stuff):
        list_of_stuff = []

    printer.print_code('def change_list(list_of_stuff):\n'
                       '\tlist_of_stuff.pop()\n')

    def change_list(list_of_stuff):
        list_of_stuff.pop()

    printer.print_code('stuff = [1, 2, 3, 4]')
    stuff = [1, 2, 3, 4]

    printer.print_code('re_asign_list(stuff)')
    re_asign_list(stuff)
    printer.print_runtime(stuff)

    input()
    printer.print_code('change_list(stuff)')
    change_list(stuff)
    printer.print_runtime(stuff)

    input()

    printer.print_code('def change_name(text):\n'
                       '\ttext.capitalize()\n')

    def change_name(text):
        text.capitalize()

    printer.print_code('name = \'Doron Feldman\'')
    name = 'Doron Feldman'

    printer.print_code('change_name(name)')
    change_name(name)
    printer.print_runtime(name)
