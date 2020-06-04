# Write a function is_even that will return true if the passed-in number is even.
# YOUR CODE HERE

def is_even(input_number):
    if int(input_number) % 2 == 0:
        print("True")
    else:
        print("False")

# Read a number from the keyboard


num = input("Enter a number: ")
is_even(num)


# Print out "Even11`11!" if the number is even. Otherwise print "Odd"
# YOUR CODE HERE

def even_checker(input_number):
    if int(input_number) % 2 == 0:
        print("Even11`11!")
    else:
        print("Odd")


num = input("Enter another number: ")
even_checker(num)
