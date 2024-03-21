# lib/cli.py

from helpers import (
    exit_program,
    list_profiles,
    list_milk_records,
    list_tea_records,
    list_tenant_records
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_profiles()
        elif choice == "2":
            list_milk_records()
        elif choice == "3":
            list_tea_records()
        elif choice == "4":
            list_tenant_records()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List of Profiles")
    print("2. Dairy Farmers Records")
    print("3. Pluckers Records")
    print("4. Tenants Records ")
   


if __name__ == "__main__":
    main()
