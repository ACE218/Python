# Write a program to input two lists from user and from a dictionary using its elements as key and values.
def create_dictionary(list1, list2):
    if len(list1) != len(list2):
        print("Error: Lists must have the same length.")
        return None
    my_dict = dict(zip(list1, list2))
    return my_dict

def main():
    list1 = input("Enter elements of the first list (comma-separated): ").split(',')
    list2 = input("Enter elements of the second list (comma-separated): ").split(',')
    result_dict = create_dictionary(list1, list2)
    if result_dict:
        print("Resulting Dictionary:", result_dict)

if __name__ == "__main__":
    main()
