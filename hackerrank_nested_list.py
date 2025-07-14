N = int(input())
marks_list = []    
for _ in range(N):
    name = input()
    score = float(input())
    marks_list.append([name, score])


scores = sorted(set(score for name, score in marks_list))
second_lowest = scores[1]

names = sorted((name for name, score in marks_list if score == second_lowest))

for name in names :
    print(name)