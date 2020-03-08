color_code_list = ['black', 'brown', 'red', 'orange', 'yellow', 
              'green', 'blue', 'violet', 'grey', 'white']

def value(colors):
    return color_code_list.index(colors[0]) * 10 + color_code_list.index(colors[1])
