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
    print('Im the function!')


def decorator_with_arguments(number):
    def my_decorator(func):
        @functools.wraps(func)
        def func_that_runs_func(*args, **kwargs):
            print('In the decorator!')
            if number == 56:
                print('Not running the function!')
            else:
                func()
            print('After the decorator!')
        return func_that_runs_func
    return my_decorator


@decorator_with_arguments(56)
def my_function_too(x, y):
    print(x + y)


my_function_too(56, 67)
