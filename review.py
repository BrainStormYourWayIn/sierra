class startTable():
    
    with open(f'''{index}.html''', 'a') as f:
        f.write(f'''\n<table>
<tr>''')
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
           
if __name__ == "__main__":
    a = startTable()
    c = ['england', 'best', 'six', 'euros']
    r1 = ['kane', 'grealish', 'sancho', 'sterling']
    r2 = ['foden', 'mount', 'bellingham', 'reece']
    r3 = ['trippier', 'stones', 'walker', 'coady']
    r = [r1, r2, r3]
    a.createTable(cols=c, rows=r)
