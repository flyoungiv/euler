# https://projecteuler.net/problem=1

def three_or_five_multiple(until):
    for num in range(1, until):
        if num % 3 == 0 or num % 5 == 0:
            yield num

print( sum(three_or_five_multiple(1000)) )
