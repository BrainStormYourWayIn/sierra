# Working with Python Loops, Functions, Variables and Conditions

Displaying Python outputs on your web applications are actually pretty simple with Sierra.
To work with this, you can use `writeWA()` or `p()`, which has been covered on the main page of the documentation.
You can print variables, output functions, use loops, conditions or anything.

Say you've loaded in a `.csv` file with pandas and write some quick code for displaying each row as a list:

```python
import pandas as pd
from sierra import *
df = pd.read_csv(r'path/to/the/file.csv')

#  df
#      this      is        a          csv
#  0   word      word1     word2      word3
#  1   test1     test2     test3      test4
#  2   foo1      foo2      foo3       foo4

for i in range(0, 3):
    for g in range(1, 4):
        if i + 1 == g:
            a = f"r{g} = {list(df.iloc[i])}{br}"
            # var 'br' stands for <br> See 'Other Functions'
            writeWA(a)

            # or if you want it on a paragraph
            p(a)

            # Output on the web application:
            # r1 = ['word', 'word1', 'word2', 'word3']
            # r2 = ['test1', 'test2', 'test3', 'test4']
            # r3 = ['foo1', 'foo2', 'foo3', 'foo4']
```

## Image Maps

Say you want to create an image map, with which you can perform different actions by clicking on shape and subsequently coordinate-secified parts of the shape on the image.
See [image map](https://www.w3schools.com/html/html_images_imagemap.asp).
You can use f-strings and for loop to make it easy:

```python
with image(src='workplace.jpg', attr="usemap='#workmap'") as i:
    i.show()

with open_tag('map', attr='name="workmap"'):
    shape = ['rect', 'rect', 'circle']
    coords = ["34,44,270,350", "290,172,333,250", "337,300,44"]
    alt = ['Computer', 'Phone', 'Coffee']
    href = ['computer.htm', 'phone.htm', 'coffee.htm']

    for shape, coord, alt, href in zip(shapes, coords, alt, href):
        with open_tag('area', attr=f'shape="{shape}" coord="{coord}" alt="{alt}" href="{href}"'):
            pass

autoPrettify()
```

Here, you first display the image and give it an attribute `usemap`, then you enter in four lists that contain the attributes of the three areas to be covered, open the `<map>` tag and map it to the attribute `usemap` given to the image.
Then you do a simple for loop and unpack each item in the lists with `zip()`, open the `<area>` tag and simply use f-strings to enter in four different attributes to three different `<area>` tags which all come under `<map>`!
So instead of manually entering in every single tag and attribute, you've used Python's list and for loop to get the job done.

## Python Functions

With Sierra, using and displaying outputs of Python functions on your web application is made easy as cake
Here's an example of scraping a webpage with requests, given it's URL, and displaying all text within the `<p>` tag:

```python
from sierra import *
import re
import urllib3

def ExtractpText(url):
    http = urllib3.PoolManager()
    req = http.request('GET', url)
    respData = RemoveThrashText(str(req.data))
    regex = '<p>(.*?)</p>'
    paragraphs = re.findall(regex, respData)
    return paragraph

title('Extracting text from the <p> tag given a URL')
openBody()
writeWA("\n"ExtractpText("http://example.com/"))
autoPrettify()


# OR you could enclose it in a div/p/section/anything and style it, if you like
title('Extracting text from the <p> tag given a URL')

# Font
addFont("https://fonts.googleapis.com/css2?family=Roboto&display=swap")
openBody(background_color="#161a21")
p(writeWA("\n"ExtractpText("http://example.com/")), attr="class='p_class'")

# CSS
with cTags('.p_class') as p_class:
    p_class.css(color="#dfe3eb", font_family="'Roboto', sans-serif")

autoPrettify()
```

Simple as that! You just use `writeWA()` for getting the job done!
Or you could just do `p(ExtractpText("http://example.com/"))`, both work.

Similarly, variables and conditional statements can be added too.

```python
some_variable = 'doggo'
p(doggo)

# or use f-strings
p(f'This is my {some_variable}!')

# or use writeWA (even with f-strings, if the use case suits you)
if some_variable == 'dog':
    writeWA(f'Grrr! This is NOT my {some_variable}')
else:
    writeWA(f'Grrr! This is MY {some_variable}! I'd like you to come just a little closer.')
```
