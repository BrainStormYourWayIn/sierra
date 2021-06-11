# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 09:32:38 2021
"""

#from flask import Flask
from bs4 import BeautifulSoup
import warnings
import webbrowser

# {index} = input('Enter the name of your HTML file')
index = 'index'
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
<title>{Title}</title>
<link rel="stylesheet" href="style.css">""")

    if type(icon) == str and icon.split('.')[-1] != '.ico':
        open(f'{index}.html', 'a+').write(f"""<link rel="shortcut icon" href={icon}>""")
    
    open('style.css', 'w').write('')

def add_font(font_link):
    with open(f'{index}.html', 'a') as f:
        f.write(f'\n<link href={font_link} rel="stylesheet">')

def head(Head, font_size, type='header', font_family="Arial", color='black', text_align='left', background_color='white', padding='0px', height=None, width=None, line_break=None, line_height=None):
    """
    Args:
        Head (str, compulsory)           : Caption header.
        type (str, optional)             : Header Size. Anything from h1 to h6. Leave blank, if not valid. Defaults to 'header'.
        font_size (str, compulsory)      : CSS Font-size parameter.
        font_family (str, optional)      : CSS Font-family parameter. Defaults to Arial.
        color (str, optional)            : CSS color parameter. Defaults to 'black'.
        text_align (str, optional)       : CSS text-align parameter. left|right|center|justify|initial|inherit. Defaults to 'left'.
        background_color (str, optional) : CSS Background-color parameter. Defaults to 'white'.
        padding (str, optional)          : CSS Padding parameter. Defaults to '0px'.
        height (str, optional)           : CSS Height parameter. Defaults to None.
        width (str, optional)            : CSS Width Parameter. Defaults to None.
        line_break (str, optional)       : CSS Line-break parameter. Defaults to None.
        line_height (str, optional)      : CSS line-height parameter. Defaults to None. 
    """

    # if type == False and font_size == False:
    #     type = 'header'
    # elif type != False and len(type) != 2:
    #     type = 'header'
    # elif font_size and type:
    #     warnings.showwarning("args 'type' and 'font_size' have been entered in head(). It is recommended to rectify or only font_size is considered", UserWarning, str(bytes), int(1))
    # elif type == False:
    #     type == 'header'

    with open(f'{index}.html', 'a') as f:
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
}}''')
        #elif type and font_size:
        #    print(r"Only type or font_size accepted in head()")
        
#head('nothing more', 'h5', False, 'rgb(50, 168, 82)', 'Arial', 'center')
#head('nothing more', False, False, False, False, False)
# No hex accepted for color in head(). RGB and normal eng works.
# If arguments font_size and type are passed, font_size seems to be given preference CSS
# In head(), color must have black as default. 
# In head(), type OR font_size are required arguments. At least one of them must be passed. 
# Warn the users that if arguments font_size and type, both are passed, font_size seems to be given preference by CSS. But, at least one argument MUST be passed.
# No hex accepted for color in head() iff type is mentioned. RGB and normal eng works. Haven't tested other mediums.

#def tags(open_tags=False, close_tags=False, *args):
#    if open_tags == False and close_tags == False:
#        pass
#    elif open_tags == False and close_tags == True:
#        for arg in args:
#            with open(f'{index}.html', 'a') as f

def open_tags(any_tag, *args):
    with open(f'{index}.html', 'a') as f:
        f.write(f'''\n<{any_tag}>''')
        for arg in args:
            f.write(f'''\n<{arg}>''')

def close_tags(any_tag, *args):
    with open(f'{index}.html', 'a') as f:
        f.write(f'''\n</{any_tag}>''')
        for arg in args:
            f.write(f'''\n</{arg}>''')

def close_tag_before(tag_to_close, tag_to_close_before):
    with open(f'{index}.html', 'r') as f:
        tag_to_close_before = f"<{tag_to_close_before}>"
        tag_to_close = f"</{tag_to_close}>"
        closed_tag = tag_to_close + f"\n{tag_to_close_before}"
        f = f.read()
        now_closed = f.replace(tag_to_close_before, closed_tag)
        open(f'{index}.html', 'w+').write(f'''{now_closed}''')

#def css(self, tag_to_style, *args):
#    var = tag_to_style, *args

#def css_att(lol):
#    print(var, lol)

#x = tags()
#x.open_tags('tag3', 'tag1', 'tag2')
#x.close_tags('tag1', 'tag2')
#x.close_tag_before('tag3', 'tag2')

#with open(ff'{index}.html', 'r') as f:
#    newlines = f.read()
#    newlines = newlines.replace('<tag1>', '<tag4>')
#    print(newlines)

def AutoCloseTags():
    warnings.showwarning(f'''Auto closing HTML tags may not be accurate and are not recommended. Further 
    development may run into issues. Please close tags manually if unsure. It is recommended to use after all development. See "bs4 auto closing tags" for more info.''', UserWarning, str, int(2))
    
    with open(f'{index}.html', 'r+') as f:
        soup = BeautifulSoup(f, 'html.parser')
        auto_close_all_tags = soup.prettify()
        open(f'{index}.html', 'w+').write(f'''{auto_close_all_tags}''')

def startBody(background=None, background_color='white', background_image=None, opacity='1', background_size='cover', background_attachment='fixed', background_position=None, background_repeat=None):
    """Opens the <body> tag and styles using CSS."""

    open(f'{index}.html', 'a').write('\n<body>')
    with open('style.css', 'a') as s:
        s.write(f'''
