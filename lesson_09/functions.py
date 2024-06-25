def find_strings(input_value):
    list_string = []
    for item in input_value:
        if type(item) is str:
            list_string.append(item)
    return list_string
