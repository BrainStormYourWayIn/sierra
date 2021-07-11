import os

def write_to_template(name_of_file):
    with open("index.html", 'r') as f:
        with open(f'''templates/{name_of_file}''', 'w') as t:
            t.write(str(f.read()))
            
    try:
        with open("style.css", 'r') as s:
            with open("static/style.css", 'w') as style:
                style.write(str(s.read()))
   
    except FileNotFoundError:
        # print('FileNotFoundError')
        pass                

    os.remove("index.html")
    os.remove('style.css')
