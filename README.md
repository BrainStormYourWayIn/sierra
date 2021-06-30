# sierra

![sierra logo](https://github.com/BrainStormYourWayIn/sierra/blob/main/logo.jpg)

Sierra is a Python3 micro templating library that makes skeletal integration with web frameworks faster. You can now develop your web application purely in Python, taking full advantage of it's powerful functionalities.
You can use this as an alternative to jinja or Django or another templating engine IF you're code doesn't involve JS, since Sierra doesn't natively support JS. If you do want to use this with JS, it has to be done manually.

We got features like displaying a table on the web application by loading in a .csv file, adding a bulleted list (ol/ul) by just passing in a Python list, automatic support for CSS styling arguments and more! You can use for loops, variables, functions - you name it, you have it, with Sierra. Harness the power of Python for your web applications!

[![Downloads](https://pepy.tech/badge/sierra)](https://pepy.tech/project/sierra)
[![Downloads](https://pepy.tech/badge/sierra/month)](https://pepy.tech/project/sierra)
![GitHub](https://img.shields.io/github/license/BrainStormYourWayIn/sierra?color=blue)

Download using `pip install sierra`   
Use `pip install --upgrade sierra` to upgrade

________________________________

## Documentation

- **Check out the [documentation of Sierra](https://brainstormyourwayin.github.io/sierra.github.io/)**
- **Check out a [comprehensive example](https://github.com/BrainStormYourWayIn/sierra_doc/blob/main/doc.py) of its use**

________________________________

## Example

Using this with Flask makes life easier if you're developing web applications with just HTML and CSS. Adding JS is not supported by Sierra and has to be done manually (if desired).

```python
from flask import Flask, render_template
from sierra import *

app = Flask(__name__)

def the_template():                              # Creating a simple template
    title('bulleted_and_description_lists')
    head('this is a bulleted list')

def img_map():
    the_template()
    with div(None, attr="id='div_id'"):             # Creating a <div> with id='div_id'
    
        with image(src='workplace.jpg', attr="usemap='#workmap'") as i:  
           # Loading an image and giving it attr usemap
            i.show()                # Displaying the image
            i.css(opacity=1.7)      # Adding CSS to it

        with open_tag('map', attr='name="workmap"'):  
        
          # Creating an image map which performs different actions
          # based on where it is clicked, which is determined by
          # specific shapes and coordinates on the image
        
            shape = ['rect', 'rect', 'circle']
            coords = ["34,44,270,350", "290,172,333,250", "337,300,44"]
            alt = ['Computer', 'Phone', 'Coffee']
            href = ['computer.htm', 'phone.htm', 'coffee.htm']

              # Using lists and for loop to make the shape and coordinate mapping faster (see doc)

            for shape, coord, alt, href in zip(shapes, coords, alt, href):       
                with open_tag('area', attr=f'shape="{shape}" coord="{coord}" alt="{alt}" href="{href}"'):
                    pass
                    
    autoPrettify()       
    write_to_template('index1.html')
    

def bulleted_and_des_list():
    the_template()
    
    with div(div_class='description_list'):       # Creating div
    
        a = [[['coffee', 'tea'], ['black coffee', 'black tea']], [['new_coffee'], ['foo', 'tea', 'green_tea']]]
                    # Displaying a description list
        des_lists(a)        
        
        with section(sec_class='unorder_list') as s:    # Creating section inside div
            ul_list = ['This', 'is', 'an', 'ul']        # Creating an unordered list
            with bullets(ul=True, points=ul_list):      # Displaying it
                pass        
        
    autoPrettify()
    write_to_template('index2.html')

@app.route("/img_map")
def show_img_map():
    img_map()
    return render_template('index1.html')

@app.route("/bulleted_and_des_list")
def show_bulleted_and_des_list()():
    bulleted_and_des_list()()
    return render_template('index2.html')

if __name__ == '__main__':
    app.run()
```
Here with `write_to_template()`, you can name your HTML file and call the function which takes only that argument to write the file into the 
`templates/` folder.
Of course, you can also define the functions in separate files and import it.
The directory structure needs to be sorted out first before running this. Run the code outside of `templates/`.

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

autoPrettify() 
```

### See the [documentation](https://brainstormyourwayin.github.io/sierra.github.io/) for more

________________________________

## Installation

To download the library (PyPi Version):

    pip install sierra

To download the library (GitHub Version):

    pip git+git://github.com/BrainStormYourWayIn/sierra

________________________________

## Upgrade

To upgrade the library:

    pip install --upgrade sierra

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
