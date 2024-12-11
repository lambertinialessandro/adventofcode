from .measure_time import measure_time, average_measured_time

def test_solution(name=None, runs=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print("\n\033[92mRunning function as-is:\033[0m")
            result = func(*args, **kwargs)

            print("\n\033[92mRunning function with measure_time:\033[0m")
            _ = measure_time(name=name)(func)(*args, **kwargs)

            print("\n\033[92mRunning function with average_measured_time:\033[0m")
            _ = average_measured_time(name=name, runs=runs)(func)(*args, **kwargs)

            print()

            return result
        return wrapper
    return decorator