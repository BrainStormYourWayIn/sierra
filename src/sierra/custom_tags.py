# Still work in progress

common_attr = [
    '_async',  
    '_reversed', 
    '_class', 
    '_for'
]

def tag(func):

    def wrapper(**kwargs):

        name = func.__name__

        # for key in kwargs.items():
        #     if key = 'some':
        #         print('')

        if kwargs:

            # print(kwargs['fodo'])
            print(*(f"{key.replace('_', '')}={value}" for key, value in kwargs.items()))

        print(name)

        func(**kwargs)
        
    return wrapper


@tag
def test(some, **kwargs):
    pass

test(some='loz', foo='bar', _class='some_class')