#This program is to translate a text file in the same location as the py file
#Author: Robert Hatfield
#Date: 10/10/2019
#Compiler: PYcharm

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ*"
vowels = "aeiouAEIOU"
nfile=""

def numcheck(word): #This function checks the input for any numbers that could have been entered
  for letter in word:
     if letter not in alphabet:
        return False
  return True

def typecheck(word): #This function prints a message when a number is found in a word
  while not numcheck(word):
     word = input("Please don't use numbers or symbols: ")
  return word

def readf(filename): #This function is used to find the file and open it using a with command so there si no need for the close command later
    while True:
        try:
            with open(filename, "r") as file_obj:
                text=file_obj.read()
        except FileNotFoundError:
            filename=input("Please enter an existing file: ")
        else:
            return text

def newfile(oldfile): #This function is used to find the end of the string in the file and set "fullstop" as its index
    fullstop = -(oldfile[::-1].find(".") + 1)  #Find the end of the text in the file
    return oldfile[:fullstop]

print("This program is a gibberish game that allows you to insert a syllable of your choice before a vowel.\n"
      "There is also a wildcard option that allows you to put a vowel character  before your syllable.\n"
      "This replaces the asterix with the vowel found in the text file. (IF YOU PRESS ENTER FOR SYLLABLES THE TEXT WILL NOT CHANGE)\n\n")

contin="y"

while contin=="y":

   first_syl=input("Please enter a syllable to go before the first vowel and use the a WILDCARD ( * ) if you want: \n")
   first_syl=typecheck(first_syl)

   second_syl=input("Please enter a syllable to go before the second vowel and use the a WILDCARD ( * ) if you want: \n")
   second_syl=typecheck(second_syl)

   filename=input("Please enter the name of the file in the same directory as the program: ")

   text=readf(filename)

   text1=""
   syl=first_syl
   lastletter= True

   for letter in text:
       if lastletter and letter in vowels:
           for character in syl:
               if character=="*":
                   text1+=letter

               else:
                   text1+=character

           text1+=letter
           syl=second_syl

           lastletter=False

       else:
           text1+=letter
           lastletter=True

           if letter==" ":
               syl=first_syl

   makefilen=newfile(filename)
   makefilen="inputFileGibberish.txt"

   with open(makefilen, "w") as nfile:
       nfile.write(text1)

   print("The text in your file reads: \n\n"+text1)
   print("\nnew file is called: \n\n"+makefilen)

   contin = input("\nPlay again? (y/n) \n\n")
   while contin not in "yn":
       contin = input("Please enter y to continue or n to quit: ")

print("\nThanks for playing!")