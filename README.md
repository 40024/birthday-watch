# Birthday Tracker Utility features and purpose

I found that managing birthdays through calendars can be cumbersome. To address this, I developed this utility to offer more granular control over birthday management, ensuring that any missed birthdays are due to my oversight rather than calendar malfunctions. It was also a valuable exercise in input normalization.

- Read, write, update: Read existing birthdays, add new ones, or delete dated/incorrect entries.
- Sorting: Sort birthdays by month and date to keep your list easy to navigate.
- Input normalization: Many checks against errors, which can be common entering mass amounts of data.
- No duplicates: Built-in checks against duplicate entries.

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