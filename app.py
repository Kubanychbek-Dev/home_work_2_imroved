import re

users_list = []

while len(users_list) < 3:
    user_data_list = []

    ask_name = input("Введите имя пользователя: ").strip().title()
    match_name = re.fullmatch(r"^[a-zA-Zа-яА-Я]+$", ask_name)
    if match_name:
        print("Имя принято")
        user_data_list.append(ask_name)
    else:
        print("Содержит неподходящие символы")
        print()
        continue

    ask_surname = input("Введите фамилию пользователя: ").strip().title()
    match_surname = re.fullmatch(r"^[a-zA-Zа-яА-Я]+$", ask_surname)
    if match_surname:
        print("Фамиля принята")
        user_data_list.append(ask_surname)
    else:
        print("Содержит неподходящие символы")
        print()
        continue

    ask_phone_number = input("Введите телефон в формате +***(**)*******: ").strip()
    match_phone = re.fullmatch(r"^(\+\d{3})(\(\d{2}\))(\d{7})$", ask_phone_number)
    if match_phone:
        print("Телефон принят")
        user_data_list.append(ask_phone_number)
    else:
        print("Не соответствует формату +***(**)*******")
        print()
        continue

    ask_email = input("Введите email на яндексе: ").strip()
    match_email = re.fullmatch(r"^[a-zA-Z_0-9]+@yandex\.ru$", ask_email)
    if match_email:
        print("Почта принята")
        user_data_list.append(ask_email)
    else:
        print("Почта должна содержать только латинские буквы или цифру затем @yandex.ru")
        print()
        continue


    if user_data_list in users_list:
        print("Уже есть пользователь с точно такими же данными, введите другие данные")
        print()
        continue
    else:
        users_list.append(user_data_list)


for item in users_list:
    print(item)
