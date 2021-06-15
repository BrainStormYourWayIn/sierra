import pandas as pd

class startTable():     
    def createTable(self, cols:list, rows:list):
        with open("index.html", 'a') as f:
            f.write('''
<table>
<tr>''')
        for col in cols:
            open("index.html", 'a').write("\n<th>{col}</th>")
        open("index.html", 'a').write("\n</tr>")
        for row in rows:
            open("index.html", 'a').write("\n<tr>")
            for row_d in row:
                open("index.html", 'a').write(f"\n<td>{row_d}</td>")
            open("index.html", 'a').write("\n</tr>")
        open("index.html", 'a').write(f'''\n</table>''')

        
    def getTable(self, dataframe:str):
        df = df = pd.read_csv(dataframe)
        cols = list(df.columns)
        rows = df.values.tolist()

        with open("index.html", 'a') as f:
            f.write('''
<table>
<tr>''')
        for col in cols:
            open("index.html", 'a').write(f'''\n<th>{col}</th>''')
        open("index.html", 'a').write(f'''\n</tr>''')
        for row in rows:
            open("index.html", 'a').write(f'''\n<tr>''')
            for row_d in row:
                open("index.html", 'a').write(f'''\n<td>{row_d}</td>''')
            open("index.html", 'a').write(f'''\n</tr>''')
        open("index.html", 'a').write(f'''\n</table>''')

    def css(self, border=False, width=False, height=False, border_collapse=False, color='black', font_family="Arial", font_weight=False, text_align=False, font_size=False, margin=False, background_color='white'):
        with open('style.css', 'a') as s:
            if self.id == 'False':
                s.write(f'''\ntable {{''')
            else:
                s.write(f'''\n#{str(self.id)} {{''')
        s.write(f'''color: {color};
font-family: {font_family};
font-weight: {font_weight};
text-align: {text_align};
font-size: {font_size};
background-color: {background_color};
border: {border};
height: {height};
width: {width};
margin: {margin};
}}''')
