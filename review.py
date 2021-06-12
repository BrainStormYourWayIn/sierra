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
                
if __name__ == "__main__":
    #title('Test')
    #head('This is the header', '20px', 'Arial')
    #AutoPrettify()
    title('nothing')
    #addInitc()
    head('nothing more', font_size='90px', color='blue', text_align='center', background_color='orange')
    startBody(background_color='green', opacity=0.8)


    a = startTable()
    # c = ['england', 'best', 'six', 'euros']
    # r1 = ['kane', 'grealish', 'sancho', 'sterling']
    # r2 = ['foden', 'mount', 'bellingham', 'reece']
    # r3 = ['trippier', 'stones', 'walker', 'coady']
    # r = [r1, r2, r3]
    # a.createTable(cols=c, rows=r)
    a.getTable("E:\Dithu's Stuff\Me projects\pytohtm\england.csv")
    

    endBody()
    closeHTML()
    
    # AutoPrettify()
