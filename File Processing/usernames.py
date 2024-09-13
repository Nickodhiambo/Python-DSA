from tkinter.filedialog import askopenfilename, asksaveasfilename

def main():
    infileName = askopenfilename()
    outfileName = asksaveasfilename()

    infile = open(infileName, 'r')
    outfile = open(outfileName, 'w')

    for line in infile:
        first, last = line.split()
        uname = (first[0]+last[:7]).lower()
        print(uname, file=outfile)

    infile.close()
    outfile.close()
    print(f'The username has been saved to {outfile}')
main()