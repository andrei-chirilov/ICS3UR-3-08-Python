#!/usr/bin/env python3

# Created by: Andrei Chirilov
# Created on: Oct 2019
# This program uses a nested if statement


def main():
    # this function calculate if the year is a leap year
    # input
    year = input("Enter a year: ")
    print("")

    # process & output
    # try & except
    try:
        number = int(year)
        # checking if year entered is a leap year
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
