# Accept a filename as input from user
# Open the file
# Parse the file content, dumping the contexts into a variable
# Count the number of sentences
# Count the number of words
# Count the number of chars

from tkinter.filedialog import askopenfilename

def main():
    filename = askopenfilename()
    f = open (filename, 'r')
    number_of_lines = len(f.readlines())
    f_text = f.read()
    words = (f_text.split(' '))
    number_of_words = len(words)

    total_chars = 0
    for word in words:
        word_length = len(word)
        total_chars += word_length

    print(f'The total number of lines is {number_of_lines}')
    print(f'The total number of words is {number_of_words}')
    print(f'The total number of chars is {total_chars}')
          
    f.close()
    
main()