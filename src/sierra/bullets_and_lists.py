def addBullets(points, ul=False, start="1", type="False", inner=False):
    """Adds bullet lists to the webpage.

    Args:
        points(list, compulsory): Takes in a list of bullets to add
        ul(bool, optional)      : If set to True, it adds bullets (unordered) rather than an ordered list
        start(str, optional)    : Starts the ordered list from a particular starting position
        type(str, optional)     : Sets the type of ordered/unordered list
        inner(bool, optional)   : Determines if bullet lists have to be added inside of a bullet list item
    """
    
    if ul == False:
        with open('index.html', 'a') as f:
            f.write(f'''<ol start="{start}" type="{type}">''')
            for point in points:
                # with open('index.html', 'a') as f:
                f.write("<li>{point}</li>")
            if inner == False:
                f.write("</ol>")
            else:
                pass
    
    if ul == True:
        with open('index.html', 'a') as f:
            f.write(f'''<ul type="{type}">''')
            for point in points:
                # with open('index.html', 'a') as f:
                f.write(f"<li>{point}</li>")
            if inner == False:
                f.write("</ul>")
            else:
                pass
