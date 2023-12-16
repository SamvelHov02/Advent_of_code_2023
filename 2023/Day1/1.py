from sys import stdin
from re import search

def main():
    total_sum = 0 
    while True:
        line = stdin.readline()
        if line == "":
            break
        else:
            number_in_row = parse_string(line)
            total_sum = total_sum + number_in_row
    
    print(total_sum)

def parse_string(line):
    first_digit = ""
    last_digit = ""
    iter_str = line[:4]
    spelled_digits = {"one": 1, "two": 2, "three":3, "four":4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    counter = 0
    for character in line[4:]:
        iter_str = iter_str + character
        
        if counter == 0:
            for i, c in enumerate(iter_str):
                if c.isnumeric():
                    for key in spelled_digits.keys():
                        if search(key, iter_str[:i]) and first_digit == "":
                            first_digit = str(spelled_digits[key])
                            break
                        elif search(key, iter_str[:i]):
                            last_digit = str(spelled_digits[key])
                            break
                   
                    if first_digit == "":
                        first_digit = c
                    else:
                        last_digit = c
                    iter_str == "----"
                    break
                            
            iter_str == "----"
            counter = 1
            continue
                    
        for key in spelled_digits.keys():
            if search(key, iter_str): 
                iter_str = "-----"
                if first_digit == "":
                    first_digit = str(spelled_digits[key])
                    break
                last_digit = str(spelled_digits[key])
                
        iter_str = iter_str[1:]
        
        try:
            int(character)
            if first_digit == "":   
                first_digit = character
                
            last_digit = character
            iter_str = "----"
        except:
            continue
        
    if last_digit == "":
        last_digit = first_digit
    
    print(f"Send out {int(first_digit + last_digit)}")
    
    return int(first_digit + last_digit)

if __name__ == "__main__":
    main()