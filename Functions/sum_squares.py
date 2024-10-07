# Output square of values in a file
# Open the file
# Read contents of file
# Convert contents to int
# sum contents
# Output the result

from square_list import squareNums
from sum_list import sumList
from str_to_num import toNumber
def sumSquares():
    list_of_numbers = [1, 2, 3, 4, 5]
    with open('squares.txt', 'w', newline=None) as f:
        sum_of_squares = squareNums(list_of_numbers)
        print(sum_of_squares, file=f)

    with open('squares.txt', 'r', newline=None) as f:
        contents = list(f.readlines())
        int_contents = toNumber(contents)
        print(f'The sum is {sumList(int_contents)}')
sumSquares()