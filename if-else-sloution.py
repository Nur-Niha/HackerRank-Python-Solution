n = int(input().strip())  
# Read an integer from user input, remove any leading/trailing spaces, and convert to int

if n % 2 != 0 and n < 20:
    # If n is odd and less than 20, print "Wierd"
    print("Wierd")
elif n % 2 == 0 and 2 <= n <= 5:
    # If n is even and between 2 and 5 (inclusive), print "Not Wierd"
    print("Not Wierd")
elif n % 2 == 0 and 6 <= n <= 20:
    # If n is even and between 6 and 20 (inclusive), print "Wierd"
    print("Wierd")
else:
    # All other cases (even numbers greater than 20), print "Not Wierd"
    print("Not Wierd")
