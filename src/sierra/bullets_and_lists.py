import traceback

def join_attr(tup):
    string = ''
    for item in tup:
        string = string + item
        string = string.replace('  ', ' ')
    return string


class bullets:   
    """
    Adds bullet lists to the webpage.
    
    Args:
    \npoints (list, compulsory): Takes in a list of bullets to add
    \nul (bool, optional)      : If set to True, it adds bullets (unordered) rather than an ordered list
    \nkwargs (optional)        : Sets specified attributes to the tag

    \nUse `kwargs` to add tag attributes. Python-conflicting attribute names like `class` and `for` to be prefixed by a double underscore, that is, to be entered in as `__class` and `__for`
    \nUse a single underscore in place of a hyphen in the `key` of `kwargs`, which is the tag atrribute name. 
    \neg. Tag attribute `initial-scale` must be `initial_scale` as the `key`

    """
    def __init__(self, ul:bool, points:list, **kwargs):

        self.ul = ul
        self.points = points
        self.kwargs = kwargs

    def __enter__(self):
        
        if self.ul == True:
            if self.kwargs:

                all_attr = "<ul ", *(f'  {key.replace("__", "").replace("_", "-")}="{value}"' for key, value in self.kwargs.items()), ">"
                open('index.html', 'a+').write(f"\n{join_attr(all_attr)}")

            else:

                with open("index.html", 'a+') as f:
                    f.write(f"\n<ul>")


        else:
            if self.kwargs:

                all_attr = "<ol ", *(f'  {key.replace("__", "").replace("_", "-")}="{value}"' for key, value in self.kwargs.items()), ">"
                open('index.html', 'a+').write(f"\n{join_attr(all_attr)}")

            else:
                with open("index.html", 'a+') as f:
                    f.write(f"\n<ol>")

        for point in self.points:
            open("index.html", 'a+').write(f"\n<li>{point}</li>")

        return self

    def __exit__(self, exc_type, exc_value, tb):
        if self.ul:
            if exc_type is not None:
                traceback.print_exception(exc_type, exc_value, tb)
            else:
                open("index.html", 'a+').write("\n</ul>")

        elif not self.ul:
            if exc_type is not None:
                traceback.print_exception(exc_type, exc_value, tb)
            else:
                open("index.html", 'a+').write("\n</ol>")


def des_lists(des_list, **kwargs):
    """
    Creates a description list from a list of lists
    
    Args:
    \ndes_list (list, compulsory): Takes in a list of lists and creates a description list on it
    \nkwargs (optional)          : Sets specified attributes to the tag
    
    \nUse `kwargs` to add tag attributes. Python-conflicting attribute names like `class` and `for` to be prefixed by a double underscore, that is, to be entered in as `__class` and `__for`
    \nUse a single underscore in place of a hyphen in the `key` of `kwargs`, which is the tag atrribute name. 
    \neg. Tag attribute `initial-scale` must be `initial_scale` as the `key`
    """
    if not kwargs:

        open('index.html', 'a+').write("\n<dl>")

    else:

        all_attr = "<dl ", *(f'  {key.replace("__", "").replace("_", "-")}="{value}"' for key, value in kwargs.items()), ">"
        open('index.html', 'a+').write(f"\n{join_attr(all_attr)}")
    
    for des_listings in des_list:
        for des_listing in des_listings[0]:
            open('index.html', 'a').write(f"\n<dt>{des_listing}</dt>")
        des_listings.remove(des_listings[0])
        for listings in des_listings:
            for listing in listings:
                open('index.html', 'a').write(f"\n<dd>{listing}</dd>")
    with open('index.html', 'a') as f:
        f.write("\n</dl>")

with bullets(ul=False, points=['f', 'fe'], __class='tclass', fo_d='d'):
    pass