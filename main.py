import json

def print_menu():
    print("Birthday Watch Menu")
    print("-------------")
    print("0. Quit")
    print("1. Print birthdays")
    print("2. Add birthday")
    print("")

def print_file():
    with open("birthdays.json", "r", encoding="utf-8") as json_file:
        file = json.load(json_file)

    for entry in file:
        print(entry["name"], entry["birthday_month_date"])

def num_from_month_name(birthday_month_date):
    # Separate month and date
    month, day = birthday_month_date.split("-")

    # Format month if needed
    try:
        month = int(month)
        if not 1 <= month <= 12:
            print("Date has to be between 1 and 12, no entry added")
            return
        else:
            # Return original date if no formatting needed
            return birthday_month_date
    except:
        months = {
            "jan": 1,
            "feb": 2,
            "mar": 3,
            "apr": 4,
            "may": 5,
            "jun": 6,
            "jul": 7,
            "aug": 8,
            "sep": 9,
            "oct": 10,
            "nov": 11,
            "dec": 12,
            "january": 1,
            "february": 2,
            "march": 3,
            "april": 4,
            "may": 5,
            "june": 6,
            "july": 7,
            "august": 8,
            "september": 9,
            "october": 10,
            "november": 11,
            "december": 12
        }

        month = month.lower()

        if month in months:
            # Maintain month congruency in json file (prevents dates such as 1-01)
            if months[month] < 10:
                return f"0{months[month]}-{day}"
            else:
                return f"{months[month]}-{day}"
        else:
            print(f"Month: {month}")
            print("Month could not be read, please use month name")

def add_birthday(name, birthday_month_date):
    # Format name and birthday
    birthday_month_date = num_from_month_name(birthday_month_date)

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
            birthday_month_date = input("Enter recipient birthday {MM-DD}: ")
            add_birthday(name, birthday_month_date)

if __name__ == "__main__":
    main()