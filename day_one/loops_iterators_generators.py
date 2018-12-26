from util import printer


class iterator:
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()


def generator(n):
    i = 0
    printer.print_red('begin generation')
    while i < n:
        printer.print_red(f'before yield {i}')
        yield i
        printer.print_red(f'after yield {i}')
        i += 1
    printer.print_red('end generation')


def learn():
    printer.print_explanation('● There are many types of objects which can be used with a for loop. \n'
                              'These are called iterable objects')
    input()
    printer.print_explanation('Array are iterable')
    printer.print_code('for i in [1, 2, 3, 4]: \n'
                       '\t print(i)')
    # Regular for loops
    for i in [1, 2, 3, 4]:
        printer.print_runtime(i)

    input()
    printer.print_explanation('Strings are iterable')
    printer.print_code('for c in \'python\': \n'
                       '\t print(c)')
    for c in 'python':
        printer.print_runtime(c)

    input()
    printer.print_explanation('Dictionaries are iterable (keys)')
    printer.print_code('for k in {"x": 1, "y": 2}: \n'
                       '\t print(k)')
    for k in {"x": 1, "y": 2}:
        printer.print_runtime(k)

    input()
    printer.print_explanation('● Another pythonic way of using a for loop \n'
                              'that creates an array or dictionary is by using list comprehensions:')

    printer.print_code('print( [x * x for x in [1, 2, 3, 4]] )')
    printer.print_runtime([x * x for x in [1, 2, 3, 4]])


    printer.print_code('\nprint( {x: x * x for x in [1, 2, 3, 4]} )')
    printer.print_runtime({x: x * x for x in [1, 2, 3, 4]})

    input()

    printer.print_explanation('● An iterator is an object that can be iterated upon, \n'
                              'meaning that you can traverse through all the values.')
    printer.print_explanation('● An Iterator is an object that has an __iter__ method, has a __next__ method. \n'
                              'Each time we call the next method on the iterator gives us the next element. \n'
                              'If there are no more elements, it raises a StopIteration error')
    printer.print_explanation('● The built-in function iter takes an iterable object and returns an iterator. \n')

    printer.print_explanation('Let\'s try running the following code: \n')
    printer.print_code(
        'try: \n'
        '\tlist_iterator = iter([1, 2, 3]) \n'
        '\twhile True: \n'
        '\t\tprint(next(list_iterator)) \n'
        'except StopIteration: \n'
        '\tprint(\'StopIteration was raised!\')')
    try:
        list_iterator = iter([1, 2, 3])
        while True:
            printer.print_runtime(next(list_iterator))
    except StopIteration:
        printer.print_runtime('StopIteration was raised!')

    printer.print_explanation('next(list_iterator) is equal to list_iterator.__next__()')
    printer.print_explanation('look at the example iterator class')
    i = iterator(5)

    input()
    printer.print_explanation('● Generators are used to simplify the creation of iterators. \n'
                              'A generator is a function that produces a sequence of results '
                              'instead of a single value.\n')
    printer.print_explanation('● When a generator function is called, it returns a generator object \n'
                              'without even beginning execution of the function. \n'
                              'When __next__ method is called for the first time, \n'
                              'the function starts executing until it reaches yield statement. \n'
                              'The yielded value is returned by the next() call.\n')

    input()
    printer.print_explanation('Let\'s run the following code:')
    printer.print_code('for g in generator(5):\n'
                       '\tprint(g)')

    for g in generator(5):
        printer.print_runtime(g)

    printer.print_explanation('● Another pythonic way of using generators \n'
                              'in on line is generator expressions, \n'
                              'basically, list comprehensions for generators:')
    printer.print_code('for g in (x * x for x in generator(5)):\n'
                       '\tprint(g)')
    for g in (x * x for x in range(5)):
        printer.print_runtime(g)
