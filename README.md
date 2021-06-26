# sierra

![sierra logo](https://github.com/BrainStormYourWayIn/sierra/blob/main/logo.jpg)

Sierra is a Python3 templating library for web frameworks

### Sierra makes integration with Flask much easier and faster! See the examples below

[![Downloads](https://pepy.tech/badge/sierra)](https://pepy.tech/project/sierra)
[![Downloads](https://pepy.tech/badge/sierra/month)](https://pepy.tech/project/sierra)

________________________________

## Documentation

Check out the [Official documentation of Sierra](https://brainstormyourwayin.github.io/sierra.github.io/).

Check out a [comprehensive example](https://github.com/BrainStormYourWayIn/sierra_doc/blob/main/doc.py) of its use.

________________________________

## Sierra

Sierra can also be used standalone without Flask, if you like

Using this with Flask makes life easier

```python3
from flask import Flask, render_template
from sierra import *

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

def description_list():
    the_template()
    a = [['coffee'], ['black coffee', 'black tea']]
    def_lists(a)
    autoPrettify()

@app.route("/bulleted_list")
def show_bulleted_list():
    return bulleted_list()
    return render_template('index1.html')
    

@app.route("/description_list")
def show_description_list():
    return description_list()
    return render_template('index2.html')
    
if __name__ == '__main__':
    app.run()

```
Of course, you can also define the functions in separate files and import it  

The directory structure needs to be sorted out first before running this. Run the code in `templates/`. In Sierra, the HTML and CSS files are automatically named `index.html` and `style.css` in the working directory, which will be sorted in the next release. 

________________________________

## Installation

To download the library (pypi version):

`pip install sierra`

To download the library (GitHub Version):

`pip git+git://github.com/BrainStormYourWayIn/sierra`

________________________________


Use `pip install --upgrade sierra` to upgrade the library

________________________________


## See the [official documentation of Sierra](https://brainstormyourwayin.github.io/sierra.github.io/) for more!

________________________________

## Upcoming

We're working on making this a templating library for web frameworks.

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
> Copyright (c) 2008-2011, AQR Capital Management, LLC, Lambda Foundry, Inc. and PyData Development Team
> Copyright (c) 2011-2020, Open source contributors.
