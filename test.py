# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 09:32:38 2021

"""
#from flask import Flask

from bs4 import BeautifulSoup
import warnings

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


def head(Head, font_size, font_family, type='h2', color='black', text_align='left'):
    font_family = font_family.replace(";", "")
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

def open_tags(any_tag, *args):
    with open('nameofhtm.html', 'a') as f:
        f.write(f'''<{any_tag}>\n''')
        for arg in args:
            f.write(f'''<{arg}>\n''')

#open_tags('tag3', 'tag1', 'tag2')

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

#close_tag_before('tag3', 'tag2')

# with open('nameofhtm.html', 'r') as f:
#     newlines = f.read()
#     newlines = newlines.replace('<tag1>', '<tag4>')
#     print(newlines)

# Close all tags automatically
def auto_close_tags():
    warnings.warn(f'''Auto closing HTML tags may not be accurate and are not recommended. Further 
    development may run into issues. Please close tags manually if unsure. 
    See "bs4 auto closing tags" for more info.''')
    with open('nameofhtm.html', 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')
        auto_close_all_tags = soup.prettify()
        with open('nameofhtm.html', 'w') as f:
            f.write(f'''{auto_close_all_tags}''') 

#auto_close_tags() 
                
#title('nothing', None, 'y')
#head('nothing more', None, '35px', '#3455eb', 'Arial', 'center')
#head('nothing more', 'h5', None, 'rgb(50, 168, 82)', 'Arial', 'center')
#head('nothing more', None, None, None, None, None)
# No hex accepted for color in head(). RGB and normal eng works.
# If arguments font_size and type are passed, font_size seems to be given preference CSS

# In head() in the argument font_family, the users MUST enter it in double quotes. Typically, it can be 
# something like
# font-family: 'Roboto', sans-serif; in CSS. But when the user is entering the value of
# font_family as ''Roboto', sans-serif' there's a SyntaxError, since there is a single quote within
# # a single quote. Hence, they must always enter it in double quotes. 
# check soup.a.prettify()

def end():
    with open('nameofhtm.html', 'a+') as f:
        f.write('</html>')
        

if __name__ == "__main__":
    title('Test')
    head('This is the header', '20px', 'Arial')
    end()
