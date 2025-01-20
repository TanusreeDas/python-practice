import os
import time
import inspect

def function_run_time(func):
    def wrapper(*args, **kwargs):
        caller_module = os.path.basename((inspect.stack())[1].filename).split('.')[0]
        start_time = time.perf_counter()
        result = func(*args, **kwargs)   # Call the original function
        end_time = time.perf_counter()
        print(f"Function '{func.__name__}' from '{caller_module}' module executed in {end_time - start_time:.10f} seconds")
        return result
    return wrapper