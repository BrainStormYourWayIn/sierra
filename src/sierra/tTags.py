import traceback

class div():
    def __init__(self, div_class=None, attr=None):
        self.div_class = div_class

        if div_class == None:
            with open('index.html', 'a+') as f:
                f.write("\n<div")
        else:
            with open('index.html', 'a+') as f:
                f.write(f"\n<div class='{self.div_class}'")

        if attr != None:
            open('index.html', 'a+').write(attr)

        open('index.html', 'a+').write(">")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, tb):
        if exc_type is not None:
            traceback.print_exception(exc_type, exc_value, tb)
        else:
            open('index.html', 'a+').write("\n</div>")

    def css(self, color='black', font_family='Arial', font_weight=False, text_align='left', font_size=False, background_color='white', \
            background=False, margin_top='0px', margin_bottom='0px', margin_left='0px', margin_right='0px', border='0px', display='block', \
            padding='0px', height=False, width=False, line_break=False, line_height=False, overflow=False, margin='0px', box_shadow=False):
        """
        Args:
            color (str, optional)            : CSS color parameter. Defaults to 'black'.
            font_family (str, optional)      : CSS font-family parameter. Defaults to 'Arial'.
            font_weight (str, optional)      : CSS font-weight parameter. Defaults to False.
            text_align (str, optional)       : CSS text-align parameter. Defaults to 'left'.
            font_size (str, optional)        : CSS font-size parameter. Defaults to False.
            background_color (str, optional) : CSS background-color parameter. Defaults to 'white'.
            background (str, optional)       : CSS background parameter. Defaults to False.
            margin_top (str, optional)       : CSS margin-top parameter. Defaults to '0px'.
            margin_bottom (str, optional)    : CSS margin-bottom parameter. Defaults to '0px'.
            margin_left (str, optional)      : CSS margin-left parameter. Defaults to '0px'.
            margin_right (str, optional)     : CSS margin-right parameter. Defaults to '0px'.
            border (str, optional)           : CSS border parameter. Defaults to '0px'.
            display (str, optional)          : CSS display parameter. Defaults to 'block'.
            padding (str, optional)          : CSS padding parameter. Defaults to '0px'.
            height (str, optional)           : CSS height parameter. Defaults to False.
            width (str, optional)            : CSS width parameter. Defaults to False.
            line_break (str, optional)       : CSS line-break parameter. Defaults to False.
            line_height (str, optional)      : CSS line-height parameter. Defaults to False.
            overflow (str, optional)         : CSS overflow parameter. Defaults to False.
            margin (str, optional)           : CSS margin parameter. Defaults to '0px'.
            box_shadow (str, optional)       : CSS box-shadow parameter. Defaults to False.
        """

        with open('style.css', 'a+') as s:
            s.write(f'''
.{self.div_class} {{
    color: {color};
    font-family: {font_family};
    font-weight: {font_weight};
    text-align: {text_align};
    font-size: {font_size};
    background-color: {background_color};
    background: {background};
    margin-top: {margin_top};
    margin-bottom: {margin_bottom};
    margin-left: {margin_left};
    margin-right: {margin_right};
    border: {border};
    display: {display};
    padding: {padding};
    height: {height};
    width: {width};
    line-break: {line_break};
    line-height: {line_height};
    overflow: {overflow};
    margin: {margin};
    box-shadow: {box_shadow};
}}''')


class section():
    def __init__(self, sec_class=None, attr=None):
        self.sec_class = sec_class

        if sec_class == None:
            with open('index.html', 'a+') as f:
                f.write("\n<section")
        else:
            with open('index.html', 'a+') as f:
                f.write(f"\n<section class='section {self.sec_class}'")

        if attr != None:
            open('index.html', 'a+').write(f''' {attr}''')

        open('index.html', 'a+').write(">")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, tb):
        if exc_type is not None:
            traceback.print_exception(exc_type, exc_value, tb)
        else:
            open('index.html', 'a+').write("\n</section>")

    def css(self, color='black', font_family='Arial', font_weight='False', text_align='False', font_size='False', background_color='False', \
            background='False', margin_top='False', margin_bottom='False', margin_left='False', margin_right='False', border='False', \
            display='block', padding='False', height='False', width='False', line_break='False', line_height='False', overflow='False', \
            margin='False', box_shadow='False'):

        """
        Args:
            color (str, optional)            : CSS color parameter. Defaults to 'black'.
            font_family (str, optional)      : CSS font-family parameter. Defaults to 'Arial'.
            font_weight (str, optional)      : CSS font-weight parameter. Defaults to False.
            text_align (str, optional)       : CSS text-align parameter. Defaults to False.
            font_size (str, optional)        : CSS font-size parameter. Defaults to False.
            background_color (str, optional) : CSS background-color parameter. Defaults to 'white'.
            background (str, optional)       : CSS background parameter. Defaults to False.
            margin_top (str, optional)       : CSS margin-top parameter. Defaults to '0px'.
            margin_bottom (str, optional)    : CSS margin-bottom parameter. Defaults to '0px'.
            margin_left (str, optional)      : CSS margin-left parameter. Defaults to '0px'.
            margin_right (str, optional)     : CSS margin-right parameter. Defaults to '0px'.
            border (str, optional)           : CSS border parameter. Defaults to '0px'.
            display (str, optional)          : CSS display parameter. Defaults to 'block'.
            padding (str, optional)          : CSS padding parameter. Defaults to False.
            height (str, optional)           : CSS height parameter. Defaults to False.
            width (str, optional)            : CSS width parameter. Defaults to False.
            line_break (str, optional)       : CSS line-break parameter. Defaults to False.
            line_height (str, optional)      : CSS line-height parameter. Defaults to False.
            overflow (str, optional)         : CSS overflow parameter. Defaults to False.
            margin (str, optional)           : CSS margin parameter. Defaults to False.
            box_shadow (str, optional)       : CSS box-shadow parameter. Defaults to False.
        """

        with open('style.css', 'a+') as s:
            s.write(f'''
.{self.sec_class} {{
    color: {color};
    font-family: {font_family};
    font-weight: {font_weight};
    text-align: {text_align};
    font-size: {font_size};
    background-color: {background_color};
    background: {background};
    margin-top: {margin_top};
    margin-bottom: {margin_bottom};
    margin-left: {margin_left};
    margin-right: {margin_right};
    border: {border};
    display: {display};
    padding: {padding};
    height: {height};
    width: {width};
    line-break: {line_break};
    line-height: {line_height};
    overflow: {overflow};
    margin: {margin};
    box-shadow: {box_shadow};
}}''')

def p(text, attr=None):
    if attr != None:
        with open('index.html', 'a+') as f:
            f.write(f'''
<p {attr}>
{text}
</p>''')
    else:
        with open('index.html', 'a+') as f:
            f.write(f'''
<p>
{text}
</p>''')


#with div(div_class='newClass', attr="id='some_id'") as d:
#    p('This is some text')
#    d.css(color='yellow')

#with section(sec_class="someClass", attr="id='new_id'") as s:
#    p('Some more text', "class='anotherClass'")
#    s.css(font_family='Times New Roman')
