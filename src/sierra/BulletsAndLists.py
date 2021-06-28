import traceback

class bullets():
    def __init__(self, ul:bool, points:list, attr=None):
        """Adds bullet lists to the webpage.
        
        Args:
            points(list, compulsory) : Takes in a list of bullets to add.
            ul(bool, optional)       : If set to True, it adds bullets (unordered) rather than an ordered list.
            start(str, optional)     : Starts the ordered list from a particular starting position.
            type(str, optional)      : Sets the type of ordered/unordered list.
            inner(bool, optional)    : Determines if bullet lists have to be added inside of a bullet list item.
        """
        
        self.ul = ul
        self.points = points
        self.attr = attr

        if self.ul:
            if attr == None:
                with open('index.html', 'a+') as f:
                    f.write("\n<ul>")
            else:
                with open('index.html', 'a+') as f:
                    f.write(f"\n<ul {self.attr}>")

        else:
            if attr == None:
                with open('index.html', 'a+') as f:
                    f.write("\n<ol>")
            else:
                with open('index.html', 'a+') as f:
                    f.write(f"\n<ol {self.attr}>")

        for point in self.points:
            open('index.html', 'a+').write(f"\n<li>{point}</li>")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, tb):
        if self.ul:
            if exc_type is not None:
                traceback.print_exception(exc_type, exc_value, tb)
            else:
                open('index.html', 'a+').write("\n</ul>")

        elif not self.ul:
            if exc_type is not None:
                traceback.print_exception(exc_type, exc_value, tb)
            else:
                open('index.html', 'a+').write("\n</ol>")


def def_lists(def_list, *args):
    """Creates a description list from a list of lists.

    Args:
        def_list(list, compulsory) : Takes in a list of lists and creates a description list on it.
        *args                      : To use global, if required. Enter them within quotes, not comma-separated.
    """

    open('index.html', 'a+').write('\n<dl')
    for arg in args:
            b = ' ' + arg
            open('index.html', 'a+').write(b)

    open('index.html', 'a+').write(">")
    for def_listings in def_list:
        for def_listing in def_listings[0]:
            open('index.html', 'a+').write(f'''\n<dt>{def_listing}</dt>''')

        def_listings.remove(def_listings[0])
        for listings in def_listings:
            for listing in listings:
                open('index.html', 'a+').write(f'''\n<dd>{listing}</dd>''')

    open('index.html', 'a+').write("\n</dl>")
