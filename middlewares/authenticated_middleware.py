from functools import wraps

def authenticated(func):
    @wraps(func)  
    def wrapper(*args, **kwargs):
        


        result = func(*args, **kwargs)
        return result
    return wrapper