def writeWA(text):
    """Writes the given text to the html file.
    
    Args:
        text (str, compulsory): HTML code snippet.
    """

    open("index.html", 'a+').write(f"\n{text}")


def writeCSS(tag, **kwargs):
    """
    Adds the given styling attributes to the tag mentioned

    \nUse `kwargs` to add styling attributes to the `tag` mentioned

    \nUse underscores instead of hyphens when adding styling attributes.        
    \nFor example, the attribute `font-size` must be entered in as `font_size`

    \nAnother example: 
    \n`writeCSS('.some_class', font-size='20px')` adds the attributes `font-size=20px` to the class `some_class`
    
    \nArgs:
    \ntag (str, compulsory) : Tag to add the CSS to. Could be a `class`, `id` or anything
    \nkwargs                : CSS styling attributes to add to the `tag` mentioned 
    """

    with open('style.css', 'a+') as s:
        s.write(f"\n\n{tag} {{")

        for key, value in kwargs.items():
            s.write(f"\n\t{key.replace('_', '-')}: {value};")

        s.write("\n}")


def writeCSS_raw(text):
    """Writes the given text to the CSS file.
    
    Args:
        text (str, compulsory): CSS style sheet.
    """
    open("style.css", 'a+').write(f"\n{text}")
