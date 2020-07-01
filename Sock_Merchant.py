#initialize the counter to 0
c = 0
#integer number of socks
n = int(input())
#socks colors in space_separate
socks = list(map(int, input().rstrip().split()))
#ensure no repetition
colours = set(socks)
for i in colours:
    c = c + socks.count(i) // 2
print(c)