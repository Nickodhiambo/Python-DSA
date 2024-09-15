# Accept plaintext message and key value from user
# Loop through the plaintext message, encoding each character
# using the key
# Return the encoded message


def main():
    plaintext = input("Enter the plaintext message to encode: ")
    key = int(input("Enter your encoding key: "))

    plaintextLower = plaintext.lower()
    encoded_message = ''

    for letter in plaintextLower:
        if letter.isalpha():
            encoded_message += chr(ord(letter) + key)
        else:
            raise Exception("Please enter an alphabetic message")
    print(f'Your encrypted message is {encoded_message}')

main()