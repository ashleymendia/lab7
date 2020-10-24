def update_frequencies():
    """
    Updates a list of nucleotide frequencies to reflect the addition of a new sequence's nucleotides.

    :param old_frequencies: A list of frequency tuples
    :param new_sequence: A string representing a DNA sequence
    :return: An updated list of frequency tuples
    """
    pass


def main():
    """
    Just some sample behavior. Feel free to try your own.
    """
    old_frequencies = [("A", 20), ("C", 23), ("T", 125), ("G", 4)]
    new_sequence = "ACCCGTTA"
    new_frequencies = update_frequencies(old_frequencies, new_sequence)

    print(new_frequencies)


# DO NOT WRITE CODE BELOW THIS LINE


if __name__ == '__main__':
    main()
