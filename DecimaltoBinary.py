# decimal number will be converted to binary and then further down the line binary will be converted to decimal again

#Author: Robert Hatfield
#Date: 26/09/19
#Compiler: PYcharm

number = int(input("Enter any decimal number: "))

if number<0:
    print("Number is negative")

    quit

else:
    # print equivalent binary number
    print("Equivalent Binary Number: ", bin(number))

binary=bin(number)

decim=int(binary, 2)
print(binary," in decimal is ", decim)

