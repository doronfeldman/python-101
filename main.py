from util import printer
from day_one import naming_conventions, modules_classes_etc, conditions, loops_iterators_generators, lambdas_map_filter
from day_two import by_ref_by_val

# A module that could be runnable
if __name__ == '__main__':
    selection = '1'
    while selection != '0':
        printer.print_white("What would you like to learn today?")
        printer.print_white("(1) naming conventions")
        printer.print_white("(2) package, modules, classes, methods, functions, class methods, static methods")
        printer.print_white("(3) conditions")
        printer.print_white("(4) loops, iterators, generators")
        printer.print_white("(5) lambdas, map, filter")
        printer.print_white("(6) by ref, by val")
        printer.print_white("(0) quit")

        selection = input()
        while selection not in ['1', '2', '3', '4', '5', '6', '0']:
            printer.print_red(f'{selection} is not an option, try again')
            selection = input()

        if selection == '1':
            naming_conventions.learn()
        elif selection == '2':
            modules_classes_etc.learn()
        elif selection == '3':
            conditions.learn()
        elif selection == '4':
            loops_iterators_generators.learn()
        elif selection == '5':
            lambdas_map_filter.learn()
        elif selection == '6':
            by_ref_by_val.learn()
