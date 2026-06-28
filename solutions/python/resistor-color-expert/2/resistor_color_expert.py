def resistor_label(colors):
    """
    Function provide the resistance value for 1 band resistor, 4 band resistor and 5 band resistor.

    input: 
        colors: list: contains the list of colors

    ouput: str: provide the total resistance value along with the maximum tolerance.
    """

    # Convert color to value
    color_value_mapping = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9,
    }

    # Convert color to tolerance value
    tolerance_band = {
        "grey": "0.05%",
        "violet": "0.1%",
        "blue": "0.25%",
        "green": "0.5%",
        "brown": "1%",
        "red": "2%",
        "gold": "5%",
        "silver": "10%",
    }

    # For 1 Band resistors
    if len(colors) == 1: 
        return "0 ohms"

    # get the significant colors
    significant_colors = colors[:3] if len(colors) == 5 else colors[:2]

    # get the digits
    digits = [color_value_mapping[color] for color in significant_colors]

    # form the number
    number = 0 
    for digit in digits:
        number = number * 10 + digit

    # get the multiplier and multiplier is always the second last band
    multiplier_color = colors[-2]
    multiplier = 10 ** color_value_mapping[multiplier_color]

    # get the tolerance and tolerace is always the last band
    tolerance_color = colors[-1]
    tolerance = tolerance_band[tolerance_color]

    # get the resistance number
    resistance_num = number * multiplier

    # helper function
    def format_resistance(resistance_number):
        if resistance_number >= 1000000:
            suffix = ' megaohms'
            resistance_number /= 1000000

        elif 1000 <= resistance_number < 1000000:
            suffix = ' kiloohms'
            resistance_number /= 1000

        else:
            suffix = ' ohms'

        return f"{resistance_number:g}{suffix}" # here 'g' removes any trailing zeros

    resistance_value = format_resistance(resistance_num)

    # output: formatted string
    resistance_value += " \u00B1" + tolerance 
    return resistance_value