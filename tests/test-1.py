# -*- coding: utf-8 -*-
import webbrowser

from sierra import (
    autoPrettify,
    closeBody,
    closeHTML,
    div,
    head,
    openBody,
    startTable,
    title,
    writeHTML,
)

# Driver
if __name__ == "__main__":
    title("nothing")
    head(
        "nothing more",
        font_size="90px",
        color="blue",
        text_align="center",
        background_color="orange",
    )
    openBody(background_color="green", opacity=0.8)

    x = div()
    x.start_p("I'm sure about this man")
    x.css(color="red", background_color="orange", line_height="25px")

    d_class = "newClass"
    x = div(div_class=True)
    x.start_div(d_class)
    x.css(color="yellow", font_family="Times New Roman", background_color="blue")

    s_class = "anotherClass"
    x = div(sec_class=True)
    x.start_sec(s_class)
    x.css(color="whitesmoke", background_color="rgb(35, 51, 89)")

    a = startTable()
    c = ["England", "best", "six", "Euros"]
    r1 = ["kane", "Grealish", "sancho", "Sterling"]
    r2 = ["foden", "mount", "Bellingham", "Greece"]
    r3 = ["trippier", "stones", "walker", "coady"]
    a.createTable(c, r1, r2, r3)

    closeBody()
    closeHTML()
    autoPrettify()  # To close unclosed tags

    webbrowser.open("index.html")  # To open HTML file in default browser
