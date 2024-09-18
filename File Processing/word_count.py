# Accept a filename as input from user
# Open the file
# Parse the file contentrfrom tkinter.filedialog import askopenfilename
from tkinter.filedialog import askopenfilename

def count_file_stats(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        words = [word for line in lines for word in line.split()]
        total_chars = sum(len(word) for word in words)

    return len(lines), len(words), total_chars

def main():
    filename = askopenfilename()
    num_lines, num_words, total_chars = count_file_stats(filename)

    print(f"Total number of lines: {num_lines}")
    print(f"Total number of words: {num_words}")
    print(f"Total number of characters: {total_chars}")

main()