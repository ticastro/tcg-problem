from .roman_functions import roman_to_int
from .helpers import make_str

def calificate_lines(inp_str):
    str_definitions = []
    iron_definitions = []
    iron_questions = []
    number_questions = []
    non_recognized = []
    response_number = 0
    list_str = inp_str.split('\n')
    for line in list_str:
        list_line = line.split(" ")
        list_line[-1] = list_line[-1].replace("\r", "")
        if list_line[-1] == 'Credits':
            iron_definitions.append((list_line,response_number))
            response_number += 1
        elif list_line[1] == 'is':
            str_definitions.append((list_line, response_number))
            response_number += 1
        elif list_line[-1] == '?':
            if list_line[1] == 'much':
                number_questions.append((list_line, response_number))
                response_number += 1
            else:
                iron_questions.append((list_line, response_number))
                response_number += 1
        else:
            list_line.append(False)
            non_recognized.append((list_line, response_number))
            response_number += 1
    dict_file = {
        'str_definitions': str_definitions,
        'iron_definitions': iron_definitions,
        'iron_questions': iron_questions,
        'number_questions': number_questions,
        'non_recognized': non_recognized
    }
    return dict_file

def str_values_dict(dict_file):
    str_values = {}
    for defi in dict_file['str_definitions']:
        value = defi[0][2]
        str_values[defi[0][0]] = defi[0][2]
        if len(value) > 1:
            str_values[defi[0][0]] = False
    return str_values 

def append_roman(dict_file, str_values):
    for line in dict_file['iron_definitions']:
        if add_roman_numbers(line[0], str_values, 1):
            one_roman_string(line[0], 1)
    
    for line in dict_file['number_questions']:
        if add_roman_numbers(line[0], str_values, 2):
            one_roman_string(line[0], 2)
    
    for line in dict_file['iron_questions']:
        if add_roman_numbers(line[0], str_values, 3):
            one_roman_string(line[0], 3)
    
def add_roman_numbers(line, str_values, case): 
    try:
        if case == 1: # iron_definition
            start = 0
            end = line.index('is') - 1 
        elif case == 2: # numer_questions 
            start = line.index('is') + 1
            end = line.index('?')
        elif case == 3: # iron_question
            start = line.index('is') + 1
            end = line.index('?') - 1
    except ValueError:
        line.append(False)
        return False
    for i in range(start, end): #agrega los valores romanos al final de la linea
        try:
            line.append(str_values[line[i]]) 
        except (KeyError, ValueError):
            line.append(False)
            return False
    return True

def one_roman_string(line, case): 
    if not line[-1]:
        return False 
    if case == 1: 
        roman_len = line.index('is') - 1
        roman_string = make_str(roman_len + 4, line)
        del line[roman_len + 3:]
        line.append(roman_string)
    if case >= 2: 
        end = line.index('?') 
        roman_string = make_str(end + 1, line)
        del line[end:]
        line.append(roman_string)
        
def replace_roman_to_int(questions): # se debe chequear que el numero sea valido
    for line in questions:
        roman_string = line[0][-1]
        if line[0][-1] == False:
            continue
        int_value = roman_to_int(roman_string)
        if not int_value:
            line[0][-1] = False
        line[0][-1] = int_value


def iron_prices(dict_file):
    prices = {}
    for line in dict_file['iron_definitions']:
        if not line[0][-1]:
            continue
        quantity = int(line[0][-1])
        metal = line[0][-4]
        price = int(line[0][-2])
        prices[metal] = float(price/quantity)
    return prices
    


def sort_questions(dict_file):
    all_questions = []
    all_questions += dict_file['number_questions']
    all_questions += dict_file['iron_questions']
    all_questions += dict_file['non_recognized']
    all_questions.sort(key=lambda x:x[1])
    return all_questions

def write_answers(all_questions, prices): #se puede mejorar la funcion
    response = ''
    for question in all_questions:
        if not question[0][-1]:
            response += 'I have no idea what you are talking about\n'
            continue
        try: 
            start = question[0].index('is') + 1
            len_question = len(question[0])
            if question[0][1] == 'much': #caso number_questions
                for i in range(start, len_question-1):
                    response += question[0][i] + ' '
                response += f'is {question[0][-1]}\n'
            elif question[0][1] == 'many': #caso iron_question
                metal = question[0][-2]
                try:
                    metal_value = prices[metal]
                except (KeyError, ValueError):
                    response += 'I have no idea what you are talking about\n'
                    continue
                credits = int(question[0][-1] * metal_value)
                for i in range(start, len_question-2):
                    response += question[0][i] + ' '
                response += metal + ' ' + str(credits) + ' Credits\n'
        except (ValueError):
            response += 'I have no idea what you are talking about\n'
    return response




def flujo(inpt_file):
    dict_file = calificate_lines(inpt_file)
    str_values = str_values_dict(dict_file)
    append_roman(dict_file, str_values)
    questions = sort_questions(dict_file)
    replace_roman_to_int(questions)
    replace_roman_to_int(dict_file['iron_definitions'])
    prices = iron_prices(dict_file)
    answers = write_answers(questions, prices)
    return answers

