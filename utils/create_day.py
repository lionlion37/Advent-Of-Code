if __name__ == '__main__':
    import argparse
    import os

    from template_generator import template_generator
    from download_input import download_input

    parser = argparse.ArgumentParser()

    parser.add_argument('day_number', help='number of the day', type=str)
    parser.add_argument('day_number_word', help='number of the day as word', type=str)
    parser.add_argument('puzzle_name_1', help='part 1 of name of puzzle', type=str)
    parser.add_argument('puzzle_name_2', help='part 2 of name of puzzle', type=str)
    parser.add_argument('int_input', help='specify if input are ints', type=str)

    args = parser.parse_args()

    template_generator(args.day_number, args.day_number_word, args.puzzle_name_1, args.puzzle_name_2, args.int_input)
    download_input(args.day_number, 'inputs')

