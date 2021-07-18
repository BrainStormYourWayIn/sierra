# Enables the user to create custom tags based on their use cases

import functools
import traceback
from contextlib import ContextDecorator

common_attr = [
    '__async',  
    '__reversed', 
    '__class', 
    '__for'
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
    \nUse `text` as a `**kwargs` argument if you want to add some short text within the tag. If you want to create a tag that takes in no text but closes immediately after the attributes, do not use `text` as an argument  
    \nUse `kwargs` to add tag attributes. Python-conflicting attribute names like `class` and `for` to be prefixed by a double underscore, that is, to be entered in as `__class` and `__for`
    \nUse a single underscore in place of a hyphen in the `key` of `kwargs`, which is the tag atrribute name. 
    \neg. Tag attribute `initial-scale` must be `initial_scale` as the `key`
    """
    @functools.wraps(func)
    def wrapper(**kwargs):

        name = func.__name__

        if kwargs:
            
            try:

                check_text = kwargs['text']
                del kwargs['text']
                
                    
                kwargs = {
                k.replace("__", "").replace("_", "-"): v for k, v in kwargs.items()
                }

                all_attr = f"<{name} ", *(f'  {key}="{value}"' for key, value in kwargs.items()), ">"
                open('index.html', 'a+').write(f"\n{join_attr(all_attr)}")

                open('index.html', 'a+').write(f"{check_text}")
                open('index.html', 'a+').write(f"</{name}>")

            except KeyError:

                kwargs = {
                k.replace("__", "").replace("_", "-"): v for k, v in kwargs.items()
                }

                all_attr = f"<{name}  ", *(f'  {key}="{value}"' for key, value in kwargs.items()), ">"
                open('index.html', 'a+').write(f"\n{join_attr(all_attr)}")

        else:

            open('index.html', 'a+').write(f"\n<{name}>")


        func(**kwargs)
        
    return wrapper


class CmTag(ContextDecorator):
    """
    Decorator to create a tag with a context-manager behavior
    \nUse `kwargs` to add tag attributes
    \nPython-conflicting attribute names like `class` and `for` to be prefixed by a double underscore, that is, to be entered in as `__class` and `__for`
    \nUse a single underscore in place of a hyphen in the `key` of `kwargs`, which is the tag atrribute name. Tag attribute `initial-scale` must be `initial_scale` as the `key`
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
            open('index.html', 'a+').write(f"\n</{name}>")

    def __call__(self, **kwargs):

        name = self.cm_tag_func.__name__

        if kwargs:

            kwargs = {
                    k.replace("__", "").replace("_", "-"): v for k, v in kwargs.items()
                    }

            all_attr = f"<{name}  ", *(f'  {key}="{value}"' for key, value in kwargs.items()), ">"
            open('index.html', 'a+').write(f"\n{join_attr(all_attr)}\n")

        else:

            open('index.html', 'a+').write(f"\n<{name}>")

        self.cm_tag_func(**kwargs)
        return self
   