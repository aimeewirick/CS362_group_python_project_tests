def conv_hex(num):
    """Takes a positive integer and returns big-endian hex string"""
    dec_to_hex = {
        0: '0', 1: '1', 2: '2', 3: '3',
        4: '4', 5: '5', 6: '6', 7: '7',
        8: '8', 9: '9', 10: 'A', 11: 'B',
        12: 'C', 13: 'D', 14: 'E', 15: 'F'
    }

    hex_str = ''
    while num > 0:
        remainder = num % 16
        hex_str = dec_to_hex[remainder] + hex_str
        num = num // 16

    if len(hex_str) % 2 != 0:
        hex_str = '0' + hex_str
    elif len(hex_str) == 0:
        hex_str = '00'

    return hex_str


def switch_endian(hex_str):
    """Takes a string representation of hex number
    and switches to little-endian"""
    new_hex = ''
    while hex_str:
        new_hex += hex_str[-2:]
        hex_str = hex_str[:-2]

    return new_hex


def insert_spaces(hex_str):
    """Inserts spaces to adhere to XX YY ZZ format"""
    new_hex = ''
    for i in range(len(hex_str)):
        new_hex += hex_str[i]
        if i % 2 != 0:
            new_hex += ' '

    return new_hex[:-1]


def insert_negative(hex_str):
    """Prepends the hex string with (-) sign"""
    return '-' + hex_str


def conv_endian(num, endian='big'):
    """Converts an integer input to a hexadecimal string"""
    valid_endian = {'big', 'little'}
    if endian not in valid_endian:
        return None

    hex_str = conv_hex(abs(num))
    if endian == 'little':
        hex_str = switch_endian(hex_str)
    hex_str = insert_spaces(hex_str)
    if num < 0:
        hex_str = insert_negative(hex_str)

    return hex_str


def my_datetime(num_sec):
    # Converts seconds provided to the current date since epoch
    # Constants
    sec_per_day = 86400
    sec_per_year = 365 * sec_per_day

    # Days per month
    days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Calculate number of years...
    years = num_sec // sec_per_year
    secs_left = num_sec - (sec_per_year * years)

    # Helper function to check number of leap years present
    def leap_year(year):
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

    # Calculate number of leap years
    leap_years = 0
    for year in range(1970, 1970 + years):
        if leap_year(year):
            leap_years += 1

    # Calculate seconds left after removing the years that have occurred w/ leap years:
    secs_left = secs_left - (sec_per_day * leap_years)

    # Adjust February if current year is a leap year
    if leap_year(1970 + years):
        days_per_month[1] = 29

    # Calculate days that have occurred in current year
    days = (secs_left // sec_per_day)

    # Calculate months
    month = 0
    while month < 12 and days >= days_per_month[month]:
        days -= days_per_month[month]
        month += 1

    # Date components and formatting
    day = days + 1
    month += 1
    year = 1970 + years

    date_string = "{:02d}-{:02d}-{:04d}".format(month, day, year)

    return date_string


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

    # Checks the string body for decimals and errors. Returns None if error OR True/False for a decimal in the string
    verification = check_body(string, hexa)
    if verification is None:
        return None
    else:
        decimal = verification
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
        decimal_numbers = string_to_number(new_string[place + 1:len(new_string)])
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
