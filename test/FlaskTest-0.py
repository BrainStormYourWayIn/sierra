from flask import Flask, render_template
from sierra import *

app = Flask(__name__)

def the_template():                              # Creating a simple template
    title('bulleted_and_description_lists')
    head('this is a bulleted list')

def img_map():
    the_template()
    with div(None, attr="id='div_id'"):             # Creating a <div> with id='div_id'
    
        with image(src='workplace.jpg', attr="usemap='#workmap'") as i:  
           # Loading an image and giving it attr usemap
        i.show()                # Displaying the image
        i.css(opacity=1.7)      # Adding CSS to it

        with open_tag('map', attr='name="workmap"'):  
        
          # Creating an image map which performs different actions
          # based on where it is clicked, which is determined by
          # specific shapes and coordinates on the image
        
            shape = ['rect', 'rect', 'circle']
            coords = ["34,44,270,350", "290,172,333,250", "337,300,44"]
            alt = ['Computer', 'Phone', 'Coffee']
            href = ['computer.htm', 'phone.htm', 'coffee.htm']

              # Using lists and for loop to make the shape and coordinate mapping faster (see doc)

            for shape, coord, alt, href in zip(shapes, coords, alt, href):       
                with open_tag('area', attr=f'shape="{shape}" coord="{coord}" alt="{alt}" href="{href}"'):
                    pass
                    
    autoPrettify()       
    write_to_template('index1.html')
    

def bulleted_and_des_list():
    the_template()
    
    with div(div_class='description_list'):       # Creating div
    
        a = [[['coffee', 'tea'], ['black coffee', 'black tea']], [['new_coffee'], ['foo', 'tea', 'green_tea']]]
                    # Displaying a description list
        des_lists(a)        
        
        with section(sec_class='unorder_list') as s:    # Creating section inside div
            ul_list = ['This', 'is', 'an', 'ul']        # Creating an unordered list
            with bullets(ul=True, points=ul_list):      # Displaying it
                pass        
        
    autoPrettify()
    write_to_template('index2.html')

@app.route("/img_map")
def show_img_map():
    img_map()
    return render_template('index1.html')

@app.route("/bulleted_and_des_list")
def show_bulleted_and_des_list()():
    bulleted_and_des_list()()
    return render_template('index2.html')

if __name__ == '__main__':
    app.run()
