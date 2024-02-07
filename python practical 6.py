#Write a program to input integer values in a list and perform Linear Search or Binary Search. Also display the position of the number in the list.
def search_number(numbers, target, search_type):
    if search_type == 'linear':
        for i, num in enumerate(numbers):
            if num == target:
                return i
    elif search_type == 'binary':
        low, high = 0, len(numbers) - 1
        while low <= high:
            mid = (low + high) // 2
            if numbers[mid] == target:
                return mid
            elif numbers[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

    return -1

def main():
    numbers = [int(x) for x in input("Enter integers separated by space: ").split()]
    target = int(input("Enter the number to search: "))
    search_type = input("Choose search type (linear/binary): ").lower()

    position = search_number(sorted(numbers), target, search_type) if search_type == 'binary' else search_number(numbers, target, search_type)

    if position != -1:
        print(f"The number {target} is found at position {position}.")
    else:
        print(f"The number {target} is not present in the list.")

if __name__ == "__main__":
    main()
