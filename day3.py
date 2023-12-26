from aoclib import AocClient
from typing import List
import re

client = AocClient(3)

def part1():
    input = client.get_input()
    lines_raw = input.splitlines()
    dots = "." * len(lines_raw[0])
    lines = [dots] + lines_raw + [dots]
    lines_padded = ["." + line + "." for line in lines]
    row = 0
    column = 0
    total = 0
    while row < len(lines_padded) - 1:
        line = lines_padded[row]
        if (column >= len(line)):
            row += 1
            column = 0
            continue
        character = line[column]
        if character.isdigit():
            start_of_number = column
            end_of_number = column
            while column + 1 < len(line) and line[column + 1].isdigit():
                column += 1
                end_of_number = column
            surrounded_by_symbol = check_surronding_symbols(lines_padded, start_of_number, end_of_number, row)
            if surrounded_by_symbol:
                total += int(line[start_of_number:end_of_number+1])
            column += 1
        else:
            column += 1
    print(total)

def check_surronding_symbols(lines: List[str], start_of_number: int, end_of_number: int, row: int) -> bool:
    row_above = lines[row - 1][start_of_number-1:end_of_number + 2]
    this_row = lines[row][start_of_number-1:end_of_number + 2]
    row_below = lines[row +1][start_of_number-1:end_of_number + 2]
    neighbourhood = [row_above, this_row, row_below]
    print(neighbourhood)
    if not re.match("^[\d\.]*$", row_above):
        print("row above")
        return True
    if not re.match("^[\d\.]*$", row_below):
        print("row below")
        return True
    if lines[row][start_of_number -1] != "." or lines[row][end_of_number+1] != ".":
        print("start or end")
        return True
    return False

part1()