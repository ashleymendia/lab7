def is_haiku():
    """
    Checks if input_string follows the syllabic and line structure of a haiku and outputs True if so.

    :param input_string: A string
    :return: True or False
    """
    pass


def haiku_string_parser():
    """
    Formats a haiku single-line string into a multi-line, readable form if input_string is in fact a haiku.

    :param input_string: A single-line string representing a haiku's syllabic and line division.
    :return: A multi-line representation of input_string.
    """
    pass


def main():
    """
    Just some sample behavior. Feel free to try your own.
    """
    haiku_string = "clouds ,mur,mur ,dark,ly/it ,is ,a ,blin,ding ,ha,bit/ga,zing ,at ,the ,moon"
    formatted_haiku = haiku_string_parser(haiku_string)
    print(formatted_haiku)


if __name__ == '__main__':
    main()
