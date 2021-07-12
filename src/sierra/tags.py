import traceback

class Tag:
    def __init__(self, tag, attr=None):
        """Opens any tag."""

        self.tag = tag
        self.attr = attr

        if self.attr == None:
            open("index.html", 'a+').write(f"<{self.tag}>")
        else:
            open("index.html", 'a+').write(f"<{self.tag} {self.attr}>")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, tb):
        if exc_type is not None:
            traceback.print_exception(exc_type, exc_value, tb)
        else:
            open("index.html", 'a+').write(f"\n</{self.tag}>")

    def css(self, **kwargs):
        """Writes the given parameters to the CSS file.

        Args:
            **kwargs (optional) : CSS parameters.
        """

        with open("style.css", 'a+') as s:
            s.write("\n\nbody {{")
            for key, value in kwargs:
                s.write(f"\n\t{key.replace('_', '-')}: {value};")
            s.write("\n}")

def openBody(**kwargs):
    """Opens the body tag and adds the required CSS.

    Args:
        **kwargs (optional) : CSS parameters.
    """

    open("index.html", 'a+').write('\n<body>')
    with open("style.css", 'a+') as s:
        for key, value in kwargs:
            s.write(f"\n\t{key.replace('_', '-')}: {value};")

def closeHTML():
    """Closes the <HTML> tag."""
    open("index.html", 'a+').write("\n</html>")

def closeBody():
    """Closes the body tag."""
    open("index.html", 'a+').write('\n</body>')
