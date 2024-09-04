# Birthday Tracker Utility purpose

- Effortless Birthday Management: Seamlessly track and organize birthdays stored in a JSON file.
- Read, Write, Sort: Conveniently read existing birthdays, add new entries, and sort them with just a few commands.
- Smart Sorting: Automatically sort birthdays by month and date to keep your list well-organized and easy to navigate.

Streamline your birthday tracking with this user-friendly utility and never miss an important date again!

# Usage 
## Read Birthdays

To read birthday data, use option 1:

```text
> Please enter an option: 1
< Foo 11-20
< Bar 01-02
```

## Add birthday
```text
> Please enter an option: 2
> Enter recipient name: Baz
> Enter recipient birthday {MM-DD}: Oct-03
< Added Baz's birthday with the date of Oct-03

> Please enter an option: 1
< Bar 11-20
< Foo 01-02
< Baz 10-03
```

## Sort birthdays
```text
> Please enter an option: 1
< Foo 11-20
< Bar 01-02
< Baz 10-03

> Please enter an option: 3
< Birthdays have been sorted

> Please enter an option: 1
< Bar 01-02
< Baz 10-03
< Foo 11-20
```