from sys import stdin
from re import findall

random = 0

def main():
    building_number = ''
    total_sum = 0 
    input = stdin.readlines()
    numbers = []
    part_nums = []
    gear_numbers = []
    last_row = len(input) - 1
    
    for row, line in enumerate(input):
        start = 0
        end = 0
        for index, character in enumerate(line):
            if character != "\n":
                if character.isnumeric() and building_number == '':
                    start = index
                    building_number = building_number + character
                elif character.isnumeric() and building_number != '':
                    building_number = building_number + character
                elif  building_number.isnumeric():
                    numbers.append(int(building_number))
                    end = index - 1
                    valid = is_number_valid(start, end, row, input, building_number)
                    if valid:
                        total_sum = total_sum + int(building_number)
                        part_nums.append(int(building_number))
                    building_number = ''
            elif building_number.isnumeric():
                numbers.append(int(building_number))
                end = index
                valid = is_number_valid(start, end, row, input, building_number)
                if valid:
                    total_sum = total_sum + int(building_number)
                    part_nums.append(int(building_number))
                building_number = ''
    
    # test_Found_all(numbers_acturally, numbers)
    print(f"Part one answer is {sum(part_nums)}")
    
    
    for row, line in enumerate(input):
        for index, character in enumerate(line):
            if character == "*":
                ratio = gear_ratio(row, index, last_row, input)
                gear_numbers.append(ratio)
                
    print(f"Part two answer is {sum(gear_numbers)}")

# Checks if a found number is valid
# Meaning that there is a special character in a rectangle 
# of size 2 + amount of digits x 3
def is_number_valid(start, end, row, all_rows, num):
    # first row 
    if row == 0:
        if start != 0 and end != len(all_rows[0]) - 1:  
            # print(all_rows[row + 0][start - 1: end + 2])
            for row_offset in range(2):
                for character in all_rows[row + row_offset][start - 1: end + 2]:
                    if row_offset == 0:
                        if not character.isnumeric() and character != '.':
                            return True
                    else:
                        if character != '.' :
                            return True
            return False
        elif start != 0 and end == len(all_rows[0]) - 1:
            # print(all_rows[row][start - 1: end])
            for row_offset in range(2):
                for character in all_rows[row + row_offset][start - 1: end]:
                    if row_offset == 0:
                        if not character.isnumeric() and character != '.':
                            return True
                    else:
                        if character != '.' :
                            return True
            return False
        elif start == 0:
            for row_offset  in range(2):
                for character in all_rows[row + row_offset][start: end + 2]:
                    if row_offset == 0:
                        if not character.isnumeric() and character != '.':
                            return True
                    else:
                        if character != '.' :
                            return True
            return False
    # Last row
    elif row == len(all_rows) - 1:
        if start != 0 and end != len(all_rows[0]) - 1: 
            for row_offset in range(-1, 1):
                for character in all_rows[row + row_offset][start - 1: end + 2]:
                    if row_offset == 0:
                        if not character.isnumeric() and character != '.':
                            return True
                    else:
                        if character != '.' :
                            return True
            return False
        elif start != 0 and end == len(all_rows[0]) - 1:
            for row_offset  in range(-1, 1):
                for character in all_rows[row + row_offset][start - 1: end]:
                    if row_offset == 0:
                        if not character.isnumeric() and character != '.':
                            return True
                    else:
                        if character != '.' :
                            return True
            return False
        elif start == 0:
            for row_offset  in range(-1, 1):
                for character in all_rows[row + row_offset][start: end + 2]:
                    if row_offset == 0:
                        if not character.isnumeric() and character != '.':
                            return True
                    else:
                        if character != '.' :
                            return True
            return False
    # All other rows
    else:
        if start != 0 and end != len(all_rows[0]) - 1: 
            
            for row_offset  in range(-1, 2):
                # print(row_offset)
                # print(all_rows[row + 0][start - 1: end + 2])
                for character in all_rows[row + row_offset][start - 1: end + 2]:
                    if row_offset == 0:
                        if not character.isnumeric() and character != '.':
                            return True
                    else:
                        if character != '.' :
                            return True
            return False
        elif start != 0 and end == len(all_rows[0]) - 1:
            for row_offset  in range(-1, 2):
                for character in all_rows[row + row_offset][start - 1: end]:
                    if row_offset == 0:
                        if not character.isnumeric() and character != '.':
                            return True
                    else:
                        if character != '.' :
                            return True
            return False
        elif start == 0:
            for row_offset  in range(-1, 2):
                for character in all_rows[row + row_offset][start: end + 2]:
                    if row_offset == 0:
                        if not character.isnumeric() and character != '.':
                            return True
                    else:
                        if character != '.' :
                            return True
            return False
    

def test_Found_all(expected, calculated):
    for i, number in enumerate(expected):
        if int(number) == calculated[i]:
            print(f"expected {number}: got {calculated[i]}")
            continue
        else:
            print("Missing a number")
            print(number)
            return False

# PART 2
# A * symbol which is within one square of two seperate numbers is a gear
# we seek the sum of all gear ratios in the enigne
# takes coordinates of * and tries two find two unique numbers
def gear_ratio(row, index, last_row, all_rows):
    gear_numbers = []
    row_offsets = []
    visited = []
    if row == 0:
        row_offsets = [0, 1]
    elif row == last_row:
        row_offsets = [-1, 0]
    else:
        row_offsets = [-1, 0, 1]
        
    for offset in row_offsets:
        visited = []
        if index == 0:
            for i, character in enumerate(all_rows[row + offset][0: 2]):
                if character.isnumeric() and i not in visited:
                    number, visited = find_number(all_rows, row + offset, i)
                    gear_numbers.append(number)
        elif index == len(all_rows[0]) - 2:
            for i, character in enumerate(all_rows[row + offset][index - 1: index + 1]):
                if character.isnumeric() and i not in visited:
                    number, visited = find_number(all_rows, row + offset, (i + index - 1))
                    gear_numbers.append(number)
        else:
            for i, character in enumerate(all_rows[row + offset][index - 1: index + 2]):
                if character.isnumeric() and i not in visited:
                    number, visited = find_number(all_rows, row + offset, (i + index - 1))
                    gear_numbers.append(number)
        

    if len(gear_numbers) >=2:
        n = unique(gear_numbers)
        prod = 0
        yayaya = n.keys()   
        print(f"times {yayaya}")
        if len(yayaya) >= 2:
            prod = 1
            for i in yayaya:
                prod = prod * i
        
        return prod
    return 0 

def find_number(all_rows, row, index):
    # Find numerical to the left
    line = all_rows[row]
    
    dont_check = []
    counter = index 
    left = ''
        
    while line[counter].isnumeric() and counter >= 0:
        left = line[counter] + left    
        counter = counter - 1
    
    if left != '':
        for j in range(counter, index + 1):
            if j <= index + 1 and j >= index - 1:
                dont_check.append(j)
    
    counter2 = index + 1
    right = ''
    
    while line[counter2].isnumeric() and counter2 <= len(line) - 2:
        right = right + line[counter2]    
        counter2 = counter2 + 1
    
    if right != '':
        for j in range(counter, index + 1):
            if j <= index + 1 and j >= index - 1:
                dont_check.append(j)
    
        
    if (left + right) != '':
        return int(left + right), dont_check
    else:
        return 0, dont_check
    
def unique(numbers):
    my_dict = {key: None for key in numbers}
    return my_dict
if __name__ == '__main__':
    main()