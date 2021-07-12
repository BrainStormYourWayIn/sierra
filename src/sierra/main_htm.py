import warnings
from bs4 import BeautifulSoup
import traceback
from flask import url_for

def title(Title, icon=False, templating=False):
    """
    Args:
        Title(str, compulsory)   : Title of the HTML file.
        icon(str, optional)      : Icon to be displayed. Should be a .ico file. Defaults to no icon.
    """
    
    with open("index.html", 'w') as f:
        f.write(f'''<!doctype html>
<html lang="en">
<meta charset="utf-8">
<head>
<title>{Title}</title>''')

        if templating == False:
            f.write(f'\n<link rel="stylesheet" href="style.css">')
        else:
            f.write(f'''\n<link rel="stylesheet" href="/static/style.css">''')

        if type(icon) == str and icon.split('.')[-1] == '.ico':
            f.write(f'''\n<link rel="shortcut icon" href={icon}>''')
    open('style.css', 'w').write('')


# def href(link:str, text:str):
#     with open('index.html', 'a+') as f:
#         f.write(f'''\n<a href="{link}">{text}</a>''')
 
    
def addFont(font_link):
    """Give the font link to add different fonts to your webpage.
    
    Args:
        font_link (str, compulsory): The font link.
    """

    with open("index.html", 'a') as f:
        f.write(f'\n<link href="{font_link}" rel="stylesheet">')

# def code(codeblock):
#     """Give the codeblock as a text to display the code in your webpage.

#     Args:
#         codeblock (str, compulsory): The code block.
#     """
    
#     with open("index.html", 'a') as f:
#         f.write(f"\n<code>{codeblock}</code>")

def head(Head, type='header', **kwargs):
    """
    Args:
        Head (str, compulsory)           : Caption header.
        type (str, optional)             : Header type. Anything from 'h1' to 'h6'
        **kwargs (optional)              : CSS styling arguments
    """
    
    # Use underscores for hyphens in **kwags for styling args

    with open(f"index.html", 'a') as f:
        f.write(f'''
<{type}>{Head}</{type}>''')
        
    if kwargs:

        for key, value in kwargs.items():
            add_to_css = f"{key}: {value};"
            add_to_css = add_to_css.replace('_', '-')
            # print(add_to_css)

            with open('style.css', 'w') as s:
                s.write(f"\n{type} {{")
                
            for key, value in kwargs.items():
                add_to_css = f"{key}: {value};"
                add_to_css = add_to_css.replace('_', '-')

                s.write(f'''
    {add_to_css}''')

            s.write("\n}")
        


class image():
    def __init__(self, src:str, attr=None):
        self.src = src
        self.attr = attr

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, tb):
        if exc_type is not None:
            traceback.print_exception(exc_type, exc_value, tb)

    def show(self):
        """
        Display the image
        """
        with open('index.html', 'a') as f:
            if self.attr == None:
                f.write(f'''\n<img src="{self.src}">''')
            else:
                f.write(f"\n<img src="{self.src}" {self.attr}>")

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
            s.write(f"\n\nimg {{")
            for key, value in kwargs.items():
                add_to_css = f"{key}: {value};"
                add_to_css = add_to_css.replace('_', '-')

                s.write(f'''
    {add_to_css}''')

            s.write("\n}")


def autoPrettify():
    """Improve overall look of code and close all tags automatically (if not already done)."""

    warnings.showwarning(r'''Auto prettifying also involves auto closing unclosed HTML tags which may not be accurate if not used after development is complete. 
    Use after all development for best results. See "bs4 auto closing tags" for more info.''', UserWarning, 'main_htm.py', 110)
    # check_unclosed()
    with open("index.html", 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')
        auto_close_all_tags = soup.prettify()
        with open("index.html", 'w') as f:
            f.write(auto_close_all_tags)
