# # input size
# n = int(input("Enter size of array: "))
#
# # array input
# arr = list(map(int, input("Enter elements: ").split()))
#
# # precompute frequency using dict
# hash_map = {}
# for num in arr:
#     hash_map[num] = hash_map.get(num, 0) + 1
#
# # number of queries
# q = int(input("Enter number of queries: "))
#
# # queries
# for _ in range(q):
#     number = int(input())
#     print(hash_map.get(number, 0))

n = input("Enter string")
hash_map = {}
for i in n:
    hash_map[ord(i)-ord("a")] = hash_map.get(ord(i)-ord("a"), 0) + 1
# queries
q = int(input("Enter number of queries: "))
for i in range(q):
    character = input("Enter character: ")
    print(hash_map[ord(character) - ord("a")])

