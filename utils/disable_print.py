from contextlib import redirect_stdout
from io import StringIO

def disable_print(func):
    def wrapper(*args, **kwargs):
        with redirect_stdout(StringIO()):
            return func(*args, **kwargs)
    return wrapper