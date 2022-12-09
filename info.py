#!/usr/bin/env python3

# Created by: Marshall Demars
# Created on: Dec 2022
# This program formats someones address using Canada Post format


def address(
    full_name,
    street_number,
    street_name,
    city,
    province,
    postal_code,
    apartement_number=None,
):

    # return proper address

    proper = full_name + "\n"
    if apartement_number != None:
        proper = proper + str(apartement_number) + "-"
    proper = proper + str(street_number)
    proper = proper + " " + street_name + "\n"
    proper = proper + city + " "
    proper = proper + province + "  "
    proper = proper + postal_code

    return proper


def main():
    # main function
    apartement_number = None

    full_name = input("Enter your full name: ")
    question = input("Do you live in an apartment? (y/n): ")
    if question == "y":
        apartement_number = input("Enter your apartment number: ")
    street_number = input("Enter your street number: ")
    street_name = input("Enter your street name and type (Pleasant prkw...): ")
    city = input("Enter your city: ")
    province = input("Enter your province (as an abbreviation, ex: ON, BC...): ")
    postal_code = input("Enter your postal code (ABC 123): ")

    try:
        if apartement_number != None:
            apartement_number = int(apartement_number)
        street_number = int(street_number)
        proper_finish = address(
            full_name,
            street_number,
            street_name,
            city,
            province,
            postal_code,
            apartement_number,
        )
        print("\n")
        print(proper_finish.upper())
    except Exception:
        print("\nInvalid Input.")

    print("\nDone.")


if __name__ == "__main__":
    main()
