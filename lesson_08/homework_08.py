new_list = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3", "23,12,2,8", "34,df,we"]


def sum_all_number(new_list):
    for item in new_list:
        item_list_str = item.split(",")  # returns list of strings: ['1', '2', '3', '4']
        item_list_int = []  # list for integer items

        try:
            for i in item_list_str:
                item_list_int.append(int(i))  # create a list of integers
            print(sum(item_list_int))  # print sum of integers
        # for cases when input value can't be converted to integer
        except ValueError:
            print("Не можу це зробити!")


sum_all_number(new_list)
