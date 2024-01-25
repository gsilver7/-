high=0
arraynum=0
array=[]
repeat=0
answer=1

arraynum=int(input("막대기의 개수를 입력하시오:"))

while repeat<arraynum:
    array.append(int(input("막대기의 높이를 입력하시오:")))
    repeat+=1

high=array.pop()
array.reverse()

for a in array:
    if a>high:
        answer+=1
        high=a

print(answer)
