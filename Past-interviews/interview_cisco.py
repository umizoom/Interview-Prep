# Question 1

my_string_1 = '192.168.1.1'

my_string_2 = 'ABC'

my_string_3 = '1.2.3.256'

my_string_4 = '0.0.0.0'  # is valid
my_string_5 = '-1.-1.-1.-1'


def verify_ip(ip_string: str) -> bool:
    """
    Valid ip:
    - must have 4 octets
    - Octet can not be greater than 255

    :param ip:
    :return:
    """
    ip = ip_string.split(".")
    if len(ip) != 4:
        print('False')
        return False
    for octet in ip:
        if octet.isdecimal() is False:
            print('False')
            return False
        if int(octet) > 255 or int(octet) < 0:
            print('False')
            return False
    print('True')
    return True


verify_ip(my_string_1)
verify_ip(my_string_2)
verify_ip(my_string_3)
verify_ip(my_string_4)
verify_ip(my_string_5)

# Question 2

array_1 = [[1, 2, 3, ],
           [2, 3, 4],
           [5, 4, 4]]

array_2 = [[5, 3, 7, ],
           [9, 6, 9],
           [5, 4, 5]]

"""
output = 
[[6, 5, 10], 
[11, 9, 13], 
[10, 8, 9]]

[[30, 15, 70], 
[99, 54, 117], 
[50, 32, 45]]
"""


def sum_muli_array(array1: list, array2: list) -> list:
    """
    array 1 and 2 are 3X3 arrays.
    Output of this fuction should print 2 arrays.
    array 3 is the sum of array 1 and 2
    array 4 is the mulplication of array 1 and 2

    :param array1:
    :param array2:
    :return:
    """

    array_3 = [[0 for row in range(3)] for row in range(3)]
    array_4 = [[0 for row in range(3)] for row in range(3)]
    for r in range(len(array1)):
        for c in range(len(array1[0])):
            array_3[r][c] = array_1[r][c]
            array_4[r][c] = array_1[r][c]

    for r in range(len(array2)):
        for c in range(len(array2[0])):
            array_3[r][c] = array_3[r][c] + array_2[r][c]
            array_4[r][c] = array_3[r][c] * array_2[r][c]
    print(array_3)
    print(array_4)


sum_muli_array(array1=array_1, array2=array_2)

# Question 3

my_string = """
umaid is nice. umaid is okay. 
umaid failed this interview.
good luck umaid
"""


def find_index_of_string(string_to_check: str) -> [int]:
    """
    Print the indexes for each match of 'umaid'
    :param string_to_check:
    :return:
    """
    import re
    search = re.findall("umaid", string_to_check)
    # Unsure about this... I think he meant print the index from the original string but I am not sure how to do that.
    for index in range(len(search)):
        print(index)
    print(search)


find_index_of_string(my_string)

# Question 4

input = '''
fruit - apple 
vegetable - Endive Carrots Broccoli 
dessert - cake
'''

output = """
{'fruit': 'apple', 'vegetable': 'Endive, Carrots, Broccoli', 'dessert': 'cake'}
"""


def sort_food(food: str) -> dict:
    """
    see input and output for explanation
    :param food:
    :return:
    """
    output = {}

    list_food = food.split('\n')
    for i in range(len(list_food) - 1):
        if list_food[i] == '':
            list_food.pop(i)
    for entry in list_food:
        new_entry = entry.split("-")
        output[new_entry[0].strip()] = output.get(new_entry[0], '') + new_entry[1].strip().replace(" ", ", ")
    print(output)
    return output


sort_food(input)

