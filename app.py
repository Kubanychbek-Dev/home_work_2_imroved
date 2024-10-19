import re

# Вам необходимо составить 4 регулярных выражения которые
# будут отвечать за проверку вводимой пользователем
# информации:
# имя пользователя - все буквы латиница и кириллица, как в
# нижнем так и в верхнем регистре, символы и цифры
# запрещены!
# фамилия пользователя - все буквы латиница и кириллица,
# как в нижнем так и в верхнем регистре, символы и цифры
# запрещены!
# телефон пользователя должен выглядеть следующим
# образом +***(**)******* (например +375(29)1234567.
# Количество символов в строке номера подчиняется
# следующим правилам: + обязателен, после символа + от 1 до
# 3 цифр, далее скобка внутри 2 цифры скобка и строго 7 цифр
# (чтобы ограничить количество закройте строку $)
# электронная почта обязательна должна содержать хотя бы 1
# символ латинского алфавита в любом регистре или 1 цифру
# после него @yandex.ru (тут тоже строку надо будет закрыть).


users_list = []

while len(users_list) < 3:
    user_data_list = []

    ask_name_i = 0

    while ask_name_i < 1:
        ask_name = input("Введите имя пользователя: ").strip().title()
        match_name = re.fullmatch(r"^[a-zA-Zа-яА-Я]+$", ask_name)
        if match_name:
            print("Имя принято")
            print()
            user_data_list.append(ask_name)
            ask_name_i += 1
        else:
            print("Содержит неподходящие символы")
            print()


    ask_surname_i = 0

    while ask_surname_i < 1:
        ask_surname = input("Введите фамилию пользователя: ").strip().title()
        match_surname = re.fullmatch(r"^[a-zA-Zа-яА-Я]+$", ask_surname)
        if match_surname:
            print("Фамиля принята")
            print()
            user_data_list.append(ask_surname)
            ask_surname_i += 1
        else:
            print("Содержит неподходящие символы")
            print()


    ask_phone_i = 0

    while ask_phone_i < 1:
        ask_phone_number = input("Введите телефон в формате +***(**)*******: ").strip()
        match_phone = re.fullmatch(r"^(\+\d{3})(\(\d{2}\))(\d{7})$", ask_phone_number)
        if match_phone:
            print("Телефон принят")
            print()
            user_data_list.append(ask_phone_number)
            ask_phone_i += 1
        else:
            print("Не соответствует формату +***(**)*******")
            print()


    ask_email_i = 0

    while ask_email_i < 1:
        ask_email = input("Введите email на яндексе: ").strip()
        match_email = re.fullmatch(r"^[a-zA-Z_0-9]+@yandex\.ru$", ask_email)
        if match_email:
            print("Почта принята")
            print()
            user_data_list.append(ask_email)
            ask_email_i += 1
        else:
            print("Почта должна содержать только латинские буквы или цифру затем @yandex.ru")
            print()


    if user_data_list in users_list:
        print("Уже есть пользователь с точно такими же данными, введите другие данные")
        print()
        continue
    else:
        users_list.append(user_data_list)


for item in users_list:
    print(item)
