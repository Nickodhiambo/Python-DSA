# Accept date string in the format mm/dd/yyyy from user
# Separate month, date and year strings
# Convert month string to an int, use it to do a month lookup
# Create a new data string in the form month day, year
# Output the new format

def main():
    dateStr = input("Enter date in the format mm/dd/yyyy: ")

    months = [
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
        'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'
    ]

    monthStr, dayStr, YearStr = dateStr.split('/')
    month = months[int(monthStr) - 1]

    print("{} {}, {}".format(month, dayStr, YearStr))

main()