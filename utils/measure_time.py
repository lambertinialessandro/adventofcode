import time

from .disable_print import disable_print

def measure_time(name=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = disable_print(func)(*args, **kwargs)
            end_time = time.time()
            display_name = name if name else func.__name__
            print(f"Execution time for \"{display_name}\": \033[93m{end_time - start_time:.3f}\033[0m seconds")
            return result
        return wrapper
    return decorator

def average_measured_time(name=None, runs=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            total_time = 0
            for _ in range(runs):
                start_time = time.time()
                result = disable_print(func)(*args, **kwargs)
                end_time = time.time()
                total_time += (end_time - start_time)
            average_time = total_time / runs
            display_name = name if name else func.__name__
            print(f"Average execution time for \"{display_name}\" over \033[95m{runs}\033[0m runs: \033[93m{average_time:.3f}\033[0m seconds")
            return result
        return wrapper
    return decorator