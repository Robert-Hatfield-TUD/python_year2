alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ*"
vowels="aeiouAEIOU"

def numcheck(word):
	for letter in word:
		if letter not in alphabet:
			return False
	return True

def typecheck(word):
	while not numcheck(word):
		word = input("Invalid input, please try again: ")
	return word


print("This program is a gibberish game that allows you to insert a syllable of your choice before a vowel. There is also a wildcard option that allows you to put the * character  before your syllable. This replaces the asterix with the vowel found in the word.\n\n")

contin="y"

while contin=="y":

    first_syl=input("Please enter a syllable to go before the first vowel and use the a WILDCARD ( * ) if you want: \n")
    first_syl=typecheck(first_syl)

    second_syl=input("Please enter a syllable to go before the second vowel and use the a WILDCARD ( * ) if you want: \n")
    second_syl=typecheck(second_syl)

    word=input("Please enter the word you want translated: \n")
    word=typecheck(word)

