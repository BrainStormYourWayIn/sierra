# Enables the user to create custom tags based on their use cases
# Still work in progress
import functools
import traceback
from contextlib import ContextDecorator
import warnings

common_attr = [
    '_async',  
    '_reversed', 
    '_class', 
    '_for'
]

def join_attr(tup):
    string = ''
    for item in tup:
        string = string + item
        string = string.replace('  ', ' ')
    return string

def tag(func):
    """
    Decorator to create short tags like &lt;area>, &lt;label>, &lt;script> or any other similar tag
    \nUse text as a `**kwargs` argument if you want to add some short text within the tag. If you want to create a tag that takes in no text but closes immediately after opening, then enter text as `text=''`   
    \nUse `kwargs` to add tag attributes. Python-conflicting attribute names like `class` and `for` to entered in as `_class` and `_for`
    """
    @functools.wraps(func)
    def wrapper(**kwargs):

        name = func.__name__


        if kwargs:
            
            try:
                check_text = kwargs['text']
                del kwargs['text']

                all_attr = f"<{name}  ", *(f"  {key.replace('_', '')}={value}" for key, value in kwargs.items()), ">"
                # print(a)
                print(join_attr(all_attr))
                print(check_text)
                print(f"</{name}>")

            except KeyError:

                all_attr = f"<{name}  ", *(f"  {key.replace('_', '')}={value}" for key, value in kwargs.items()), ">"
                print(join_attr(all_attr))

        else:

            warnings.showwarning(r'''
Execution not possible if you're not using **kwargs, please use Tag() or decorator CmTag() instead of 
decorator tag()''', 
            UserWarning, 'custom_tags.py', 'decorator tag()')


        func(**kwargs)
        
    return wrapper



class CmTag(ContextDecorator):
    """
    Decorator to create a tag with a context-manager behavior
    \nUse `kwargs` to add tag attributes.
    \nPython-conflicting attribute names like `class` and `for` to entered in as `_class` and `_for` 
    """

    def __init__(self, cm_tag_func):

        self.cm_tag_func = cm_tag_func
        

    def __enter__(self):        
        return self

    def __exit__(self, exc_type, exc_value, tb):
        if exc_type is not None:
            traceback.print_exception(exc_type, exc_value, tb)
        else:
            name = self.cm_tag_func.__name__
            print(name)

    def __call__(self, **kwargs):

        name = self.cm_tag_func.__name__
        print(name)
        print(kwargs)
        self.cm_tag_func(**kwargs)
        return self

# @CmTag
# def testingg(**kwargs):
#     pass

# with testingg(foo='bar') as a:
#     print('a test')


@tag
def meta(**kwargs):
    pass

meta(name="viewport", content="width=device-width, initial-scale=1.0")
# <meta name="viewport" content="width=device-width initial-scale=1.0"/>

@tag
def script(text, **kwargs):
    pass

someJStext = f'''
      # JS text
      '''
script(text=someJStext, _async="", src="some_src")

# <script async="", src="some_src">
#     someJStext
# </script>

# OR use @CmTag (work-in-progress)

@CmTag
def script(**kwargs):
    pass

with script(_async="", src="some_src"):
    writeWA(someJStext)

# <script async="", src="some_src">
#     someJStext
# </script>
    



