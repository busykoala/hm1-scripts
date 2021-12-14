def get_value(mantissas_str, base, exponent):
    """ convert numbers of different bases to decimal
    """
    mantissas = [int(x) for x in mantissas_str]
    return sum([
        mantissa * base ** (exponent - index)
        for index, mantissa
        in enumerate(mantissas, start=1)
    ])


# example: 0.71537*8^2 => 57.685546875
mantissas = '71537'
base = 8
exponent = 2
print(get_value(mantissas, base, exponent))


def convert_hex_string(hex):
    """ hex string to list of decimal number values.
    """
    hex_map = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
               '9': 9, 'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
    hex_lower = hex.lower()
    return [hex_map[x] for x in hex_lower]


# example: AB3C9F => [10, 11, 3, 12, 9, 15]
print(convert_hex_string('AB3C9F'))


def ieee745(ieee_number):
    """ ieee 745 number to decimal number conversion.
    """
    sign = int(ieee_number[0])
    exp = int(ieee_number[1:9], 2)
    mant = int("1" + ieee_number[9:], 2)
    return (-1) ** sign * mant / (1 << (len(ieee_number) - 9 - (exp - 127)))


# example: 1 10000001 10100000000000000000000 => -6.5
ieee_number = '11000000110100000000000000000000'
print(ieee745(ieee_number))


def min_max_maschine_num(base, e_min, e_max, mantissa_positions):
    """ smallest/biggest maschine number.
    """
    x_max = (1 - base ** (-mantissa_positions)) * base ** e_max
    x_min = base ** (e_min - 1)
    return x_min, x_max


# example: [n = 4, 0 <= e <= 3] => (0.5, 7.5)
base = 2
e_min = 0
e_max = 3
mantissa_positions = 4
print(min_max_maschine_num(base, e_min, e_max, mantissa_positions))
