# -*- coding: utf-8 -*-
import webbrowser
from pyramid_nightly import *

# Driver
if __name__ == "__main__":
    title('nothing')
    addInitc()
    head('nothing more', font_size='90px', color='blue', text_align='center', background_color='orange')
    startBody(background_color='green', opacity=0.8)
    
    x = tTags(True)
    x.start_p("I'm sure about this man")
    x.css(color='green')
    close_tags('p')

    d_class = 'newClass'
    x = tTags(div_class=True)
    x.start_div(d_class)
    x.css(color='yellow', font_family='Times New Roman', background_color='blue')

    WriteHTML("I'm REALLY" + b + "sure of this")
    close_tags('div')

    s_class = 'anotherClass'
    x = tTags(sec_class=True)
    x.start_sec(s_class)
    x.css(color='whitesmoke', background_color='rgb(35, 51, 89)')

    WriteHTML("I'm defo" + b + "sure of this")
    close_tags('section')

    endBody()
    AutoCloseTags()

    webbrowser.open(f'{index}.html')
