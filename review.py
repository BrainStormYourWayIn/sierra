class startTable():
    def __init__(self, index="index"):
        self.index = index

    def createTable(self, cols, *args):
        open(f'''{self.index}.html''', 'a').write(f'''\n<table>
<tr>''')
        for col in cols:
            open(f'''{self.index}.html''', 'a').write(f'''\n<th>{col}</th>''')
        open(f'''{self.index}.html''', 'a').write(f'''\n</tr>''')
        for row in args:
            open(f'''{self.index}.html''', 'a').write(f'''\n<tr>''')
            for row_d in row:
                open(f'''{self.index}.html''', 'a').write(f'''\n<td>{row_d}</td>''')
            open(f'''{self.index}.html''', 'a').write(f'''\n</tr>''')
        open(f'''{self.index}.html''', 'a').write(f'''\n</table>''')
           
if __name__ == "__main__":
    a = startTable()
    c = ['england', 'best', 'six', 'euros']
    r1 = ['kane', 'grealish', 'sancho', 'sterling']
    r2 = ['foden', 'mount', 'bellingham', 'reece']
    r3 = ['trippier', 'stones', 'walker', 'coady']
    a.createTable(c, r1, r2, r3)
