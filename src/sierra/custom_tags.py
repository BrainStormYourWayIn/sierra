# Still work in progress

def tag(func):

    def wrapper(*args, **kwargs):

        name = func.__name__

        if kwargs:

            print(args, *(f"{key}={value}" for key, value in kwargs.items()))

        print(name)

        func(*args, **kwargs)
        
    return wrapper


@tag
def test(**kwargs):
    pass

test(foo='bar', haha='lol')