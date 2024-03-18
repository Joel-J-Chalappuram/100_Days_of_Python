# Instructions
# Write a program that calculates and outputs the number of
# characters in any name. The automated tests will try out lots of
# different names as the input. Your code should work for any name
# Your code should only output the number, no other text is needed.
# Hint
# Remember, you can use len ( ) around any piece of text to
# calculate the number of characters.
str = input("Enter the text you want to find the number of string = ")
noofletters = len(str)
print("The string ",str,"contains ",noofletters,"letters")