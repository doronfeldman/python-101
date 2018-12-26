from util import printer, objectFromDict


def add_function(x, y):
    return x + y


add_lambda = lambda x, y: x + y


def learn():
    printer.print_explanation('Lambda operator or lambda function is used for creating small, \n'
                              'one-time and anonymous function objects in Python. \n')
    printer.print_explanation('Let\'s look at the following example: \n')
    printer.print_code('def add_function(x, y):\n'
                       '\treturn x + y\n')
    printer.print_explanation('is the same as the following lambda: \n')
    printer.print_code('add_lambda = lambda x, y: x + y')

    printer.print_code('add_function(4, 5)')
    printer.print_runtime(add_function(4, 5))
    printer.print_code('add_lambda(4, 5)')
    printer.print_runtime(add_lambda(4, 5))

    input()
    printer.print_explanation('map functions expects a function and any number of iterables \n'
                              'like list, dictionary, etc. It executes the function for each \n'
                              'element in the sequence and returns a list of the elements modified by the function '
                              'object.\n')
    printer.print_code('map(lambda x: x * x, [1, 2, 3, 4])')
    printer.print_runtime(list(map(lambda x: x * x, [1, 2, 3, 4])))

    input()
    printer.print_code("language_dict = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]")
    printer.print_code("map(lambda x: x['name'], language_dict)")

    language_dict = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]
    map(lambda x: x['name'], language_dict)

    printer.print_runtime(list(map(lambda x: x['name'], language_dict)))

    input()
    printer.print_code('list_a = [1, 2, 3]')
    printer.print_code('list_b = [10, 20, 30]')
    printer.print_code('map(lambda x, y: x + y, list_a, list_b)')

    list_a = [1, 2, 3]
    list_b = [10, 20, 30]
    map(lambda x, y: x + y, list_a, list_b)

    printer.print_runtime(list(map(lambda x, y: x + y, list_a, list_b)))

    input()
    printer.print_explanation('filter function expects two arguments, function_object and an iterable. \n'
                              'function_object returns a boolean value. function_object is called for \n'
                              'each element of the iterable and filter returns only those element for \n'
                              'which the function_object returns True.\n')

    printer.print_code('a = [1, 2, 3, 4, 5, 6]')
    printer.print_code('filter(lambda x: x % 2 == 0, a)')
    a = [1, 2, 3, 4, 5, 6]
    filter(lambda x: x % 2 == 0, a)

    printer.print_runtime(list(filter(lambda x: x % 2 == 0, a)))

    input()
    printer.print_explanation(
        'Both map and filter function in python returns an iterator which gets lazily evaluated. \n'
        'We cannot access the elements of the filter object with index nor can \n'
        'we use len() to find the length of the filter result without converting to list.')

