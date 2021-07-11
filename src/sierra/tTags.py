import traceback

class div():
    def __init__(self, div_class=None, attr=None):
        self.div_class = div_class

        if div_class == None:
            with open('index.html', 'a+') as f:
                f.write("\n<div")
        else:
            with open('index.html', 'a+') as f:
                f.write(f"\n<div class='{self.div_class}'")

        if attr != None:
            open('index.html', 'a+').write(f''' {attr}''')

        open('index.html', 'a+').write(">")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, tb):
        if exc_type is not None:
            traceback.print_exception(exc_type, exc_value, tb)
        else:
            open('index.html', 'a+').write("\n</div>")

    def css(self, **kwargs):

        """
        Only applies when div_class is valid. Else, use cTags(), writeCSS() or writeCSS_raw()

        Args:

            **kwargs (optional)              : CSS styling arguments

        """

        if self.div_class != None:

            for key, value in kwargs.items():
                add_to_css = f"{key}: {value};"
                add_to_css = add_to_css.replace('_', '-')
                # print(add_to_css)

            with open('style.css', 'a+') as s:
                s.write(f"\n\n.{self.div_class} {{")
                for key, value in kwargs.items():
                    add_to_css = f"{key}: {value};"
                    add_to_css = add_to_css.replace('_', '-')

                    s.write(f'''
        {add_to_css}''')

                s.write("\n}")


class section():
    def __init__(self, sec_class=None, attr=None):
        self.sec_class = sec_class

        if sec_class == None:
            with open('index.html', 'a+') as f:
                f.write("\n<section")
        else:
            with open('index.html', 'a+') as f:
                f.write(f"\n<section class='{self.sec_class}'")

        if attr != None:
            open('index.html', 'a+').write(f''' {attr}''')

        open('index.html', 'a+').write(">")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, tb):
        if exc_type is not None:
            traceback.print_exception(exc_type, exc_value, tb)
        else:
            open('index.html', 'a+').write("\n</section>")

    def css(self, **kwargs):

        """
        Only applies when sec_class is valid. Else, use cTags(), writeCSS() or writeCSS_raw()

        Args:

            **kwargs (optional)              : CSS styling arguments

        """

        if self.sec_class != None:

            for key, value in kwargs.items():
                add_to_css = f"{key}: {value};"
                add_to_css = add_to_css.replace('_', '-')
                # print(add_to_css)

            with open('style.css', 'a+') as s:
                s.write(f"\n\n.{self.sec_class} {{")
                for key, value in kwargs.items():
                    add_to_css = f"{key}: {value};"
                    add_to_css = add_to_css.replace('_', '-')

                    s.write(f'''
        {add_to_css}''')

                s.write("\n}")

def p(text, attr=None):
    if attr != None:
        with open('index.html', 'a+') as f:
            f.write(f'''\n<p {attr}>
{text}
</p>''')
    else:
        with open('index.html', 'a+') as f:
            f.write(f'''\n<p>
{text}
</p>''')


# with div(div_class='newClass', attr="id='some_id'") as d:
#     p('This is some text')
#     d.css(color='yellow')

# with section(sec_class="someClass", attr="id='new_id'") as s:
#     p('Some more text', "class='anotherClass'")
#     s.css(font_family='Times New Roman')
