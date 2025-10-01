#extraction
n = int(input("Enter the number"))
# while n!= 0:
#     print(n%10)
#     n = int(n/10)

#reverse
# rev_string = 0
# while n!= 0:
#     last_digit = n % 10
#     n = int(n/10)
#     rev_string = (rev_string*10) + last_digit
# print(rev_string)


#pallindrome
# duplicate = n
# rev_string = 0
# while n!= 0:
#     last_digit = n%10
#     n = int(n/10)
#     rev_string = (rev_string*10) + last_digit
# if rev_string==duplicate:
#     print("The number is palindrome")


#armstrong
# duplicate = n
# sum = 0
# while n!= 0:
#     last_digit = n%10
#     n = int(n/10)
#     sum = sum + (last_digit*last_digit*last_digit)
# if sum == duplicate:
#     print("The number is Armstrong number")

#divisors
# count= 0
# for i in range(1,int(n**0.5)+1):
#     if n%i == 0:
#         count+=1
#         print(i)
#     if i != int(n/i):
#         count+=1
#         print(int(n/i))

#prime
# count = 0
# for i in range(1,int(n**0.5)+1):
#     if n % i == 0:
#         count +=1
#     if i != int(n/i):
#         if n%(int(n/i)) == 0:
#             count+=1
# if count == 2:
#     print("prime")

#gcd
#euclidean algotithm => gcd(a,b) = gcd(a%b,b) = gcd(a-b,b)
# m = int(input("Enter the 2nd number"))
# while n>0 and m>0:
#     if m>n:
#         m = m%n
#     else:
#         n = n%m
#
# if n== 0:
#     print("GCD is",m)
# else:
#     print("GCD is", n)
