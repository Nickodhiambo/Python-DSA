def toNumber(strList):
    return [int(item) for item in strList]


def test():
    list_of_number_str = ['1', '2', '3', '4', '5']
    list_of_int_str = toNumber(list_of_number_str)
    print(sum(list_of_int_str))

test()