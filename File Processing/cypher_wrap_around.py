# Accept text as input from user
# Convert to lowercase
# Initialize an empty encoded message string
# Initialize an alphabet string to check against input characters
# Loop through the input string
  #Check if a chr is alphabetic
    #check its position in the alphabet string
    #create a new circular index which shifts the current index using the key
    # find the letter value for the new index, add it to encoded string
  # else if chr is a space, add it directly to encoded str
  # else throw an error
# print the encoded message
  
def main():
    message = input("Enter the text to encode: ")
    key = int(input("Enter the encoding key: "))

    messageLowerCase = message.lower()
    encoded_message = ''
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for letter in messageLowerCase:
        if letter.isalpha():
            index = alphabet.index(letter)
            new_index = (index + key) % len(alphabet)
            encoded_message += alphabet[new_index]
        
        elif letter == " ":
            encoded_message += " "

        else:
            raise Exception("Invalid input message or key")
        
    print(f'Your encoded message is {encoded_message}')

main()
