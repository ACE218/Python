#Write a menu driven program in python which will accept a number and choice as ""," from the user and calculate the following according to the user choice (use user defined function): a. Factorial of each digit (Calculate factorial of each digit and return the same.
#b. Reverse of that number (Calculate Reverse of the number and display).

#c. Factors of that number (Display factors of the number).
import math

def factorial_of_digit(digit):
    return math.factorial(int(digit))

def reverse_of_number(number):
    return int(str(number)[::-1])

def factors_of_number(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def main():
    while True:
        print("\nMenu:")
        print("1. Factorial of each digit")
        print("2. Reverse of the number")
        print("3. Factors of the number")
        print("4. Quit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '4':
            break

        number = int(input("Enter a number: "))

        if choice == '1':
            result = [factorial_of_digit(digit) for digit in str(number)]
            print(f"Factorials of each digit: {result}")
        elif choice == '2':
            result = reverse_of_number(number)
            print(f"Reverse of the number: {result}")
        elif choice == '3':
            result = factors_of_number(number)
            print(f"Factors of the number: {result}")
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
