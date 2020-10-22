#Implement function `ToLowerCase()` that has a string parameter str, and returns the same string in lowercase.
#Steps
# Have an input s that will take in the sentence
# Have a function called ToLowerCase.
# Have a variable called lower case that will change the sentense to lowercase

#Sudo code
# s = Enter a sentense: 
# function ToLowerCase:
#	lower case = lower_case(s)

# Real code

s = input("Enter your sentense:  ")

def ToLowerCase():
    lower_case = s.lower()
    print(lower_case)
ToLowerCase()