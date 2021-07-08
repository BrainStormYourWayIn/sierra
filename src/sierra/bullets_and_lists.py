import traceback

class bullets():
    def __init__(self, ul:bool, points:list, attr=None):
        """
        Adds bullet lists to the webpage.
        
        Args:
        points(list, compulsory): Takes in a list of bullets to add
        ul(bool, optional)      : If set to True, it adds bullets (unordered) rather than an ordered list
        attr(str, optional)     : Sets specified attributes to the tag
    
        """

        self.ul = ul
        self.points = points
        self.attr = attr

        if self.ul:
            if attr == None:
                with open("index.html", 'a+') as f:
                    f.write("\n<ul>")
            else:
                with open("index.html", 'a+') as f:
                    f.write(f"\n<ul {self.attr}>")

        else:
            if attr == None:
                with open("index.html", 'a+') as f:
                    f.write("\n<ol>")
            else:
                with open("index.html", 'a+') as f:
                    f.write(f"\n<ol {self.attr}>")

        for point in self.points:
            open("index.html", 'a+').write(f"\n<li>{point}</li>")

    def __enter__(self):
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


def des_lists(des_list, attr=None):
    """
    Creates a description list from a list of lists
    
    Args:
    des_list(list, compulsory): Takes in a list of lists and creates a description list on it
    attr(str, optional)     : Sets specified attributes to the tag
    
    """
    if attr == None:
        with open('index.html', 'a') as f:
            f.write(f'''\n<dl>''')
    else:
        with open('index.html', 'a') as f:
            f.write(f'''\n<dl {attr}>''')
    
    for des_listings in des_list:
        for des_listing in des_listings[0]:
            open('index.html', 'a').write(f'''\n<dt>{des_listing}</dt>''')
        des_listings.remove(des_listings[0])
        for listings in des_listings:
            for listing in listings:
                open('index.html', 'a').write(f'''\n<dd>{listing}</dd>''')
    with open('index.html', 'a') as f:
        f.write("\n</dl>")
