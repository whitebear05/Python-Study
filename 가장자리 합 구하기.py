# 정수 A를 입력받아 A*A까지 2차원 배열에 저장한 후 사각 테두리에 있는 배열값들만 합하여 출력하세요
#
# 입력
# 3
#
# 출력
# 20

n = int(input())
print(1 + n + n * n + (n * n - n + 1))
