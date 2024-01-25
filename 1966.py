import sys

testnum=sys.stdin.readline()



def findhigh():           #중요도 리스트에서 처음 등장하는 최고 중요도의 인덱스 찾기
    global importance
    highindex = 0
    for a in range(len(importance)):
        if importance[a]>importance[highindex]:
            highindex=a
    return(highindex)



for c in range(int(testnum)):
    answer=1
    count,seatnum = map(int,sys.stdin.readline().split())

#중요도 리스트의 길이
#주어진 인덱스


    importance = list(map(int,sys.stdin.readline().split()))   #중요도 리스트



    target = importance[seatnum]  #주어진 인덱스의 중요도



    while True:
        highindex=findhigh()
        if importance[highindex]>target:#하이인덱스까지 배열의 뒤로 옮기고 마지막 리스트 제거하기
            part1 = importance[:highindex]
            part2 = importance[highindex:]
            part2.pop(0)
            importance = part2 + part1
            answer+=1
            if seatnum<highindex:
                seatnum+=len(part2)
            elif seatnum>highindex:
                seatnum-=(len(part1)+1)
    
        elif importance[highindex]==target:
            if highindex<seatnum:#하이인덱스까지 배열의 뒤로 옮기고 마지막 리스트 제거하기
                part1 = importance[:highindex]
                part2 = importance[highindex:]
                part2.pop(0)
                importance = part2 + part1
                answer+=1
                seatnum-=(len(part1)+1)
            else:
                break
    print(answer)

