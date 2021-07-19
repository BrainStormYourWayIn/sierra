# sierra

<p align='center'>
<img src="https://github.com/BrainStormYourWayIn/sierra/blob/main/logo.jpg" alt="Sierra"/>
</p>

![GitHub](https://img.shields.io/github/license/BrainStormYourWayIn/sierra?color=blue)

Sierra is a Python library to write HTML and CSS in pure Python using the DOM API in a simple yet elegant manner. Take advantage of Python's powerful 
functionalities with ease. Loops, variables, functions, libraries - you name it, you have it.

Here are a few advantages of using Sierra over other Python libraries that use the DOM API:

- Out-of-the-box support for all CSS styling attributes for all tags
- Display a table by simply putting in a CSV file
- Create your own tag functions with absolute ease using `@tag` and `@CmTag`. You can decide their behavior and use them within content-managers too
- Improvement in the arrangement look of the code and intelligent handling of tags with    
`autoPrettify()` - Powered by bs4 and a feature like no other

You may also use this as a templating engine, although jinja and Django's templating engine is strongly recommended over this 

________________________________

## Documentation

- **Check out the [documentation of Sierra](https://brainstormyourwayin.github.io/sierra.github.io/)**

________________________________

**Installation and Upgrade**

    pip install sierra
    
    pip install --upgrade sierra
    
Starting off is pretty simple and straightforward:
```python
from sierra import *
    
title('Hello World!')
```
    
The `title()` function at the start is mandatory, since it commences the HTML and the CSS file, which is created in the working directory upon execution on the code.

You can create custom tag functions with @tag and @CmTag with just three lines of code. Say you want to create a function for &lt;meta&gt;:
```python
@tag
def meta(**kwargs):
    pass
        
# Using them
    
meta(name="description", content="This is some description")
meta(name="viewport", content="width=device-width", initial_scale=1.0)
```

Underscores are used for hyphens (same applies to CSS) and Python-conficting arguments are prefixed with a double underscore.

Using argument `text` inside of a function defined in `@tag` will create a tag that opens, enters text, and closes. Something like this:
```python
@tag
def script(**kwargs):
    pass
script(__async="", src="some_src", text="some_text")
```
Is the equivalent of:
```html
<script async="" src="some_src">some_text</script>
```
Want to add some JS? Simple enough. Just create a function for the &lt;script&gt; tag with a context manager behavior using `@CmTag` and you're golden.   
```python
@CmTag
def script(**kwargs):
    pass

# Here I'll be replicating the script needed to add Google Analytics to a webpage

with script(__aync="", src="https://www.googletagmanager.com/gtag/js?id=UA—XXXXXXXX-X"):
    pass
    
with script():

    writeWA('''
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'UA—XXXXXXXX-X');
  ''')
```
This is the equivalent of:
```html
<script async src="https://www.googletagmanager.com/gtag/js?id=UA—XXXXXXXX-X"></script>

<script>
    
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'UA—XXXXXXXX-X');
    
</script>
```
`writeWA()` writes text entered into it into the HTML file as it is. 

You can add fonts using `addFont()`
```python
addFont("https://fonts.googleapis.com/css2?family=Roboto&display=swap")
```
Once things at the `<head>` of the HTML are settled (CSS is automatically linked), begin the body of the HTML with
```python
openBody()
# You can add any number of styling arguments to the body within openBody()
openBody(background_color='yellowgreen', opacity='0.9')
```
You can create `div` and `section` tags this way:
```python
with div(__class="some_class") as d:
    p('This is a paragraph!')
    d.css(background_color="#5886d1")
```
Let's break this down but-by-bit:  
First, we start a `div` with a context manager behavior and give it an attribute `__class`, which is essentially the tag attribute `class` (remember Python-conflicting) arguments are prefixed by a double underscore.

`p()` is a function, as the name suggests, to add a `<p>` tag. You can give the tag attributes with `**kwargs`, if you like.   
`p('Hello World!', __class='p_class')` is the same as `<p class="p_class">Hello World!</p>`

After the paragraph, there's a `d.css()`. This adds CSS to the `class` mentioned within `div()`. If a `class` is mentioned, CSS is added to that class as the first priority. If an `id` is mentioned, CSS is added to that `id` as a second priority. If none of both are mentioned, CSS is just added to `div`.

The behavior of `div` shown above also applies to `section`.

You can open a new tag with `Tag()`
```python
with Tag('some_tag', id='some_id') as t:
    p('A paragraph in <some_tag>')
    t.css(color='blue')
```
Although here, `.css()` behaves differently. It is independent of tag attributes, meaning CSS is added directly to the tag mentioned, which is `some_tag`

To add CSS to a specific attribute in the tag, use `writeCSS()`
```python
writeCSS(tag_name, **kwargs)

writeCSS("#some_id", color='blue')
```
This adds CSS to the `some_id`.

You can add a table to the HTML page by inputting in a CSV file this way:
```python
with Table() as t:
    t.get_table("path/to/file.csv")   # Add attributes with **kwargs here
    t.css(border="1px solid black")   # Use writeCSS to add CSS to a specific attribute
```
There are MANY more functionalities to Sierra that you can see from the [documentation](https://brainstormyourwayin.github.io/sierra.github.io/)

At the end of all development with Sierra, use
```python
autoPrettify()
```
It takes in no arguments, but provides SO much to the code.

Have a look at this example to see just how `autoPrettify()` works:
   
<p align=center>
<a href="https://colab.research.google.com/github/pranavr2003/hvejbvfn/blob/main/sierra_interactive.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
</p>

________________________________

### Contact Us

Email: brainstormyourwayin@gmail.com

**Or you can contact either of us individually if you like. See our individual GitHub profiles for information**.

________________________________

**Open with GitPod**

[![GitPod](https://www.gitpod.io/svg/media-kit/logo-dark-theme.svg)](https://gitpod.io/#https://github.com/BrainStormYourWayIn/sierra/)

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
