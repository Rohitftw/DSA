n = int(input("Enter a number"))
#print the name n times
# def Q1(val,n):
#     if val > n:
#         return
#     print("Name")
#     Q1(val+1, n)
#
# Q1(1,n)
#TC, SC = O(n)

#print linearly 1 to n
# def Q2(val, n):
#     if val> n:
#         return
#     print(val)
#     Q2(val+1,n)
# Q2(1,10)
# TC,SC= O(n)

#print n to 1
# def Q3(n):
#     if n== 0:
#         return
#     print(n)
#     Q3(n-1)
# Q3(n)

#print 1 to n using backtrack
# def Q4(i,n):
#     if i< 1:
#         return
#     Q4(i-1,n)
#     print(i)
# Q4(n,n)

#print n to 1 using backtrack
# def Q5(i,n):
#     if i> n:
#         return
#     Q5(i+1,n)
#     print(i)
# Q5(1,n)
#/*Re2 end*/

#paramaterized
# def Q1(n,sum):
#     if n<1:
#         print(sum)
#         return
#     Q1(n-1,sum+n)
# Q1(n,0)

#functional recursion
# def sum(n):
#     if n == 0:
#         return 0
#     return n + sum(n-1)
# print(sum(n))

#factorial
# def factorial(n):
#     if n==1:
#         return 1
#     return n*factorial(n-1)
# print(factorial(n))

# \*Re3 end*\

# arr = list(map(int, input("Enter numbers: ").split()))
# print(arr)
# n = len(arr)

# def swap(l,r):
#     if l>=r:
#         return arr
#     arr[l],arr[r] = arr[r],arr[l]
#     return swap(l+1,r-1)
# print(swap(0,n-1))

# def swap(i):
#     if i > n/2:
#         return
#     arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
#     swap(i+1)
# swap(0)
# print(arr)

# string = 'MADAM'
# def pallindrome(i, string):
#     if i>= len(string)/2:
#         return True
#     if string[i] != string[len(string)-i-1]:
#         return False
#     return pallindrome(i+1,string)
# print(pallindrome(0,string))

#/*Re 4 end*/

#multiple recursion calls
# def fib(n):
#     if n<=1:
#         return n
#     last = fib(n-1)
#     slast = fib(n-2)
#     return last + slast
# print(fib(n))

#/*Re5 end*/

