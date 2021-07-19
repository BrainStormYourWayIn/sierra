#Copyright (c) 2008-2011, AQR Capital Management, LLC, Lambda Foundry, Inc. and PyData Development Team
#Copyright (c) 2011-2020, Open source contributors

import traceback
import pandas as pd

def join_attr(tup):
    string = ''
    for item in tup:
        string = string + item
        string = string.replace('  ', ' ')
    return string

class Table:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, tb):
        if exc_type is not None:
            traceback.print_exception(exc_type, exc_value, tb)
        else:
            # open("index.html", 'a+').write("\n</section>")
            pass

    def create_table(self, heads:list, rows:list, **kwargs):
        """Creates a table out of lists.
        \nThe first row (which is the header) goes into `heads`
        \nThe other rows are passed in to `rows` as a list of lists

        \nUse `kwargs` to add tag attributes. Python-conflicting attribute names like `class` and `for` to be prefixed by a double underscore, that is, to be entered in as `__class` and `__for`
        \nUse a single underscore in place of a hyphen in the `key` of `kwargs`, which is the tag atrribute name. 
        \neg. Tag attribute `initial-scale` must be `initial_scale` as the `key`

        Args:
            heads (list, compulsory) : Adds table headers.
            row (list, compulsory)   : Takes in a list of lists, each list representing a row.
            kwargs (optional)        : Adds tag attributes to <table>
        """

        self.kwargs = kwargs

        if not self.kwargs:
            open("index.html", 'a+').write("\n<table>")

        else:
            all_attr = "<table ", *(f'  {key.replace("__", "").replace("_", "-")}="{value}"' for key, value in self.kwargs.items()), ">"
            open('index.html', 'a+').write(f"\n{join_attr(all_attr)}")


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


    def get_table(self, dataframe, **kwargs):
        """Displays .csv file as a HTML table.

        \nUse `kwargs` to add tag attributes. Python-conflicting attribute names like `class` and `for` to be prefixed by a double underscore, that is, to be entered in as `__class` and `__for`
        \nUse a single underscore in place of a hyphen in the `key` of `kwargs`, which is the tag atrribute name. 
        \neg. Tag attribute `initial-scale` must be `initial_scale` as the `key`

        Args:
            dataframe(str, compulsory) : Link to the .csv file to display.
            kwargs (optional)          : Adds tag attributes to <table>
        """
        self.kwargs = kwargs

        df = pd.read_csv(dataframe)
        heads = list(df.columns)
        rows = df.values.tolist()

        if not self.kwargs:
            open("index.html", 'a+').write('\n<table>')
        else:
            all_attr = "<table ", *(f'  {key.replace("__", "").replace("_", "-")}="{value}"' for key, value in self.kwargs.items()), ">"
            open('index.html', 'a+').write(f"\n{join_attr(all_attr)}")

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

        \nUse underscores instead of hyphens when adding styling attributes.
        \nFor example, the attribute `font-size` must be entered in as `font_size`

        \nNote that CSS is added directly to  `<table>` and not to any `__class` or `id given`, unlike in the case of `<div>` and `<section>`
        \nUse `writeCSS()` instead to add CSS to a mentioned `__class` or `id`

        Args:
            **kwargs (optional) : CSS parameters.
        """

        with open("style.css", 'a+') as s:
            s.write("\n\ntable {{")

            for key, value in kwargs:
                s.write(f"\n\t{key.replace('_', '-')}: {value};")

            s.write("\n}")
