# Example how to add info/hints for functions
# When using function in code, press ctrl + space to see it. 
# How to define it? Immediately under function definition and need to be between """"  """"

def show_name_title(name):
    """Simple function that change string with random sized letters to tittled one"""
    print(name.title())

show_name_title(input("Give me your unformatted name: "))