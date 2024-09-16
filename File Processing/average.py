# Accept a sentence from user
# Split the sentence into words
# Count the number of split words
# Count the number of letters in each word and sum them
# Divide letter count with word count
# Output the results


def main():
    sentence = input("Enter a sentence: ")

    words = sentence.split()
    word_count = len(words)

    total_letter_count = 0
    for word in words:
        letter_count = len(word)
        total_letter_count += letter_count
    
    average_word_count = total_letter_count // word_count
    print(f"The average word length is {average_word_count}")

main()