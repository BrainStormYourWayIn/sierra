import warnings
from bs4 import BeautifulSoup

b = ' <br> '

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

def addInitc(box_sizing='False', margin=False, padding=False, border=False, position='relative'):
    """Sets the tone of CSS.

    Args:
        box_sizing (str, optional)  : CSS box-sizing parameter. Defaults to 'False'.
        margin (str, optional)      : CSS margin parameter. Defaults to False.
        padding (str, optional)     : CSS padding parameter. Defaults to False.
        border (str, optional)      : CSS border parameter. Defaults to False.
        position (str, optional)    : CSS position parameter. Defaults to 'relative'.
    """
    
    with open('style.css', 'a') as s:
        s.write(f"*,*:before,*:after {{box-sizing:{box_sizing};margin:{margin}; padding:{padding}; border:{border}; position: {position};}}")

def href(link, text=None):
    """Adds href to a text.
    
    Args:
        link (str, compulsory) : link for href
        text (str, optional)   : text for redirect. defaults to link
    """
    
    if text == None: text = link
    with open('index.html', 'a') as f:
        f.write(f'''<a href="{link}"> {text} </a>''')
 
    
def addFont(font_link):
    """Give the font link to add different fonts to your webpage.
    
    Args:
        font_link (str, compulsory): The font link.
    """
    open("index.html", 'a').write(f'''<link href="{font_link}" rel="stylesheet">''')

def code(codeblock):
    """Give the codeblock as a text to display the code in your webpage.

    Args:
        codeblock (str, compulsory): The code block.
    """
    open("index.html", 'a').write(f"<code>{codeblock}</code>")

def head(Head, type='header', font_size=False, font_family="Arial", color='black', text_align='left', background_color=False, padding=False, height=False, width=False, line_break=False, line_height=False, border=False, margin=False):
    """
    Args:
        Head (str, compulsory)           : Caption header.
        type (str, optional)             : Header Size. Anything from h1 to h6. Leave blank, if not valid. Defaults to 'header'.
        color (str, optional)            : CSS Color (in hex code or name). Defaults to 'black'.
        font_family (str, optional)      : CSS font-family. Defaults to Arial.
        text_align (str, optional)       : CSS text-align parameter. left|right|center|justify|initial|inherit. Defaults to 'left'.
        font_size (str, optional)        : CSS font-size parameter (in any valid measure). Leave blank, if not valid.
        background_color (str, optional) : CSS background-color parameter. Defaults to 'white'.
        padding (str, optional)          : CSS padding parameter. Defaults to False.
        height (str, optional)           : CSS Height parameter. Defaults to False.
        width (str, optional)            : CSS Width parameter. Defaults to False.
        line_break (str, optional)       : CSS Line-break parameter. Defaults to False.
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
    #    type == 'header'

    with open(f"index.html", 'a') as f:
        f.write(f'''
<{type}>{Head}</{type}>
</head>''')
        with open('style.css', 'a') as s:
                s.write(f'''
{type} {{
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
      
#! No hex accepted for color in head(). RGB and normal eng works.
#! If arguments font_size and type are passed, font_size seems to be given preference CSS
#NOTE: No hex accepted for color in head() if type is mentioned. RGB and normal eng works. Haven't tested other mediums.
#! In head() in the argument font_family, the users MUST enter it in double quotes.

#head('nothing more', 'h5', False, 'rgb(50, 168, 82)', 'Arial', 'center')
#head('nothing more', False, False, False, False, False)

#def tags(openTags=False, closeTags=False, *args):
#    if openTags == False and closeTags == False:
#        pass
#    elif openTags == False and closeTags == True:
#        for arg in args:
#            with open("index.html", 'a') as f

class addImg():
    def __init__(self, src:str, href="False", alt="This is an image", img_class='False'):
        self.src = src
        self.href = href
        self.alt = alt
        self.img_class = img_class

    def show(self):
        with open('index.html', 'a') as f:
            if self.href != "False":
                f.write(f'''\n<a href="{self.href}">''')
            if self.img_class != 'False':
                f.write(f'''\n<img src="{self.src}" alt="{self.alt}" class="{self.img_class}">''')
            else:
                f.write(f'''\n<img src="{self.src}" alt="{self.alt}">''')
            if self.href != "False":
                f.write(f'''\n</a>''')

    def css(self, height='False', width='False', margin='False', vertical_align='False', display='False', border='False', margin_top='False', margin_bottom='False', margin_left='False', margin_right='False', opacity='False', filter='False'):
        """
        Args:
            margin_top (str, optional)       : CSS image margin-top parameter. Defaults to 'False'.
            margin_bottom (str, optional)    : CSS image margin-bottom parameter. Defaults to 'False'.
            margin_left (str, optional)      : CSS image margin-left parameter. Defaults to 'False'.
            margin_right (str, optional)     : CSS image margin-right parameter. Defaults to 'False'.
            border (str, optional)           : CSS image border parameter. Defaults to 'False'.
            display (str, optional)          : CSS image display parameter. Defaults to 'block'.
            height (str, optional)           : CSS image height parameter. Defaults to False.
            width (str, optional)            : CSS image width parameter. Defaults to False.
            margin (str, optional)           : CSS image margin parameter. Defaults to False.
            vertical-align (str, optional)   : CSS image vertical-align parameter. Defaults to False.
            opacity (int/float, optional)    : CSS image opacity parameter. Defaults to 'False'.
            filter (str, optional)           : CSS image filter parameter. Defaults to 'False'.
        """

        with open('style.css', 'a') as s:
            if self.img_class != 'False': s.write(f'''.{self.img_class} {{''')
            else: s.write("img {")
            s.write(f'''    margin-top: {margin_top};
    margin-bottom: {margin_bottom};
    margin-left: {margin_left};
    margin-right: {margin_right};
    border: {border};
    display: {display};
    height: {height};
    width: {width};
    margin: {margin};
    vertical-align: {vertical_align};
    opacity: {opacity};
    filter: {filter};
}}''')

def autoPrettify():
    """Improve overall look of code and close all tags automatically (if not already done)."""

    warnings.showwarning(r'''Auto prettifying also involves auto closing HTML tags which may not be accurate if not already closed and are not recommended. Further development may run into issues. Please close tags manually if unsure.
    It is recommended to use after all development for best results. See "bs4 auto closing tags" for more info.''', UserWarning, str, int(186))
    
    with open("index.html", 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')
        auto_close_all_tags = soup.prettify()
        f.write(f'''{auto_close_all_tags}''')
