import traceback

class cTags:
    def __init__(self, tag):
        """Add CSS to custom tags. Use writeCSS() for custom CSS arguments."""
        self.tag = tag

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, tb):
        if exc_type is not None:
            traceback.print_exception(exc_type, exc_value, tb)

    def css(self, **kwargs):
        """Writes the given parameters to the CSS file.

        Args:
            **kwargs (optional) : CSS parameters.
        """

        with open("style.css", 'a+') as s:
            s.write(f"\n\n{self.tag} {{")
            for key, value in kwargs:
                s.write(f"\n\t{key.replace('_', '-')}: {value};")
            s.write("\n}")
