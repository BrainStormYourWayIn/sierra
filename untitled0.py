# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 09:32:38 2021

"""
#from flask import Flask

#nameofhtm = input('Enter the name of your HTML file')

# icon argument must be a .ico file

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

#Head:
# head type is h1 to h6
# size in any valid measure
# text-align: left|right|center|justify|initial|inherit

def head(Head, type, font_size, color, font_family, text_align):
    with open('nameofhtm.html', 'a') as f:
        if font_size:
            f.write(f'''<header>{Head}</header>''')
            with open('style.css', 'a') as s:
                s.write(f'''header {{
    color: {color};
    font-family: {font_family};
    text-align: {text_align};
    font-size: {font_size};
}}''')
            
        elif type:
            f.write(f'''<{type}>{Head}</{type}>''')
            with open('style.css', 'a') as s:
                s.write(f'''{type} {{
    color: {color};
    font-family: {font_family};
    text-align: {text_align};
}}''')
        #elif type and font_size:
            #print("Only type or font_size accepted in head()")
        
title('nothing', None, 'y')
head('nothing more', None, '35px', '#3455eb', 'Arial', 'center')
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
