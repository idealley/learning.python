
# Closure allow to access a variable after the enclosing function stopped executing
# by declaring another function that can be called later on.
def make_printer(msg):
    def printer():
        print(msg)
    return printer

printer = make_printer('Foo!')
printer()

# In pthon with closures you can read (e.g. the print line) the value of a variable
# but you cannot write it (JS offers this possiblity)
def initCounter():
    x = 0
    def counter ():
        x += 1 ##Error, x not defined
        print(x)
    return counter

count = initCounter()

count() ##Error