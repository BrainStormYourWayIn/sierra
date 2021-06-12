class startTable():
    def createTable(self, cols, *args):
        open('index.html', 'a').write('''
<table>
<tr>''')
        for col in cols:
            open('{index.html', 'a').write(f'''\n<th>{col}</th>''')
        open('index.html', 'a').write(f'''\n</tr>''')
        for row in args:
            open('index.html', 'a').write(f'''\n<tr>''')
            for row_d in row:
                open('index.html', 'a').write(f'''\n<td>{row_d}</td>''')
            open('index.html', 'a').write(f'''\n</tr>''')
        open('index.html', 'a').write(f'''\n</table>''')
