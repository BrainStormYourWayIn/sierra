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
