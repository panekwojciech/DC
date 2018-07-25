'''
24/04/2018
https://projecteuler.net/problem=4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''

def is_palindrome(n):
    lst = [int(x) for x in str(n)]
    
    while len(lst) > 1:
        if lst[0] == lst[-1]:
            del lst[0]
            del lst[-1]
        else:
            return False
        
    return True

result = []
a = 999
for i in range(999,900, -1):
    for j in range(a,900, -1):
        temp = i * j
        if is_palindrome(temp):
            result.append(temp)
            #print('{0} * {1} = {2}'.format(i,j,temp))
    a -=1

print(max(result))
