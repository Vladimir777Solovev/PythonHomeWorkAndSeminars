# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи
# (Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, 
# и Вы должны реализовать функционал для изменения и удаления данных

def choose_action(phonebook):
    while True:
        print('What would you like to do?')
        user_choice = input('1 - Find contact\n2 - Add contact\n3 - Change contact\n4 - Delete contact\n5 - List of contacts\n6 - Exit\n')

        print()
        if user_choice == '1':
            contact_list = read_file_to_dict(phonebook)
            find_number(contact_list)
        elif user_choice == '2':
            add_phone_number(phonebook)
        elif user_choice == '3':
            change_phone_number(phonebook)
        elif user_choice == '4':
            delete_contact(phonebook)
        elif user_choice == '5':
            show_phonebook(phonebook)
        elif user_choice == '6':
            print('Have a nice day')
            break
        else:
            print('Wrong input')
            print()
            continue



def read_file_to_dict(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    headers = ['Last Name', 'Name', 'Phone number']
    contact_list = []
    for line in lines:
        line = line.strip().split()
        contact_list.append(dict(zip(headers, line)))
    return contact_list


def read_file_to_list(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        contact_list = []
        for line in file.readlines():
            contact_list.append(line.split())
    return contact_list


def search_parameters():
    print('In which field you would like to search?')
    search_field = input('1 - In Last Name\n2 - In Name\n3 - In Phone numbers\n')
    print()
    search_value = None
    if search_field == '1':
        search_value = input('Input the Last Name: ')
        print()
    elif search_field == '2':
        search_value = input('Input the Name: ')
        print()
    elif search_field == '3':
        search_value = input('Input the Phone number: ')
        print()
    return search_field, search_value


def find_number(contact_list):
    search_field, search_value = search_parameters()
    search_value_dict = {'1': 'Last name', '2': 'Name', '3': 'Phone number'}
    found_contacts = []
    for contact in contact_list:
        if contact[search_value_dict[search_field]] == search_value:
            found_contacts.append(contact)
    if len(found_contacts) == 0:
        print('Wrong contact')
    else:
        print_contacts(found_contacts)
    print()


def get_new_number():
    last_name = input('Input the Last Name: ')
    first_name = input('Input the Name: ')
    phone_number = input('Input the Phone number: ')
    return last_name, first_name, phone_number


def add_phone_number(file_name):
    info = ' '.join(get_new_number())
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(f'{info}\n')


def show_phonebook(file_name):
    list_of_contacts = sorted(read_file_to_dict(file_name), key=lambda x: x['Last Name'])
    print_contacts(list_of_contacts)
    print()
    return list_of_contacts


def search_to_modify(contact_list: list):
    search_field, search_value = search_parameters()
    search_result = []
    for contact in contact_list:
        if contact[int(search_field) - 1] == search_value:
            search_result.append(contact)
    if len(search_result) == 1:
        return search_result[0]
    elif len(search_result) > 1:
        print('A few contacts found')
        for i in range(len(search_result)):
            print(f'{i + 1} - {search_result[i]}')
        num_count = int(input('Choose the number of contact you wish to change or delete: '))
        return search_result[num_count - 1]
    else:
        print('Wrong contact')
    print()


def change_phone_number(file_name):
    contact_list = read_file_to_list(file_name)
    number_to_change = search_to_modify(contact_list)
    contact_list.remove(number_to_change)
    print('Which field you would like to change?')
    field = input('1 - Last name\n2 - Name\n3 - Phone number\n')
    if field == '1':
        number_to_change[0] = input('Input the Last Name: ')
    elif field == '2':
        number_to_change[1] = input('Input the Name: ')
    elif field == '3':
        number_to_change[2] = input('Input the Phone number: ')
    contact_list.append(number_to_change)
    with open(file_name, 'w', encoding='utf-8') as file:
        for contact in contact_list:
            line = ' '.join(contact) + '\n'
            file.write(line)


def delete_contact(file_name):
    contact_list = read_file_to_list(file_name)
    number_to_change = search_to_modify(contact_list)
    contact_list.remove(number_to_change)
    with open(file_name, 'w', encoding='utf-8') as file:
        for contact in contact_list:
            line = ' '.join(contact) + '\n'
            file.write(line)


def print_contacts(contact_list: list):
    for contact in contact_list:
        for key, value in contact.items():
            print(f'{key}: {value:12}', end='')
        print()


if __name__ == '__main__':
    file = 'Phonebook.txt'
    choose_action(file)