# Accept a phrase from user
# Split phrase into substrings
# Loop through each substring, extracting the first letter
# Store first letters in a variable as one
# capitalize the acryonym
# Output the acronym

def main():
    phrase = input("Enter a phrase you want an acronym for: ")

    substrings = phrase.split()
    acroynm_string = ''

    for substring in substrings:
        first_letter = substring[0]
        acroynm_string += first_letter
    print(f'The acronym for "{phrase}" is {acroynm_string.upper()}')

main()

