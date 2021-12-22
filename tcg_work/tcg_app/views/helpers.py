from ..constants import equivalences_dict

def listify(roman):
    roman_list = [number_sign for number_sign in roman]
    return roman_list


def integerify(char):
    try:
        return equivalences_dict[char]
    except (ValueError, KeyError):
        return False

def make_str(start, line):
    roman_string = ''
    for i in range(start, len(line)):
        if not line[i]:
            return False
        roman_string += line[i]
    return roman_string

