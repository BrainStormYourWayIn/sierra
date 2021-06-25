#Copyright (c) 2008-2011, AQR Capital Management, LLC, Lambda Foundry, Inc. and PyData Development Team

#Copyright (c) 2011-2020, Open source contributors

import pandas as pd

class startTable():     
    def createTable(self, heads:list, rows:list, *args):
        """Creates a table out of lists.
        
        Args:
            heads (list, compulsory) : Adds table headers.
            rows (list, compulsory)  : Takes in a list of lists, each list representing a row.
            *args                    : To use global and event attributes, if required. Enter all of them within quotes, not comma-separated.
        """
        
        open("index.html", 'a').write('''\n<table''')
        for arg in args:
            b = ' ' + arg
            open('index.html', 'a').write(f"{b}")
        open('index.html', 'a').write(">")
        open('index.html', 'a').write("\n<tr>")
        for col in heads:
            open("index.html", 'a').write(f"\n<th>{col}</th>")
        open("index.html", 'a').write("\n</tr>")
        for row in rows:
            open("index.html", 'a').write("\n<tr>")
            for row_d in row:
                open("index.html", 'a').write(f"\n<td>{row_d}</td>")
            open("index.html", 'a').write("\n</tr>")
        open("index.html", 'a').write(f"\n</table>")

        
    def getTable(self, dataframe:str):
        """Displays .csv file as a HTML table.
        
        Args:
            dataframe(str, compulsory): Link to the .csv file to display.
        """
        
        df = pd.read_csv(dataframe)
        heads = list(df.columns)
        rows = df.values.tolist()

        with open("index.html", 'a') as f:
            f.write('''
<table>
<tr>''')
        for col in heads:
            open("index.html", 'a').write(f'''\n<th>{col}</th>''')
        open("index.html", 'a').write(f'''\n</tr>''')
        for row in rows:
            open("index.html", 'a').write(f'''\n<tr>''')
            for row_d in row:
                open("index.html", 'a').write(f'''\n<td>{row_d}</td>''')
            open("index.html", 'a').write(f'''\n</tr>''')
        open("index.html", 'a').write(f'''\n</table>''')

    def css(self, border=False, width=False, height=False, border_collapse=False, color='black', font_family="Arial", font_weight=False, text_align=False, font_size=False, margin=False, background_color='white'):
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
            margin (str, optional)           : CSS margin parameter. Defaults to False.
            background_color (str, optional) : CSS background-color parameter. Defaults to 'white'.
        """
        
        with open('style.css', 'a') as s:
            if self.id == 'False': s.write(f'''\ntable {{''')
            else: s.write(f'''\n#{self.id} {{''')
             
            s.write(f'''    border: {border};
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
