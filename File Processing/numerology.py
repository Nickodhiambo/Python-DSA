# Ask for name input from user
# 
# Loop through the name, assigning each letter a corresponding number
# Sum up the numbers that make up a letter
# Output the sum

def main():
    print("This program generates numerological number of a name")
    name = input("Enter a single name : ")
    lowerName = name.lower()

    total_value = 0

    for letter in lowerName:
        if letter.isalpha():
            total_value += ord(letter) - ord('a') + 1
        else:
            raise Exception("Program only accepts alphabetic names")
    print(f"The numerological value of {name} is {total_value}")
    

main()

