def writeHTML(text):
    """Writes the given text to the html file."""

    open("index.html", 'a+').write("\n" + text)


def writeCSS(tag, *args):
    """Writes the given parameters to the CSS file."""

    with open("style.css", 'a+') as s:
        s.write(f"\n{tag} {{")
        for arg in args:
            for parameter, value in arg.items():
                s.write(f"\n\t{parameter}: {value};")
        s.write("\n}")


def writeCSS_raw(CSS_text):
    """Writes the given code to the CSS file."""

    open("style.css", 'a+').write('\n' + CSS_text)
