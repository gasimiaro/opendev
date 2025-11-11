n,k = map(int, input().split())
l = list(map(int, input().split()))
for i in range(k):
    next_l = []
    for j in range(n-1):
        next_l.append(abs(l[j]-l[j+1]))
    next_l.append(0)
    if next_l == l:
        break
    l = next_l
print(*l)