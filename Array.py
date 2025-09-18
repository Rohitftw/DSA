arr = list(map(int, input("Enter elements: ").split()))
# find the largest element in the array
# largest_number = arr[0]
#
# for i in range(len(arr)):
#     if arr[i] > max:
#         largest_number = arr[i]
# print(largest_number)


# Second-largest number in an array
# largest_number = arr[0]
# slargest = float('-inf')
# for i in range(len(arr)):
#     if arr[i] > largest_number:
#         slargest = largest_number
#         largest_number = arr[i]
#     elif arr[i] < largest_number and arr[i] > slargest:
#         slargest = arr[i]
# print(largest_number)
# print(slargest)


# Second smallest
# smallest = float('inf')
# second_smallest = float('inf')
# for i in range(len(arr)):
#     if arr[i] < smallest:
#         second_smallest = smallest
#         smallest = arr[i]
#     elif arr[i] != second_smallest and arr[i] < second_smallest:
#         second_smallest = arr[i]
# print(second_smallest)
# print(smallest)

# Sorted array
# def sorted_array(arr):
#     for i in range(1, len(arr)):
#         if arr[i] < arr[i-1]:
#             return False
#     return True

# Duplicates
# def duplicate(arr):
#     i = 0
#     for j in range(1, len(arr)):
#         if arr[i] != arr[j]:
#             arr[i+1] = arr[j]
#             i += 1
#     return arr[:i+1]
# /arr lecture 1 end/

# Left rotate array by 1
# temp = arr[0]
# for i in range(1, len(arr)):
#     arr[i-1] = arr[i]
# arr[-1] = temp

# Left rotate an array by D places
# brute
#D = int(input("Enter the value of D"))
#
# temp = arr[:D]
# print(temp)
# for i in range(len(arr) - D):
#     arr[i] = arr[i+D]
# for i in range(D):
#     arr[len(arr) - D + i] = temp[i]
# print(arr)

# optimal
# arr[:D] = arr[:D][::-1]
# arr[D:] = arr[D:][::-1]
# arr = arr[::-1]
# print(arr)

# Right rotation by D
# arr[len(arr) - D:] = arr[len(arr) - D:][::-1]
# arr[:len(arr) - D] = arr[:len(arr) - D][::-1]
# arr[:] = arr[::-1]


# Move Zeros to end
# j = 0
# for i in range(len(arr)):
#     if arr[i] != 0:
#         arr[i], arr[j] = arr[j], arr[i]
#         j += 1
# print(arr)

# Linear Search
# n = int(input("Enter the number"))
# for i in range(len(arr)):
#     if n == arr[i]:
#         print(i)

# union of two sorted arr
# def union(arr, arr2):
#     i, j = 0, 0
#     union_array = []
#
#     while i < len(arr) and j < len(arr2):
#         if arr[i] <= arr2[j]:
#             if len(union_array) == 0 or union_array[-1] != arr[i]:
#                 union_array.append(arr[i])
#             i += 1
#         else:
#             if len(union_array) == 0 or union_array[-1] != arr2[j]:
#                 union_array.append(arr2[j])
#             j += 1
#
#     while i < len(arr):  # remaining arr1
#         if len(union_array) == 0 or union_array[-1] != arr[i]:
#             union_array.append(arr[i])
#         i += 1
#
#     while j < len(arr2):  # remaining arr2
#         if len(union_array) == 0 or union_array[-1] != arr2[j]:
#             union_array.append(arr2[j])
#         j += 1
#
#     return union_array
#
#
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# arr2 = [2, 3, 4, 4, 5, 11, 12]
#
# print(union(arr, arr2))


# Intersection of two sorted array

# def intersection(arr1, arr2):
# #     i, j = 0, 0
# #     result = []
# #     while i < len(arr1) and j < len(arr2):
# #         if arr1[i] == arr2[j]:
# #             result.append(arr1[i])
# #             i += 1
# #             j += 1
# #         elif arr1[i] > arr2[j]:
# #             j += 1
# #         elif arr1[i] < arr2[j]:
# #             i += 1
# #     return result
# # arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # arr2 = [2, 3, 4, 4, 5, 11, 12]
# # print(intersection(arr1, arr2))


# Find missing number in an array
N = int(input("Enter the number"))
def missingNumber(arr, N):
    xor1 = 0
    xor2 = 0

    for i in range(N - 1):
        xor2 = xor2 ^ a[i]  # XOR of array elements
        xor1 = xor1 ^ (i + 1)  # XOR up to [1...N-1]

    xor1 = xor1 ^ N  # XOR up to [1...N]

    return xor1 ^ xor2

def findMaxConsecutiveOnes(arr):
    count = 0
    maximum = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            count += 1
        else:
            count = 0
        maximum = max(maximum, count)
    return maximum

