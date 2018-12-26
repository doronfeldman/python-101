from util import printer


class Test:
    def __init__(self):
        self.regular_test = 1
        self._private_test = 2
        self.__mangled_test = 3


def learn():
    printer.print_explanation('● Always give meaningful names, no a, b, c')
    input()
    printer.print_explanation('● Avoid using names that are too general or too wordy')
    printer.print_red('  Bad: data_structure, my_list, info_map,')
    printer.print_red('  dictionary_for_the_purpose_of_storing_data_representing_word_definitions')
    input()
    printer.print_explanation('● Almost everything in python is named with snake_case')
    input()
    printer.print_explanation('● Classes are named in PascalCase')
    input()
    printer.print_explanation('● Non public method or instance variables should begin with a single underscore _')
    input()
    printer.print_explanation('● Non public method or instance variables that should be mangled '
                              'begin with a double underscore __')
    printer.print_explanation('let\'s define a a class \n')
    printer.print_code('class Test: \n'
                       '\tdef __init__(self): \n'
                       '\tself.regular_test = 1 \n'
                       '\tself._private_test = 2 \n'
                       '\tself.__mangled_test = 3 \n')

    props = [bla for bla in dir(Test()) if bla.endswith('_test')]
    printer.print_explanation('now let\'s see how it\'s defined in runtime using dir(Test()): \n')
    printer.print_runtime(f'{props}')

    input()
    printer.print_explanation('● Constant names must be FULLY_CAPITALIZED')
