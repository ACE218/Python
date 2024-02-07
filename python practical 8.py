#Program to determine whether a given number is a happy number. The happy number can be defined as a number which will yield 1 when it is replaced by the sum of the square of its digits repeatedly, if this process results in an endless cycle of numbers containing 4, then the number is called an unhappy number. (use math module) For example, 32 is a happy number as the process yields 1 as follows 3+22 13 12+32=10 12+0² = 1
import math

def is_happy_number(number):
    seen_numbers = set()

    while number != 1 and number not in seen_numbers:
        seen_numbers.add(number)
        number = sum(int(digit) ** 2 for digit in str(number))

    return number == 1

def main():
    # Input a number from the user
    num = int(input("Enter a number: "))

    if is_happy_number(num):
        print(f"{num} is a happy number.")
    else:
        print(f"{num} is an unhappy number.")

if __name__ == "__main__":
    main()
