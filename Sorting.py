# Selection Sort TC: O(n^2)
arr = list(map(int, input("Enter elements: ").split()))
# for i in range(len(arr) - 1):
#     minimum = i
#     for j in range(i + 1, len(arr)): # you can  use range from i but using i + 1 reduces 4 steps
#         if arr[j] < arr[minimum]:
#             minimum = j
#     arr[i], arr[minimum] = arr[minimum], arr[i]
#
# print(arr)

# Bubble Sort TC: Best and avg = O(n^2) but best can be O(n)
# for i in range(len(arr)):
#     swap = 0
#     for j in range(len(arr)-i - 1):
#         if arr[j] > arr[j+1]:
#             arr[j], arr[j+1] = arr[j+1], arr[j]
#             swap = 1
#     if swap == 0:
#         break
# print(arr)


# Insertion Sort TC: worst and avg O(n^2) and best O(n^2)
# for i in range(len(arr)):
#     j = i
#     while j < 0 and arr[j - 1] > arr[j]:
#         arr[j - 1], arr[j] = arr[j], arr[j - 1]
# print(arr)


# Merge Sort TC: O(nlogn)
def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    i = j = 0
    temp = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            temp.append(left[i])
            i += 1
        else:
            temp.append(right[j])
            j += 1
    temp.extend(left[i:])
    temp.extend(right[j:])

    return temp


print(mergesort(arr))