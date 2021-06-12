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
        
def closeBody():
    with open(f'''{index}.html''', 'a') as f:
        f.write(f'''\n</body>''')
