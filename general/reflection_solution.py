#Given a string, write a python function to check if the reverse of the string is #the same as string.


#Steps
       #Have an input for receiving the sting
       #Have a function
       #Have a variable reverse which will reverse the string
       #Have an if statement to check if the variable reverse is the same as the input.


#Sudo Code

#input Enter any word:  
#def reverse_function():
	#reverse = reverse input
	#if reverse is the same as input:
		#Yay
	#else:
		#No

## Real code
input1 = input("Enter any word:  ")
def reverse_word():
    reverse = input1[::-1]

    if reverse == input1:
        print("Yes")
    else:
        print("No")
reverse_word()