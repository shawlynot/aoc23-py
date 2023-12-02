import re
numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
numbers_as_re = "|".join(numbers)

def get_digit(digit: str) -> str: 
    if re.search(f"({numbers_as_re})", digit) is not None:
        return str(numbers.index(digit) + 1)
    return digit

with open("_input") as input:
    total = 0
    for line in input.readlines():
        digits = re.findall(f"(\d|{numbers_as_re})", line)
        first_digit = get_digit( digits[0])
        second_digit = get_digit( digits[-1])
        number_str = "".join([first_digit, second_digit])
        total += int(number_str)
print(total)

