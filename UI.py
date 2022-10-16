def print_data(data):
    print(data)


def input_data(data):
    input(f"{data}")


def input_name_directory():
    phone = check_phone()
    ID = input('id: ')
    surname = input("Фамилия: ")
    name = input("Имя: ")
    patronymic = input("Отчество: ")
    post = input('Должность: ')
    department = input('Отдел: ')
    return f"id: {ID} Фамилия: {surname} Имя: {name} Отчество: {patronymic} Телефон: +7 {phone}\
        Должность: {post} Отдел: {department}"

def check_phone():
    flag = False
    while flag == False:
        phone = input("Телефон: +7 ")
        if phone.isdigit():
            flag = True
            return phone
        else:
            print("Некорректный ввод, повторите попытку.")

def input_check_choice(text):
    flag = False
    while flag == False:
        user_answer = input(text)
        try:
            int(user_answer)
            if 0 < int(user_answer) < 3:
                return int(user_answer)
            else:
                flag == False
        except ValueError:
            flag == False
