# sierra

<p align='center'>
<img src="https://github.com/BrainStormYourWayIn/sierra/blob/main/logo.jpg" alt="Sierra"/>
</p>

![GitHub](https://img.shields.io/github/license/BrainStormYourWayIn/sierra?color=blue)

Sierra is a Python native engine for web development, which makes templating for the backend faster, as well as have full control on your frontend. You can now develop your web application purely in Python, taking full advantage of its powerful functionalities with simple and elegant syntax. 

This was in part inspired by [Dominate](https://github.com/Knio/dominate), but has support for CSS styling attributes, better syntax, more use cases and many more functionalities

It can be used standalone in developing web applications

You can also use this as an alternative to jinja or Django's templating or any other templating engine, or even use it along with one

It's got features like displaying a table on the web application by loading in a .csv file, adding a bulleted list (ol/ul) by just passing in a list, automatic support for CSS styling arguments and more! You can use for loops, variables, functions - you name it, you have it, with Sierra. Improvement in the overall look of the code and intelligent handling of tags with `autoPrettify()`, a feature like no other. Harness the power of Python for your web applications!

________________________________

## Documentation

- **Check out the [documentation of Sierra](https://brainstormyourwayin.github.io/sierra.github.io/)**
- **Check out a [few examples](https://github.com/BrainStormYourWayIn/sierra_examples/) of its use**

> The examples mentioned above is a simple bare-boned book search engine created with requests, bs4, Flask and Sierra; and the documentation of Sierra, which was written with Sierra standalone

________________________________
**Have a look at `src/sierra/custom_tags.py` and `release_prots.py` for a sneak-peek on the next release updates. We got some things going on there!**
________________________________


## Example

Using this with Flask makes life easier if you're developing web applications with just HTML and CSS. Adding JS with manual functions will be supported by Sierra in the coming release(s)

Here's a little example for this:

```python
from flask import Flask, render_template
from sierra import *

app = Flask(__name__)

def the_template():                              
    title('Some title', templating=True)         # Set templating to True if you're using Flask 
    head('Just a heads up', 'h2')
    openBody()

def adding_table():

    the_template()
    with div(None, attr="id='div_id'"):           

        with startTable() as st:                    # Creating a table within the <div> tag
        
            st.getTable('path/to/file.csv')    
            st.css(font_family="Arial, Helvetica, sans-serif", border="1px solid #d1d5e8", padding='8px', width='20%')     
               
            
    autoPrettify()
    write_to_template('index1.html')

def pre_and_unordered_list():

    the_template() 
    with div(div_class='description_list'):       

        with open_tag('pre') as pr:
            writeWA("Some text within the <pre> tag")
            pr.css(background_color="#e1e8e3")

        with section(sec_class='unordered_list') as s:                 # Creating section inside div
            ul_list = ['This', 'is', 'an', 'unordered', 'list']        
            with bullets(ul=True, points=ul_list):      
                pass        

    autoPrettify()
    write_to_template('index2.html')

@app.route("/adding_table")
def show_adding_table():
    adding_table()
    return render_template('index1.html')

@app.route("/pre_and_unordered_list")
def show_pre_and_unordered_list():
    pre_and_unordered_list()
    return render_template('index2.html')

if __name__ == '__main__':
    app.run()
```

First, the directory structure needs to get sorted before running this. Run the code outside of `templates/`.

Here with `write_to_template()`, you can name your HTML file and call the function which takes only that argument to write the file into the `templates/` folder. `style.css` is automatically put into `static/` when this function is called. 

In `title()`, set the argument `templating` to True, if Sierra is being used to template with Flask

Of course, you can also define the functions in separate files and import it.   

Sierra can also be used standalone without Flask, like this:

```python
from sierra import *

title('The title goes here')
head('Sierra!', type='h2', color="#0388fc")
openBody()

with open_tag('newTag'):      

    with div('someClass') as d:     
        p('Some text within the div')                   
        d.css(background_color='rgb(211, 111, 121)')          # Adding CSS to the div
        
        with section('anotherClass', "id='some_id'"):         # Creating section within the div within 'newTag'
            with startTable() as st:
                st.getTable(/path/to/file.csv, attr="id='table_id'")   
                
                with cTags('#table_id') as t:
                    t.css(font_family="Arial, Helvetica, sans-serif", border="1px solid #d1d5e8", padding='8px', width='20%')     
                    
            p("This is a paragrah within a section, which is within a div tag and comes afer the table")

    with image(src='sierra.jpg'):    
        i.show()                        # Displaying an image
        i.css(opacity=1.2)              # Adding CSS to it
         
    p("This is a paragraph that doesn't come under any div or a section, but comes under <newTag>. Simple stuff, really!")
    
autoPrettify() 
```

Here's another example of using it standalone - a function to scrape all text within the `<p>` tag from the source code of a URL using requests:
    
```python

import re
import requests
from sierra import *
    
def extractpText(url):

    http = urllib3.PoolManager()
    req = http.request('GET', url)
    respData = str(req.data)    
    regex = '<p>(.*?)</p>'
    paragraphs = re.findall(regex, respData)
    return paragraph

# Displaying it on the web application

title('Extracting text from the p tag given a URL')
openBody()

with open_tag('pre'):           # Showing the output within the <pre> tag

    writeWA(f'''
    All following text appears within the &lt;p> tag of 'http://example.com':
    {extractpText("http://example.com/")}
    ''')


autoPrettify()

```
Notice that while `&lt;` was used as an escape sequence for the '<' of the paragraph tag, `&gt;` was not used. Why? Well that's because of the power of `autoPrettify()` at the end! It detects a starting escape sequence and detects that where there's a closing tag, an escape sequence was intended. So it fills the gap in when you use the function at the end of development. Huh! How cool is that?!


### See the [documentation](https://brainstormyourwayin.github.io/sierra.github.io/) for more

________________________________

## Installation

To download the library:

    pip install sierra

________________________________

## Upgrade

To upgrade the library:

    pip install --upgrade sierra

________________________________

### Upcoming (in order of priority):

- Enable auto-introduction of custom tags tags like `span`, `label`, `input` or anything, with decorators (See `release_prots.py`)
- In-memory storage for the HTML and CSS file (See `release_prots.py`)
- Deprecate cTags() and just introduce a new function called css(), since adding CSS with a class is longer than simply doing css('.some_class', color='blue',           font_size='20px')
- Deprecate the attr argument and instead use **kwargs to add tag attributes
- Add an option for in-memory storage, see release_prots.py
- Use `kwargs` to add tag attributes
- Change startTable and createTable to start_table and create_table

**See `release_prots.py`**

________________________________

### Contact Us

Email: brainstormyourwayin@gmail.com

**Or you can contact either of us individually if you like. See our individual GitHub profiles for information**.

________________________________

**We work exclusively on GitPod**

![GitPod](https://www.gitpod.io/svg/media-kit/logo-dark-theme.svg)

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
>> Copyright (c) 2008-2011, AQR Capital Management, LLC, Lambda Foundry, Inc. and PyData Development Team.    
>> Copyright (c) 2011-2020, Open source contributors.
