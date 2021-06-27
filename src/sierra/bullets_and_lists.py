def addBullets(points, ul=False, start="1", type="False", inner=False):
    """Adds bullet lists to the webpage.

    Args:
        points (list, compulsory) : Takes in a list of bullets to add.
        ul (bool, optional)       : If set to True, it adds bullets (unordered) rather than an ordered list.
        start (str, optional)     : Starts the ordered list from a particular starting position.
        type (str, optional)      : Sets the type of ordered/unordered list.
        inner (bool, optional)    : Determines if bullet lists have to be added inside of a bullet list item.
    """
    
    if ul:
        with open('index.html', 'a') as f:
            f.write(f'\n<ul type="{type}">\n')
            for point in points:
                # with open('index.html', 'a') as f:
                f.write(f'<li>{point}</li>\n')
        if not inner:
            with open('index.html', 'a') as f:
                f.write("</ul>")
    
    elif not ul:
        with open('index.html', 'a') as f:
            f.write(f'\n<ol start="{start}" type="{type}">')
            for point in points:
                # with open('index.html', 'a') as f:
                f.write(f'''<li>{point}</li>\n''')
        if not inner:
            with open('index.html', 'a') as f:
                f.write("</ol>")

def def_lists(def_list, *args):
    """Creates a description list from a list of lists.
    
    Args:
        def_list (list, compulsory) : Takes in a list of lists and creates a description list on it.
        *args (compulsory)          : To use global, if required. Enter them within quotes, not comma-separated.
    """

    open('index.html', 'a').write(f'''\n<dl''')
    for arg in args:
            b = ' ' + arg
            with open('index.html', 'a') as f:
                f.write(b)

    open('index.html', 'a').write(">")
    for def_listings in def_list:
        for def_listing in def_listings[0]:
            open('index.html', 'a').write(f'''\n<dt>{def_listing}</dt>''')

        def_listings.remove(def_listings[0])

        for listings in def_listings:
            for listing in listings:
                open('index.html', 'a').write(f'''\n<dd>{listing}</dd>''')

    open('index.html', 'a').write("\n</dl>")
