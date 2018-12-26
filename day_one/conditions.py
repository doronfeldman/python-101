from util import printer


class AnotherFalseClass:
    def __len__(self):
        return 0


class FalseClass(object):
    def __bool__(self):
        return False


def learn():
    printer.print_explanation('● There are a lot of False/True conditions in python:')
    if not False:
        printer.print_runtime('False is False')
    if not None:
        printer.print_runtime('None is False')
    if not 0:
        printer.print_runtime('0 is False')
    if not []:
        printer.print_runtime('[] is False')
    if not {}:
        printer.print_runtime('{} is False')
    input()

    if True:
        printer.print_runtime('True is True')
    if object():
        printer.print_runtime('object() is True')
    if 1:
        printer.print_runtime('1 is True')
    if [1, 2]:
        printer.print_runtime('[1, 2] is True')
    if {1: 2}:
        printer.print_runtime('{1: 2} is True')
    input()

    printer.print_explanation('● But there is actually a way to define our own classes to be equal to False:')
    if not FalseClass():
        printer.print_runtime('FalseClass() is False')
    if not AnotherFalseClass():
        printer.print_runtime('AnotherFalseClass() is False')
    input()

    printer.print_explanation('● What about inline conditions')
    printer.print_explanation("look at the following condition: \n")
    printer.print_code("condition = 1 == 1 \n"
                       "'Condition is True' if condition else 'Condition is False'")
    printer.print_explanation('What will be the result?')
    input()

    condition = (1 == 1)
    printer.print_runtime(f'The result: {"Condition is True" if condition else "Condition is False"}')
