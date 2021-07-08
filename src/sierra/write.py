def writeWA(text):
    """Writes the given text to the html file.
    
    Args:
        text (str, compulsory): HTML code snippet.
    """

    open("index.html", 'a+').write(text)


def writeCSS(tag, *args):
    """Writes the given parameters to the CSS file.
    
    Args:
        tag (str, compulsory)    : CSS tag name for styling.
        *args (dict, compulsory) : CSS styling in {parameter: desc.} format.
    """

    with open("style.css", 'a+') as s:
        s.write(f"\n{tag} {{")
        for arg in args:
            for parameter, value in arg.items():
                s.write(f"\n\t{parameter}: {value};")
        s.write("\n}")


def writeCSS_raw(text):
    """Writes the given code to the CSS file.
    
    Args:
        text (str, compulsory): CSS style sheet.
    """

    open("style.css", 'a+').write(text)
