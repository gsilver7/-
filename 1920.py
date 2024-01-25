import sys

num1 =  int(sys.stdin.readline())

arr1 = list(map(int,sys.stdin.readline().split()))

arr1.sort()



num2 = int(sys.stdin.readline())

arr2 = list(map(int,sys.stdin.readline().split()))

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    # 원하는 값 찾은 경우 인덱스 반환
    if array[mid] == target:
        return mid
    # 원하는 값이 중간점의 값보다 작은 경우 왼쪽 부분(절반의 왼쪽 부분) 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    # 원하는 값이 중간점의 값보다 큰 경우 오른쪽 부분(절반의 오른쪽 부분) 확인
    else:
        return binary_search(array, target, mid + 1, end)

for target in arr2:
    result = binary_search(arr1, target, 0, num1 - 1)
    if result is None:
        print(0)
    else:
        print(1)
