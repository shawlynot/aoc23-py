import re

with open("_input") as input:
    total = 0
    for line in input.readlines():
        digits = re.findall("\d", line)
        number_str = "".join([digits[0], digits[-1]])
        total += int(number_str)
print(total)