# Code where time measurement is repeated
# ---------------------------------------
from time import sleep, time

def f():
    sleep(.3)

def g():
    sleep(.5)

t = time()
f()
print('f took: ', time() - t)  # f took: 0.3003859519958496

t = time()
g()
print('g took:', time() - t)  # g took: 0.5005719661712646

# First attempt at not repeating the code:
from time import sleep, time

def f():
    sleep(.3)

def g():
    sleep(.5)

def measure(func):
    t = time()
    func()
    print(func.__name__, 'took:', time() - t)

measure(f)  # f took: 0.30041074752807617
measure(g)  # g took: 0.5006198883056641

# The same thing but with args
# ----------------------------
from time import sleep, time

def f(sleep_time=0.1):
    sleep(sleep_time)

def measure(func, *args, **kwargs):
    t = time()
    func(*args, **kwargs)
    print(func.__name__, 'took:', time() - t)

measure(f, sleep_time=0.3)  # f took: 0.3004162311553955
measure(f, 0.2)  # f took: 0.20028162002563477

# First step of decoration
# ------------------------
from time import sleep, time

def f(sleep_time=0.1):
    sleep(sleep_time)

def measure(func):
    def wrapper(*args, **kwargs):
        t = time()
        func(*args, **kwargs)
        print(func.__name__, 'took:', time() - t)
    return wrapper

f = measure(f)  # decoration point

f(0.2)  # f took: 0.2002875804901123
f(sleep_time=0.3)  # f took: 0.3003721237182617
print(f.__name__)  # wrapper  <- ouch! f() is calling wrapper() 

# Python decorator syntax (PEP 318)
# -----------------------
def func(arg1, arg2, ...):
    pass
func = decorator(func)

# is equivalent to the following:
@decorator
def func(arg1, arg2, ...):
    pass

# Fix the wrapper issue
# ---------------------
from time import sleep, time
from functools import wraps # needed to import

def measure(func):
    @wraps(func) # decorate with this func
    def wrapper(*args, **kwargs):
        t = time()
        func(*args, **kwargs)
        print(func.__name__, 'took:', time() - t)
    return wrapper

@measure
def f(sleep_time=0.1):
    """I'm a cat. I love to sleep! """
    sleep(sleep_time)

f(sleep_time=0.3)  # f took: 0.30039525032043457
print(f.__name__, ':', f.__doc__)
# f : I'm a cat. I love to sleep! // original name and docstring are now maintainded 

# Multiple decorators (the order matters)
# -------------------
def func(arg1, arg2, ...):
    pass
func = deco1(deco2(func))

# is equivalent to the following:

@deco1
@deco2
def func(arg1, arg2, ...):
    pass

# Decorators with args
# --------------------
def func(arg1, arg2, ...):
    pass
func = decoarg(argA, argB)(func)

# is equivalent to the following:

@decoarg(argA, argB)
def func(arg1, arg2, ...):
    pass

# Full example with two decorators
# --------------------------------

from time import sleep, time
from functools import wraps

def measure(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t = time()
        result = func(*args, **kwargs)
        print(func.__name__, 'took:', time() - t)
        return result
    return wrapper

def max_result(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result > 100:
            print('Result is too big ({0}). Max allowed is 100.'
                .format(result))
        return result
    return wrapper

@measure
@max_result
def cube(n):
    return n ** 3

print(cube(2))
print(cube(5))
# cube took: 7.62939453125e-06  #
# 8  #
# Result is too big (125). Max allowed is 100.
# cube took: 1.1205673217773438e-05
# 125    

# Decorator factory
# -----------------

from functools import wraps

def max_result(threshold):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result > threshold:
                print(
                    'Result is too big ({0}). Max allowed is {1}.'
                    .format(result, threshold))
            return result
        return wrapper
    return decorator

@max_result(75)
def cube(n):
    return n ** 3

print(cube(5))
# Result is too big (125). Max allowed is 75.
# 125

# Decorating a function with a decorator that takes arguments is 
# the same as writing func = decorator(argA, argB)(func), 
# so when we decorate cube with max_result(75), we're doing cube = max_result(75)(cube).

# Let's go through what happens, step by step. When we call max_result(75), we enter its body. 
# A decorator function is defined inside, which takes a function as its only argument. 
# Inside that function, the usual decorator trick is performed. We define a wrapper, 
# inside of which we check the result of the original function's call. The beauty of 
# this approach is that from the innermost level, we can still refer to both func and threshold, 
# which allows us to set the threshold dynamically.

# wrapper returns result, decorator returns wrapper, and max_result returns decorator. 
# This means that our call cube = max_result(75)(cube), actually becomes cube = decorator(cube). 
# Not just any decorator though, but one for which threshold has the value 75. This is achieved 
# by a mechanism called closure.
