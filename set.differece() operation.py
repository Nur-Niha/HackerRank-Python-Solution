# Input: number of English newspaper subscribers
N1 = int(input())
# English subscriber roll numbers
S_eng = set(map(int, input().split()))

# Input: number of French newspaper subscribers
N2 = int(input())
# French subscriber roll numbers
S_fr = set(map(int, input().split()))

# Find students only subscribed to English
only_eng = S_eng.difference(S_fr)

# Output the count
print(len(only_eng))
