class tTags():
    def __init__(self, p=True, div_class='False', sec_class='False'):
        self.p = p
        self.div_class = div_class
        self.sec_class = sec_class

    def start_p(self, p_text: str, close=False):
        """Opens the <p> tag.
        
        Args: 
            p_text (str, compulsory): the text that has to be displayed.
            close (bool, optional)  : closes the <p> tag without using closeTags().
        """
        
        if self.p == True:
            open("index.html", 'a+').write(f"\n<p>\n{p_text}")
            if close == True:
                open("index.html", 'a').write(f"\n</p>")

    def start_div(self, *args):
        """Starts the <div> tag.
        
        Args:
            *args: To use global and event attributes, if required. Enter all of them within quotes, not comma-separated.
        """

        if self.div_class != 'False':
            with open("index.html", 'a') as f:
                f.write(f'''\n<div class="{self.div_class}"''')
        else:
            with open("index.html", 'a') as f:
                f.write(f'''\n<div''')
            for arg in args:
                b = ' ' + arg
                with open('index.html', 'a') as f:
                    f.write(f'''{b}''')
            open('index.html', 'a').write(">")
    
    def start_sec(self, *args):
        """Starts the <section> tag.
        
        Args:
            *args: To use global and event attributes, if required. Enter all of them within quotes, not comma-separated.
        """
        
        if self.sec_class != 'False':
            open('index.html', 'a').write(f'''\n<section class="section {self.sec_class}"''')
        else:
            open('index.html', 'a').write(f"\n<section")
            for arg in args:
                b = ' ' + arg
                open('index.html', 'a').write(f'''{b}''')
            open('index.html', 'a').write(">")
            
    def css(self, color='black', font_family='Arial', font_weight='False', text_align='left', font_size='False', background_color='False', background='False', margin_top='False', margin_bottom='False', margin_left='False', margin_right='False', border='False', display='block', padding='False', height='False', width='False', line_break='False', line_height='False', overflow='False', margin='False', box_shadow='False'):
        """
        Args:
            color (str, optional)            : CSS Color parameter. Defaults to 'black'.
            font_family (str, optional)      : CSS Font-Family parameter. Defaults to 'Arial'.
            font_weight (str, optional)      : CSS Font-weight parameter. Defaults to False.
            text_align (str, optional)       : CSS Text-align parameter. Defaults to 'left'.
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
        
        with open('style.css', 'a') as s:
            if self.p:
                s.write(f'''
p {{
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
            elif self.div_class != 'False':
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
            elif self.sec_class != 'False':
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
