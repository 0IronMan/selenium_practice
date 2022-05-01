"""
WAP to find a fibonacci series
"""
fib = [0,1]
n=10
for i in range(1,n-1):
    a = fib[i]+fib[i-1]
    fib.append(a)
# print(fib)
print(fib[n-1])
""" armstrong number """
n = 153
size = len(str(n))
out = 0
for chr in str(n):
    out += int(chr)**size
if out == n:
    print(f"{n} armstrong number")
else:
    print(f"{n}not armstrong number")


















# WAP to print 1 to 10 using range
# for i in range(1,11):
#     print(i)