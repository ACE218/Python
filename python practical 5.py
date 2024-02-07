#Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged
def modify_string(input_string):
    if len(input_string) < 3:
        return input_string
    elif input_string.endswith('ing'):
        return input_string + 'ly'
    else:
        return input_string + 'ing'

def main():
    input_string = input("Enter a string: ")

    modified_string = modify_string(input_string)

    print("Modified String:", modified_string)

if __name__ == "__main__":
    main()
