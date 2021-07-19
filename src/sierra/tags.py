import traceback

def join_attr(tup):
    string = ''
    for item in tup:
        string = string + item
        string = string.replace('  ', ' ')
    return string

class Tag:

    def __init__(self, tag, **kwargs):
        """Opens any tag.
        
        \nUse `kwargs` to add tag attributes. Python-conflicting attribute names like `class` and `for` to be prefixed by a double underscore, that is, to be entered in as `__class` and `__for`
        \nUse a single underscore in place of a hyphen in the `key` of `kwargs`, which is the tag atrribute name. 
        \neg. Tag attribute `initial-scale` must be `initial_scale` as the `key`
        """

        self.tag = tag
        self.kwargs = kwargs

    def __enter__(self):

        if self.kwargs:
            # open("index.html", 'a+').write(f"\n<{self.tag}>")
            all_attr = f"<{self.tag} ", *(f'  {key.replace("__", "").replace("_", "-")}="{value}"' for key, value in self.kwargs.items()), ">"
            open('index.html', 'a+').write(f"\n{join_attr(all_attr)}")

        else:
            open("index.html", 'a+').write(f"\n<{self.tag}>")

        return self

    def __exit__(self, exc_type, exc_value, tb):
        if exc_type is not None:
            traceback.print_exception(exc_type, exc_value, tb)
        else:
            open("index.html", 'a+').write(f"\n</{self.tag}>")

    def css(self, **kwargs):
        """Adds the given styling attributes to the `Tag` mentioned

        \nUse `kwargs` to add styling attributes to the `Tag` mentioned
        \nThis adds CSS directly to the tag mentioned, irrespective of any `__class` or `id` mentioned

        \nUse `writeCSS()` instead to add CSS to a specific `class` or `id`

        \nUse underscores instead of hyphens when adding styling attributes
        \nFor example, the attribute `font-size` must be entered in as `font_size`

        \nArgs:
        \n    **kwargs (optional) : CSS parameters.
        """

        with open("style.css", 'a+') as s:
            s.write(f"\n\n{self.tag} {{")

            for key, value in kwargs.items():
                s.write(f"\n\t{key.replace('_', '-')}: {value};")

            s.write("\n}")

def openBody(**kwargs):
    """Opens the body tag and adds the required CSS.

    \nArgs:
    **kwargs (optional) : CSS parameters.
    """

    open("index.html", 'a+').write('\n<body>')
    with open("style.css", 'a+') as s:
        s.write("\nbody {")

        for key, value in kwargs.items():
            s.write(f"\n\t{key.replace('_', '-')}: {value};")

        s.write("\n}")