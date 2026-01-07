def add(a,b):
    return a+b
def div(a,b):
    if b==0:
        raise ValueError("any number can't divided by zero")
    return a/b