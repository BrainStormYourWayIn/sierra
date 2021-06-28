#Copyright (c) 2008-2011, AQR Capital Management, LLC, Lambda Foundry, Inc. and PyData Development Team
#Copyright (c) 2011-2020, Open source contributors

import traceback
import pandas as pd

# <class 'startTable'>
class startTable():     
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, tb):
        if exc_type is not None:
            traceback.print_exception(exc_type, exc_value, tb)
        else:
            open('index.html', 'a+').write("\n</section>")

    def createTable(self, heads:list, rows:list, attr=None):
        """Creates a table out of lists.

        Args:
            heads(list, compulsory) : Adds table headers.
            rows(list, compulsory)  : Takes in a list of lists, each list representing a row.
            attr(str, optional)     : Adds attributes to <table>.
        """

        self.attr = attr

        if self.attr == None:
            open("index.html", 'a+').write("\n<table>")
        else:
            open("index.html", 'a+').write(f'\n<table {attr}>')

        open('index.html', 'a+').write("\n<tr>")
        for col in heads:
            open("index.html", 'a+').write(f"\n<th>{col}</th>")

        open("index.html", 'a+').write("\n</tr>")
        for row in rows:
            open("index.html", 'a+').write("\n<tr>")
            for row_d in row:
                open("index.html", 'a+').write(f"\n<td>{row_d}</td>")
            open("index.html", 'a+').write("\n</tr>")
        open("index.html", 'a+').write("\n</table>")

        
    def getTable(self, dataframe:str, attr=None):
        """Displays .csv file as a HTML table.

        Args:
            dataframe(str, compulsory) : Link to the .csv file to display
            attr(str, optional)        : Adds attributes to <table>
        """
        
        self.attr = attr
        df = pd.read_csv(dataframe)
        heads = list(df.columns)
        rows = df.values.tolist()

        if self.attr == None:
            open("index.html", 'a+').write('\n<table>')
        else:
            open("index.html", 'a+').write(f'\n<table {attr}>')

        for col in heads:
            open("index.html", 'a+').write(f'\n<th>{col}</th>')

        open("index.html", 'a+').write('\n</tr>')
        for row in rows:
            open("index.html", 'a+').write('\n<tr>')
            for row_d in row:
                open("index.html", 'a+').write(f'\n<td>{row_d}</td>')
            open("index.html", 'a+').write('\n</tr>')
        open("index.html", 'a+').write('\n</table>')

    def css(self, border=False, width=False, height=False, border_collapse=False, color='black', font_family='Arial', font_weight=False,\
            text_align='left', font_size=False, margin='0px', background_color='white'):
        """
        Args:
            border (str, optional)           : CSS border parameter. Defaults to False.
            width (str, optional)            : CSS border width parameter. Defaults to False.
            height (str, optional)           : CSS height parameter. Defaults to False.
            border_collapse (str, optional)  : CSS border-collapse parameter. Defaults to False.
            color (str, optional)            : CSS color parameter. Defaults to 'black'.
            font_family (str, optional)      : CSS font-family parameter. Defaults to "Arial".
            font_weight (str, optional)      : CSS font-weight parameter. Defaults to False.
            text_align (str, optional)       : CSS text-align parameter. Defaults to False.
            font_size (str, optional)        : CSS font_size parameter. Defaults to False.
            margin (str, optional)           : CSS margin parameter. Defaults to '0px'.
            background_color (str, optional) : CSS background-color parameter. Defaults to 'white'.
        """
        
        with open('style.css', 'a+') as s:
            s.write(f'''
table {{
    border: {border};
    width: {width};
    height: {height};
    border-collapse: {border_collapse};
    color: {color};
    font-family: {font_family};
    font-weight: {font_weight};
    text-align: {text_align};
    font-size: {font_size};
    margin: {margin};
    background-color: {background_color};
}}''')
