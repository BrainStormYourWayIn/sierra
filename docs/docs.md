# Documentation - Sierra v2.4.0

Wecome to the documentation of Sierra - **Sierra is a Python library to write HTML and CSS in pure Python using the DOM API in a simple yet elegant manner.**
Take advantage of Python's powerful functionalities with ease. **Loops, variables, functions, libraries** - you name it, you have it.
You can now develop your web application purely in Python, taking full advantage of its powerful functionalities with **simple and elegant syntax.**
You can use this along with another **templating engine**, or use it **standalone** - even without a web framework, if you like.
If you have any specific requests, open a discussion/issue on our GitHub page. Any contributions can also be made there.

Please read our [LICENSE](https://github.com/BrainStormYourWayIn/sierra/blob/main/LICENSE) before moving forward.

## Contents

- [Opening tags, Creating custom functions for you own, and controlling their behavior](#tags)
- [Using CSS](#css-ing)
- [Working with div, section and p tags](#tTags)
- [Adding images](#add_img)
- [Working with tables (Pandas supported)](#tables)
- [Bulleted lists (ordered and unordered)](#bullets_and_lists)
- [Adding a description list](#des_lists)
- [Other functions (add Bootstrap, script, escaping and more)](#other_funcs)
- [Working with Python Loops, Functions, Variables, Conditions and others](./python-features.md)

## Getting Started

```powershell
pip3 install sierra
```

can be done as an easier way of installing. You can also clone the repository and work inside of src/sierra if you like.

To import the library, simply use:

```python
from sierra import *
```

Once imported, **the first line of syntax is mandatory**, and all development to be displayed on the webpage must come after this:

```python
title(Title, icon=False)

#Args:
#    Title(str, compulsory) : Title of the HTML file.
#    icon(str, optional) : Icon to be displayed. Should be a .ico file. Defaults to no icon.
```

This creates an `index.html` and a `style.css` in the working directory.

You can add a header with `head()`. Start the body of the web application with `openBody()`. Add CSS with `**kwargs`.

```python
head(Head, type='header', **kwargs)
# head('Sierra', type='h1', color='#4287f5', font_family='Times New Roman')

#Args:
#    Head (str, compulsory)           : Caption header.
#    type (str, optional)             : Header type. Anything from 'h1' to 'h6'
#    **kwargs (optional)              : CSS styling arguments
        
openBody(**kwargs)
# openBody(background_color='blue', opacity=1.8)
```

You may notice in styling with `**kwargs`, that the styling argument `font-family` and `background-color` is entered in as `font_family` and `background-color`.
That is, underscores are used in `**kwargs` in the place of hyphens.
This is because Python returns a `SyntaxError` when hyphens are used in the key of `**kwargs`.

Hence, use underscores in `**kwargs` for hyphens in styling arguments.

Fonts can be added with `addFont()` which takes only one argument, which is the link to the font.

```python
addFont(font_link)
# If you're using Google Fonts, take only the href attribute.
# If <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@100&display=swap" rel="stylesheet"> 
# is the the font tag to Roboto, take only the href attribute, then use.

# addFont("https://fonts.googleapis.com/css2?family=Roboto:wght@100&display=swap") 
            
# You can then add "'Roboto', sans-serif" to the CSS as the font_family argument/font-family attribute,
# depending on the method of CSS used (See 'Using CSS').
```

---

## Using tags {#tags}

Tags can be opened with `Tag(name_of_tag, **kwargs)`, and CSS can be added with `.css()`, which is the same mechanism that `head()` and `openBody()` contains, except that it is now used as a function under a class.
Any inline within that tag can be entered with a context manager approach under `with`

```python
with open_tag('tag_name', attr=None) as t:
    t.css(font_color='rgb(11, 176, 89)')

    #  ---  Any content  ---  
```

Coming out of `with` automatically closes the tag. The `**kwargs` method, in `Tag()` enables the user to add attributes to their HTML tag.

```python
with open_tag('tag_name', attr="class='someClass' id='some_id'") as t:
    t.css(font_color='rgb(11, 176, 89)')

    #  ---  Any content  ---  
```

This is the equivalent of `<tag_name class='someClass' id='some_id'>`.

**Prefix Python-conflicting arguments with a double underscore, and use a single underscore in the place of a hyphen**.
Here, CSS is added to `tag_name`

With v2.4.0, you can **CREATE** functions for any tag and even control their behavior! Here's how you create 'short' tags that mostly come under `<head>`:

```python
@tag
def meta(**kwargs):
    pass

meta(name="description", content="This is some description")
meta(name="viewport", content="width=device-width", initial_scale=1.0)
```

This is equivalent to:

```html
<meta name="description" content="This is some description">
<meta name="viewport" content="width=device-width" initial-scale=1.0>
```

**Using argument `text=""` makes the tag close after the opening of the tag**, causing it to behave differently than tags like meta, which don't need
a closing. Remember that `__` is the equivalent of a single underscore and `_` is the equivalent of a hyphen!

```python
@tag
def script(**kwargs):
    pass

script(__async="", src="some_src", text="")            
# You can get any text to appear within the tag. 
# Not using 'text' creates a tag similar to the <meta> tag
# This is the equivalent of <script _async= src=some-src></script>
```

---

## Using CSS {#css-ing}

There are three ways you can add CSS to tags. The first one is with `.css()`, which takes in `**kwargs`, and can only be used within the context managers of already existing syntax, like `Tag()` and `div()`.
Underscores are used in the key or `**kwargs` instead of hyphens in styling attributes.

```python
.css(**kwargs)
```

The second way is to use `writeCSS()`. It takes in a dictionary of CSS attributes, and adds them to the tag mentioned as the first argument in `writeCSS()`.

```python
writeCSS(tag, *args)
# *args takes in a dictionary of styling attributes.

#writeCSS('pre', {"background-color": "#edf7f7", "margin-left": "0.1%"})
# This adds the specified CSS attributes in the dictionary to the tag <pre>
```

The third way is to use `writeCSS_raw()`. Any text you specify in `writeCSS_raw()` gets written into the CSS file.

```python
writeCSS_raw(r"""
pre {
    background-color: #edf7f7;
    margin-left: 0.1%;
} a""")

# This writes the exact text in writeCSS_raw() to style.css
```

---

## Working with div, section and p tags {#tTags}

Division and section tags can be opened the same way as `Tag()`, except the syntax is `div(**kwargs)` and `section(**kwargs)` respectively.
It can take in tag attributes through the `**kwargs` method.
Prefix conflicting arguments with a double underscore and use a single underscore for hyphens.
While adding CSS for this is similar to the mechanism in `Tag()`, it differs in the fact that the `.css()` here prioritizes tag attributes given.
The first priority being for `__class`, the second being for `id`, and if both don't exist, CSS is just added to the tag raw.
That is `div` or `section`. Entering in both `__class` and `id` results in CSS being added to the class, and enters it to id in the absence of `__class`.
If you don't want to add CSS this way using `.css()`, use `writeCSS()` instead, where you can add CSS to any tag/attribute, simply use `'#name_of_id'` or `'.name_of_class'` as the first argument.

```python
div(**kwargs)
section(**kwargs)

#with div(__class='div_class') as d:
#    d.css(background_color="#e0e330")
#    with section(id='sec_id'):
#        p("This is a paragraph inside a section which has attribute id=sec_id, and is inside a div")

#writeCSS('#sec_id', margin_top='30px')
```

`<p>` tags can be added with `p()`.
The text to be added goes into the `text` attribute, and tag attributes, as usual, can be added to `attr`.
However, `p()` is not a context manager-based approach, as shown above under the section tag, and closes upon argument exit.
Use `writeCSS()` or `writeCSS_raw()` to add css.

```python
p(text, **kwargs)
# p('This is some text that goes inside a paragraph. Atrributes can be added to attr', __class='someClass')
```

---

## Adding images {#add_img}

Images can be added with `image()` as context manager based approach, `.show()` which takes no arguments is used to display the image and `.css()` can be used to add CSS (no priorities, just adds to `img`), or one of the other three methods to add it to a class or an id.

```python
image(src:str, **kwargs)

with image('sierra.jpg', alt='Sierra', href='https://www.google.com', target='_blank') as i:
    i.show()
    i.css(opacity=1.1, width='50px')
```

---

## Working with tables (Pandas supported) {#tables}

Adding a table could never have been easier with a context manager approach on `Table()`, which takes no arguments and has objects `create_table()` and `get_table()`.
Sierra is compatible with Pandas, meaning just enter the path to the CSV file in `arg dataframe` in `getTable()`, and the table will display!

```python
get_table(self, dataframe:str, **kwargs)

with Table() as t:
    t.get_table("path/to/file.csv", id="some_id")
    st.css(font_family='Times New Roman')

    # CSS styling arguments for get_table() and start_table() are as usual.
    # No priorities. Use writeCSS() to add CSS to specific tag attributes.

.css(**kwargs)
```

As mentioned, you can also add a table with `create_table()`. Make sure the arg rows is a list of lists, even if there's only one row

```python
createTable(self, heads:list, rows:list, **kwargs)
# heads(list, compulsory): Adds table headers
# rows(list, compulsory) : Takes in a list of lists, each list representing a row
# kwargs(optional)       : Adds tag attributes to 

with Table() as t:
    c = ['foo', 'foo1', 'foo2']
    r1 = ['united states', 'croatia', 'austria']
    r2 = ['czech', 'denmark', 'canada']
    r3 = ['netherlands', 'scotland', 'england']
    r = [r1, r2, r3]

    t.create_table(heads=c, rows=r, id='table_id')

# Adding CSS        
writeCSS(font_family="Arial, Helvetica, sans-serif", border="1px solid #d1d5e8", padding='8px', width='30%')
```

Output:

| foo | foo1 | foo2 |
|-----|------|------|
| United States | Croatia | Austria |
| Czech | Denmark | Canada |
| Netherlands | Scotland | England |

---

## Bulleted lists (ordered and unordered) {#bullets_and_lists}

Ordered and/or unordered lists can be added with `bullets()` using `with`.
Just enter a list into the argument `points`, specify the type of the list (ordered or unordered), attributes if necessary, and you're good to go.
It doesn't have a `.css()` function - use one of the three methods to add CSS to it.

```python
bullets(ul:bool, points:list, attr=None)

a = ['pt1', 'pt2', 'pt3']
b = ['pt4', 'pt5']
c = ['pt6']

with bullets(ul=False, points=a, attr="start='1' type='i'"):
    with bullets(True, b, attr="type='square'"):
        pass
with bullets(ul=False, points=c, attr="start='4' type='I'"):
    pass
```

Output:

1. pt1
2. pt2
3. pt3
   - pt4
   - pt5

4. pt6

---

## Adding a description list {#des_lists}

Description lists can be added with `des_lists()`, which takes in argument `des_list` and of course, attributes can be added with `**kwargs`.
Just enter in a list of lists as the first argument, and it will show as a description list.
It is not a context manager-based approach.

```python
writeCSS('#d_list', {"margin-left":"40px"})

a = [[['foo'], ['foo1', 'foo2']], [['py' a, 'py1'], ['PEP', 'PEP8']]]
des_lists(a, "id='d_list'")
```

Output:

<dl id="d_list">
    <dt>foo</dt>
    <dd>- foo1</dd>
    <dd>- foo2</dd>
    <dt>py</dt>
    <dt>py1</dd>
    <dd>- PEP</dd>
    <dd>- PEP8</dd>
</dl>

Here,
`[['foo'], ['- foo1', '- foo2']]` is the first description list, and `[['py', 'py1'], ['- PEP', '- PEP8']]` is the
second. These two are separated by commas and are subsets of a list that contains them both. The attribute `id='d_list'` was
added to the description list, and CSS was added to the id with `writeCSS()`.

So get careful with the list arrangement!

---

## Other functions {#other_funcs}

Python functions/variables or anything can be added onto the web application using Sierra with much ease. However, keep in mind that every
function/CSS/tag, or anything that is to be added to the HTML must come only after `title()`.

Here's a list of other functions you can use with Sierra:

```python
writeWA(text)
# writeWA() can be used to add any text/inline onto the web application.
# This can be used to add text within certain tags.
```

Here's an example:

```python
with open_tag('pre'):
    writeWA(r"This appears inside the <pre class=><code> tag")

# Or say you want to add some Bootstrap to your page:
title()

@tag
def link(**kwargs):
    pass

@tag
def script(**kwargs):
    pass

addFont('Any font link')

#  Bootstrap link tags:
link(rel="stylesheet", href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css")
script(src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js")
script(src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js")
```

Regular HTML escape sequences and glyphs and regular tags like `<a>` can be used within the context manager or any functions that involve displaying on the web application, like

```python
p('HTML <a href="some_link">tag</a> within a paragraph <br> This sentence comes after a break')

autoPrettify()
# It handles tags beautifully, closes unclosed tags, and improves overall look of the HTML inline.
# Use this at the end of all development outside all context managers. 
# Using it inside or at a working stage will not work well. 
# However if you want to add inline to the HTML after </html>, use autoPrettify(), add inline, 
# and THEN use autoPrettify() AGAIN

# Go to this to see the beauty of autoPrettify()
```

---

## License

See [LICENSE](https://github.com/BrainStormYourWayIn/sierra/blob/main/LICENSE)

Pandas (pandas) -- table

Copyright (c) 2008-2011, AQR Capital Management, LLC, Lambda Foundry, Inc. and PyData Development Team
Copyright (c) 2011-2020, Open source contributors.
