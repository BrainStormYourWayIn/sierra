# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 09:32:38 2021

"""
#from flask import Flask

#nameofhtm = input('Enter the name of your HTML file')

# icon argument must be a .ico file

def title(Title, icon):
    with open('nameofhtm.html', 'w') as f:
        
        f.write(f'''<html>
<title>{Title}</title>
<link rel="shortcut icon" href={icon}>\n''')

def head(Head, type, size):
    with open('nameofhtm.html', 'a') as f:
        if size:
            print('CSS')
        elif type:
            f.write(f'''<{type}>{Head}</{type}>''')
        elif type and size:
            print('Invalid')
        
title('nothing', None)
head('nothing more', 'h3', None)


