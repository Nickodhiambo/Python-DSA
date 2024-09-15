# Accept full name from user
# split full name into individual names
# Loop through each individual name
# Loop through each letter in each name, assigning a number to it
# Sum up the value of each letter
# Output the sum

def main():
    full_name = input(" Enter your full name: ")
    lowerFullName = full_name.lower()

    separatedNames = lowerFullName.split()

    total_value = 0

    for name in separatedNames:
        for letter in name:
            if letter.isalpha():
                total_value += ord(letter) - ord('a') + 1
            else:
                raise Exception('Input name must be an alphabetical string')
    print(f'The numerological value of your name is {total_value}')

main()