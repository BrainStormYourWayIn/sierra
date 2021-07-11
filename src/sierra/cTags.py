import traceback

class cTags():

    def __init__(self, tag):

        """
        Add CSS to custom tags. Use writeCSS() for custom CSS arguments
        """
        self.tag = tag

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, tb):
        if exc_type is not None:
            traceback.print_exception(exc_type, exc_value, tb)

    def css(self, **kwargs):
        """
        Args:

            **kwargs (optional)              : CSS styling arguments

        """

        for key, value in kwargs.items():
            add_to_css = f"{key}: {value};"
            add_to_css = add_to_css.replace('_', '-')
            # print(add_to_css)

        with open('style.css', 'a+') as s:
            s.write(f"\n\n{self.tag} {{")
            for key, value in kwargs.items():
                add_to_css = f"{key}: {value};"
                add_to_css = add_to_css.replace('_', '-')

                s.write(f'''
    {add_to_css}''')

            s.write("\n}")
