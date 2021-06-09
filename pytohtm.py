# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 09:32:38 2021

"""
#from flask import Flask

#nameofhtm = input('Enter the name of your HTML file')

# icon argument must be a .ico file

#def check_tag_open(tag):

from bs4 import BeautifulSoup
import warnings

def title(Title, icon=None):
    with open('nameofhtm.html', 'w') as f:
        if icon == None or icon.split('.')[-1] != '.ico':
            icon = None
        
            f.write(f'''<!doctype html>
<html lang="en">
<meta charset="utf-8">
<head>
<title>{Title}</title>
<link rel="shortcut icon" href={icon}>
<link rel="stylesheet" href="style.css">\n''')

        else:

            f.write(f'''<!doctype html>
<html lang="en">
<meta charset="utf-8">
<head>
<title>{Title}</title>
<link rel="shortcut icon" href={icon}>
<link rel="stylesheet" href="style.css">\n''')
    with open('style.css', 'w') as f:
            f.write('')

def add_font(font_link):
    with open('nameofhtm.html', 'a') as f:
        f.write(f'''<link href={font_link} rel="stylesheet">\n''')

#Head:
# head type is h1 to h6
# size in any valid measure
# text-align: left|right|center|justify|initial|inherit

def head(Head, font_size=None, font_family="Arial", type='h3', color='black', text_align='left', background_color='None'):
    """
    Args:
        Head (str, compulsory)        : Caption header;
        font_size (str, optional)     : Font size in any valid measure;
        font_family (str, optional)   : any possible Font family. Must be entered only in double quotes;
        type (str, optional)          : Header Size. Anything from h1 to h6. None is accepted; 
        color (str, optional)         : Color of Font. Does not take in HEX values;  
        text_align (str, optional)    : left|right|center|justify|initial|inherit. Defaults to 'left'.
    """
    if type == None and font_size == None:
        type = 'header'
    elif type != None and len(type) != 2:
        type = 'header'
    elif font_size and type:
        warnings.showwarning("agrs 'type' and 'font_size' have been entered in head(). It is recommended to rectify or only font_size is considered", UserWarning, str(bytes), int(1))
    
    with open('nameofhtm.html', 'a') as f:
        f.write(f'''<{type}>{Head}</{type}>
</head>\n''')
        with open('style.css', 'a') as s:
                s.write(f'''{type} {{
    color: {color};
    font-family: {font_family};
    text-align: {text_align};
    font-size: {font_size};
    background-color: {background_color};
}}''')
        #elif type and font_size:
            #print("Only type or font_size accepted in head()")
        
title('nothing', 'y')
# head('nothing more', font_size=None, font_family='Arial', type='header', color='black', text_align='left', background_color='None')
head('nothing more', font_size='2px', type='h1', color='blue', text_align='center', background_color='orange')

#head('nothing more', 'h5', None, 'rgb(50, 168, 82)', 'Arial', 'center')
#head('nothing more', None, None, None, None, None)
# No hex accepted for color in head(). RGB and normal eng works.
# If arguments font_size and type are passed, font_size seems to be given preference CSS


# In head(), color must have black as default. 
# In head(), type OR font_size are required arguments. At least one of them must be passed. 
# Warn the users that if arguments font_size and type, both are passed, font_size seems to be given preference 
# by CSS. But, at least one argument MUST be passed.
# No hex accepted for color in head() iff type is mentioned. RGB and normal eng works. Haven't tested
# other mediums.
# In title(), default value of ico and css_bool are None. 
# Also in title(), icon argument MUST be a .ico file. Check if the last 4 letters are '.ico'
# In head() in the argument font_family, the users MUST enter it in double quotes. Typically, it can be 
# something like
# font-family: 'Roboto', sans-serif; in CSS. But when the user is entering the value of
# font_family as ''Roboto', sans-serif' there's a SyntaxError, since there is a single quote within
# # a single quote. Hence, they must always enter it in double quotes. 
# check soup.a.prettify()


def open_tags(any_tag, *args):
    with open('nameofhtm.html', 'a') as f:
        f.write(f'''<{any_tag}>\n''')
        for arg in args:
            f.write(f'''<{arg}>\n''')
def close_tags(any_tag, *args):
    with open('nameofhtm.html', 'a') as f:
        f.write(f'''</{any_tag}>\n''')
        for arg in args:
            f.write(f'''</{arg}>\n''')
def close_tag_before(tag_to_close, tag_to_close_before):
    with open('nameofhtm.html', 'r') as f:
        tag_to_close_before = f"<{tag_to_close_before}>"
        tag_to_close = f"</{tag_to_close}>"
        closed_tag = tag_to_close + tag_to_close_before
        f = f.read()
        now_closed = f.replace(tag_to_close_before, closed_tag)
        with open('nameofhtm.html', 'w') as f:
            f.write(f'''{now_closed}''')

    # def css(self, tag_to_style, *args):
    #     var = tag_to_style, *args
    #     def css_att(lol):
    #         print(var, lol)
            


# x = tags()
# x.open_tags('tag3', 'tag1', 'tag2')
# x.close_tags('tag1', 'tag2')
# x.close_tag_before('tag3', 'tag2')

# with open('nameofhtm.html', 'r') as f:
#     newlines = f.read()
#     newlines = newlines.replace('<tag1>', '<tag4>')
#     print(newlines)

# Close all tags automatically
def AutoCloseTags():

    warnings.showwarning(f'''Auto closing HTML tags may not be accurate and are not recommended. Further 
    development may run into issues. Please close tags manually if unsure. It is recommended to use after all development. See "bs4 auto closing tags" for more info.''', UserWarning, str, int(2))
    
    with open('nameofhtm.html', 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')
        auto_close_all_tags = soup.prettify()
        with open('nameofhtm.html', 'w') as f:
            f.write(f'''{auto_close_all_tags}''') 

#auto_close_tags() 
#AutoCloseTags()
#def (close_tag, open_new)

class cTags():
    def __init__(self, tag):
        self.tag = tag

    def css(self, color=None, font_family=None, font_weight=None, text_align=None, font_size=None, background_color=None, background=None, margin_top=None, margin_bottom=None, margin_left=None, margin_right=None, border=None, display=None, padding=None, height=None, width=None, *args):
        if background_color != None:
            background = ''
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
}}''')
        for arg in args:
            s.write(f'''\n{str(self.tag)} {{
    {arg};
}}''')

# x = tags()
# x.open_tags('tag1')
# y = cTags('tag1')
# y.css(color='blue')

# open class textTags()

class tTags():
    def __init__(self, p=False, div_class=False, sec_class=False):
        self.p = p
        self.div_class = div_class
        self.sec_class = sec_class

    def start_p(self, p_text):
        with open('nameofhtm.html', 'a') as f:
            f.write(f'''<p> {p_text} \n</p>''')

    def start_div(self, d_class):
        with open('nameofhtm.html', 'a') as f:
            f.write(f'''\n<div class="{d_class}">
''')

    def start_sec(self, s_class):
        with open('nameofhtm.html', 'a') as f:
            f.write(f'''<section class="section {s_class}">
''')

    def css(self, color=None, font_family=None, font_weight=None, text_align=None, font_size=None, background_color=None, background=None, margin_top=None, margin_bottom=None, margin_left=None, margin_right=None, border=None, display='block', padding=None, height=None, width=None):
        if background_color != None:
            background = ''
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
}}''')

def add_text(text):
    with open('nameofhtm.html', 'a') as f:
        f.write(f'''{text}''')

b = '<br>'

p_text = "I'm sure about this man"
x = tTags(True)
x.start_p(p_text)
x.css(color='green')

d_class = 'newClass'
x = tTags(div_class=True)
x.start_div(d_class)
x.css(color='yellow', font_family='Times New Roman', background_color='blue')

add_text("I'm REALLY" + b + "sure of this")
close_tags('div')

s_class = 'anotherClass'
x = tTags(sec_class=True)
x.start_sec('anotherClass')
x.css(color='purle', background_color='green')

add_text("I'm defo" + b + "sure of this")
close_tags('section')



def WriteHTML(text):
    """Writes the given code to the HTML file."""
    
    open('index.html', 'a+').write(text)

def WriteCSS(text):
    """Writes the given code to the CSS file."""

    open('style.css', 'a+').write(text)
        
if __name__ == "__main__":
    title('Test')
    head('This is the header', '20px', 'Arial')
    AutoCloseTags()
