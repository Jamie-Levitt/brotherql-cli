import functools
import sys

def os_switch(macfunc:function):
    def decorater(func:function):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if sys.platform == 'win32':
                return func(*args, **kwargs)
            elif sys.platform == 'darwin':
                return macfunc(*args, **kwargs)
        return wrapper
    return decorater