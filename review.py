def writeCSS(tag, *args):
    """Writes the given code to the CSS file."""

    with open('style.css', 'a+') as s:
        s.write(f"""\n{tag} {{""")
        print(args)
        for parameter, value in args[0].items():
            s.write(f"""\n\t{parameter}: {value};""")
        s.write("\n}")
