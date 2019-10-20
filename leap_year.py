#!/usr/bin/env python3

# Created by: Andrei Chirilov
# Created on: Oct 2019
# This program uses a nested if statement


def main():
    year = input("Enter a year: ")
    print("")

    try:
        number = int(year)
        if (number % 4) == 0:
            if (number % 100) == 0:
                if (number % 400) == 0:
                    print("{} is a leap year." .format(year))
                else:
                    print("{} is not a leap year." .format(year))
            else:
                print("{} is a leap year." .format(year))
        else:
            print("{} is not a leap year." .format(year))
    except Exception:
        print("This wasn't a valid entry. Please try again")
    finally:
        print("Thank you for using me to detirmine if it's a leap year or not")


if __name__ == "__main__":
    main()
