#Vince Sevilleno
#3/10/2014
#Selection Revision Execise 4

number1=int(input("Please enter the first number:"))
print()
number2=int(input("Please enter the second number:"))
print()
if number1>number2:
    print("{0} is larger than {1}".format(number1,number2))
elif number2>number1:
    print("{0} is larger than {1}.".format(number2,number1,))
elif number1==number2:
    print(" Both numbers are the same so the largest number is {0}".format(number1))

