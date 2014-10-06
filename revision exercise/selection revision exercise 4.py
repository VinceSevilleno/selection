#Vince Sevilleno
#3/10/2014
#Selection Revision Execise 4

number1=int(input("Please enter the first number:"))
print()
number2=int(input("Please enter the second number:"))
print()
number3=int(input("Please enter the third number:"))
print()
if number1>number2 and number3:
    print("{0} is larger than {1} and {2}.".format(number1,number2,number3))
elif number2>number1 and number3:
    print("{0} is larger than {1} and {2}.".format(number2,number1,number3))
elif number3>number1 and number2:
    print("{0} is larger than {1} and {2}.".format(number3,number1,number2))
elif number1==number2 and number3:
    print(" All three numbers are the same, so the largest number is {0}.".format(number1))
