# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 09:32:38 2021

"""
#from flask import Flask

def title(Title, icon=None, css_bool=True):
    """
    Args:
        Title(str, compulsory)   : Title of the HTML file.
        icon(str, optional)      : Icon to be displayed. Should be a .ico file. Defaults to no icon.
        css_bool(bool, optional) : Do you want CSS in your HTML code? (True or False)
    """



    if icon == None or icon.split('.')[-1] != '.ico':
        with open('nameofhtm.html', 'w+') as f:
                f.write(f"""<!DOCTYPE html>
<html lang="en">
<meta charset="utf-8">
<head>
<title>{Title}</title>
<link rel="shortcut icon" href={icon}>\n""")
    else:
        with open('nameofhtm.html', 'w+') as f:
                f.write(f"""<!DOCTYPE html>
<html lang="en">
<meta charset="utf-8">
<head>
<title>{Title}</title>""")
    
    if css_bool == True:
        with open('nameofhtm.html', 'a') as f:
            f.write(f'<link rel = "stylesheet" href = "style.css">\n')
        with open('style.css', 'w') as f:
            f.write('')
    elif css_bool == False:
        pass
    else:
        print('arg css_bool only takes value False (default) or True')
    #TODO: add link rel = style.css in html code, get clothes first


def head(Head, font_size, font_family, type='header', color='black', text_align='left'):
    """Head:
        head type is h1 to h6
        size in any valid measure
        text-align: left|right|center|justify|initial|inherit


    Args:
        Head (str, compulsory)        : Caption header
        font_size (str, compulsory)   : Font size in any valid measure.
        font_family (str, compulsory) : any possible Font family
        type (str, optional)          : Header Size. Anything from h1 to h6.
        color (str, optional)         : Color of Font. Defaults to 'black'. HEX value not supported.
        text_align (str, optional)    : left|right|center|justify|initial|inherit. Defaults to 'left'.
    """

    with open('nameofhtm.html', 'a+') as f:
        f.write(f'''<{type}>{Head}</{type}>''')
        with open('style.css', 'a') as s:
                s.write(f'''{type} {{
    color: {color};
    font-family: {font_family};
    text-align: {text_align};
    font-size: {font_size};
}}''')

def end():
    with open('nameofhtm.html', 'a+') as f:
        f.write('</html>')
#title('nothing', None, 'y')
#head('nothing more', None, '35px', '#3455eb', 'Arial', 'center')
#head('nothing more', 'h5', None, 'rgb(50, 168, 82)', 'Arial', 'center')
#head('nothing more', None, None, None, None, None)
# No hex accepted for color in head(). RGB and normal eng works.
# If arguments font_size and type are passed, font_size seems to be given preference CSS

if __name__ == "__main__":
    title('Test')
    head('This is the header', '20px', 'Arial')
    end()
