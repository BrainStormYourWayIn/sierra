# These are release prototypes, a good view of what you can expect in the coming release(s)

# See the history for previous prototypes. 
# 1/1 implemented
# 1/1 todo

# In memory storage of HTML and CSS files.
# Right now, an `index.html` and `style.css` is created in the working directory when Sierra's title() is executed.
# In-mem storage uses StringIO to save the contents of `index.html` and `style.css` into variables.
# This will be useful when using Sierra with frameworks other than Flask.

# So something like:

import io
import os
from flask import Flask

def autoPrettify(in_mem=False):
    if in_mem is False:
        # Auto Prettify's working code
        pass
    if in_mem == True:
        autoPrettify(in_mem=False)
        
        with open("index.html", 'a+') as f:
            f.write("\n\n<style>")
            styling = open("style.css", 'r').read()
            f.write(f"\n{styling}")
            f.write("\n\n</style>")
            
        os.remove("style.css")

        global index_html
        index_html = open("index.html", 'r').read()
        index_html = io.StringIO(index_html)

app = Flask(__name__)

@app.route("/some_route")
def some_func():
    autoPrettify()
    return index_html

# This way, Sierra can also be used with other web frameworks in an easier way.
# This is still just a prototype, yet to test and run.
