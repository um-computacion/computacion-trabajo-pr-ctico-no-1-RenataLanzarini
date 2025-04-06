dic = [
    (1000 , 'M'),
    (900 , 'CM'),
    (500 , 'D'),
    (400 , 'CD'),
    (100 , 'C'),
    (90 , 'XC'),
    (50 , 'L'),
    (40 , 'XL'),
    (10 , 'X' ),
    (9 , 'IX' ),
    (5, 'V'),
    (4, 'IV'),
    (1, 'I'),
]


def decimal_to_roman(number):
    if  3999 < number or 1 > number:
        return "Error, el numero debe ser entre 1 y 3999"
    result = ''
    for value,simbol in dic:
        while(number >= value):
            result += simbol
            number -= value
    return result





        