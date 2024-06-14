print("task 01")


def solution(test_string):
    test_string = test_string.split(": ")
    return test_string[-1]


successful = "2023-04-27 15:30:45 - TestCase: login_successful"
invalid = "2023-04-27 15:35:12 - TestCase: invalid_password"
print(solution(successful))
print(solution(invalid))

print("\ntask 02")


def check_file_format(file_list: list, extention: str):
    new_list = []
    for file in file_list:
        if file.endswith(extention):
            new_list.append(file)
    return new_list


list = ["a.txt", "b.txt", "c.log", "d.html", "e.log", ".diff"]
ext_01 = ".txt"
print(check_file_format(list, ext_01))
print(check_file_format(list, ext_01) == ["a.txt", "b.txt"])

ext_02 = ".log"
print(check_file_format(list, ext_02))
print(check_file_format(list, ext_02) == ["c.log", "e.log"])

ext_03 = ".json"
# Очікуваний список = []

print(check_file_format(list, ext_03))

print("\ntask 03")
def change_params(old_value:str, new_value:str):
    filetext = """\
    screen_size = 800x600
    paralel_processes = 10
    db_conection = localhost:5432"""
    # YOUR CODE HERE
    filetext = filetext.replace(old_value, new_value)

    return filetext


print(change_params('800x600', '1024x800'))
