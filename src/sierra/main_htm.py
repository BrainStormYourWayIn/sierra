import warnings
from bs4 import BeautifulSoup
import traceback

br = ' <br> '

def title(Title, icon=False):
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
<title>{Title}</title>
<link rel="stylesheet" href="style.css">''')

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
        f.write(f'''\n<link href="{font_link}" rel="stylesheet">''')

# def code(codeblock):
#     """Give the codeblock as a text to display the code in your webpage.

#     Args:
#         codeblock (str, compulsory): The code block.
#     """
    
#     with open("index.html", 'a') as f:
#         f.write(f"\n<code>{codeblock}</code>")

def head(Head, type='header', font_size=False, font_family="Arial", color='black', text_align='left', background_color=False, padding=False, height=False, width=False, line_break=False, line_height=False, border=False, margin=False):
    """
    Args:
        Head (str, compulsory)           : Caption header.
        type (str, optional)             : Header Size. Anything from h1 to h6. Leave blank, if not valid. Defaults to 'header'.
        color (str, optional)            : CSS Color (in any color code or name). Defaults to 'black'.
        font_family (str, optional)      : CSS font-family. Defaults to Arial.
        text_align (str, optional)       : CSS text-align parameter. left|right|center|justify|initial|inherit. Defaults to 'left'.
        font_size (str, optional)        : CSS font-size parameter (in any valid measure). Leave blank, if not valid.
        background_color (str, optional) : CSS background-color parameter. Defaults to 'white'.
        padding (str, optional)          : CSS padding parameter. Defaults to False.
        height (str, optional)           : CSS Height parameter. Defaults to False.
        width (str, optional)            : CSS Width parameter. Defaults to False.
        line_break (str, optional)       : CSS Line-break parameter. Defaults to False.
        line_height (str, optional)      : CSS line-height parameter. Defaults to False. 
        border (str, optional)           : CSS border parameter. Defaults to False.
        margin (str, optional)           : CSS margin parameter. Defaults to False.
    """
    
    #if type == False and font_size == False:
    #    type = 'header'
    #elif type != False and len(type) != 2:
    #    type = 'header'
    #elif font_size and type:
    #    warnings.showwarning("args 'type' and 'font_size' have been entered in head(). It is recommended to rectify or only font_size is considered", UserWarning, str(bytes), int(1))
    #elif type == False:
    #    type == 'header'

    with open(f"index.html", 'a') as f:
        f.write(f'''
<{type}>{Head}</{type}>
</head>''')
        with open('style.css', 'a') as s:
                s.write(f'''
{type} {{
    color: {color};
    font-family: {font_family};
    text-align: {text_align};
    font-size: {font_size};
    background-color: {background_color};
    padding: {padding};
    height: {height};
    width: {width};
    line-break: {line_break};
    line-height: {line_height};
    border: {border};
    margin: {margin};
}}''')
        #elif type and font_size:
            #print("Only type or font_size accepted in head()")
        


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
                f.write(f'''\n<img src="{self.src}" {self.attr}>''')

    def css(self, height='False', width='False', margin='False', vertical_align='False', display='False', border='False', margin_top='False', margin_bottom='False', margin_left='False', margin_right='False', opacity='False', filter='False'):
        """
        Args:
            margin_top (str, optional)       : CSS image margin-top parameter. Defaults to 'False'.
            margin_bottom (str, optional)    : CSS image margin-bottom parameter. Defaults to 'False'.
            margin_left (str, optional)      : CSS image margin-left parameter. Defaults to 'False'.
            margin_right (str, optional)     : CSS image margin-right parameter. Defaults to 'False'.
            border (str, optional)           : CSS image border parameter. Defaults to 'False'.
            display (str, optional)          : CSS image display parameter. Defaults to 'block'.
            height (str, optional)           : CSS image height parameter. Defaults to False.
            width (str, optional)            : CSS image width parameter. Defaults to False.
            margin (str, optional)           : CSS image margin parameter. Defaults to False.
            vertical-align (str, optional)   : CSS image vertical-align parameter. Defaults to False.
            opacity (int/float, optional)    : CSS image opacity parameter. Defaults to False.
            filter (str, optional)           : CSS image filter parameter. Defaults to False.
        """

        with open('style.css', 'a') as s:
            s.write(f'''\nimg {{
    margin-top: {margin_top};
    margin-bottom: {margin_bottom};
    margin-left: {margin_left};
    margin-right: {margin_right};
    border: {border};
    display: {display};
    height: {height};
    width: {width};
    margin: {margin};
    vertical-align: {vertical_align};
    opacity: {opacity};
    filter: {filter};
}}''')



def autoPrettify():
    """Improve overall look of code and close all tags automatically (if not already done)."""

    warnings.showwarning(r'''Auto prettifying also involves auto closing unclosed HTML tags which may not be accurate if not used after development is complete. 
    Use after all development for best results. See "bs4 auto closing tags" for more info.''', UserWarning, str, int(186))
    # check_unclosed()
    with open("index.html", 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')
        auto_close_all_tags = soup.prettify()
        with open("index.html", 'w') as f:
            f.write(f'''{auto_close_all_tags}''')
