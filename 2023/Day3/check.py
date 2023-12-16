mine = []
expected = []
with open('mine.txt', 'r') as my_file:
    while True:
        num = my_file.readline()
        if num != "":
            mine.append(num)
        else:
            break

with open('actual.txt', 'r') as actual:
    while True:
        num = actual.readline()
        if num != "":
            expected.append(num)
        else:
            break
        
        
for i, number in enumerate(expected):
    if number != mine[i]:
        print(i)
        break