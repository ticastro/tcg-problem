from ..constants import equivalences_dict
from .helpers import integerify, listify

def check_quantities(roman): #chequear que si son 4, se tenga que estan separados 3 y 1
    if roman.count('I') <= 4:
        if not check_four(roman, 'I'):
            return False
    elif roman.count('X') <= 4:
        if not check_four(roman, 'X'):
            return False
    elif roman.count('C') <= 4:
        if not check_four(roman, 'C'):
            return False
    elif roman.count('M') <= 4:
        if not check_four(roman, 'M'):
            return False
    elif roman.count('D') > 1:
        return False
    elif roman.count('L') > 1:
        return False
    elif roman.count('V') > 1:
        return False
    return True

def check_four(roman, char):
    count = roman.count(char)
    if count < 4:
        return True
    elif count == 4: # cambiar esta parte.
        first_appear = roman.index(char)
        list_appearance = [first_appear, first_appear+1, first_appear+2, first_appear+4]
        for place in list_appearance:
            try:
                if roman[place] != char:
                    return False
            except IndexError:
                return False
        return True
    else:
        return False

def roman_list_integerify(roman_list):
    for position in range(len(roman_list)):
        int_value = integerify(roman_list[position])
        if int_value:
            roman_list[position] = int_value
        else:
            return False 
    return roman_list

def list_value(int_list):
    if not isinstance(int_list, list):
        return False
    total = 0
    current = int_list[0]
    repetions = 0
    for position in range(len(int_list)):
        number = int_list[position]
        if number == current:
            repetions += 1
            if position == len(int_list) - 1:
                total += current*repetions
        elif number > current:
            substraction = repetions*current
            if not check_subs(number, substraction): #esta funcion tiene que chequear que se esten restando los numeros adecuados
                return False
            total += number - substraction
            repetions = 0
            if position != len(int_list) - 1:
                current = int_list[position + 1]
        elif number < current:
            total += current * repetions
            repetions = 1
            current = number
            if position == len(int_list) - 1:
                total += current*repetions

    return total

def roman_to_int(roman_number):
    if not check_quantities(roman_number):
        return False
    roman_list = listify(roman_number)
    int_list = roman_list_integerify(roman_list)
    return list_value(int_list)

def check_subs(number, substraction):
    if substraction not in (1,10,100):
        return False
    if substraction == 1:
        if number not in (5, 10):
            return False
    elif substraction == 10:
        if number not in (50, 100):
            return False
    elif substraction == 100:
        if number not in (500, 1000):
            return False
    return True

