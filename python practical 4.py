#Write a Python program to find the maximum frequency of a character in a given string
def max_frequency_char(input_string):
    char_frequency = {}

    for char in input_string:
        char_frequency[char] = char_frequency.get(char, 0) + 1

    max_char = max(char_frequency, key=char_frequency.get)

    return max_char, char_frequency[max_char]

def main():
    input_string = input("Enter a string: ")

    result_char, frequency = max_frequency_char(input_string)

    print(f"The character '{result_char}' has the maximum frequency of {frequency} in the given string.")

if __name__ == "__main__":
    main()
