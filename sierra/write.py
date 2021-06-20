def writeHTML(text):
    """Writes the given text to the html file."""

    with open('index.html', 'a+') as f:
        f.write(f'''{text}''')

def writeCSS(tag, *args):
    """Writes the given code to the CSS file."""

    with open('style.css', 'a+') as s:
        s.write(f"""{tag} {{""")
        for arg in args:
            for parameter, value in arg.items():
                s.write(f"\t{parameter}: {value};")
        s.write("}")
