def writeCSS(tag, *args):
    """Writes the given code to the CSS file."""

    with open('style.css', 'a+') as s:
        s.write(f"""\n{tag} {{""")
        for parameter, value in args.items():
            s.write(f"""\n\t{parameter}: {value};""")
        s.write("\n}")
        
