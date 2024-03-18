# print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.")
# print("2. Knead the dough for 10 minutes.")
# print("3. Add 3g of Salt.")
# print("4. Leave to rise for 2 hours.")
# print("5. Bake at 200 degrees C for 30 minutes.")

# do write this in the program
# print("hi 'joel' how are you")
# or 
# print("hi \"joel\" how are you")

# string concatenation
# print("Hello "+"World")
# output
# "HelloWorld"
# Fix the code below 4

# print("Day 1 - String Manipulation")
# print("String Concatenation is done witsh the "+" sign.")
# print('e.g. print ("Hello" + "world")')
# print("New lines can be created with a backslash and n.")

# print("Hello" + " " + input(" What is your name ") + "!")

# for commenting the shortcut is mac: command + / 
# for uncommenting just press the same key for uncommenting mac: command + / 



def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str
 
s = input("Enter the string you want to reverse")
 
print("The reversed string(using loops) is : ", end="")
print(reverse(s))