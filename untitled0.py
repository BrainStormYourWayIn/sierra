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

def title(Title, icon, css_bool):
    with open('nameofhtm.html', 'w') as f:
        
            f.write(f'''<!doctype html>
<html lang="en">
<meta charset="utf-8">
<head>
<title>{Title}</title>
<link rel="shortcut icon" href={icon}>\n''')
    
    if css_bool == 'y':
        with open('nameofhtm.html', 'a') as f:
            f.write(f'''<link rel = "stylesheet" href = "style.css">\n''')
        with open('style.css', 'w') as s:
            s.write('')
    elif css_bool == None:
        pass
    else:
        print('css_bool only takes value None (default) or "y"')
# add link rel = style.css in html code, get clothes first

def add_font(font_link):
    with open('nameofhtm.html', 'a') as f:
        f.write(f'''<link href={font_link} rel="stylesheet">\n''')

#Head:
# head type is h1 to h6
# size in any valid measure
# text-align: left|right|center|justify|initial|inherit

def head(Head, type, font_size, color, font_family, bg_color, text_align):
    font_family = font_family.replace(";", "")
    with open('nameofhtm.html', 'a') as f:
        if font_size:
            f.write(f'''<header>{Head}</header>\n''')
            with open('style.css', 'a') as s:
                s.write(f'''header {{
    color: {color};
    font-family: {font_family};
    background-color: {bg_color};
    text-align: {text_align};
    font-size: {font_size};
}}''')
            
        elif type:
            f.write(f'''<{type}>{Head}</{type}>\n''')
            with open('style.css', 'a') as s:
                s.write(f'''{type} {{
    color: {color};
    background-color: {bg_color};
    font-family: {font_family};
    text-align: {text_align};
}}''')
        #elif type and font_size:
            #print("Only type or font_size accepted in head()")
        
title('nothing', None, 'y')
head('nothing more', None, '35px', '#3455eb', 'Arial', None, 'center')


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

open_tags('tag3', 'tag1', 'tag2')

def close_tags(any_tag, *args):
    with open('nameofhtm.html', 'a') as f:
        f.write(f'''</{any_tag}>\n''')
        for arg in args:
            f.write(f'''</{arg}>\n''')

#close_tags('tag1', 'tag2')

def close_tag_before(tag_to_close, tag_to_close_before):
    with open('nameofhtm.html', 'r') as f:
        tag_to_close_before = f"<{tag_to_close_before}>"
        tag_to_close = f"</{tag_to_close}>"
        closed_tag = tag_to_close + tag_to_close_before
        f = f.read()
        now_closed = f.replace(tag_to_close_before, closed_tag)
        with open('nameofhtm.html', 'w') as f:
            f.write(f'''{now_closed}''')

close_tag_before('tag3', 'tag2')

# with open('nameofhtm.html', 'r') as f:
#     newlines = f.read()
#     newlines = newlines.replace('<tag1>', '<tag4>')
#     print(newlines)

# Close all tags automatically
def auto_close_tags():
    warnings.warn(f'''Auto closing HTML tags may not be accurate and are not recommended. Further 
    development may run into issues. Please close tags manually if unsure. 
    See "bs4 auto closing" for more info.''')
    with open('nameofhtm.html', 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')
        auto_close_all_tags = soup.prettify()
        with open('nameofhtm.html', 'w') as f:
            f.write(f'''{auto_close_all_tags}''') 

#auto_close_tags() 
