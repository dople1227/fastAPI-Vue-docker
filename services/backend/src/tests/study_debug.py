def outer_function():
    print("Start of outer function")
    inner_function()
    print("End of outer function")


def inner_function():
    print("1")
    print("Inside inner function")
    print("3")


outer_function()
