import json

def print_menu():
    print("Birthday Watch Menu")
    print("-------------")
    print("0. Quit")
    print("1. Print birthdays")
    print("2. Add birthday")
    print("3. Birthday month name function unit test")

def print_file():
    with open("birthdays.json", "r", encoding="utf-8") as json_file:
        file = json.load(json_file)

    for entry in file:
        print(entry["name"], entry["birthday_month_date"])

def format_month_name_input(birthday_month_date):
    print(birthday_month_date)

def add_birthday(name, birthday_month_date):
    # Format name and birthday
    birthday_month_date = format_month_name_input(birthday_month_date)

    new_data = [
        {
            "name": name,
            "birthday_month_date": birthday_month_date
        }
    ]

    # Read existing and append new data to existing
    try:
        with open("birthdays.json", 'r', encoding='utf-8') as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = []

    if isinstance(existing_data, list):
        existing_data.extend(new_data)
    else:
        print("Error: The existing JSON data is not a list.")

    # Write the updated data back to the file
    with open("birthdays.json", 'w', encoding='utf-8') as file:
        json.dump(existing_data, file, ensure_ascii=False, indent=4)

def main():

    while True:
        print_menu()
        # Input
        option = int(input("Please enter an option: "))
        if option == 0:
            print("Goodbye!")
            exit()
        elif option == 1:
            print_file()
        elif option == 2:
            name = input("Enter recipient name: ")
            birthday_month_date = input("Enter recipient birthday {Month-Date}: ")
            add_birthday(name, birthday_month_date)
        elif option == 3:
            name = input("Enter recipient name: ")
            birthday_month_date = input("Enter recipient birthday {Month-Date}: ")
            format_month_name_input(birthday_month_date)

if __name__ == "__main__":
    main()