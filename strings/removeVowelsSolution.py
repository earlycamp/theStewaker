#Given a string S, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.
      
#Steps
# Have an input s that will take in the sentence
# Have a function called remove_vowels_function.
# Have a variable called remove_vowels that will remove the vowels

#Sudo code
# s = Enter a word: 
# function remove_vowels_function:
#	remove vowels = remove_vowels

# Real code
s = input("Enter a sentense:  ")
def remove_vowels_function():
    print(s.translate({ord(i): None for i in 'aeiou'}))
remove_vowels_function()