def value(colors):
    color_val = {
        "black": "0",
        "brown": "1",
        "red": "2",
        "orange": "3",
        "yellow": "4",
        "green": "5",
        "blue": "6",
        "violet": "7",
        "grey": "8",
        "white": "9"
    }
    output = ""
    for color in colors:
        if color in color_val: 
            output += color_val[color]

    return int(output[:2])
            
