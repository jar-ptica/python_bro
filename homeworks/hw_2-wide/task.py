#1 - Numeric Operation
def sum_of_two_numbers(number_a, number_b):
    """
    function should return sum of two numbers, int or float
    number_a - (int or float)
    number_b - (int or float)
    return: int or float
    """
    return number_a + number_b


#2 - Numeric Operation Error checking
def absolute_numeric_value(value):
    """
    function should return absolute numeric value,
    if not possible - should raise ValueError
    value - (any)
    return: any numeric
    """
    if isinstance(value, (int, float)):
        return abs(value)
    else:
        raise ValueError



#3 - Numeric Operation Error checking
def sum_of_two_integer_numbers_with_conversion(number_a, number_b):
    """
    function should return sum of two INT numbers,
    if any variable is NOT int type - should round it to int
    number_a - (any numeric)
    number_b - (any numeric)
    return: int
    """
    list = [number_a, number_b]
    for i in range(len(list)):
        value = list[i]
        if type(value) == float:
            value = round(value)
        else:
            value = value
        list[i] = value
    return sum(list)


#4 - Numeric Operation Error checking
def sum_of_two_absolute_numbers(number_a, number_b):
    """
    function should return sum of two absolute numerics,
    number_a - (any numeric)
    number_b - (any numeric)
    return: any numeric
    """
    return abs(number_a) + abs(number_b)

#5 - String Operation Error Checking
def string_from_two_strings_with_conversion(string_a, string_b):
    """
    function should return sum of two strings as one complete string
    if any variable not string type - should convert to string
    if conversion NOT possible - should raise TypeError
    string_a - (string)
    string_b - (string)
    return: string
    """
    list_arg = [string_a, string_b]
    for i in range(0, 2):
        value = list_arg[i]
        if not type(value) == str:
            value = str(value)
        else:
            value = value
        list_arg[i] = value
    result = list_arg[0] + list_arg[1]
    return result



#6 - String Operation Error Checking
def is_word_in_text(text, word):
    """
    function should return True if word is in given text, False if not
    if any variable not string type - should convert to string
    if conversion NOT possible - should raise TypeError
    text - (string)
    word - (string)
    return: bool
    """
    if not isinstance(text, str):
        text = str(text)
    if not isinstance(word, str):
        word = str(word)
    return word in text

#7 - String Operation Error Checking
def string_part_replacement(text, search_value, replace_value):
    """
    function should string where 'search_value' will be replaced to 'replace_value'
    if any variable not string type - should convert it to string
    if conversion not possible - should raise ValueError
    text - (any)
    string_a - (any)
    string_b - (any)
    return: string
    """
    try:
        if not isinstance(text, str):
            text = str(text)
        if not isinstance(search_value, str):
            search_value = str(search_value)
        if not isinstance(replace_value, str):
            replace_value = str(replace_value)
    except ValueError:
        print('invalid data')

    return text.replace(search_value, replace_value)

#8 - String Operation Error Checking
def string_to_words(text):
    """
    function should return different words list
    if input variable not string type - should raise TypeError
    if not possible to return more than two words - return empty list
    text - (any)
    return: list [string, string] or None
    """
    if not isinstance(text, str):
        raise TypeError
    else:
        if " " in text:
            return text.split(' ')
        else:
            return None


#7 - String Operation Error Checking - Cycles
def every_word_capitalize(text):
    """
    function should string where each separate word has to be capitalized
    if input variable not string type - should raise TypeError
    text - (any)
    return: string
    """
    if not isinstance(text, str):
        raise TypeError
    else:
        return text.title()

#8 - String Operation Error Checking
def string_upper_case(text):
    """
    function should return string in upper case
    if input variable not string type - should raise TypeError
    text - (any)
    return: string
    """
    if not isinstance(text, str):
        raise TypeError
    else:
        return text.upper()

#9 - String Operation Error Checking - Cycles, temp_variable
def word_in_upper_case(text, word_number):
    """
    function should return string where word with number{'word_number'} has to be in lower case
    if input variable not string type - should raise TypeError
    text - (any)
    return: string
    """
    if not isinstance(text, str):
        raise TypeError
    else:
        words_in_text = text.split(" ")
        new = words_in_text[word_number].upper()
        result = text.replace(words_in_text[word_number], new)
        return result

#10 - String Operation Error Checking
def join_words(word_a, word_b):
    """
    function should return string joined from {'word_a'} {'word_b'}
    if any input variable not string type - should raise TypeError
    word_a - (any)
    word_b - (any)
    return: string
    """
    if any([not isinstance(word_a, str), not isinstance(word_b, str)]):
        raise TypeError
    else:
        return word_a + word_b

#11 - String Operation Error Checking
def string_is_starts_with(text, part):
    """
    function should return True if {'text'} value starts with {'part'}, else return False
    if any input variable not string type - should convert to string type
    if not possible - should raise TypeError
    text - (any)
    part - (any)
    return: bool
    """
    return

#12 - String Operation Error Checking
def string_is_ends_with_part(text, part):
    """
    function should return True if {'text'} value ends wits with {'part'}, else return False
    if any input variable not string type - should convert to string type
    if not possible - should raise TypeError
    text - (any)
    return: bool
    """
    return

#13 - String Operation Error Checking
def string_is_ends_with_part_upper_case(text, part):
    """
    function should return True if {'text'} value ends wits with {'part'} in upper case, else return False
    if any input variable not string type - should convert to string type
    if not possible - should raise TypeError
    text - (any)
    part - (any)
    return: bool
    """
    return

#14 - String Operation Error Checking
def string_is_ends_with_three_numbers(text):
    """
    function should return True if {'text'} value ends wits with 3 digits, else return False
    if any input variable not string type - should convert to string type
    if not possible - should raise TypeError
    text - (any)
    return: bool
    """
    return


#15 - List Operation Error Checking
def join_of_two_lists(list_a, list_b):
    """
    function should return list including elements from both input lists in given order
    list_a - (list)
    list_b - (list)
    return: list
    """
    return

#16 - List Operation Error checking
def sum_of_list_elements(list_num,):
    """
    function should return sum of list elements
    if any variable not numeric type - should raise TypeError
    list_a - (list)
    list_b - (list)
    return: list
    """
    return

#17 - List Operation Error checking
def max_from_numeric_list(list_n):
    """
    function should return maximum value of list of numerics,
    if any element not numeric type - should raise TypeError
    list_n - (list) - [0, -1, 5,..]
    return: any numeric
    """
    return

#18 - Numeric Operation Error checking
def min_from_numeric_list(list_n):
    """
    function should return minimum value of list of numerics,
    if element not numeric type - should raise TypeError
    list_n - (list) - [0, -1, 5,..]
    return: any numeric
    """
    return

#19 - List Operation Error checking
def get_negative_numbers_count(list_n):
    """
    function should return count of NEGATIVE values from numeric list,
    if element not numeric type - should raise TypeError
    list_n - (list) - [0, -1, 5,..]
    return: int
    """
    return

#20 - List Operation Error checking
def remove_elements_from_list(list_a, list_b):
    """
    function should return list which contains {'list_a'} elements without {'list_b'} elements,
    if any variable not list type, should return empty list
    list_a - (list)
    list_b - (list)
    return: list
    """
    return