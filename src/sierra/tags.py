def openTags(any_tag, *args):
    """Opens any HTML or XML tag."""
    
    with open("index.html", 'a+') as f:
        f.write(f"\n<{any_tag}>")
        for arg in args:
            f.write(f"\n<{arg}>")

def closeTags(any_tag, *args):
    """Closes any HTML or XML tag."""
    
    with open("index.html", 'a+') as f:
        f.write(f"\n</{any_tag}>")
        for arg in args:
            f.write(f"\n</{arg}>")

def closeTagBefore(tag_to_close, tag_to_close_before):
    with open("index.html", 'r') as f:
        tag_to_close_before = f"<{tag_to_close_before}>"
        tag_to_close = f"</{tag_to_close}>"
        closed_tag = tag_to_close + f"\n{tag_to_close_before}"
        f = f.read()
        now_closed = f.replace(tag_to_close_before, closed_tag)
        open("index.html", 'w').write(now_closed)

#x = tags()
#x.openTags('tag3', 'tag1', 'tag2')
#x.closeTags('tag1', 'tag2')
#x.close_tag_before('tag3', 'tag2')

def closeHTML():
    """Closes the <HTML> tag."""
    open("index.html", 'a+').write("\n</html>")

def openBody(background='False', background_color='white', background_image=False, opacity=1.00, background_size='cover', background_attachment='fixed', background_position='center', background_repeat='no-repeat'):
    """Opens the body tag and adds the required CSS.

    Args:
        background (str, optional)            : CSS background parameter. Defaults to 'False'.
        background_color (str, optional)      : CSS background-color parameter. Defaults to 'white'.
        background_image (str, optional)      : CSS background-image parameter. Defaults to False.
        opacity (float/int, optional)         : CSS opacity parameter. Defaults to 1.00.
        background_size (str, optional)       : CSS background-size parameter. Defaults to 'cover'.
        background_attachment (str, optional) : CSS background-attachment parameter. Defaults to 'fixed'.
        background_position (str, optional)   : CSS background-position parameter. Defaults to 'center'.
        background_repeat (str, optional)     : CSS background-repeat parameter. Defaults to 'no-repeat'.
    """

    open("index.html", 'a+').write(f"\n<body>")
    with open('style.css', 'a+') as s:
        s.write(f'''
body {{
    background: {background};
    background-color: {background_color};
    background-image: {background_image};
    opacity: {opacity};
    background-size: {background_size};
    background-attachment: {background_attachment};
    background-position: {background_position};
    background-repeat: {background_repeat};
}}''')

def closeBody():
    """Closes the body tag."""
    open("index.html", 'a+').write("\n</body>")
