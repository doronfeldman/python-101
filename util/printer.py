from colorama import init, Fore, Back, Style

init(autoreset=True)


def print_red(message):
    print(f'{Style.BRIGHT}{Fore.RED}{message}')


def print_blue(message):
    print(f'{Style.BRIGHT}{Fore.BLUE}{message}')


def print_cyan(message):
    print(f'{Style.BRIGHT}{Fore.CYAN}{message}')


def print_explanation(message):
    print_cyan(message)


def print_green(message):
    print(f'{Style.BRIGHT}{Fore.GREEN}{message}')


def print_magenta(message):
    print(f'{Style.BRIGHT}{Fore.MAGENTA}{message}')


def print_runtime(message):
    print_magenta(message)


def print_yellow(message):
    print(f'{Style.BRIGHT}{Fore.YELLOW}{message}')


def print_code(message):
    print_yellow(message)


def print_white(message):
    print(f'{Style.BRIGHT}{Fore.WHITE}{message}')


def show_off(message):
    print_red(message)
    print_blue(message)
    print_explanation(message)
    print_green(message)
    print_runtime(message)
    print_code(message)
    print_white(message)
