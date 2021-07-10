# These are release prototypes, a good view of what you can expect in the coming release(s)

# Better CSS handling
# Right now, there's automatic support for certain styling arguments. This may be disadvantageous since future CSS updates may deprectate certain 
# styling attributes/modify them.

# Current: 

def head(Head, color='black', font_size='20px', background_color='yellowgreen' etc.)
# This outputs ALL the arguments into the CSS file whether or not they've been used, which is not efficient

# Possible:
def head(Head, **kwargs):
  for key, value in kwargs.items():
        a = f"{key}: {value};"
        a = a.replace('_', '-')
        print(a)

        # The user can use underscores for hyphens in **kwargs
        
# So
head('test', font_size='30px', color='blue', background_color='yellowgreen')
# Outputs:
font-size: 30px;
color: blue;
background-color: yellowgreen;
