# 1080 행렬

n, m = map(int, input().split()) 

listA = []
listB = []
cnt = 0

for i in range(n): 
    listA.append(list(map(int, list(input()))))

for i in range(n): 
    listB.append(list(map(int, list(input()))))

# 뒤집기 함수
def reverse(i, j):
    for x in range(i, i+3):
        for y in range(j, j+3):
            if listA[x][y] == 0:
                listA[x][y] = 1
            else:
                listA[x][y] = 0

# 3보다 작거나 안될때(예외처리)
if listA != listB:
    for r in range(n-2):
        for c in range(m-2):
            if listA[r][c] != listB[r][c]:
                cnt += 1
                reverse(r, c)

if cnt != -1:
    if listA != listB:
        cnt = -1
print(cnt)