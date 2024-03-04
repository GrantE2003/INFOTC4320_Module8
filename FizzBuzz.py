# I have done this project before... so while this code is original, I only
# have this single branch since it only took me one attempt.

#For Loop
for i in range(1,101):
    # Check if number "i" is a multiple of 3 and 5
    if ((i % 3) == 0 and (i % 5) == 0):
        # Print FizzBuzz if "i" is a multiple of 3 and 5
        print("FizzBuzz")
    # Check to see if "i" is multiple of 3
    elif ((i % 3) == 0):
        # Print Fizz if "i" is a multiple of 3
        print("Fizz")
    # Check to see if "i" is a multiple of 5
    elif ((i % 5) == 0):
        # Print Buzz if "i" is a multiple of 5
        print("Buzz")
    # Check if number "i" is not a multiple of 3 or 5
    else :
        # Print "i" if it is not a multiple of 3 or 5
        print(i)