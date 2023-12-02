import re

numbers_as_re = "|".join(["on(?=e)", "tw(?=o)", "thre(?=e)", "four", "fiv(?=e)", "six", "seve(?=n)", "eigh(?=t)", "nin(?=e)"])
numbers = ["on", "tw", "thre", "four", "fiv", "six", "seve", "eigh", "nin"]

def get_digit(digit: str) -> str: 
    if digit.isdigit():
        return digit
    return str(numbers.index(digit) + 1)
   
def main(): 
    with open("_input") as input:
        total = 0
        for line in input.readlines():
            digits = re.findall(f"(\d|{numbers_as_re})", line)
            first_digit = get_digit( digits[0])
            second_digit = get_digit( digits[-1])
            number_str = "".join([first_digit, second_digit])
            total += int(number_str)
        print(total)

if (__name__ == "__main__"):
    main()