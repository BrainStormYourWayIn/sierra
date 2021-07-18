import traceback

def join_attr(tup):
    string = ''
    for item in tup:
        string = string + item
        string = string.replace('  ', ' ')
    return string

class div:
    """
    Creates a &lt;div&gt; tag. 

    \nUse `kwargs` to add tag attributes. Python-conflicting attribute names like `class` and `for` to be prefixed by a double underscore, that is, to be entered in as `__class` and `__for`
    \nUse a single underscore in place of a hyphen in the `key` of `kwargs`, which is the tag atrribute name. 
    \neg. Tag attribute `initial-scale` must be `initial_scale` as the `key`
    """
    def __init__(self, **kwargs):

        self.kwargs = kwargs


    def __enter__(self):

        if not self.kwargs:
            open('index.html', 'a+').write("\n<div>")
        else:
            all_attr = "<div ", *(f'  {key.replace("__", "").replace("_", "-")}="{value}"' for key, value in self.kwargs.items()), ">"
            open('index.html', 'a+').write(f"\n{join_attr(all_attr)}")

        return self

    def __exit__(self, exc_type, exc_value, tb):
        if exc_type is not None:
            traceback.print_exception(exc_type, exc_value, tb)
        else:
            open("index.html", 'a+').write("\n</div>")

    def css(self, **kwargs):
        """Writes the given parameters to the CSS file.

        \nIf `__class` is given, CSS is added to that class
        \nIf `id` is given, CSS is added to that id as a second priority
        \nIf none of these are given, CSS is just added to `section`

        \nUse an underscore instead of a hyphen in the `key` or `kwargs`
        \nFor example, enter in `font_size=20px` instead of `font-size=20px`. The latter gives a `SyntaxError`

        Args:
            **kwargs (optional) : CSS parameters.
        """
        # self.kwargs = kwargs

        with open("style.css", 'a+') as s:

            try:
                s.write(f"\n\n.{self.kwargs['__class']} {{")

            except:
                try:
                    s.write(f"\n\n#{self.kwargs['id']} {{")
                except:
                    s.write("\n\ndiv {")


        for key, value in kwargs.items():
            open("style.css", 'a+').write(f"\n\t{key.replace('_', '-')}: {value};")
        open("style.css", 'a+').write("\n}")


class section:
    """
    Creates a &lt;section&gt; tag. 

    \nUse `kwargs` to add tag attributes. Python-conflicting attribute names like `class` and `for` to be prefixed by a double underscore, that is, to be entered in as `__class` and `__for`
    \nUse a single underscore in place of a hyphen in the `key` of `kwargs`, which is the tag atrribute name. 
    \neg. Tag attribute `initial-scale` must be `initial_scale` as the `key`
    """
    def __init__(self, **kwargs):

        self.kwargs = kwargs


    def __enter__(self):

        if not self.kwargs:
            open('index.html', 'a+').write("\n<section>")
        else:
            all_attr = "<section ", *(f'  {key.replace("__", "").replace("_", "-")}="{value}"' for key, value in self.kwargs.items()), ">"
            open('index.html', 'a+').write(f"\n{join_attr(all_attr)}")

        return self


    def __exit__(self, exc_type, exc_value, tb):
        if exc_type is not None:
            traceback.print_exception(exc_type, exc_value, tb)
        else:
            open("index.html", 'a+').write("\n</section>")

    def css(self, **kwargs):
        """Writes the given parameters to the CSS file.

        \nIf `__class` is given, CSS is added to that class
        \nIf `id` is given, CSS is added to that id as a second priority
        \nIf none of these are given, CSS is just added to `section`

        \nUse an underscore instead of a hyphen in the `key` or `kwargs`
        \nFor example, enter in `font_size=20px` instead of `font-size=20px`. The latter gives a `SyntaxError`

        Args:
            **kwargs (optional) : CSS parameters.
        """
        # self.kwargs = kwargs

        with open("style.css", 'a+') as s:

            try:
                s.write(f"\n\n.{self.kwargs['__class']} {{")

            except:
                try:
                    s.write(f"\n\n#{self.kwargs['id']} {{")
                except:
                    s.write("\n\nsection {")


        for key, value in kwargs.items():
            open("style.css", 'a+').write(f"\n\t{key.replace('_', '-')}: {value};")
        open("style.css", 'a+').write("\n}")


def p(text, attr=None):
    if attr != None:
        with open("index.html", 'a+') as f:
            f.write(f'''\n<p {attr}>
{text}
</p>''')
    else:
        with open("index.html", 'a+') as f:
            f.write(f'''\n<p>
{text}
</p>''')


