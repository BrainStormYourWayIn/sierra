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

def head(Head, type, font_size, in_hex, font_family, text_align):
    with open('nameofhtm.html', 'a') as f:
        if font_size:
            f.write(f'''<header>{Head}</header>''')
            with open('style.css', 'a') as s:
                s.write(f'''header {{
    color: {in_hex};
    font-family: {font_family};
    text-align: {text_align};
    font-size: {font_size};
}}''')
            
        elif type:
            f.write(f'''<{type}>{Head}</{type}>''')
            with open('style.css', 'a') as s:
                s.write(f'''{type} {{
    color: {in_hex};
    font-family: {font_family};
    text-align: {text_align};
}}''')
        #elif type and font_size:
            #print("Only type or font_size accepted in head()")
        
title('nothing', None, 'y')
#head('nothing more', None, '35px', '#3455eb', 'Arial', 'center')
head('nothing more', 'h5', None, 'rgb(50, 168, 82)', 'Arial', 'center')
# No hex accepted for type in head(). RGB and normal eng works.
# If arguments font_size and type are passed, font_size seems to be given more preference CSS
