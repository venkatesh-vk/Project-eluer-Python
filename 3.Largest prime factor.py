'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
n=600851475143
a=[]
b=[]
for i in range(2,n+1):
    if i not in a:
        b.append(i)
        for j in range(i**2,n+1,i):
            a.append(j)
print(max(b))