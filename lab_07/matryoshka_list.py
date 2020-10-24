def get_matryoshka_list():
    """
    Builds a list of sublists to according to ascending order according to the following algorithm:

    1. Our program will start the 0th index of the list, and will begin traversing it.
    2. Our program will create a list for every section of the original list that is **ascending**.
    3. Once our program encounters a number that is not in ascending order with the past ones, it will stop creating a
    list and add it to a "repository" list.
    4. Once our program reaches the end of the original list, it will return our repository list of lists.

    :param original_list: A list of integers
    :return: A list of nested ascending lists
    """
    pass

def main():
    """
    Just some sample behavior. Feel free to try your own.
    """
    original_list = [1, 2, 3, 5, 20, 19, 3, 4, 7, 45, 100, 1, 1, 3]
    matryoshka_list = get_matryoshka_list(original_list)

    print(matryoshka_list)


# DO NOT WRITE CODE BELOW THIS LINE


if __name__ == '__main__':
    main()
