from sys import stdin
from re import search

def main():
    total_sum = 0 
    row = 0
    while True:
        row = row + 1
        line = stdin.readline()
        if line == "":
            break
        else:
            number_in_row = parse_string(line, row)
            total_sum = total_sum + number_in_row
    
    print(total_sum)
    
def parse_string(line, row):
    first_digit = ""
    last_digit = ""
    digits = {'one': 1, 'two': 2, 'three': 3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine': 9}
    curr_str = ""
    
    for character in line:
        if character.isnumeric():
            if first_digit == "":
                first_digit = character
            else: 
                last_digit = character
            curr_str = ""
        else:
            curr_str = curr_str + character
            for key in digits.keys():
                if search(key, curr_str):
                    if first_digit == "":
                        first_digit = str(digits[key])
                    else:
                        last_digit = str(digits[key])
                    curr_str = cut_key_offset(curr_str, len(key))
                    break
        
    if last_digit == "":
        last_digit = first_digit
    print(f"Number returned {int(first_digit + last_digit)} from row {row}")         
    return int(first_digit + last_digit)

def cut_key_offset(line, n):
    to_be_deleted = len(line) - n
    ret_str = ""
    for i, c in enumerate(line):
        if i == to_be_deleted:
            continue
        ret_str = ret_str + c
        
    return ret_str

if __name__ == '__main__':
    main()