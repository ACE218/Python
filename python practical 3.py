#Python Program to check if a Given Kay Exists in a Dictionary or Not. If present print its value in the Dictionary Rainfall ('SUNDAY: 3.4, 'MONDAY: 5.6, "TUESDAY: 4.2, WEDNESDAY: 1.0, THURSDAY: 0.0, FRIDAY: 2.5, SATURDAY: 3.1)
def check_and_print_value(dictionary, key_to_check):
    if key_to_check in dictionary:
        print(f"The value for key '{key_to_check}' is: {dictionary[key_to_check]}")
    else:
        print(f"The key '{key_to_check}' does not exist in the dictionary.")

def main():
    Rainfall = {'SUNDAY': 3.4, 'MONDAY': 5.6, 'TUESDAY': 4.2, 'WEDNESDAY': 1.0, 'THURSDAY': 0.0, 'FRIDAY': 2.5, 'SATURDAY': 3.1}

    print("Original Dictionary:", Rainfall)

    key_to_check = input("Enter the key to check: ")

    check_and_print_value(Rainfall, key_to_check)

if __name__ == "__main__":
    main()
