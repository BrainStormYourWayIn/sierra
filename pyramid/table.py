class startTable():     
    def createTable(self, cols:list, rows:list):
        with open(f'''{index}.html''', 'a') as f:
            f.write(f'''\n<table>
<tr>''')
        for col in cols:
            with open(f'''{index}.html''', 'a') as f:
                f.write(f'''\n<th>{col}</th>''')
        with open(f'''{index}.html''', 'a') as f:
            f.write(f'''\n</tr>''')
        for row in rows:
            with open(f'''{index}.html''', 'a') as f:
                f.write(f'''\n<tr>''')
            for row_d in row:
                with open(f'''{index}.html''', 'a') as f:
                    f.write(f'''\n<td>{row_d}</td>''')
            with open(f'''{index}.html''', 'a') as f:
                f.write(f'''\n</tr>''')
        with open(f'''{index}.html''', 'a') as f:
            f.write(f'''\n</table>''')

        
    def getTable(self, dataframe:str):
        df = df = pd.read_csv(dataframe)
        cols = list(df.columns)
        rows = df.values.tolist()

        with open(f'''{index}.html''', 'a') as f:
            f.write(f'''\n<table>
<tr>''')
        for col in cols:
            with open(f'''{index}.html''', 'a') as f:
                f.write(f'''\n<th>{col}</th>''')
        with open(f'''{index}.html''', 'a') as f:
            f.write(f'''\n</tr>''')
        for row in rows:
            with open(f'''{index}.html''', 'a') as f:
                f.write(f'''\n<tr>''')
            for row_d in row:
                with open(f'''{index}.html''', 'a') as f:
                    f.write(f'''\n<td>{row_d}</td>''')
            with open(f'''{index}.html''', 'a') as f:
                f.write(f'''\n</tr>''')
        with open(f'''{index}.html''', 'a') as f:
            f.write(f'''\n</table>''')
