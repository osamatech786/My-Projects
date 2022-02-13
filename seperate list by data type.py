'''
Program to seperate the list by data type
7/3/20
'''
choice = input(
    "Enter 1 for custom list & 2 for using sample list : ")

if choice == '2':
    l = [11, 'a', 22, 'b', 33, 'c', 44, 'd']

    list_str = []
    list_int = []

    for i in range(len(l)):
        if isinstance(l[i], int) == True:
            list_int.append(l[i])
        else:
            list_str.append(l[i])
    print("Original list :      ", l)
    print("Integer only list :  ", list_int)
    print("String only list :   ", list_str)

else:
    print("\nEnter elements to create 2 different lists\n&")
    print('Enter "exit" or "ex" to quit input and to show lists')

    list_str = []
    list_fl = []

    while 1 == 1:
        elem = input("element : ")
        if elem == 'exit' or elem == 'ex':
            print("\nList of string : ", list_str)
            print("List of float : ", list_fl)
            break
        else:
            try:
                list_fl.append(float(elem))
            except:
                list_str.append(elem)
