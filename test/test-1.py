# -*- coding: utf-8 -*-
import webbrowser
from sierra import *

# Driver
if __name__ == "__main__":
    title('nothing')
    head('nothing more', font_size='90px', color='blue', text_align='center', background_color='orange')
    openBody(background_color='green', opacity=0.8)
    
    x = tTags(True)
    x.start_p("I'm sure about this man")
    x.css(color='red', background_color='orange', line_height='25px')
    closeTags('p')

    d_class = 'newClass'
    x = tTags(div_class=True)
    x.start_div(d_class)
    x.css(color='yellow', font_family='Times New Roman', background_color='blue')

    writeHtm("I'm REALLY" + b + "sure of this")
    closeTags('div')

    s_class = 'anotherClass'
    x = tTags(sec_class=True)
    x.start_sec(s_class)
    x.css(color='whitesmoke', background_color='rgb(35, 51, 89)')

    writeHTML("I'm defo" + b + "sure of this")
    closeTags('section')

    a = startTable()
    c = ['england', 'best', 'six', 'euros']
    r1 = ['kane', 'grealish', 'sancho', 'sterling']
    r2 = ['foden', 'mount', 'bellingham', 'reece']
    r3 = ['trippier', 'stones', 'walker', 'coady']
    a.createTable(c, r1, r2, r3)

    closeBody()
    closeHTML()
    autoPrettify()                # To close unclosed tags

    webbrowser.open("index.html") # To open HTML file in default browser
