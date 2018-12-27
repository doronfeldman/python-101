from util import printer

global_variable = 5


def learn():
    pass


def learn1():
    global_variable = 6
    print(global_variable)  # will print 6


learn1()
print(global_variable)  # will print 5
# --------------------------------------------

another_global_variable = 'Hello!'


def learn2():
    global another_global_variable
    another_global_variable = "Goodbye!"


print(another_global_variable)  # will print Hello!
learn2()
print(another_global_variable)  # will print Goodbye!

# --------------------------------------------

x = "a"


def outer():
    x = "b"

    def inner():
        x = "c"
        print("from inner:", x)

    inner()
    print("from outer:", x)


outer()
print("globally:", x)

# inner: c
# outer: b
# global: a

# --------------------------------------------

x = "a"


def outer():
    x = "b"

    def inner():
        nonlocal x
        x = "c"
        print("from inner:", x)

    inner()
    print("from outer:", x)


outer()
print("globally:", x)

# inner: c
# outer: c
# global: a
