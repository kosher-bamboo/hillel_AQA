def find_strings(list: list):
    list_string = []
    for item in list:
        if type(item) is str:
            list_string.append(item)
    return list_string

find_strings([-94.79, 'vjqbxrguip', -58, '19', 60, 'True', True, '-43', 'okqnacfc', False, 43, 54, 40, 'bcx', 5,
          'qiqvcvwyln', True, 'zsqbqbmw', 'z', 'qcj'])

# new_list = ["1,2,3,4", "1,2,3,4,50"]
# new_list = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3", "23,12,2,8", "34,df,we"]


# def sum_all_number(new_list):
#     for item in new_list:
#         item_list_str = item.split(",")  # returns list of strings: ['1', '2', '3', '4']
#         item_list_int = []  # list for integer items
#
#         try:
#             for i in item_list_str:
#                 item_list_int.append(int(i))  # create a list of integers
#             return sum(item_list_int)  # print sum of integers
#         # for cases when input value can't be converted to integer
#         except ValueError:
#             # print("Не можу це зробити!")
#             return "Не можу це зробити!"
#
#
# sum_all_number(["1,2,3,4", "1,2,3,4,50"])
