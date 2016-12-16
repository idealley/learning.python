def outer():
    test = 1  # outer scope
    test2 = 0 # outer scope 

    def inner():
        ##### TO REMEMBER
        global test3
        nonlocal test2 # allows modification of outer scope
        test = 2  # inner scope
        test2 = 3
        test3 = 4
        print('inner: ', test)
    inner()
    print('outer: ', test)
    print('outer test 2 : ', test2)
test = 0  # global scope
test3 = 0  # global scope
outer()
print('global: ', test)
print('global test 3 : ', test3)

#### Mutables and scope

x = [1, 2, 3]
def func(x):
    x[1] = 42  # this changes the caller! but actually it accesses the caller 
               # and changes the value at an index 
    print('before new x:', id(x))           
    x = 'something else'  # this points x to a new string object
    print('func scope: ', id(x))
    
    # This is not anymore possible... x is now locally a string
    # x[2] = 55

func(x)
print(x)  # prints: [1, 42, 3]
print('outer scope', id(x))