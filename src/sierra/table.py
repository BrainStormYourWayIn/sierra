# Copyright (c) 2008-2011, AQR Capital Management, LLC, Lambda Foundry, Inc. and PyData Development Team
# Copyright (c) 2011-2020, Open source contributors

import pandas as pd
import traceback

class startTable():     

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, tb):
        if exc_type is not None:
            traceback.print_exception(exc_type, exc_value, tb)
        else:
            pass

    def createTable(self, heads:list, rows:list, attr=None):

        """
        Creates a table out of lists
        
        Args:
        heads(list, compulsory): Adds table headers
        rows(list, compulsory) : Takes in a list of lists, each list representing a row
        attr(str, optional)    : Adds attributes to <table>

        """
        self.attr = attr

        if self.attr == None:
            with open("index.html", 'a') as f:
                f.write("\n<table>")
        else:
            with open("index.html", 'a') as f:
                f.write(f"\n<table {attr}>")

        open('index.html', 'a').write(f"\n<tr>")
        for col in heads:
            open("index.html", 'a').write(f"\n<th>{col}</th>")
        open("index.html", 'a').write("\n</tr>")
        for row in rows:
            open("index.html", 'a').write("\n<tr>")
            for row_d in row:
                open("index.html", 'a').write(f"\n<td>{row_d}</td>")
            open("index.html", 'a').write("\n</tr>")
        open("index.html", 'a').write("\n</table>")

        
    def getTable(self, dataframe:str, attr=None):

        """
        Displays .csv file as a HTML table
        Args:
        dataframe(str, compulsory): Link to the .csv file to display
        attr(str, optional)       : Adds attributes to <table>

        """
        self.attr = attr

        df = df = pd.read_csv(dataframe)
        heads = list(df.columns)
        rows = df.values.tolist()

        if self.attr == None:
            with open("index.html", 'a') as f:
                f.write("\n<table>")
        else:
            with open("index.html", 'a') as f:
                f.write(f"\n<table {attr}>")

        for col in heads:
            open("index.html", 'a').write(f"\n<th>{col}</th>")
        open("index.html", 'a').write("\n</tr>")
        for row in rows:
            open("index.html", 'a').write("\n<tr>")
            for row_d in row:
                open("index.html", 'a').write(f"\n<td>{row_d}</td>")
            open("index.html", 'a').write("\n</tr>")
        open("index.html", 'a').write("\n</table>")

    def css(self, **kwargs):
        """
        Args:

            **kwargs (optional)              : CSS styling arguments

        """

        for key, value in kwargs.items():
            add_to_css = f"{key}: {value};"
            add_to_css = add_to_css.replace('_', '-')
            # print(add_to_css)

        with open('style.css', 'a+') as s:
            s.write("\n\ntable {")
            for key, value in kwargs.items():
                add_to_css = f"{key}: {value};"
                add_to_css = add_to_css.replace('_', '-')

                s.write(f'''
    {add_to_css}''')

            s.write("\n}")
