# Advent of Code
https://adventofcode.com

My solutions for Advent of Code in Python.

<!--- advent_readme_stars table --->
## 2023 Results

| Day | Part 1 | Part 2 |
| :---: | :---: | :---: |
| [Day 1](https://adventofcode.com/2023/day/1) | ⭐ | ⭐ |
| [Day 2](https://adventofcode.com/2023/day/2) | ⭐ | ⭐ |
| [Day 3](https://adventofcode.com/2023/day/3) | ⭐ | ⭐ |
| [Day 4](https://adventofcode.com/2023/day/4) | ⭐ | ⭐ |
| [Day 5](https://adventofcode.com/2023/day/5) | ⭐ | ⭐ |
| [Day 6](https://adventofcode.com/2023/day/6) | ⭐ | ⭐ |
| [Day 7](https://adventofcode.com/2023/day/7) | ⭐ | ⭐ |
| [Day 8](https://adventofcode.com/2023/day/8) | ⭐ | ⭐ |
| [Day 9](https://adventofcode.com/2023/day/9) | ⭐ | ⭐ |
| [Day 10](https://adventofcode.com/2023/day/10) | ⭐ | ⭐ |
| [Day 11](https://adventofcode.com/2023/day/11) | ⭐ | ⭐ |
<!--- advent_readme_stars table --->

## Download input and create .py template

utils/create_day.py downloads the respective input of the day and creates a .py template. To use it, the year has to be specified in download_input.py and template_generator.py. To access the user-specific input, a cookie value has to be set in download_input.py.

    python create_day.py --help
    usage: create_day.py [-h] day_number day_number_word puzzle_name_1 puzzle_name_2 int_input
    
    positional arguments:
      day_number       int;  number of the day
      day_number_word  str;  number of the day as word
      puzzle_name_1    str;  part 1 of name of puzzle
      puzzle_name_2    str;  part 2 of name of puzzle
      int_input        bool; specify if input are ints
    
    options:
      -h, --help       show this help message and exit
