import controller
from UI import del_id


def open_file(file):
    with open(f"{file}", "r") as text_in:
        str_in = text_in.readline()
    return str_in


def write_file(file, data):
    with open(file, "w") as text_out:
        text_out.write(data)


def remove_data():
    id = del_id()
    lst = open_file("uses.csv").split(",")
    result = 0
    for i in range(0, len(lst)):
        if len(lst) > 0:
            if f"id: {id}" in lst[i]:
                del lst[i]
                lst = str(",".join(lst))
                print(f"Сотрудник c ID {id} успешно удален из базы!")
                result = 1
    if result == 0:
        print(f"Сотрудника c ID {id} в базе не обнаружено!")
    controller.button_click()
