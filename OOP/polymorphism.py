"""In our car example, we call engine.start() (check -> inheritance.py), regardless of what kind of engine it is. 
As long as it exposes the start method, we can call it. That's polymorphism in action.

In Python, polymorphism is implicit, nothing prevents you to call a method on an object,
therefore, technically, there is no need to implement interfaces or other patterns.

There is a special kind of polymorphism called ad hoc polymorphism, which is 
what we saw in the last paragraph: operator overloading. The ability of 
an operator to change shape, according to the type of data it is fed.
"""