# a = input("Enter First Number : ")
# b = input("Enter Second Number : ")
# print("The Sum Of Two Numbers is : ",int(a)+int(b))


a = input("Enter First Number : ")
b = input("Enter Second Number : ")
choice = input("Enter any operator to perform any operation : ")
if choice == '+':
    print("a + b = ",int(a)+int(b))
if choice == '-':
    print("a - b = ",int(a)-int(b))
if choice == '*':
    print("a * b = ",int(a)*int(b))
if choice == '/':
    print("b / a = ",int(b)/int(a))
if choice == '%':
    print("a % b = ",int(a)%int(b))
else:
    print("INVALID OPERATOR")
