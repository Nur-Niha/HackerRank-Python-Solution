# A program that takes an integer N as input (number of commands),
# then reads N commands and performs list operations accordingly.


N = int(input())                                          # read the number of commands
mylist = []                                               # initialize an empty list

for _ in range(N):
    command = input().split()                             # splits a input line in a list of words and stores in command                 
    if command[0] == "insert":
        mylist.insert(int(command[1]), int(command[2]))   # insert element at a specified position
    elif command[0] == "print":
        print(mylist)                                     # prints the list 
    elif command[0] == "remove":
        mylist.remove(int(command[1]))                    # removes the specified element 
    elif command[0] == "append":
        mylist.append(int(command[1]))                    # add specified element at the end                   
    elif command[0] == "sort":
        mylist.sort()                                     # sorts the list in ascending order
    elif command[0] == "pop":
        mylist.pop()                                      # removes the last item
    elif command[0] == "reverse":
        mylist.reverse()                                  # reverses the list
         
