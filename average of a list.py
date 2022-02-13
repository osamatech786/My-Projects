'''
Program to calculate average using list concept
7/3/20
'''
listt = []

print("Enter numbers to calculate average\n&")
print('Enter "exit" or "ex" to quit input and to calculate average')

while 1 == 1:
    num = input("number : ")
    if num == 'exit' or num == 'ex':
        print("List : ", listt)
        print("Average of list is : ", sum(listt)/len(listt))
        break
    else:
        listt.append(float(num))