body {{
    background: {background};
    background-color: {background_color};
    background-image: {background_image};
    opacity: {opacity};
    background-size: {background_size};
    background-attachment: {background_attachment};
    background-position: {background_position};
    background-repeat: {background_repeat};
}}''')

# Should be used after StartBody() and before EndBody()
def AddPicture(src, alt=None, height=None, width=None):
    open(f'{index}.html', 'a').write(f"""<img src="{src}" alt="{alt}" height={height} width={width}>""")

def WriteHTML(text):
    """Writes the given text to the html file."""
    open(f'{index}.html', 'a+').write(text)

def WriteCSS(text):
    """Writes the given code to the CSS file."""
    open('style.css', 'a').write(text)

def endBody():
    """closes </body> tag."""
    open(f'{index}.html', 'a').write(f'''\n</body>''')

# Initc() if used, must always come after title()
def addInitc(box_sizing='False', margin='0px', padding='0px', border='0px', position='relative'):
    """
    Args:
        box_sizing (str, optional)  : CSS box-sizing parameter. Defaults to 'False'.
        margin (str, optional)      : CSS margin parameter. Defaults to '0px'.
        padding (str, optional)     : CSS padding parameter. Defaults to '0px'.
        border (str, optional)      : CSS border parameter. Defaults to '0px'.
        position (str, optional)    : CSS position parameter. Defaults to 'relative'.
    """

    with open('style.css', 'a') as s:
        s.write(f'''*,*:before,*:after {{
    box-sizing:{box_sizing};
    margin:{margin};
    padding:{padding};
    border:{border};
    position: {position};
}}''')

# Class cTags
class cTags():
    def __init__(self, tag):
        self.tag = tag

    def css(self, color='black', font_family='Arial', font_weight='normal', text_align='left', font_size='16px', background_color='white', background='inherit', margin_top='0px', margin_bottom='0px', margin_left='0px', margin_right='0px', border='0px', display='block', padding='0px', height=None, width=None, line_break=None, line_height=None, overflow=None, margin='0px', box_shadow="none"):
        """
        Args:
            color (str, optional)            : CSS color parameter. Defaults to 'black'.
            font_family (str, optional)      : CSS font-family parameter. Defaults to 'Arial'.
            font_weight (str, optional)      : CSS font-weight parameter. Defaults to 'normal'.
            text_align (str, optional)       : CSS text-align parameter. Defaults to 'left'.
            font_size (str, optional)        : CSS font-size parameter. Defaults to '16px'.
            background_color (str, optional) : CSS background-color parameter. Defaults to 'white'.
            background (str, optional)       : CSS background parameter. Defaults to 'inherit'.
            margin_top (str, optional)       : CSS margin-top parameter. Defaults to '0px'.
            margin_bottom (str, optional)    : CSS margin-bottom parameter. Defaults to '0px'.
            margin_left (str, optional)      : CSS margin-left parameter. Defaults to '0px'.
            margin_right (str, optional)     : CSS margin-right parameter. Defaults to '0px'.
            border (str, optional)           : CSS border parameter. Defaults to '0px'.
            display (str, optional)          : CSS display parameter. Defaults to 'block'.
            padding (str, optional)          : CSS padding parameter. Defaults to '0px.
            height (str, optional)           : CSS height parameter. Defaults to None.
            width (str, optional)            : CSS width parameter. Defaults to None.
            line_break (str, optional)       : CSS line-break parameter. Defaults to None.
            line_height (str, optional)      : CSS line-height parameter. Defaults to None.
            overflow (str, optional)         : CSS overflow parameter. Defaults to None.
            margin (str, optional)           : CSS margin parameter. Defaults to "0px".
            box_shadow (str, optional)       : CSS box-shadow parameter. Defaults to "none".
        """

        with open('style.css', 'a') as s:
            s.write(f'''\n{self.tag} {{
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
#x.open_tags('tag1')
#y = cTags('tag1')
#y.css(color='blue')

# Class tTags()
class tTags():
    def __init__(self, p=False, div_class=False, sec_class=False):
        self.p = p
        self.div_class = div_class
        self.sec_class = sec_class

    def start_p(self, p_text):
        """Opens and closes the <p> tag."""
        open(f'{index}.html', 'a+').write(f'''\n<p> \n{p_text} \n</p>''')

    #d_class = 'dummy_var'
    def start_div(self, d_class):
        """Opens the <div> tag."""
        with open(f'{index}.html', 'a') as f:
            f.write(f'''\n<div class="{d_class}">''')
            #f.write(f'''<div class="{d_class}">''')
    
    #s_class = 'dummy_var'
    def start_sec(self, s_class):
        open(f'{index}.html', 'a+').write(f'''\n<section class="section {s_class}">''')
            
    def css(self, color='black', font_family='Arial', font_weight='normal', text_align='left', font_size='16px', background_color='white', background='inherit', margin_top='0px', margin_bottom='0px', margin_left='0px', margin_right='0px', border='0px', display='block', padding='0px', height=None, width=None, line_break=None, line_height=None, overflow=None, margin='0px', box_shadow="none"):
        """
        Args:
            color (str, optional)            : CSS color parameter. Defaults to 'black'.
            font_family (str, optional)      : CSS font-family parameter. Defaults to 'Arial'.
            font_weight (str, optional)      : CSS font-weight parameter. Defaults to 'normal'.
            text_align (str, optional)       : CSS text-align parameter. Defaults to 'left'.
            font_size (str, optional)        : CSS font-size parameter. Defaults to '16px'.
            background_color (str, optional) : CSS background-color parameter. Defaults to 'white'.
            background (str, optional)       : CSS background parameter. Defaults to 'inherit'.
            margin_top (str, optional)       : CSS margin-top parameter. Defaults to '0px'.
            margin_bottom (str, optional)    : CSS margin-bottom parameter. Defaults to '0px'.
            margin_left (str, optional)      : CSS margin-left parameter. Defaults to '0px'.
            margin_right (str, optional)     : CSS margin-right parameter. Defaults to '0px'.
            border (str, optional)           : CSS border parameter. Defaults to '0px'.
            display (str, optional)          : CSS display parameter. Defaults to 'block'.
            padding (str, optional)          : CSS padding parameter. Defaults to '0px.
            height (str, optional)           : CSS height parameter. Defaults to None.
            width (str, optional)            : CSS width parameter. Defaults to None.
            line_break (str, optional)       : CSS line-break parameter. Defaults to None.
            line_height (str, optional)      : CSS line-height parameter. Defaults to None.
            overflow (str, optional)         : CSS overflow parameter. Defaults to None.
            margin (str, optional)           : CSS margin parameter. Defaults to "0px".
            box_shadow (str, optional)       : CSS box-shadow parameter. Defaults to "none".
        """

        with open('style.css', 'a') as s:
            if self.p == True:
                s.write(f'''\np {{
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
                s.write(f'''\n.{str(d_class)} {{
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
                s.write(f'''\n.{str(s_class)} {{
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

# Class startTable
class startTable():
    with open('index.html', 'a') as f:
        f.write(f'''\n<table>
<tr>''')

    #def __init__(self, rows:int, columns:int):
    #    self.columns = columns
    #    self.rows = rows
    #    cList = [*range(1, 1+columns)]
    #    rList = [*range(1, 1+rows)]
    
    # tHead is always a list, and len(tHead) = columns
    def table(self, tHead):
        for header in tHead:
            with open('index.html', 'a') as f:
                f.write(f'''\n<th>{header}</th>''')
        with open('index.html', 'a') as f:
            f.write(f'''\n</tr>''')

    def close():
        with open('index.html', 'a') as f:
            f.write(f'''\n</table>''')

if __name__ == "__main__":

    title('nothing')
    #addInitc()
    head('nothing more', font_size='90px', color='blue', text_align='center', background_color='orange')
    startBody(background_color='green', opacity=0.8)
    
    x = tTags(True)
    x.start_p("I'm sure about this man")
    x.css(color='red', background_color='orange', line_height='25px')
    close_tags('p')

    d_class = 'newClass'
    x = tTags(div_class=True)
    x.start_div(d_class)
    x.css(color='yellow', font_family='Times New Roman', background_color='blue')

    writeHtm("I'm REALLY" + b + "sure of this")
    close_tags('div')

    s_class = 'anotherClass'
    x = tTags(sec_class=True)
    x.start_sec(s_class)
    x.css(color='whitesmoke', background_color='rgb(35, 51, 89)')

    writeHtm("I'm defo" + b + "sure of this")
    close_tags('section')

    endBody()

    a = startTable()
    tHead = ['one', 'two']
    a.table(tHead)
    a.close

    closeHTML()
    
    AutoCloseTags()
