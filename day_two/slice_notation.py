from util import printer


def learn():
    printer.print_explanation('how does slice notation look like? \n'
                              'a_list[start:end:step]\n'
                              'Now let\'s look at examples!\n')

    printer.print_code('a_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]')
    printer.print_code('a_list[0:4]')

    a_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    printer.print_runtime(a_list[0:4])

    input()
    printer.print_explanation('the first parameter can be dropped, it will be assumed as 0')
    printer.print_code('a_list[:4]')
    printer.print_runtime(a_list[:4])

    input()
    printer.print_code('a_list[5:10]')
    printer.print_runtime(a_list[5:10])
    printer.print_explanation('the second parameter can be dropped as well, it will be assumed as last index')
    printer.print_code('a_list[5:]')
    printer.print_runtime(a_list[5:])

    input()
    printer.print_explanation('Wait! but what does the third parameter do??\n'
                              'The third parameter, is how much to step each time')
    printer.print_code('a_list[0:10:2]')
    printer.print_runtime(a_list[0:10:2])

    input()
    printer.print_explanation('Some quick examples (Warning, mind might be blown):')
    printer.print_code('a_list[:-1]')
    printer.print_runtime(a_list[:-1])

    input()
    printer.print_code('a_list[-3:-1]')
    printer.print_runtime(a_list[-3:-1])

    input()
    printer.print_code('a_list[::-1]')
    printer.print_runtime(a_list[::-1])
    printer.print_code('a_list[:5:-1]')
    printer.print_runtime(a_list[:5:-1])

