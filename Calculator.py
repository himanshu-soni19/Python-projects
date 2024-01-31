First_number = float(input("Enter the first number: "))
Second_number = float(input("Enter the second number: "))
add = First_number + Second_number
sub = First_number - Second_number
multi = First_number * Second_number

# To avoid an error, since a number can not be divided by zero.
if Second_number != 0 :
    div = First_number / Second_number
else: div = "Number can not be divide by zero."

user_choice = input("Enter the variable you want to print (add, sub, multi, div): ")
if user_choice == "add" :
    print(add)
elif user_choice == "sub" :
    print(sub)
elif user_choice == "multi" :
    print(multi)
elif user_choice == "div" :
    print(div)
