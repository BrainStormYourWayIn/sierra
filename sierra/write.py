def writeHTML(text):
    """Writes the given text to the html file."""

    with open('index.html', 'a+') as f:
        f.write(f'''\n{text}''')

def writeCSS(tag, *args):
    """Writes the given code to the CSS file."""

    with open('style.css', 'a+') as s:
        s.write(f"""\n{tag} {{""")
        print(args)
        for parameter, value in args[0].items():
            s.write(f"""\n\t{parameter}: {value};""")
        s.write("\n}")
