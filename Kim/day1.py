def star(n, i, j):
    for i in range(n):
        for j in range(n):
            if i == z and j == z :
                print("", end=" ")
                continue
            print("*", end="")
        print()

num = 3
for i in range(num):
    for j in range(num):
        star(num,i,j)
