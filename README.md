# sierra

![sierra logo](https://github.com/BrainStormYourWayIn/sierra/blob/main/logo.jpg)

Sierra is a Python micro templating engine that makes skeletal integration with web frameworks faster. You can now develop your web application purely in Python, taking full advantage of its powerful functionalities. 

It can also be used standalone in developing web applications

You can also use this as an alternative to jinja or Django or another templating engine, or use it along with one

It's got features like displaying a table on the web application by loading in a .csv file, adding a bulleted list (ol/ul) by just passing in a Python list, automatic support for CSS styling arguments and more! You can use for loops, variables, functions - you name it, you have it, with Sierra. Improvement in the overall look of the code and intelligent handling of tags with `autoPrettify()`, a feature like no other. Harness the power of Python for your web applications!

![GitHub](https://img.shields.io/github/license/BrainStormYourWayIn/sierra?color=blue)

This is a relatively new project, so we're developing at a fast pace. If you have any suggestions or issues or just want to open a discussion, feel free to do so!

________________________________

## Documentation

- **Check out the [documentation of Sierra](https://brainstormyourwayin.github.io/sierra.github.io/)**
- **Check out a [comprehensive example](https://github.com/BrainStormYourWayIn/sierra_doc/blob/main/doc.py) of its use**

> The example mentioned above is the documentation of Sierra, which was written with Sierra - standalone

________________________________

## Example

Using this with Flask makes life easier if you're developing web applications with just HTML and CSS. Adding JS is not supported by Sierra and has to be done manually (if desired).

Here's a little example for this:

```python
from flask import Flask, render_template
from sierra import *

app = Flask(__name__)

def the_template():                              # Creating a simple template
    title('bulleted_and_description_lists')
    head('this is a bulleted list')

def adding_table():
    the_template()
    with div(None, attr="id='div_id'"):             # Creating a <div> with id='div_id'

        with startTable() as st:                    # Creating a table within the <div> tag
        
            st.getTable('path/to/file.csv')    # Dislaying the table from a csv file
            st.css('font_family="Arial, Helvetica, sans-serif", border="1px solid #d1d5e8", padding='8px', width='20%')
               
            
    autoPrettify()
    write_to_template('index1.html')

def bulleted_and_des_list():
    the_template()
    
    with div(div_class='description_list'):       # Creating div

        a = [[['coffee', 'tea'], ['black coffee', 'black tea']], [['new_coffee'], ['foo', 'tea', 'green_tea']]]
        # Displaying a description list
        des_lists(a)

        with section(sec_class='unordered_list') as s:    # Creating section inside div
            ul_list = ['This', 'is', 'an', 'ul']        # Creating an unordered list
            with bullets(ul=True, points=ul_list):      # Displaying it
                pass        

    autoPrettify()
    write_to_template('index2.html')

@app.route("/adding_table")
def show_adding_table():
    adding_table()
    return render_template('index1.html')

@app.route("/bulleted_and_des_list")
def show_bulleted_and_des_list():
    bulleted_and_des_list()
    return render_template('index2.html')

if __name__ == '__main__':
    app.run()
```

First, the directory structure needs to get sorted before running this. Run the code outside of `templates/`.

Here with `write_to_template()`, you can name your HTML file and call the function which takes only that argument to write the file into the 
`templates/` folder.    

Move `style.css` manually into the `static/`. On `<link rel=stylesheet href=style.css>`, change the `href` attribute and voila!   

Of course, you can also define the functions in separate files and import it.   

Sierra can also be used standalone without Flask, like this:

```python
from sierra import *

title('The title goes here')
head('Sierra!', type='h2', color="#0388fc")
openBody()

with open_tag('newTag') as t:       # Opening a tag 'newTag'

    with div('someClass') as d:     # Creating a div within  'newTag'
        p('Some text')                   # Adding a paragraph
        d.css(background_color='rgb(211, 111, 121)')          # Adding CSS to the div
        
        with section('anotherClass', "id='some_id'"):         # Creating section within the div within 'newTag'
            with startTable() as st:
                st.getTable(/path/to/file.csv, attr="id='table_id'")     # Displaying a table from a CSV and giving it an id
                
                with cTags('#table_id') as t:          # Adding CSS from the table id
                    t.css(font_family="Arial, Helvetica, sans-serif", border="1px solid #d1d5e8", padding='8px', width='20%')     
                    
            p('This is a paragrah within a section, which is within a div tag and comes afer the table')

    with image(src='sierra.jpg'):    
        i.show()                        # Displaying an image
        i.css(opacity=1.2)              # Adding CSS to it
         
    p('This is a paragraph that doesn't come under any div or a section, but comes under <newTag>. Simple stuff, really!')
    
autoPrettify() 
```

Here's another example of using it standalone - a function to scrape all text within the p tag from the source code of a URL using requests:
    
```python3

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

- Improved `write_to_template()` to provide for stylesheets
- Deprecation of automatic styling arguments, better handling will be done (possibly using `**kwargs`)
- Support for HTML forms
- `get_input()` for input tags
- Support for Close-on-Close tags (like <area>. While this is covered by `autoPrettify()` when you use `open_tag('area/any other tag')`, we think it's probably better to have a separate function dedicated to this to improve the look of the Python code)
- Support to make a web application mobile-friendly

**See `release_prots.py`**

________________________________

### Contact Us

Email: brainstormyourwayin@gmail.com

**Or you can contact either of us individually if you like. See our individual GitHub profiles for information**.

________________________________


**It featured on the [Python Weekly Newsletter Issue 505](https://newsletterest.com/message/62517/Python-Weekly-Issue-505) just 2 weeks into the first release.**

**It got mentioned by [AwesomePython](https://pythonawesome.com/a-python-framework-for-building-and-integrating-web-app/).**

**...and [got tweeted out by PythonHub on Twitter](https://twitter.com/pythonhub/status/1409727123888259073), which has about 75k followers.**

All in just the first three weeks of releasing the first version of Sierra!

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
>
>> Copyright (c) 2011-2020, Open source contributors.
