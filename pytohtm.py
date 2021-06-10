# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 09:32:38 2021
"""

#from flask import Flask
from bs4 import BeautifulSoup
import warnings

# {index} = input('Enter the name of your HTML file')
index = 'index'

# icon argument must be a .ico file
# def check_tag_open(tag):
b = ' <br> '

def title(Title, icon=None):
    """
    Args:
        Title(str, compulsory)   : Title of the HTML file.
        icon(str, optional)      : Icon to be displayed. Should be a .ico file. Defaults to no icon.
    """

    with open(f'{index}.html', 'w+') as f:
        f.write(f"""<!DOCTYPE html>
<html lang="en">
<meta charset="utf-8">
<head>
<title>{Title}</title>\n""")
    if type(icon) == str and icon.split('.')[-1] != '.ico':
        with open(f'{index}.html', 'a+') as f:
            f.write(f"""<link rel='shortcut icon' href={icon}>
<link rel="stylesheet" href="style.css">\n""")


def add_font(font_link):
    with open(f'{index}.html', 'a+') as f:
        f.write(f'<link href={font_link} rel="stylesheet">')

def head(Head, font_size=None, font_family="Arial", type='header', color='black', text_align='left', background_color='white', padding='None', height='None', width='None', line_break='None', line_height='None'):
    """
    Args:
        Head (str, compulsory)           : Caption header.
        font_size (str, compulsory)      : Font size in any valid measure. Leave blank, if not valid.
        font_family (str, compulsory)    : any possible Font family. Defaults to Arial.
        type (str, optional)             : Header Size. Anything from h1 to h6. Leave blank, if not valid. Defaults to 'header'.
        color (str, optional)            : Color of Font in hex code. Defaults to '#000000'.
        text_align (str, optional)       : left|right|center|justify|initial|inherit. Defaults to 'left'.
        background_color (str, optional) : Background color. Defaults to '#FFFFFF'.
        padding (str, optional)          : Padding. Defaults to None.
        height (str, optional)           : Height of text. Defaults to None.
        width (str, optional)            : Width of text. Defaults to None.
        line_break (str, optional)       : Line break. Defaults to None.
        line_height (str, optional)      : Line height. Defaults to None. 
    """

    # if type == False and font_size == False:
    #     type = 'header'
    # elif type != False and len(type) != 2:
    #     type = 'header'
    # elif font_size and type:
    #     warnings.showwarning("args 'type' and 'font_size' have been entered in head(). It is recommended to rectify or only font_size is considered", UserWarning, str(bytes), int(1))
    # elif type == False:
    #     type == 'header'

    with open(f'{index}.html', 'a+') as f:
        f.write(f'''\n<{type}>{Head}</{type}>
</head>\n''')
        with open('style.css', 'a+') as s:
                s.write(f'''{type} {{
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
}}''')
        #elif type and font_size:
            #print("Only type or font_size accepted in head()")
        

#head('nothing more', 'h5', False, 'rgb(50, 168, 82)', 'Arial', 'center')
#head('nothing more', False, False, False, False, False)
# No hex accepted for color in head(). RGB and normal eng works.
# If arguments font_size and type are passed, font_size seems to be given preference CSS
# In head(), color must have black as default. 
# In head(), type OR font_size are required arguments. At least one of them must be passed. 
# Warn the users that if arguments font_size and type, both are passed, font_size seems to be given preference 
# by CSS. But, at least one argument MUST be passed.
# No hex accepted for color in head() iff type is mentioned. RGB and normal eng works. Haven't tested
# other mediums.
# In title(), default value of ico and css_bool are False. 
# Also in title(), icon argument MUST be a .ico file. Check if the last 4 letters are '.ico'
# In head() in the argument font_family, the users MUST enter it in double quotes. Typically, it can be 
# something like
# font-family: 'Roboto', sans-serif; in CSS. But when the user is entering the value of
# font_family as ''Roboto', sans-serif' there's a SyntaxError, since there is a single quote within
# # a single quote. Hence, they must always enter it in double quotes.

# check soup.a.prettify()
# def tags(open_tags=False, close_tags=False, *args):
#     if open_tags == False and close_tags == False:
#         pass
#     elif open_tags == False and close_tags == True:
#         for arg in args:
#             with open(f'{index}.html', 'a') as f

def open_tags(any_tag, *args):
    with open(f'{index}.html', 'a+') as f:
        f.write(f'''\n<{any_tag}>''')
        for arg in args:
            f.write(f'''\n<{arg}>''')



def close_tags(any_tag, *args):
    with open(f'{index}.html', 'a+') as f:
        f.write(f'''\n</{any_tag}>''')
        for arg in args:
            f.write(f'''\n</{arg}>''')



def close_tag_before(tag_to_close, tag_to_close_before):
    with open(f'{index}.html', 'r+') as f:
        tag_to_close_before = f"<{tag_to_close_before}>"
        tag_to_close = f"</{tag_to_close}>"
        closed_tag = tag_to_close + f"\n{tag_to_close_before}"
        f = f.read()
        now_closed = f.replace(tag_to_close_before, closed_tag)
        with open(f'{index}.html', 'w+') as f:
            f.write(f'''{now_closed}''')

# def css(self, tag_to_style, *args):
#     var = tag_to_style, *args
#     def css_att(lol):
#         print(var, lol)

# x = tags()
# x.open_tags('tag3', 'tag1', 'tag2')
# x.close_tags('tag1', 'tag2')
# x.close_tag_before('tag3', 'tag2')

# with open(ff'{index}.html', 'r') as f:
#     newlines = f.read()
#     newlines = newlines.replace('<tag1>', '<tag4>')
#     print(newlines)

def AutoCloseTags():

    warnings.showwarning(f'''Auto closing HTML tags may not be accurate and are not recommended. Further 
    development may run into issues. Please close tags manually if unsure. It is recommended to use after all development. See "bs4 auto closing tags" for more info.''', UserWarning, str, int(2))
    
    with open(f'{index}.html', 'r+') as f:
        soup = BeautifulSoup(f, 'html.parser')
        auto_close_all_tags = soup.prettify()
        with open(f'{index}.html', 'w+') as f:
            f.write(f'''{auto_close_all_tags}''')

#auto_close_tags() 
#AutoCloseTags()
#def (close_tag, open_new)

class cTags():
    def __init__(self, tag):
        self.tag = tag

    def css(self, color='black', font_family='Arial', font_weight=None, text_align=None, font_size=None, background_color='white', background=None, margin_top='0px', margin_bottom='0px', margin_left='0px', margin_right='0px', border='0px', display='block', padding=None, height=None, width=None, line_break=None, line_height=None):
        """
        Args:
            color (str, optional)            : CSS Color parameter. Defaults to 'black'.
            font_family (str, optional)      : CSS Font-Family parameter. Defaults to 'Arial'.
            font_weight (str, optional)      : CSS Font-weight parameter. Defaults to None.
            text_align (str, optional)       : CSS Text-align parameter. Defaults to None.
            font_size (str, optional)        : CSS Font-size parameter. Defaults to None.
            background_color (str, optional) : CSS Background-color parameter. Defaults to 'white'.
            background (str, optional)       : CSS Background parameter. Defaults to None.
            margin_top (str, optional)       : CSS margin-top parameter. Defaults to '0px'.
            margin_bottom (str, optional)    : CSS margin-bottom parameter. Defaults to '0px'.
            margin_left (str, optional)      : CSS margin-left parameter. Defaults to '0px'.
            margin_right (str, optional)     : CSS margin-right parameter. Defaults to '0px'.
            border (str, optional)           : CSS border parameter. Defaults to '0px'.
            display (str, optional)          : CSS display parameter. Defaults to 'block'.
            padding (str, optional)          : CSS padding parameter. Defaults to ''None.
            height (str, optional)           : CSS height parameter. Defaults to None.
            width (str, optional)            : CSS width parameter. Defaults to None.
            line_break (str, optional)       : CSS line-break parameter. Defaults to None.
            line_height (str, optional)      : CSS line-height parameter. Defaults to None.
        """
        with open('style.css', 'a+') as f:
            f.write(f'''
{self.tag} {{
    color: {color};
    font-family: {font_family};
    font-weight: {font_weight};
    text-align: {text_align};
    font-size: {font_size};
    background-color: {background_color};
    background: {background};
    margin-top: {margin_top};
    margin-bottom: {margin_bottom};
    margin-left: {margin_left};
    margin-right: {margin_right};
    border: {border};
    display: {display};
    padding: {padding};
    height: {height};
    width: {width};
    line-break: {line_break};
    line-height: {line_height};
}}''')

#x = tags()
#x.open_tags('tag1')
#y = cTags('tag1')
#y.css(color='blue')

# open class textTags()

class tTags():
    def __init__(self, p=False, div_class=False, sec_class=False):
        self.p = p
        self.div_class = div_class
        self.sec_class = sec_class

    def start_p(self, p_text):
        with open(f'{index}.html', 'a+') as f:
            f.write(f'''\n<p> \n{p_text} \n</p>''')

    #d_class = 'dummy_var'
    def start_div(self, d_class):
        with open(f'{index}.html', 'a+') as f:
            f.write(f'''\n<div class="{d_class}">''')
            #f.write(f'''<div class="{d_class}">''')
    
    #s_class = 'dummy_var'
    def start_sec(self, s_class):
        with open(f'{index}.html', 'a+') as f:
            f.write(f'''\n<section class="section {s_class}">''')
            
    def css(self, color='black', font_family='Arial', font_weight=False, text_align=False, font_size=False, background_color=False, background=False, margin_top=False, margin_bottom=False, margin_left=False, margin_right=False, border=False, display='block', padding=False, height=False, width=False, line_break=False, line_height=False):
        with open('style.css', 'a+') as s:
            if self.p == True:
                s.write("\np {{")
            elif self.div_class == True:
                s.write(f"\n.{self.div_class} {{")
            elif self.sec_class == True:
                s.write(f"\n.{self.sec_class} {{")

        with open('style.css', 'a+') as s:
            s.write(f'''
    color: {color};
    font-family: {font_family};
    font-weight: {font_weight};
    text-align: {text_align};
    font-size: {font_size};
    background-color: {background_color};
    background: {background};
    margin-top: {margin_top};
    margin-bottom: {margin_bottom};
    margin-left: {margin_left};
    margin-right: {margin_right};
    border: {border};
    display: {display};
    padding: {padding};
    height: {height};
    width: {width};
    line-break: {line_break};
    line-height: {line_height};
}}''')


def startBody(background=None, background_color='white', background_image=None, opacity='1', background_size='cover', background_attachment='fixed', background_position=None, background_repeat=None):
    with open(f'{index}.html', 'a') as f:
        f.write(f'''\n<body>''')
    with open('style.css', 'a') as s:
        s.write(f'''\nbody {{
background: {background};
background-color: {background_color};
background-image: {background_image};
opacity: {opacity};
background-size: {background_size};
background-attachment: {background_attachment};
background-position: {background_position};
background-repeat: {background_repeat};
}}''')


def WriteHTML(text):
    """Writes the given text to the html file."""

    open(f'{index}.html', 'a+').write(text)


def WriteCSS(text):
    """Writes the given code to the CSS file."""

    open('style.css', 'a').write(text)


if __name__ == "__main__":
    #title('Test')
    #head('This is the header', '20px', 'Arial')
    #AutoCloseTags()
    title('nothing')
    head('nothing more', font_size='90px', color='blue', text_align='center', background_color='orange')
    startBody(background_color='green', opacity=0.5)
    
    x = tTags(True)
    x.start_p("I'm sure about this man")
    x.css(color='green')

    d_class = 'newClass'
    x = tTags(div_class=True)
    x.start_div(d_class)
    x.css(color='yellow', font_family='Times New Roman', background_color='blue')

    WriteHTML("I'm REALLY" + b + "sure of this")
    close_tags('div')

    s_class = 'anotherClass'
    x = tTags(sec_class=True)
    x.start_sec(s_class)
    x.css(color='purple', background_color='green')

    WriteHTML("I'm defo" + b + "sure of this")
    close_tags('section')

    #endBody()
    #AutoCloseTags()
