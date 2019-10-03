# Experiment with scopes in Python.
# Good reading: https://www.programiz.com/python-programming/global-local-nonlocal-variables

# When you use a variable in a function, it's local in scope to the function.
x = 12


def changeX():
    global x
    x = 99
    print(f"1>>{x}")


changeX()

# This prints 12. What do we have to modify in changeX() to get it to print 99?
print(x)


# This nested function has a similar problem.

def outer():
    # y = [120]
    # outer.y = 120
    y = 120

    def inner():
        #y[0] = 999
        # outer.y = 999
        nonlocal y
        y = 999
    inner()

    # This prints 120. What do we have to change in inner() to get it to print
    # 999? Google "python nested function scope".

    # 3 possible soulutions:
    # Create y as an interable in outer function and define y[0] in inner function
    # Specify variable name in outer function to mirror inner function on lines 24 and 29
    # Declare y as nonlocal in inner function, this only works with python3

    print(y)
    # print(outer.y)


outer()
