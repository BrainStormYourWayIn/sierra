def writeHTML(text):
    """Writes the given text to the html file.
    
    Args:
        text (str, compulsory): HTML code snippet.
    """

    open("index.html", 'a+').write(text)


def css(**kwargs):
    """Writes the given parameters to the CSS file.
    
    Args:
        **kwargs (optional) : CSS parameters.
    """

    with open("style.css", 'a+') as s:
        for key, value in kwargs:
            s.write(f"\n\t{key.replace('_', '-')}: {value};")
        s.write("\n}")


def writeCSS_raw(text):
    """Writes the given code to the CSS file.
    
    Args:
        text (str, compulsory): CSS style sheet.
    """

    open("style.css", 'a+').write(text)
