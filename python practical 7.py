#Write a Python program to remove duplicates from an integer fist (Elements supplied by the user). Find 2 largest number from the list.
def remove_duplicates_and_find_largest(nums):
    unique_nums = list(set(nums))  # Remove duplicates by converting the list to a set and then back to a list
    unique_nums.sort()  # Sort the unique numbers in ascending order

    if len(unique_nums) < 2:
        print("Not enough unique numbers to find the two largest.")
        return None

    return unique_nums[-1], unique_nums[-2]

def main():
    # Input integer values into a list
    numbers = [int(x) for x in input("Enter integers separated by space: ").split()]

    # Remove duplicates and find two largest numbers
    result = remove_duplicates_and_find_largest(numbers)

    if result:
        largest1, largest2 = result
        print(f"The two largest numbers are: {largest1} and {largest2}")

if __name__ == "__main__":
    main()
