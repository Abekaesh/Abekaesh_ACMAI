rows = 5
spaces = 4
for i in range(1,rows+1):
    print(spaces*" ",end="")
    for j in range(-1,rows%i):
        print(i,end="   ")
    print()
    if i <= int(rows/2):
        spaces -= 2
    else:
        spaces += 2
