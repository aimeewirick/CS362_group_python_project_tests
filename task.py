
def conv_num(num_str):
    """Converts a number string to an integer or float including hexadecimal or base10 numbers"""
    number = None
    hexa = False
    negative = False
    decimal = False

    # Checks correct string type and basic content
    if type(num_str) != str:
        return None
    if num_str == "":
        return None

    # Checks for negative or hexadecimal prefixes
    hexa = check_prefix(num_str)[0]
    negative = check_prefix(num_str)[1]

    # Cuts out the prefix so we don't need to check that part redundantly
    string = prefix_remover(num_str, hexa, negative)

    # Checks the string body for correct content returns 'None' if incorrect content found
    if check_body(string, hexa) is None:
        return None
    else:
        # Checks the string body for decimal returns True if decimal is found False if no decimal
        decimal = check_body(string, hexa)
    if hexa is True:
        # Converts a hexadecimal string
        number = hex_converter(string, negative)
    else:
        # Converts a base 10 string
        number = base10_converter(string, negative, decimal)
    return number


def check_prefix(num_str):
    """Helper function for conv_num: checks the prefix of a number returns True/False for hexa and negative prefix"""
    hexa = False
    negative = False
    prefix_options = ["0X", "0x"]
    # Checks for negative sign
    if num_str[0] == "-":
        negative = True
    # Checks for correct hexadecimal prefix
    for option in prefix_options:
        if option in num_str:
            if negative is True:
                if num_str.index(option) == 1:
                    hexa = True
            if num_str.index(option) == 0:
                hexa = True
    return hexa, negative


def prefix_remover(num_str, hexa, negative):
    """Helper function for conv_num: Removes hex or negative prefix from a string"""
    string = []
    if hexa is True:
        string = num_str[2:len(num_str)]
        if negative is True:
            string = num_str[3:len(num_str)]
    else:
        if negative is True:
            string = num_str[1:len(num_str)]
        else:
            string = num_str[0:len(num_str)]
    return string


def check_body(string, hexa):
    """Helper function for conv_num: Checks string body. Returns decimal True/False  or None if incorrect content"""
    decimal = False
    allowed_alphabet = "ABCDEFabcdef"
    allowed_prefix = "xX"
    allowed_numbers = "1234567890"
    allowed_sign = "-"
    allowed_decimal = "."
    all_allowed = allowed_alphabet + allowed_sign + allowed_prefix + allowed_decimal + allowed_numbers
    for item in string:
        if item not in all_allowed:
            return None
        if item in allowed_prefix:
            return None
        if item in allowed_alphabet:
            if hexa is False:
                return None
        if item in allowed_sign:
            return None
        if item in allowed_decimal:
            if hexa is True:
                return None
            if decimal is True:
                return None
            decimal = True
    return decimal


def hex_converter(string, negative):
    """Helper function for conv_num: Converts a hexadecimal string to an integer"""
    number = 0
    exponent = len(string) - 1
    converted_string = string_to_number(string)
    for num in converted_string:
        total = num * (16 ** exponent)
        number = number + total
        exponent -= 1
    if negative is True:
        number = number * -1
    return number


def string_to_number(string):
    """Helper function for conv_num: Converts a number string (hexadecimal or decimal) to a list of numbers"""
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    number_string = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    upper_letter_string = ["A", "B", "C", "D", "E", "F"]
    lower_letter_string = ["a", "b", "c", "d", "e", "f"]
    hex_number_list = [10, 11, 12, 13, 14, 15]
    converted_string = []
    for num in string:
        # uses indexing to lookup number equivalents by their string counterpart
        if num in number_string:
            converted_string.append(number_list[number_string.index(num)])
        if num in upper_letter_string:
            converted_string.append(hex_number_list[upper_letter_string.index(num)])
        if num in lower_letter_string:
            converted_string.append(hex_number_list[lower_letter_string.index(num)])
    return converted_string


def base10_converter(string, negative, decimal):
    """Helper function for conv_num: Converts a base10 number string (whole or decimal) to an integer or float"""
    whole_numbers = []
    decimal_numbers = []
    new_string = string
    place = len(new_string)
    # Splits up the whole numbers and decimal numbers to separate strings for conversion into lists
    if decimal is True:
        place = new_string.index(".")
        whole_numbers = string_to_number(new_string[0:place])
        decimal_numbers = string_to_number(new_string[place+1:len(new_string)])
    if decimal is False:
        whole_numbers = string_to_number(new_string)
    converted_number = 0
    divisor = 10
    if place == len(new_string) - 1:
        converted_number = converted_number + .0
    if whole_numbers:
        # Converts numbers in a whole number list to a whole number
        for num in whole_numbers:
            total = num * 10 ** (place - 1)
            converted_number = converted_number + total
            place -= 1
    if decimal_numbers:
        # Converts numbers in decimal list to a decimal number
        for num in decimal_numbers:
            total = num / divisor
            divisor = divisor * 10
            converted_number = converted_number + total
    if negative is True:
        converted_number = converted_number * -1
    if len(decimal_numbers) > 4:
        converted_number = round(converted_number, len(decimal_numbers))
    else:
        converted_number = round(converted_number, 4)
    return converted_number
