#. Write a program to remove the given key from a dictionary, Rainfall ('SUNDAY: 3.4, "MONDAY: 5.6, TUESDAY: 4.2, "WEDNESDAY: 1.0, THURSDAY:0 FRIDAY: 2.5, 'SATURDAY: 3.1)
def remove_key(dictionary, key_to_remove):
    if key_to_remove in dictionary:
        del dictionary[key_to_remove]
        print(f"Key '{key_to_remove}' removed successfully.")
    else:
        print(f"Key '{key_to_remove}' not found in the dictionary.")

def main():
    Rainfall = {'SUNDAY': 3.4, 'MONDAY': 5.6, 'TUESDAY': 4.2, 'WEDNESDAY': 1.0, 'THURSDAY': 0, 'FRIDAY': 2.5, 'SATURDAY': 3.1}

    print("Original Dictionary:", Rainfall)

    key_to_remove = input("Enter the key to remove: ")

    remove_key(Rainfall, key_to_remove)

    print("Updated Dictionary:", Rainfall)

if __name__ == "__main__":
    main()
