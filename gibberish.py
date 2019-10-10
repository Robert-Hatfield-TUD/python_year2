#This program will translate an entered word to gibberish when entered
#Author: Robert Hatfield
#Date: 7/10/19
#Compiler: PYcharm

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

   gibberishword=""
   syl=first_syl

   for letter in word:
       if letter in vowels:
           for character in syl:
                if character=="*":
                    gibberishword+=letter
                else:
                    gibberishword+=character
           gibberishword+=letter
           syl=second_syl
       else:
           gibberishword+=letter

   print("Your gibberish word is: \n"+gibberishword)

   contin=input("Do you want to play the gibberish game again? (y/n)\n\n")
   while contin not in "yn":
       contin=input("Please enter only y or n to play again or quit\n\n")

print("Thank you for playing!\n\n\")