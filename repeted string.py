import sys


s = input().strip()
n = int(input().strip())

k = s.count("a")*(n//len(s))
k += s[:n%len(s)].count("a")
print(k) 