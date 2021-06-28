# sierra

![sierra logo](https://github.com/BrainStormYourWayIn/sierra/blob/main/logo.jpg)

Sierra is a Python3 templating library for web frameworks

### Sierra makes skeletal integration with Flask easier and faster! See the examples below

[![Downloads](https://pepy.tech/badge/sierra)](https://pepy.tech/project/sierra)
[![Downloads](https://pepy.tech/badge/sierra/month)](https://pepy.tech/project/sierra)

## The next release coming very soon will have major changes in the working and syntax revamps. See 'Upcoming' 

________________________________

## Documentation

**Check out the [documentation of Sierra](https://brainstormyourwayin.github.io/sierra.github.io/).**

**Check out a [comprehensive example](https://github.com/BrainStormYourWayIn/sierra_doc/blob/main/doc.py) of its use.**

________________________________

## Sierra

Sierra can also be used standalone without Flask, if you like

Using this with Flask makes life easier if you're developing web applications with just HTML and CSS. Adding JS is not supported by Sierra and has to be done manually, if desired

```python3
from flask import Flask, render_template
from sierra import *
import os

app = Flask(__name__)

def the_template():
    title('bulleted_and_description_lists')
    head('this is a bulleted list')
    
def bulleted_list():
    the_template()
    abc = 'stuff!'
    bullets = ['This', 'is', 'easy', abc]
    addBullets(points=bullets)
    autoPrettify()
    os.rename('index.html', 'index1.html')

def description_list():
    the_template()
    a = [[['coffee', 'tea'], ['black coffee', 'black tea']], [['new_coffee'], ['foo', 'tea', 'green_tea']]]
    def_lists(a)
    autoPrettify()
    os.rename('index.html', 'index2.html')

@app.route("/bulleted_list")
def show_bulleted_list():
    bulleted_list()
    return render_template('index1.html')
    

@app.route("/description_list")
def show_description_list():
    description_list()
    return render_template('index2.html')
    
if __name__ == '__main__':
    app.run()
```

Of course, you can also define the functions in separate files and import it  

The directory structure needs to be sorted out first before running this. Run the code in `templates/`. In Sierra, the HTML and CSS files are automatically named `index.html` and `style.css` in the working directory, so you need to run `os.rename()`

________________________________

## Installation

To download the library (pypi version):

    pip install sierra

To download the library (GitHub Version):

    pip git+git://github.com/BrainStormYourWayIn/sierra

________________________________

## Upgrade

Use to upgrade the library:

    pip install --upgrade sierra

________________________________

## Upcoming

##### We're working on making this a templating library for web frameworks. The next release will have major revamps to both the syntax and the working, including efficient handling of closing and opening tags, using div section and p tags, and addition of attributes to HTML tags among others

________________________________

## License

   Copyright 2021 BrainStormYourWayIn

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

> Pandas (pandas)
> 
> Copyright (c) 2008-2011, AQR Capital Management, LLC, Lambda Foundry, Inc. and PyData Development Team.
> 
> Copyright (c) 2011-2020, Open source contributors.
