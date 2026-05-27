# Sierra

## About

**Sierra is a Python library to write HTML and CSS in pure Python using the DOM API in a simple yet elegant manner.**

Take advantage of Python's powerful functionalities with ease.
Loops, variables, functions, libraries - you name it, you have it.

Here are a few advantages of using Sierra over other Python libraries that use the DOM API:

- Out-of-the-box support for all CSS styling attributes for all tags
- Display a table by simply putting in a CSV file
- Create your own tag functions with absolute ease using `@tag` and `@CmTag`. You can decide their behavior and use them within content-managers too
- Improvement in the arrangement look of the code and intelligent handling of tags with `autoPrettify()` - Powered by bs4 and a feature like no other

**You may also use this as a templating engine, although jinja and Django's templating engine is strongly recommended over this.**

## Installation

To Download the library:

```bash
pip3 install sierra
```

## Upgrade

To Upgrade the library:

```bash
pip3 install --upgrade sierra
```

## Documentation

Check out the [documentation](./Documentation.md) of Sierra

Starting off is pretty simple and straightforward:

```python
from sierra import *

title('Hello World!')
```

The `title()` function at the start is mandatory, since it commences the HTML and the CSS file, which is created in the working directory upon execution on the code.

You can create custom tag functions with `@tag` and `@CmTag` with just three lines of code. Say you want to create a function for `<meta>`

```python
@tag
def meta(**kwargs):
    pass

# Using them
meta(name="description", content="This is some description")
meta(name="viewport", content="width=device-width", initial_scale=1.0)
```

Underscores are used for hyphens (same applies to CSS) and Python-conficting arguments are prefixed with a double underscore.

Using argument text inside of a function defined in `@tag` will create a tag that opens, enters text, and closes. Something like this:

```python
@tag
def script(**kwargs):
    pass
script(__async="", src="some_src", text="some_text")
```

Is the equivalent of:

```html
<script async="" src="some_src">
  some_text
</script>
```

Want to add some JS? Simple enough. Just create a function for the `<script>` tag with a context manager behavior using `@CmTag` and you're golden.

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
    gtag('config', 'UA—XXXXXXXX-X');''')
```

This is the equivalent of:

```html
<script
  async
  src="https://www.googletagmanager.com/gtag/js?id=UA—XXXXXXXX-X"
></script>

<script>
  window.dataLayer = window.dataLayer || [];
  function gtag() {
    dataLayer.push(arguments);
  }
  gtag("js", new Date());
  gtag("config", "UA—XXXXXXXX-X");
</script>
```

`writeWA()` writes text entered into it into the HTML file as it is.

You can add fonts using `addFont()`

```python
addFont("https://fonts.googleapis.com/css2?family=Roboto&display=swap")
```

Once things at the `<head>` of the HTML are settled (CSS is automatically linked), begin the body of the HTML with:

```python
openBody()
# You can add any number of styling arguments to the body within openBody()
openBody(background_color='yellowgreen', opacity='0.9')
```

You can create `<div>` and `<section>` tags this way:

```python
with div(__class="some_class") as d:
    p('This is a paragraph!')
    d.css(background_color="#5886d1")
```

Let's break this down but-by-bit:

First, we start a div with a context manager behavior and give it an attribute `__class`, which is essentially the tag attribute class (remember Python-conflicting) arguments are prefixed by a double underscore.

`p()` is a function, as the name suggests, to add a `<p>` tag. You can give the tag attributes with `**kwargs`, if you like.

`p('Hello World!', __class='p_class')` is the same as `<p class="p_class">Hello World!</p>`

After the paragraph, there's a `d.css()`. This adds CSS to the class mentioned within `div()`. If a class is mentioned, CSS is added to that class as the first priority. If an id is mentioned, CSS is added to that id as a second priority. If none of both are mentioned, CSS is just added to div.

The behavior of div shown above also applies to section.

You can open a new tag with `Tag()`

```python
with Tag('some_tag', id='some_id') as t:
    p('A paragraph in <some_tag>')
    t.css(color='blue')
```

Although here, `.css()` behaves differently. It is independent of tag attributes, meaning CSS is added directly to the tag mentioned, which is some_tag

You can add a table to the HTML page by inputting in a CSV file this way:

```python
with Table() as t:
    t.get_table("path/to/file.csv")   # Add attributes with **kwargs here
    t.css(border="1px solid black")   # Use writeCSS to add CSS to a specific attribute
```

There are MANY more functionalities to Sierra that you can see from the [documentation](./docs.md)

At the end of all development with Sierra, use

```python
autoPrettify()
```

It takes in no arguments, but provides SO much to the code.

Have a look at this example to see just how `autoPrettify()` works.

## Example

Using this with Flask makes life easier if you're developing web applications with just HTML and CSS.
It can also be used standalone in developing web applications. You can also use this as an alternative to jinja or Django or another templating engine, or use it along with one.
It's got features like displaying a table on the web application by loading in a .csv file, adding a bulleted list (ol/ul) by just passing in a Python list, automatic support for CSS styling arguments and more! You can use for loops, variables, functions - you name it, you have it, with Sierra.
Improvement in the overall look of the code and intelligent handling of tags with `autoPrettify()`, a feature like no other. Harness the power of Python for your web applications!

> **Note for users**
> If you have any suggestions or issue or just want to open a discussion, feel free to do so!

## Contact Us

Check out the [contact page](./contact.md) for more information on how to get in touch with us.
