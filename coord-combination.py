import sys

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

if __name__ == "__main__":
    print("Please input a list of numbers you would like combined:\n")
    i_list = list(input().split(" "))
    i_list = [int(x) for x in i_list]
    print(f'The list of numbers entered: {i_list}')

    list_len = len(i_list)
    returned_list = []
    permStr = 'returned_list = [['
    #build sub-list first
    for i in range(list_len):
        permStr = permStr + alpha[i] + ','
    permStr = permStr[:-1]
    #build the list comprehension
    permStr += '] '
    for i in range(list_len):
        permStr = permStr + 'for ' + alpha[i] + ' in' + ' range(' + str(i_list[i]) + '+1) '
    permStr = permStr[:-1]
    permStr += ']'
    exec(permStr)
    print(returned_list)