# for i in range(5):
#     for j in range(5):
#         print("*",end="")
#     print("")
# *****
# *****
# *****
# ***** Q1


# for i in range(5):
#     for j in range(i+1):
#         print("*",end=" ")
#     print("")
# *
# * *
# * * *
# * * * *
# * * * * * Q2

# for i in range(6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print("")
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5 Q3

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print("")
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5  Q4

# for i in range(5):
#     for j in range(5-i):
#         print("*",end=' ')
#     print()
# * * * * *
# * * * *
# * * *
# * *
# * Q5

# for i in range(6):
#     for j in range(1,6-i):
#         print(j,end=" ")
#     print()
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

# for i in range(5):
#     for j in range(5-i):
#         print(" ",end=" ")
#     #star
#     for j in range(1+2*i):
#         print("*",end=" ")
#     for j in range(5- i):
#         print(" ",end=" ")
#
#     print()
#
#           *
#         * * *
#       * * * * *
#     * * * * * * *
#   * * * * * * * * *   Q6

# for i in range(5):
#     for j in range(i):
#         print(" ",end=" ")
#     #space
#     for j in range(9-2*i):
#         print("*",end=" ")
#     for j in range(i):
#         print(" ", end= " ")
#     print()
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *      Q7
# start = 1
# for i in range(5):
#     if i % 2 == 0:
#         start =1
#     else:
#         start = 0
#     for j in range(i+1):
#         print(start, end=" ")
#         start = 1 - start
#
#     print()
#
# 1
# 0 1
# 1 0 1
# 0 1 0 1
# 1 0 1 0 1 Q8
n = 4  # rows

# for i in range(1, n + 1):
#     # left side increasing numbers
#     for j in range(1, i + 1):
#         print(j, end="")
#
#     # spaces in between (except last line)
#     if i != n:
#         print(" " * (2 * (n - i)), end="")
#
#     # right side decreasing numbers
#     for j in range(i, 0, -1):
#         print(j, end="")
#
#     print()  # new line
# 1      1
# 12    21
# 123  321
# 12344321 Q9
