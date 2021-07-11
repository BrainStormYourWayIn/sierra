def writeWA(text):
    """Writes the given text to the html file."""

    with open('index.html', 'a+') as f:
        f.write(text)

def writeCSS(tag, *args):
    """
    Writes the given code to the CSS file.
    Enter in a dictionary
    """

    with open('style.css', 'a+') as s:
        s.write(f"""\n{tag} {{""")
        for arg in args:
            for parameter, value in arg.items():
                s.write(f"""\n\t{parameter}: {value};""")
        s.write("\n}")

def writeCSS_raw(tag, text):
    """
    Writes the given code to the CSS file.
    """
    with open('style.css', 'a+') as s:
        s.write(text)
