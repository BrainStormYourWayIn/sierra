def addBullets(points, ul=False, start="1", type="False", inner=False):

    if ul == False:
        with open('index.html', 'a') as f:
            f.write(f'''\n<ol start="{start}" type="{type}">''')
            for point in points:
                # with open('index.html', 'a') as f:
                f.write(f'''<li>{point}</li>\n''')
        if inner == False:
            with open('index.html', 'a') as f:
                f.write(f'''</ol>''')
        else:
            pass
    
    if ul == True:
        with open('index.html', 'a') as f:
            f.write(f'''\n<ul type="{type}">\n''')
            for point in points:
                # with open('index.html', 'a') as f:
                f.write(f'''<li>{point}</li>\n''')
        if inner == False:
            with open('index.html', 'a') as f:
                f.write(f'''</ul>''')
        else:
            pass
