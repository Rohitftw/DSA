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


