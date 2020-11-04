# https://projecteuler.net/problem=22

names = open("data/p022_names.txt", "r").read().split(",")
names = [name.strip('"') for name in names]
names.sort()


def get_letter_value(letter):
    return ord(letter) - 64  # ASCII value for capital A is 65, so A = 1


total_name_score = 0

for i, name in enumerate(names):
    name_score = 0
    for letter in name:
        name_score += get_letter_value(letter)
    name_score *= i + 1
    total_name_score += name_score

print(total_name_score)
