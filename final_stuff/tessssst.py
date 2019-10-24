def iskap(num):
    num=int(num)
    num1=num**2
    num1=str(num1)
    numi=list(num1)

    num2=numi[:len(numi)//2]
    num3=numi[len(numi)//2:]

    num2="".join(num2)
    num3="".join(num3)

    num2=int(num2)
    num3=int(num3)

    num4=0
    num4=int(num4)
    num4=num2+num3

    if num == num4:
        print("Your number is good", num)


    else:
        print("Your number is bad")

    print("\n")

num=input("Please enter a number for KAPS: ")
num=str(num)
i=10
i=int(i)
iskap(num)

print("Here are the numbers up to yours that are kap\n")
num=int(num)

while i < num:
    numa = i * i
    numk= str(numa)
    numu = list(numk)
    numb = numu[:len(numu) // 2]
    numc = numu[len(numu) // 2:]

    numb = "".join(numb)
    numc = "".join(numc)

    numb = int(numb)
    numc = int(numc)

    numd = 0
    numd = int(numd)
    numd = numb + numc

    if numd == i:
        print(numd)

    i=i+1