vowels="aeiouAEIOU"
cons="BCDFGHJKLMNPQRSTVXZWYbcdfghjklmnpqrstvxzwy"

def countey(word):
    V=0
    C=0
    for letter in word:
        if letter in vowels:
            V=1+V

        if letter in cons:
            C=1+C

    print("Vowels = ", V)
    print("\n\nConsonants = ", C)

word=input("Please enter a word: \n\n")

countey(word)

quit(0)