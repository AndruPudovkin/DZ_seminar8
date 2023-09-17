from pathlib import Path
def Print1():#посмотрет метод strip() 

    file_data = Path("Telephone_directory.txt")
    with open (file_data , "r",encoding="UTF-8") as file_data:
        print(file_data.read())
def Print2():
    file_data = Path("Telephone_directory.txt")
    with open (file_data , "a", encoding="UTF-8") as file_data:
        name_new1 = input("Введите Фаилию: ").title() #переводит в верхний регист для поиска  (андре---> Андрей)
        name_new2 = input("Введите Имя: ").title()
        tel_new = input("Введите телефон: ")
        string_new = name_new1, name_new2, tel_new
        file_data.write("\n"+name_new1+", "+name_new2+", "+tel_new)
def Print3():
    file_data = Path("Telephone_directory.txt")
    with open (file_data , "r", encoding="UTF-8") as file_data:
        find_name = input('Введите искомый контакт: ').title()
        s = True
        lines = file_data.readlines()
        for line in lines:
           if find_name in line:
                print(f"Контакт найден: {line}", end="")
                s = False
        if s:
            print("Такого кантакта нет")
def Print4():
    f= Path("Telephone_directory.txt")
    update_name1 = input("Введите имя контакта который хотите изменить: ")
    update_name2 = input("Введите фамилию контакта который хотите изменить: ")
    with open(f, "r", encoding="UTF-8") as file_data:
        lines = file_data.readlines()
        s = False
        for i in range(len(lines)):
            contact = lines[i].strip().split(", ")
            contact_name1 = contact[0].strip()
            # contact_name2 = contact[1].strip()
            if update_name1 == contact_name1:
            # and update_name2 == contact_name2:
                new_name1 = input("Введите новое имя: ")       
                new_name2 = input("Введите новую фамилию: ")    
                new_phone = input("Введите новый телефон: ")    
                contact[0] = new_name1
                contact[1] = new_name2
                contact[2] = new_phone
                lines[i] = ','.join(contact)+"\n"
                s=True
                break
        if s:
            with open(f, "w", encoding="UTF-8") as file_data:
                file_data.writelines(lines) #???
            print("Контакт успешно обнавлен")
        else:
            print("Контакт ненайден")


def Print5():
    f= Path("Telephone_directory.txt")
    del_name1 = input("Введите имя контакта который хотите удалить: ")
    del_name2 = input("Введите фамилию контакта который хотите удалить: ")
    with open(f, "r", encoding="UTF-8") as file_data:
        lines = file_data.readlines()
    with open(f, "w", encoding="UTF-8") as file_data:
        s = False
        for line in lines:
            contact = line.strip().split(", ")
            print(contact)
            if not ((del_name1 in contact) and (del_name2 in contact)):
                file_data.write(line)
            else:
                s=True
        if s:
            print("Контакт успешно удален")
        else:
            print("Контакт не найден")


   
      



print("1. Вывод всех записей справочника; \n2. Добавить запись;\n3. Поиск записи;\n4. Изменение записи;\n5. Удалить запись\n0. Выйти из справочника")
num = int(input("Введите номер действия, которое будем выполнять: "))
if num == 1:
    Print1()
elif num == 2:
    Print2()
elif num == 3:
    Print3()
elif num == 4:
    Print4()
elif num ==5:
    Print5()
elif num==0:
    print()
else:
    print("Такого пункта нет в меню")
