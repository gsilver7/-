1457

import sys

l = list(map(int,sys.stdin.readline().split()))
N=l[0]
k=l[1]

listA = list(range(N+1))
listA.pop(0)

num=len(listA)
index=k-1

answer=[]

for a in range(N):
    if index>=num:
        index=index%num
        answer.append(listA.pop(index))
        index-=1
        index+=k
        num-=1
    else:
        answer.append(listA.pop(index))
        index-=1
        index+=k
        num-=1
        
print(f"<{', '.join(map(str, answer))}>")
