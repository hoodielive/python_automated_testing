import functools 

def my_decorator(func):
    @functools.wraps(func)
    def func_that_runs_func():
        print('In the decorator!')
        func()
        print('After the decorator')
    return func_that_runs_func


@my_decorator
def my_function():
    print("I'm the function!")

my_function()
