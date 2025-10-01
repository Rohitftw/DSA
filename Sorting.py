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

# Bubble Sort TC: worst and avg = O(n^2) but best can be O(n)
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
# def insertion_sort(arr):
#     n = len(arr)
#     for i in range(n):   # i = 0 to n-1
#         j = i
#         while j > 0 and arr[j - 1] > arr[j]:
#             # swap arr[j-1] and arr[j]
#             arr[j - 1], arr[j] = arr[j], arr[j - 1]
#             j -= 1
#     return arr


# Merge Sort TC: O(nlogn)
# def mergesort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left = mergesort(arr[:mid])
#     right = mergesort(arr[mid:])
#     return merge(left, right)
#
#
# def merge(left, right):
#     i = j = 0
#     temp = []
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             temp.append(left[i])
#             i += 1
#         else:
#             temp.append(right[j])
#             j += 1
#     temp.extend(left[i:])
#     temp.extend(right[j:])
#
#     return temp
#
#
# print(mergesort(arr))

# Quick Sort
# def partition(arr, low, high):
#     pivot = arr[low]   # pehla element ko pivot lete hain
#     i = low
#     j = high
#
#     while i < j:
#         # left side se pivot se chhote ya equal elements ko skip karo
#         while i <= high - 1 and arr[i] <= pivot:
#             i += 1
#         # right side se pivot se bade elements ko skip karo
#         while j >= low + 1 and arr[j] > pivot:
#             j -= 1
#         # agar i aur j cross nahi hue toh swap
#         if i < j:
#             arr[i], arr[j] = arr[j], arr[i]
#
#     # pivot ko sahi jagah par daalna
#     arr[low], arr[j] = arr[j], arr[low]
#     return j
#
#
# def quicksort(arr, low, high):
#     if low < high:
#         pIndex = partition(arr, low, high)
#         quicksort(arr, low, pIndex - 1)   # left part
#         quicksort(arr, pIndex + 1, high) # right part
#
#
# print("Original:", arr)
# quicksort(arr, 0, len(arr) - 1)
# print("Sorted:", arr)
