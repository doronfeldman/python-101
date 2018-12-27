from util import printer
from abc import ABC, abstractmethod


class AbstractClass(ABC):
    @abstractmethod
    def do_something_else(self):
        pass


class AnotherAbstractClass(ABC):
    def __init__(self, value):
        self.value = value

    @abstractmethod
    def do_something(self):
        pass


class ConcreteClassExample(AnotherAbstractClass, AbstractClass):
    def do_something_else(self):
        pass

    def do_something(self):
        pass


def method_with_stuff(param: AbstractClass):
    printer.print_runtime('i still work')


def learn():
    c = ConcreteClassExample(1)
    printer.print_code('issubclass(ConcreteClassExample, AnotherAbstractClass)')
    printer.print_runtime(issubclass(ConcreteClassExample, AnotherAbstractClass))
    printer.print_code('isinstance(c, AbstractClass)')
    printer.print_runtime(isinstance(c, AbstractClass))
    printer.print_code('isinstance(c, AnotherAbstractClass)')
    printer.print_runtime(isinstance(c, AnotherAbstractClass))
    method_with_stuff({})
