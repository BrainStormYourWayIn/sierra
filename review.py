import warnings

def AutoPrettify():
    warnings.showwarning('''Auto prettifying also involves auto closing HTML tags which may not be accurate if not already closed and are not recommended. Further development may run into issues. Please close tags manually if unsure. It is recommended to use after all development for best results.
    See "bs4 auto closing tags" for more info.''', UserWarning, str, int(2))
    
def writeCSS(tag, *args):
    """Writes the given code to the CSS file."""

    with open('style.css', 'a+') as s:
        s.write(f"""\n{tag} {{""")
        for parameter, value in args.items():
            s.write(f"""\n{parameter}: {value};""")
        s.write("\n}")
        
#Stuff like StartBody and EndBody changed to startBody() and endBody()
