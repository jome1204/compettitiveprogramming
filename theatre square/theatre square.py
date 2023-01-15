import math
n,m,a = map(int,input().split())
first = math.ceil(n/a)
second = math.ceil(m/a)
print(first*second)
