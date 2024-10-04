def sumN(n):
    _sum = 0
    for num in range(n + 1):
        _sum += num
    return _sum


def sumNCubes(n):
    total = 0
    for num in range(n + 1):
        total += num ** 3
    return total

def test():
    n = int(input('Enter the count of the first n natural numbers: '))
    print(f'The sum of the first {n} natural numbers is {sumN(n)}')
    print(f'The sum of cubes of the first {n} natural numbers is {sumNCubes(n)}')

test()