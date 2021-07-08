import traceback

class cTags():

    def __init__(self, tag):

        """
        Add CSS to custom tags. Use writeCSS() for custom CSS arguments
        """
        self.tag = tag

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, tb):
        if exc_type is not None:
            traceback.print_exception(exc_type, exc_value, tb)

    def css(self, 
            color=False, font_family='Arial', font_weight=False, text_align=False, font_size=False, 
            background_color=False, background=False, margin_top=False, margin_bottom=False, margin_left=False, margin_right=False, 
            border=False, display=False, padding=False, height=False, width=False, line_break=False, line_height=False, overflow=False, margin=False, box_shadow=False):
        """
        Args:
            color (str, optional)            : CSS Color parameter. Defaults to False.
            font_family (str, optional)      : CSS Font-Family parameter. Defaults to 'Arial'.
            font_weight (str, optional)      : CSS Font-weight parameter. Defaults to False.
            text_align (str, optional)       : CSS Text-align parameter. Defaults to False.
            font_size (str, optional)        : CSS Font-size parameter. Defaults to False.
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
{self.tag} {{
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
