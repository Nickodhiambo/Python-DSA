# Accept a sentence from user
# split the sentence based on spaces and add it to a list
# Find the length of the list
# Print the length


def main():
    sentence = input("Enter a sentence: ")
    print(f'The total number of words is {len(sentence.split(' '))}')

main()