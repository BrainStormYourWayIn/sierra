import traceback

class open_tag():

    def __init__(self, tag, attr=None):
        """
        Opens a tag
        """

        self.tag = tag
        self.attr = attr

        if self.attr == None:
            open('index.html', 'a+').write(f"<{self.tag}>")
        else:
            open('index.html', 'a+').write(f"<{self.tag} {self.attr}>")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, tb):
        if exc_type is not None:
            traceback.print_exception(exc_type, exc_value, tb)
        else:
            open('index.html', 'a+').write(f"\n</{self.tag}>")

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
            

def closeHTML():
    """Closes the <HTML> tag. Use autoPrettify() instead"""
    
    open("index.html", 'a').write("\n</html>")
        
def openBody(**kwargs):
    
    """
    Opens the body tag and adds CSS, if applicable

    Args:

        **kwargs (optional)              : CSS styling arguments

    """
    
    open("index.html", 'a').write("\n</head>\n<body>")


    for key, value in kwargs.items():
            add_to_css = f"{key}: {value};"
            add_to_css = add_to_css.replace('_', '-')
            # print(add_to_css)

    with open('style.css', 'a+') as s:
        s.write("\n\nbody {")

        for key, value in kwargs.items():
            add_to_css = f"{key}: {value};"
            add_to_css = add_to_css.replace('_', '-')

            s.write(f'''
    {add_to_css}''')

        s.write("\n}")
        
def closeBody():
    """Closes the body tag. Use autoPrettify() instead"""
    
    open("index.html", 'a').write("\n</body>")
