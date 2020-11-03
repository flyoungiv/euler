raw_triangle = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''


def create_triangle(string):
    triangle = []

    lines = string.split("\n")
    for line in lines:
        triangle.append([int(number) for number in line.split(" ")])

    return triangle


def sum_max_adjacent_numbers(triangle):
    total = 0
    pos = 0

    for line in triangle:
        if len(line) == 1:
            total += line[0]
            continue
        adjacent_numbers = [line[pos], line[pos + 1]]
        bigger_number = max(adjacent_numbers)
        total += bigger_number
        pos += adjacent_numbers.index(bigger_number)
    
    print(total)
    return total

triangle = create_triangle(raw_triangle)
sum_max_adjacent_numbers(triangle)

print(sum([75,
95,
47,
87,
82,
75,
73,
28,
83,
47,
43,
73,
91,
67,
98]))