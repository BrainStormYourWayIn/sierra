#Copyright (c) 2008-2011, AQR Capital Management, LLC, Lambda Foundry, Inc. and PyData Development Team
#Copyright (c) 2011-2020, Open source contributors

import traceback
import pandas as pd

class Table():
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, tb):
        if exc_type is not None:
            traceback.print_exception(exc_type, exc_value, tb)
        else:
            # open("index.html", 'a+').write("\n</section>")
            pass

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

        open("index.html", 'a+').write("\n<tr>")
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
            dataframe(str, compulsory) : Link to the .csv file to display.
            attr(str, optional)        : Adds attributes to <table>.
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

    def css(self, **kwargs):
        """Writes the given parameters to the CSS file.

        Args:
            **kwargs (optional) : CSS parameters.
        """

        with open("style.css", 'a+') as s:
            for key, value in kwargs:
                s.write(f"\n\t{key.replace('_', '-')}: {value};")
            s.write("\n}")
 
