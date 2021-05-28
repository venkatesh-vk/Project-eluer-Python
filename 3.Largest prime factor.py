'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
import sympy as s
import math as m
n=m.floor(m.sqrt(600851475143))
b=600851475143
a=[]
for i in range(2,n,1):
    if(s.isprime(i)):
        if(b%i==0):
            a.append(i)
print(max(a))
