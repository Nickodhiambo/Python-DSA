def main():
    score = input("Enter a score between 0 and 100: ")

    grades = ['A', 'B', 'C', 'D', 'F']
    score_ranges = [90, 80, 70, 60, 0]

    for i in range(len(score_ranges)):
        if int(score) >= score_ranges[i]:
            print(f'Your grade is {grades[i]}')
            break

2
main()