# sierra

![sierra logo](https://github.com/BrainStormYourWayIn/sierra/blob/main/logo.jpg)

Sierra is a Python3 micro templating library that makes skeletal integration with web frameworks faster. You can now develop your web application purely in Python, taking full advantage of it's powerful functionalities.
You can use this as an alternative to jinja or Django or another templating engine IF you're code doesn't involve JS, since Sierra doesn't natively support JS. If you do want to use this with JS, it has to be done manually.

[![Downloads](https://pepy.tech/badge/sierra)](https://pepy.tech/project/sierra)
[![Downloads](https://pepy.tech/badge/sierra/month)](https://pepy.tech/project/sierra)

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

def the_template():
    title('bulleted_and_description_lists')
    head('this is a bulleted list')

def bulleted_list():
    the_template()
    with bullets(ul=True, points=['This', 'is', 'easy', 'stuff!']):
        pass
    autoPrettify()
    write_to_template('index1.html')

def description_list():
    the_template()
    a = [[['coffee', 'tea'], ['black coffee', 'black tea']], [['new_coffee'], ['foo', 'tea', 'green_tea']]]
    def_lists(a)
    autoPrettify()
    write_to_template('index2.html')

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

Sierra can also be used standalone without Flask, like this:

```python
from sierra import *

title('The title goes here')
head('Sierra!', type='h2', color="#0388fc")
openBody()

with open_tag('newTag') as t:
    with div('someClass') as d:
        p('Some text')
        d.css(background_color='rgb(211, 111, 121)')
        with section('anotherClass', "id='some_id'"):
            with bullets(ul=True, points=['pt1', 'pt2']):
                pass
            p('THIS IS SO EASY! Lesser code and more productivity!')

    with image(src='sierra.jpg'):
        i.show()
        i.css(opacity=1.2)

autoPrettify() 
```

Of course, you can also define the functions in separate files and import it.
The directory structure needs to be sorted out first before running this. Run the code outside of `templates/`.

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
