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
    '''
    - Takes in an integer (+/-) value as num and
    converts it to a hexadecimal number.
    - The endian type is determined by the flag endian.
    - Returns the converted number as a string,
    or None in case of invalid endian type.
    - Format = "XX YY ZZ"
    '''
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
