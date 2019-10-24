i=0
lista=[0,0,0,0,0]
listb=[0,0,0,0,0]

while i<5:
    lista[i]=input("Please enter a number into the list: ")
    i=i+1

i=0
while i<5:

    a=0
    b=0
    c=0

    if i == 0:
        a=lista[i]
        b=lista[i+1]
        a=int(a)
        b=int(b)
        listb[i]=a+b

    if i == 4:
        a=lista[i]
        c=lista[i-1]
        a = int(a)
        c = int(c)
        listb[i]=a+c

    if i > 0 and i < 4:

        a=lista[i-1]
        b=lista[i]
        c=lista[i+1]
        a = int(a)
        b = int(b)
        c=int(c)
        listb[i]=a+b+c

    i=i+1

print(lista)
print(listb)