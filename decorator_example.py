import time
from functools import wraps

def logging_decorator(func):
    @wraps(func)
    def wrapper(args,kwargs):
        print(f"{func.__name__} was called")
        return func(args,kwargs)
    return wrapper

def timer_decorator(func):
    @wraps(func)
    def wrapper(args,kwargs):
        start_time = time.time()
        result = func(args,kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time} seconds")
        return result
    return wrapper

@logging_decorator
@timer_decorator
def example_function():
    time.sleep(1)

example_function()
