# Accept the encoded message
# Accept encoding key
# Use encoding key to decode the message
# Output the decoded message


def main():
    encoded_message: str = input("Enter the encoded text: ")
    key: int = int(input("Enter the encoding key: "))

    decoded_message = ''

    for letter in encoded_message:
        if letter.isalpha():
            decoded_message += chr(ord(letter) - key)
        else:
            raise Exception('Incorrect message or key')
    print(f'The message is: {decoded_message}')

main()