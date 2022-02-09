# Uses python3
def binary_search(key, query, low, high):
    if high < low:
      return -1
    mid = low + (high-low)//2
    if key == query[mid]:
      if mid-1 < 0:
        return mid
      if query[mid-1] != key:
        return mid
      return binary_search(key, query, low, mid-1)
    elif key < query[mid]:
      return binary_search(key, query, low, mid-1)
    else:
      return binary_search(key, query, mid+1, high)
    return -1

n = int(input())
a = list(map(int, input().split()))
k = int(input())
b = list(map(int, input().split()))

result = []

for x in b:
  result.append(binary_search(x, a, 0, len(a)-1))

print(*result)