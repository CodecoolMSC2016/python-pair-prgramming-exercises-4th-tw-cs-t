import csv
import sys
from person import Person


def open_csv(file_name):
    result_list = []
    with open(file_name, 'r') as fileka:
        data = csv.reader(fileka)
        for line in data:
            name,phonenumber = line.split(",")
            result_list.append(Person(name,phonenumber))
    return result_list





def get_csv_file_name(argv_list):
    return argv_list[1:]


def format_output(person):
    return 'This number belongs to: ' + person._name


def get_person_by_phone_number(person_list, user_input_phone_number):
    for personka in person_list:
        if personka._phonenumber == user_input_phone_number:
            return personka
    return None


def main():
    file_name = get_csv_file_name(sys.argv)
    if file_name is None:
        print('No database file was given.')
        sys.exit(0)

    person_list = open_csv(file_name)
    user_input_phone_number = input('Please enter the phone number: ')
    match_person = get_person_by_phone_number(person_list, user_input_phone_number)

    print(format_output(match_person))

if __name__ == '__main__':
    main()
