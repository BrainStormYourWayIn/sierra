def openTags(any_tag, *args):
    with open(f'''{index}.html''', 'a') as f:
        f.write(f'''\n<{any_tag}>''')
        for arg in args:
            f.write(f'''\n<{arg}>''')
            
def closeTags(any_tag, *args):
    with open(f'''{index}.html''', 'a') as f:
        f.write(f'''\n</{any_tag}>''')
        for arg in args:
            f.write(f'''\n</{arg}>''')
            
def closeTagBefore(tag_to_close, tag_to_close_before):
    with open(f'''{index}.html''', 'r') as f:
        tag_to_close_before = f"<{tag_to_close_before}>"
        tag_to_close = f"</{tag_to_close}>"
        closed_tag = tag_to_close + f"\n{tag_to_close_before}"
        f = f.read()
        now_closed = f.replace(tag_to_close_before, closed_tag)
        with open(f'''{index}.html''', 'w') as f:
            f.write(f'''{now_closed}''')

    # def css(self, tag_to_style, *args):
    #     var = tag_to_style, *args
    #     def css_att(lol):
    #         print(var, lol)
            
# x = tags()
# x.openTags('tag3', 'tag1', 'tag2')
# x.closeTags('tag1', 'tag2')
# x.close_tag_before('tag3', 'tag2')

def closeHTML():
    with open(f'''{index}.html''', 'a') as f:
        f.write(f'''\n</html>''')
        
def openBody(background='False', background_color='white', background_image=False, opacity=False, background_size='cover', background_attachment='fixed', background_position=False, background_repeat=False):
    with open(f'''{index}.html''', 'a') as f:
        f.write(f'''\n<body>''')
    with open('style.css', 'a') as s:
        s.write(f'''\nbody {{
    background-color: {background_color};
    background-image: {background_image};
    opacity: {opacity};
    background-size: {background_size};
    background-attachment: {background_attachment};
    background-position: {background_position};
    background-repeat: {background_repeat};
}}''')
        
def closeBody():
    with open(f'''{index}.html''', 'a') as f:
        f.write(f'''\n</body>''')
