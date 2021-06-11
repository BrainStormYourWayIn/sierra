def writeCSS(tag, *args):
    """Writes the given code to the CSS file."""

    with open('style.css', 'a+') as s:
        s.write(f"""\n{tag} {{""")
        for parameter, value in args.items():
            s.write(f"""\n{parameter}: {value};""")
        s.write("\n}")
        
#Stuff like StartBody and EndBody changed to startBody() and endBody()
