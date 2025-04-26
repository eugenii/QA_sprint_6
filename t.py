import sys

data = [i.strip() for i in sys.stdin.readlines()]
# print(data)
result = set()

for line in data:
    line = line.split()
    last_of_first = int(line[0]) % 10
    for num in line:
        sum_of_three = sum(int(i) for i in num[:3])
        # sum_of_three = int(num[0]) + int(num[1]) + int(num[2])
        if int(num[0]) >= last_of_first and sum_of_three % 2 != int(line[0]) % 2:
            result.add(num)
    print(". ".join(result))
    result.clear()

