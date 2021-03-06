# ord : 유니코드 정수
# chr : 유니코드 문자

print(ord('a')) # 97
print(ord('A')) # 65

print(chr(99)) # c

# 소문자 출력
for i in range(97, 123):
    print(chr(i), end=' ')
print()
for i in range(0, 26):
    print(chr(ord('a') + i), end=' ')



# 0으로 채우는 zfill
# Fill the string with zeros

n = 20
print(hex(n)) # 0x14

n = str(hex(n))
print(n.zfill(10))

n1 = str(30)
print(n1.zfill(10))

n2 = 'hello'
print(n2.zfill(10))



Group = {}
print("### K-Pop 그룹 관리 프로그램 ###")
while True:
    menu = int(input("[1]등록 [2]삭제 [3]조회 [4]종료 : "))
    if menu == 4:
        break
    elif menu == 1:
        name = input("그룹 이름이 무엇인가?")
        member = input("그룹 인원이 몇 명인가?")
        Group[name] = member
    elif menu == 2:
        delete = input("삭제할 그룹 이름이 무엇인가?")
        del(Group[delete])
    elif menu == 3:
        print(Group)

    print("### K-Pop 관리 프로그램 종료 ###")




sum = 0
for i in range(1010):
    sum += i
print("sum :{}".format(sum))
print("%d" % sum)




# 파이썬 큐, 스택 구현
from collections import deque
queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)
print(queue.popleft())
print(queue.popleft())
print(queue.popleft())
print(queue)



from collections import deque
queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)
print(queue.popleft())
print(queue.popleft())
print(queue)
queue.append(11)
queue.append(22)
queue.append(33)
print(queue)
# print(queue.reverse()) # 이렇게 하면 안 됨.
queue.reverse()
print(queue)





# 리스트 자료구조
stack = []
stack.append(5)
stack.append(3)
stack.append(8)
stack.append(6)
stack.append(4)
stack.pop()
stack.append(1)
stack.pop()
print(stack)
print(stack[0])
print(stack[::-1]) # Extended Slices
print('stack pop', stack.pop())
print('stack pop', stack.pop())
print('stack pop', stack.pop())
print('stack pop', stack.pop())




# 리스트 index 연습
a = []*6
print(a)
a = [0, 2, 3, 4, 5, 1]
print(a)
for i in range(1, 6):
    a[i] = a[a[i]]
print(a)
for i in range(1, 6):
    a[i] = a[a[i]]
print(a)




# 팩토리얼
def f_iter(n):
    r = 1
    for i in range(1, n + 1):
        r *= i
    return r

def f_rec(n):
    if n <= 1:
        return 1
    else:
        return n * f_rec(n-1)

print(f_iter(5))
print(f_rec(5))





# 딕셔너리 생성 (여러 빈칸이 있는 경우 처리법)
d1 = {}
k = input()
v = input()
d1[k] = v
k = input()
v = input()
d1[k] = v
print(d1)



# 딕셔너리 생성 (빈칸이 한 번 있는 경우)
dct1 = {}
for _ in range(2):
    k, v = input().split()
    dct1[k] = v
print(dct1)




# map 함수를 사용하는 것과 아닌 것의 차이

# 리스트에 값을 하나씩 더해서 새로운 리스트를 만드는 작업
myList = [1, 2, 3, 4, 5]

# for 반복문 이용
result1 = []
for val in myList:
    result1.append(val + 1)
print(f'result1 : {result1}')

# map 함수 이용
def add_one(n):
    return n + 1
result2 = list(map(add_one, myList)) # map 반환을 list로 변환
print(f'result2 : {result2}')





# 리스트와 map 함수
import math

# 리스트의 값을 정수 타입으로 변환
result1 = list(map(int, [1.1, 2.2, 3.3, 4.4, 5.5]))
print(f'map(intm 리스트) : {result1}')

# 리스트 값 제곱
def func_pow(x):
    return pow(x, 5) # x의 5제곱을 반환
result2 = list(map(func_pow, [1,2,3,4,5]))
print(f'map(func_pow, 리스트) : {result2}')

# 리스트 값 소수점 올림
result3 = list(map(math.ceil, [1.1, 2.2, 3.3, 4.4, 5.5, 6.6]))
print(f'map(func_ceil, 리스트) : {result3}')


