# A program that takes an integer input N,
# reads the names and scores of N students,
# and prints the name(s) of student(s) who have the second lowest score.

N = int(input())                              # Take integer input N (number of students)
marks_list = []                               # Create an empty list to store [name, score] pairs

for _ in range(N):                            # Repeat the loop N times
    name = input()                            # Read the student's name
    score = float(input())                    # Read the student's score and convert to float
    marks_list.append([name, score])          # Append the [name, score] pair to the list

# Extract all scores, remove duplicates using set, then sort them to find the second lowest
scores = sorted(set(score for name, score in marks_list))    

second_lowest = scores[1]                     # The second lowest score will be at index 1 after sorting

# Get names of students who have the second lowest score, sorted alphabetically
names = sorted(name for name, score in marks_list if score == second_lowest)  

# Print each name on a new line
for name in names:
    print(name)
