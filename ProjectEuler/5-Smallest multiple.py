'''
25/07/2018
https://projecteuler.net/problem=5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''


#All numbers from 1 to 20 factorized to primes and insert into array without unnecesarry repetitions.

array = [2, 2, 2, 2, 3, 3, 5, 7, 11, 13, 17, 19]
a = 1
for i in array:
    a *= i

print(a)
