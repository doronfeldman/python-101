# from package/module_name import <name> as <alt_name>
# from util import printer
# from util import printer as a_printer
# from util import *
# from util.printer import print_white

from util import printer


def a_function():
    pass


class Test:
    class_variable = 1

    def __init__(self):
        self.instance_variable = 1

    def instance_method(self):
        self.instance_variable += 1

    @classmethod
    def class_method(cls):
        cls.class_variable += 1

    @staticmethod
    def static_method():
        pass


def learn():
    test1 = Test()
    test2 = Test()

    printer.print_explanation('We defined a class named Test (look at the class)')
    input()
    printer.print_explanation('now let\'s define 2 instances of this class \n')
    printer.print_code('test1 = Test() \n'
                       'test2 = Test() \n')
    printer.print_runtime(f'test1.instance_variable: {test1.instance_variable}')
    printer.print_runtime(f'test1.class_variable: {test1.class_variable}')
    printer.print_runtime(f'test2.instance_variable: {test2.instance_variable}')
    printer.print_runtime(f'test2.class_variable: {test2.class_variable}')
    input()
    printer.print_explanation('Now we will execute the following: \n')
    printer.print_code('test1.class_method() \n'
                       'test1.instance_method() \n')

    printer.print_explanation('by the way, est1.class_method() == Test.class_method() \n')
    test1.class_method()
    test1.instance_method()

    printer.print_runtime(f'test1.instance_variable: {test1.instance_variable}')
    printer.print_runtime(f'test1.class_variable: {test1.class_variable}')
    input()

    printer.print_explanation('Now we will execute the following: \n')
    printer.print_code('test2.class_method() \n'
                       'test2.instance_method() \n')
    test2.class_method()
    test2.instance_method()

    printer.print_runtime(f'test2.instance_variable: {test2.instance_variable}')
    printer.print_runtime(f'test2.class_variable: {test2.class_variable}')

    input()
    printer.print_explanation('as you can see, the class methods span across instances')
