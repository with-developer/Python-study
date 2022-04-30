gugudan = [[0 for j in range(9)] for i in range(8)]

for num1 in range(8):
    for num2 in range (9):
        gugudan[num1][num2] = (num1+2)*(num2+1)

print(gugudan)
