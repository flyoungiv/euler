# https://projecteuler.net/problem=21

def is_proper_divisor(divisor, n):
    if divisor >= n:
        return False
    if n % divisor == 0:
        return True
    return False


def sum_proper_divisors(n):
    sum = 0

    for x in range(1, n + 1):
        if is_proper_divisor(x, n):
            sum += x

    return sum


def divisor_sums_in_range(n):
    number_pairs = []

    for x in range(1, n + 1):
        number_pairs.append((x, sum_proper_divisors(x)))

    return number_pairs


def is_amicable_pair(p1, p2):
    if p1[0] == p2[1] and p1[1] == p2[0]:
        return True
    return False

# would be better if this function removed items from the list as they were checked


def sum_amicable_pairs(n):
    amicable_pairs = 0

    divisor_sums = divisor_sums_in_range(n)
    for x in divisor_sums:
        for y in divisor_sums:
            if x == y:
                continue
            if is_amicable_pair(x, y):
                amicable_pairs += x[0]

    return amicable_pairs


print(sum_amicable_pairs(10000))
