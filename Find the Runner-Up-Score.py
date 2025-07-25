if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

arr = set(arr)
sorted_array = sorted(arr, reverse =True)
if len(sorted_array) >= 2:
     print(sorted_array[1])
else:
     pass
