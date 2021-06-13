# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 09:32:38 2021
"""
#from flask import Flask
from bs4 import BeautifulSoup
import warnings
import pandas as pd

#b = ' <br> '

def closeHTML():
    """Closes the <HTML> tag."""
    
    open("index.html", 'a').write(f'''\n</html>''')

def title(Title, icon=False):
    """
    Args:
        Title(str, compulsory)   : Title of the HTML file.
        icon(str, optional)      : Icon to be displayed. Should be a .ico file. Defaults to no icon.
    """

    with open("index.html", 'w') as f:
        
        f.write(f'''<!DOCTYPE html>
<html lang="en">
<meta charset="utf-8">
<head>
<title>{Title}</title>
<link rel="stylesheet" href="style.css">''')

        if type(icon) == str and icon.split('.')[-1] == '.ico':
            f.write(f'''\n<link rel="shortcut icon" href={icon}>''')
    open('style.css', 'w').write('')

def addFont(font_link):
    with open("index.html", 'a') as f:
        f.write(f'''\n<link href={font_link} rel="stylesheet">''')

#Head:
# head type is h1 to h6
# size in any valid measure
# text-align: left|right|center|justify|initial|inherit

def head(Head, type='header', color='black',font_family="Arial", text_align='left', font_size=False, background_color=False, padding=False, height=False, width=False, line_break=False, line_height=False, border=False, margin=False):
    """
    Args:
        Head (str, compulsory)           : Caption header.
        type (str, optional)             : Header Size. Anything from h1 to h6. Leave blank, if not valid. Defaults to 'header'.
        color (str, optional)            : CSS Color parameter. Defaults to 'black'.
        font_family (str, optional)      : CSS font-family parameter. Defaults to Arial.
        text_align (str, optional)       : CSS text-align parameter. left|right|center|justify|initial|inherit. Defaults to 'left'.
        font_size (str, optional)        : CSS font-size parameter in any valid measure. Leave blank, if not valid.
        background_color (str, optional) : CSS background-color parameter. Defaults to 'white'.
        padding (str, optional)          : CSS padding parameter. Defaults to False.
        height (str, optional)           : CSS height parameter. Defaults to False.
        width (str, optional)            : CSS width parameter. Defaults to False.
        line_break (str, optional)       : CSS line-break parameter. Defaults to False.
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
    #    type = 'header'

    with open("index.html", 'a') as f:
        f.write(f'''\n<{type}>{Head}</{type}>
</head>''')
        with open('style.css', 'a') as s:
                s.write(f'''\n{type} {{
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

#head('nothing more', 'h5', False, 'rgb(50, 168, 82)', 'Arial', 'center')
#head('nothing more', False, False, False, False, False)
# No hex accepted for color in head(). RGB and normal eng works.
# If arguments font_size and type are passed, font_size seems to be given preference CSS

# In head(), color must have black as default. 
# In head(), type OR font_size are required arguments. At least one of them must be passed. 
# Warn the users that if arguments font_size and type, both are passed, font_size seems to be given preference by CSS.
# But, at least one argument MUST be passed.
# No hex accepted for color in head() if type is mentioned. RGB and normal eng works. Haven't tested other mediums.
# In title(), default value of ico and css_bool are False. 
# Also in title(), icon argument MUST be a .ico file. Check if the last 4 letters are '.ico'
# In head() in the argument font_family, the users MUST enter it in double quotes. Typically, it can be something like
# check soup.a.prettify()

# def tags(openTags=False, closeTags=False, *args):
#     if openTags == False and closeTags == False:
#         pass
#     elif openTags == False and closeTags == True:
#         for arg in args:
#             with open("index.html", 'a') as f

def openTags(any_tag, *args):
    """Opens any HTML  or XML tag."""
    with open("index.html", 'a') as f:
        f.write(f'''\n<{any_tag}>''')
        for arg in args:
            f.write(f'''\n<{arg}>''')
            
def closeTags(any_tag, *args):
    """Closes any HTML or XML tag."""
    with open("index.html", 'a') as f:
        f.write(f'''\n</{any_tag}>''')
        for arg in args:
            f.write(f'''\n</{arg}>''')
            
def closeTagBefore(tag_to_close, tag_to_close_before):
    with open("index.html", 'r') as f:
        tag_to_close_before = f"<{tag_to_close_before}>"
        tag_to_close = f"</{tag_to_close}>"
        closed_tag = tag_to_close + f"\n{tag_to_close_before}"
        text = f.read()
        now_closed = text.replace(tag_to_close_before, closed_tag)
        open("index.html", 'w').write(f'''{now_closed}''')

    # def css(self, tag_to_style, *args):
    #     var = tag_to_style, *args
    #     def css_att(lol):
    #         print(var, lol)

# x = tags()
# x.openTags('tag3', 'tag1', 'tag2')
# x.closeTags('tag1', 'tag2')
# x.close_tag_before('tag3', 'tag2')

# with open("index.html", 'r') as f:
#     newlines = f.read()
#     newlines = newlines.replace('<tag1>', '<tag4>')
#     print(newlines)

def autoPrettify():
    """Close all tags automatically."""

    warnings.showwarning(r'''Auto prettifying also involves auto closing HTML tags which may not be accurate if not already closed and are not recommended. Further development may run into issues. Please close tags manually if unsure.
    It is recommended to use after all development for best results. See "bs4 auto closing tags" for more info.''', UserWarning, str, int(2))
    
    with open("index.html", 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')
        auto_close_all_tags = soup.prettify()
        with open("index.html", 'w') as f:
            f.write(f'''{auto_close_all_tags}''')

class cTags():
    def __init__(self, tag):
        self.tag = tag

    def css(self, color='black', font_family='Arial', font_weight=False, text_align=False, font_size=False, background_color=False, background=False, margin_top=False, margin_bottom=False, margin_left=False, margin_right=False, border=False, display='block', padding=False, height=False, width=False, line_break=False, line_height=False, overflow=False, margin=False, box_shadow=False):

        """
        Args:
            color (str, optional)            : CSS Color parameter. Defaults to 'black'.
            font_family (str, optional)      : CSS Font-Family parameter. Defaults to 'Arial'.
            font_weight (str, optional)      : CSS Font-weight parameter. Defaults to False.
            text_align (str, optional)       : CSS Text-align parameter. Defaults to False.
            font_size (str, optional)        : CSS Font-size parameter. Defaults to False.
            background_color (str, optional) : CSS background-color parameter. Defaults to 'white'.
            background (str, optional)       : CSS background parameter. Defaults to False.
            margin_top (str, optional)       : CSS margin-top parameter. Defaults to '0px'.
            margin_bottom (str, optional)    : CSS margin-bottom parameter. Defaults to '0px'.
            margin_left (str, optional)      : CSS margin-left parameter. Defaults to '0px'.
            margin_right (str, optional)     : CSS margin-right parameter. Defaults to '0px'.
            border (str, optional)           : CSS border parameter. Defaults to '0px'.
            display (str, optional)          : CSS display parameter. Defaults to 'block'.
            padding (str, optional)          : CSS padding parameter. Defaults to ''False.
            height (str, optional)           : CSS height parameter. Defaults to False.
            width (str, optional)            : CSS width parameter. Defaults to False.
            line_break (str, optional)       : CSS line-break parameter. Defaults to False.
            line_height (str, optional)      : CSS line-height parameter. Defaults to False.
            overflow (str, optional)         : CSS overflow parameter. Defaults to False.
            margin (str, optional)           : CSS margin parameter. Defaults to False.
            box_shadow (str, optional)       : CSS box-shadow parameter. Defaults to False.
        """

        with open('style.css', 'a') as s:
            s.write(f'''\n{str(self.tag)} {{
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
    overflow: {overflow};
    margin: {margin};
    box-shadow: {box_shadow};
}}''')

#x = tags()
#x.openTags('tag1')
#y = cTags('tag1')
#y.css(color='blue')

class tTags():
    def __init__(self, p=False, div_class=False, sec_class=False):
        self.p = p
        self.div_class = div_class
        self.sec_class = sec_class

    def start_p(self, p_text: str):
        """Opens the <p> tag.
        
        Args: 
            p_text (str, compulsory): the text that has to be displayed.
        """

        open("index.html", 'a+').write(f"\n<p> \n{p_text}")

    #d_class = 'dummy_var'
    def start_div(self, d_class: str):
        """starts the <div> tag.

        Args:
            d_class (str, compulsory): the class name of the <div> tag
    
        """
        with open("index.html", 'a+') as f:
            f.write(f'''\n<div class="{d_class}">''')
            #f.write(f'''<div class="{d_class}">''')
    
    #s_class = 'dummy_var'
    def start_sec(self, s_class):
        """Starts the <section> tag.

        Args:
            s_class (str, compulsory): The class name of the <section> tag.
        """

        open("index.html", 'a+').write(f'''\n<section class="section {s_class}">''')
            
    def css(self, color='black', font_family='Arial', font_weight=False, text_align=False, font_size=False, background_color=False, background='False', margin_top=False, margin_bottom=False, margin_left=False, margin_right=False, border=False, display='block', padding=False, height=False, width=False, line_break=False, line_height=False, overflow=False, margin=False, box_shadow=False):
        """
        Args:
            color (str, optional)            : CSS Color parameter. Defaults to 'black'.
            font_family (str, optional)      : CSS Font-Family parameter. Defaults to 'Arial'.
            font_weight (str, optional)      : CSS Font-weight parameter. Defaults to False.
            text_align (str, optional)       : CSS Text-align parameter. Defaults to False.
            font_size (str, optional)        : CSS Font-size parameter. Defaults to False.
            background_color (str, optional) : CSS background-color parameter. Defaults to 'white'.
            background (str, optional)       : CSS background parameter. Defaults to False.
            margin_top (str, optional)       : CSS margin-top parameter. Defaults to '0px'.
            margin_bottom (str, optional)    : CSS margin-bottom parameter. Defaults to '0px'.
            margin_left (str, optional)      : CSS margin-left parameter. Defaults to '0px'.
            margin_right (str, optional)     : CSS margin-right parameter. Defaults to '0px'.
            border (str, optional)           : CSS border parameter. Defaults to '0px'.
            display (str, optional)          : CSS display parameter. Defaults to 'block'.
            padding (str, optional)          : CSS padding parameter. Defaults to False.
            height (str, optional)           : CSS height parameter. Defaults to False.
            width (str, optional)            : CSS width parameter. Defaults to False.
            line_break (str, optional)       : CSS line-break parameter. Defaults to False.
            line_height (str, optional)      : CSS line-height parameter. Defaults to False.
            overflow (str, optional)         : CSS overflow parameter. Defaults to False.
            margin (str, optional)           : CSS margin parameter. Defaults to False.
            box_shadow (str, optional)       : CSS box-shadow parameter. Defaults to False.
        """
        
        with open('style.css', 'a') as s:
            if self.p == True:
                s.write(f'''
p {{
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
    overflow: {overflow};
    margin: {margin};
    box-shadow: {box_shadow};
}}''')
            elif self.div_class == True:
                s.write(f'''
.{self.div_class} {{
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
    overflow: {overflow};
    margin: {margin};
    box-shadow: {box_shadow};
}}''')
            elif self.sec_class == True:
                s.write(f'''
.{self.sec_class} {{
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
    overflow: {overflow};
    margin: {margin};
    box-shadow: {box_shadow};
}}''')

def writeHtm(text):
    """Writes the given text to the html file."""

    with open("index.html", 'a') as f:
        f.write(f'''\n{text}''')

def writeCSS(tag, *args):
    """Writes the given code to the CSS file."""

    with open('style.css', 'a+') as s:
        s.write(f"""\n{tag} {{""")
        print(args)
        for parameter, value in args[0].items():
            s.write(f"""\n\t{parameter}: {value};""")
        s.write("\n}")

def openBody(background='False', background_color='white', background_image=False, opacity=False, background_size='cover', background_attachment='fixed', background_position=False, background_repeat=False):
    """Opens the body tag and adds the required CSS."""
    
    open("index.html", 'a').write(f'''\n<body>''')
    with open('style.css', 'a') as s:
        s.write(f'''
body {{
    background : {background}
    background-color: {background_color};
    background-image: {background_image};
    opacity: {opacity};
    background-size: {background_size};
    background-attachment: {background_attachment};
    background-position: {background_position};
    background-repeat: {background_repeat};
}}''')
        
def closeBody():
    """Closes the body tag."""
    open("index.html", 'a').write(f'''\n</body>''')

# Initc() if used, must always come after title()

def addInitc(box_sizing='False', margin=False, padding=False, border=False, position='relative'):
    """
    Args:
        box_sizing (str, optional)  : CSS box-sizing parameter. Defaults to 'False'.
        margin (str, optional)      : CSS margin parameter. Defaults to False.
        padding (str, optional)     : CSS padding parameter. Defaults to False.
        border (str, optional)      : CSS border parameter. Defaults to False.
        position (str, optional)    : CSS position parameter. Defaults to 'relative'.
    """
    
    with open('style.css', 'a') as s:
        s.write(f'''
*,*:before,*:after {{
    box-sizing:{box_sizing};
    margin:{margin};
    padding:{padding};
    border:{border};
    position: {position};
}}''')

class startTable():
    #def __init__(self, rows:int, columns:int):
    #    self.columns = columns
    #    self.rows = rows
    #    cList = [*range(1, 1+columns)]
    #    rList = [*range(1, 1+rows)]
    
    # tHead is always a list, and len(tHead) = columns

    def table(self, tHead):
        for header in tHead:
            with open("index.html", 'a') as f:
                f.write(f'''\n<th>{header}</th>''')
        with open("index.html", 'a') as f:
            f.write(f'''\n</tr>''')

    def close():
        with open("index.html", 'a') as f:
            f.write(f'''\n</table>''')

    def createTable(self, cols:list, rows:list):
        with open("index.html", 'a') as f:
            f.write(f'''\n<table>
<tr>''')
        for col in cols:
            open("index.html", 'a').write(f'''\n<th>{col}</th>''')
        open("index.html", 'a').write(f'''\n</tr>''')
        for row in rows:
            open("index.html", 'a').write(f'''\n<tr>''')
            for row_d in row:
                open("index.html", 'a').write(f'''\n<td>{row_d}</td>''')
            open("index.html", 'a').write(f'''\n</tr>''')
        open("index.html", 'a').write(f'''\n</table>''')
        
    def getTable(self, dataframe:str):
        df = pd.read_csv(dataframe)
        cols = list(df.columns)
        rows = df.values.tolist()

        with open("index.html", 'a') as f:
            f.write(f'''
<table>
<tr>''')
        for col in cols:
            open("index.html", 'a').write(f'''\n<th>{col}</th>''')
        open("index.html", 'a').write(f'''\n</tr>''')
        for row in rows:
            open("index.html", 'a').write(f'''\n<tr>''')
            for row_d in row:
                open("index.html", 'a').write(f'''\n<td>{row_d}</td>''')
            open("index.html", 'a').write(f'''\n</tr>''')
        open("index.html", 'a').write(f'''\n</table>''')
