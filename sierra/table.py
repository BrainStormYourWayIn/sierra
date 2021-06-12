index = 'index'

class startTable():     
    def createTable(self, cols:list, rows:list):
        with open(f'''{index}.html''', 'a') as f:
            f.write('''
<table>
<tr>''')
        for col in cols:
            open(f'''{index}.html''', 'a').write("\n<th>{col}</th>")
        open(f'''{index}.html''', 'a').write("\n</tr>")
        for row in rows:
            open(f'''{index}.html''', 'a').write("\n<tr>")
            for row_d in row:
                open(f'''{index}.html''', 'a').write(f"\n<td>{row_d}</td>")
            open(f'''{index}.html''', 'a').write("\n</tr>")
        open(f'''{index}.html''', 'a').write(f'''\n</table>''')

        
    def getTable(self, dataframe:str):
        df = df = pd.read_csv(dataframe)
        cols = list(df.columns)
        rows = df.values.tolist()

        with open(f'''{index}.html''', 'a') as f:
            f.write('''
<table>
<tr>''')
        for col in cols:
            open(f'''{index}.html''', 'a').write(f'''\n<th>{col}</th>''')
        open(f'''{index}.html''', 'a').write(f'''\n</tr>''')
        for row in rows:
            open(f'''{index}.html''', 'a').write(f'''\n<tr>''')
            for row_d in row:
                open(f'''{index}.html''', 'a').write(f'''\n<td>{row_d}</td>''')
            open(f'''{index}.html''', 'a').write(f'''\n</tr>''')
        open(f'''{index}.html''', 'a').write(f'''\n</table>''')
