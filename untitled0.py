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
        with open('index.html', 'w+') as f:
                f.write(f"""<!DOCTYPE html>
<html lang="en">
<meta charset="utf-8">
<head>
<title>{Title}</title>
<link rel="shortcut icon" href={icon}>\n""")
    else:
        with open('index.html', 'w+') as f:
                f.write(f"""<!DOCTYPE html>
<html lang="en">
<meta charset="utf-8">
<head>
<title>{Title}</title>""")
    
    if css_bool == True:
        with open('index.html', 'a+') as f:
            f.write(f'<link rel="stylesheet" href="style.css">\n')
        with open('style.css', 'w') as f:
            f.write('')
    elif css_bool == False:
        pass
    else:
        print('arg css_bool only takes value False (default) or True')

def head(Head, font_size=None, font_family='Arial', type='header', color='black', text_align='left', bg_color='None'):
    """
    Args:
        Head (str, compulsory)        : Caption header
        font_size (str, optional)     : Font size in any valid measure. 
        font_family (str, compulsory) : any possible Font family. Must be entered only in double quotes
        type (str, optional)          : Header Size. Anything from h1 to h6. None is accepted. 
        color (str, optional)         : Color of Font. Does not take in HEX values  
        text_align (str, optional)    : left|right|center|justify|initial|inherit. Defaults to 'left'.
    """
    if len(type) == 2:
        font_size = None
    elif type == None:
        type = 'header'
    elif font_size and type:
        type = 'header'
        warnings.warn('Both font_size and type are given. Please rectify or only font_size is considered')
    elif font_size == None and type == None:
        type = 'h2'
        warnings.warn('type is None. Defaults to h2')
    elif len(type) != 2 and type != None:
        type = 'h3'
        warnings.warn("Argument 'type' only takes in None or a value from h1 to h6. Please rectify ot type defaults to 'h3'")

    with open('index.html', 'a+') as f:
        f.write(f'''<{type}>{Head}</{type}>
</head>\n''')
        with open('style.css', 'a') as s:
                s.write(f'''{type} {{
    color: {color};
    font-family: {font_family};
    text-align: {text_align};
    font-size: {font_size};
    background-color: {bg_color};
}}''')

def open_tags(any_tag, *args):
    with open('index.html', 'a') as f:
        f.write(f'''<{any_tag}>\n''')
        for arg in args:
            f.write(f'''<{arg}>\n''')

#open_tags('tag3', 'tag1', 'tag2')

def close_tags(any_tag, *args):
    with open('index.html', 'a') as f:
        f.write(f'''</{any_tag}>\n''')
        for arg in args:
            f.write(f'''</{arg}>\n''')

#close_tags('tag1', 'tag2')

def close_tag_before(tag_to_close, tag_to_close_before):
    with open('index.html', 'r') as f:
        tag_to_close_before = f"<{tag_to_close_before}>"
        tag_to_close = f"</{tag_to_close}>"
        closed_tag = tag_to_close + tag_to_close_before
        f = f.read()
        now_closed = f.replace(tag_to_close_before, closed_tag)
        with open('index.html', 'w') as f:
            f.write(f'''{now_closed}''')

#close_tag_before('tag3', 'tag2')

# with open('nameofhtm.html', 'r') as f:
#     newlines = f.read()
#     newlines = newlines.replace('<tag1>', '<tag4>')
#     print(newlines)

# Close all tags automatically
def AutoCloseTags():
    """Closes the HTML Tags that ar open."""

    warnings.warn(r'''Auto closing HTML tags may not be accurate and are not recommended. Further 
    development may run into issues. Please close tags manually if unsure. 
    See "bs4 auto closing tags" for more info.''')
    with open('index.html', 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')
        auto_close_all_tags = soup.prettify()
        with open('index.html', 'w') as f:
            f.write(f'''{auto_close_all_tags}''') 

#auto_close_tags()                 
#title('nothing', None, 'y')
#head('nothing more', None, '35px', '#3455eb', 'Arial', 'center')
#head('nothing more', 'h5', None, 'rgb(50, 168, 82)', 'Arial', 'center')
#head('nothing more', None, None, None, None, None)

# No hex accepted for color in head(). RGB and normal eng works.
# If arguments font_size and type are passed, font_size seems to be given preference CSS
# In head() in the argument font_family, the users MUST enter it in double-quotes. Typically, it can be something like
# font-family: 'Roboto', sans-serif; in CSS. But when the user is entering the value of
# font_family as ''Roboto', sans-serif' there's a SyntaxError, since there is a single quote within
# a single quote. Hence, they must always enter it in double-quotes. 

# check soup.a.prettify()

def WriteHTML(text):
    """Writes the given code to the HTML file."""
    
    open('index.html', 'a+').write(text)

def WriteCSS(text):
    """Writes the given code to the CSS file."""

    open('style.css', 'a+').write(text)
        
if __name__ == "__main__":
    title('Test')
    head('This is the header', '20px', 'Arial')
    AutoCLoseTags()
