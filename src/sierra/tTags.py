import traceback

class div:
    def __init__(self, div_class=None, attr=None):
        self.div_class = div_class

        if div_class == None:
            open("index.html", 'a+').write("\n<div")
        else:
            open("index.html", 'a+').write(f"\n<div class='{self.div_class}'")

        if attr != None:
            open("index.html", 'a+').write(' ' + attr)

        open("index.html", 'a+').write(">")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, tb):
        if exc_type is not None:
            traceback.print_exception(exc_type, exc_value, tb)
        else:
            open("index.html", 'a+').write("\n</div>")

    def css(self, **kwargs):
        """Writes the given parameters to the CSS file.

        Args:
            **kwargs (optional) : CSS parameters.
        """

        with open("style.css", 'a+') as s:
            for key, value in kwargs:
                s.write(f"\n\t{key.replace('_', '-')}: {value};")
            s.write("\n}")


class Section:
    def __init__(self, sec_class=None, attr=None):
        self.sec_class = sec_class

        if sec_class == None:
            open('index.html', 'a+').write("\n<section")
        else:
            open('index.html', 'a+').write(f"\n<section class='{self.sec_class}'")

        if attr != None:
            open("index.html", 'a+').write(' ' + attr)
        open("index.html", 'a+').write(r">")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, tb):
        if exc_type is not None:
            traceback.print_exception(exc_type, exc_value, tb)
        else:
            open("index.html", 'a+').write("\n</section>")

    def css(self, **kwargs):
        """Writes the given parameters to the CSS file.
        
        Args:
            **kwargs (optional) : CSS parameters.
        """

        with open("style.css", 'a+') as s:
            for key, value in kwargs:
                s.write(f"\n\t{key.replace('_', '-')}: {value};")
            s.write("\n}")

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
