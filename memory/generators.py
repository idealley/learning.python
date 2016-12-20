# Generator functions
# -------------------
# -------------------

def get_squares(n):  # classic function approach
    return [x ** 2 for x in range(n)]
print(get_squares(10))

def get_squares_gen(n):  # generator approach
    for x in range(n):
        yield x ** 2  # we yield, we don't return
print(list(get_squares_gen(10)))

# Manual use of generator

def get_squares_gen(n):
    for x in range(n):
        yield x ** 2

squares = get_squares_gen(4)  # this creates a generator object
print(squares)  # <generator object get_squares_gen at 0x7f158...>
print(next(squares))  # prints: 0
print(next(squares))  # prints: 1
print(next(squares))  # prints: 4
print(next(squares))  # prints: 9
# the following raises StopIteration, the generator is exhausted,
# any further call to next will keep raising StopIteration
print(next(squares))

# Use of return in a generator to stop iteration
def geometric_progression(a, q):
    k = 0
    while True:
        result = a * q**k
        if result <= 100000:
            yield result
        else:
            return
        k += 1

for n in geometric_progression(2, 5):
    print(n)

# Beyond next (send, throw, close)
# -----------

# next(generator) proxies generator.__next__() method
def get_squares_gen(n):
    for x in range(n):
        yield x ** 2

squares = get_squares_gen(3)
print(squares.__next__())  # prints: 0
print(squares.__next__())  # prints: 1
print(squares.__next__())  # prints: 4
# the following raises StopIteration, the generator is exhausted,
# any further call to next will keep raising StopIteration
print(squares.__next__())

# send()

#forever
def counter(start=0):
    n = start
    while True:
        yield n
        n += 1

c = counter()
print(next(c))  # prints: 0
print(next(c))  # prints: 1
print(next(c))  # prints: 2

# non pythonic stop
stop = False
def counter(start=0):
    n = start
    while not stop:
        yield n
        n += 1

c = counter()
print(next(c))  # prints: 0
print(next(c))  # prints: 1
stop = True
print(next(c))  # raises StopIteration

# unsing send()
def counter(start=0):
    n = start
    while True:
        result = yield n             # A
        print(type(result), result)  # B
        if result == 'Q':
            break
        n += 1

c = counter()
print(next(c))         # C
print(c.send('Wow!'))  # D
print(next(c))         # E
print(c.send('Q'))     # F

#prints:
# 0
# <class 'str'> Wow!
# 1
# <class 'NoneType'> None
# 2
# <class 'str'> Q
# Traceback (most recent call last):
#   File "gen.send.py", line 14, in <module>
#     print(c.send('Q'))     # F
# StopIteration

# throw()
    #todo
# close()
    #todo

# Yield from
# ----------

# yield way
def print_squares(start, end):
    for n in range(start, end):
        yield n ** 2

for n in print_squares(2, 5):
    print(n)

# yield from way
def print_squares(start, end):
    yield from (n ** 2 for n in range(start, end))

for n in print_squares(2, 5):
    print(n)

# Generator expressions
# ---------------------
# ---------------------

# The syntax is exactly the same as list comprehensions, only, 
# instead of wrapping the comprehension with square brackets, 
# you wrap it with round braces. That is called a generator expression.

# In general, generator expressions behave like equivalent list comprehensions, 
# but there is one very important thing to remember: generators allow for 
# one iteration only, then they will be exhausted

>>> cubes = [k**3 for k in range(10)]  # regular list
>>> cubes
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
>>> type(cubes)
<class 'list'>
>>> cubes_gen = (k**3 for k in range(10))  # create as generator
>>> cubes_gen
<generator object <genexpr> at 0x7ff26b5db990>
>>> type(cubes_gen)
<class 'generator'>
>>> list(cubes_gen)  # this will exhaust the generator
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
>>> list(cubes_gen)  # nothing more to give
[]

# map
def adder(*n):
    return sum(n)
s1 = sum(map(lambda n: adder(*n), zip(range(100), range(1, 101))))
s2 = sum(adder(*n) for n in zip(range(100), range(1, 101)))

#filter
cubes = [x**3 for x in range(10)]
odd_cubes1 = filter(lambda cube: cube % 2, cubes)
odd_cubes2 = (cube for cube in cubes if cube % 2)

N = 20
cubes1 = map(
    lambda n: (n, n**3),
    filter(lambda n: n % 3 == 0 or n % 5 == 0, range(N))
)
cubes2 = (
    (n, n**3) for n in range(N) if n % 3 == 0 or n % 5 == 0)

# Generator are easier to read and shorter

# all the following are equal from the point of view of results
s1 = sum([n**2 for n in range(10**6)]) #list comprehension, before doing the sum the list needs to be created
s2 = sum((n**2 for n in range(10**6))) #parenthesis are redundant
s3 = sum(n**2 for n in range(10**6))   # uses less memory has it does the sum then calls next

s = sum([n**2 for n in range(10**8)])  # this is killed (or put a bigger exponent if your computer/box as more memory)
s = sum(n**2 for n in range(10**8))  # this succeeds
print(s)
