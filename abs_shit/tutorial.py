def E(mass):
    mass=float(mass)
    c=89875243264
    c=float(c)
    ES=float(0)
    ES = mass*c
    ES=float(ES)

    return(ES)

mass=input("Please enter a mass amount: ")

Eset=E(mass)
Eset=float(Eset)

print("The value of E is: ", Eset)

quit(0)