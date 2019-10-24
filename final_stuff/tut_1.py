num=input("Please enter a number to have all kapreker numbers up to it printed off: ")

print("\n\n")

list=[ 10, 45, 55, 99, 100, 297, 703, 999, 1000, 2223, 2728, 4879, 4950, 5050, 5292, 7272, 7777, 9999, 17344, 22222, 38962, 77778, 82656, 95121, 99999]

num=int(num)
i=0

while list[i] <= num:
    print(list[i])
    i=i+1

