from random import randint
print("Vvedete kolichestvo monetok:")
n = int(input())
array = [randint(0, 1) for i in range(n)]
sumR = 0 # reshka = 0
sumO = 0 # oryol = 1
print(array)
for i in range(n):
    if array[i] == 0:
        sumR += 1
    else:
        sumO += 1
print(f'Na stole lejit reshkoy: {sumR} \n Na stole lejit oryol: {sumO}')
if sumR > sumO:
    for i in range(n):
        if array[i] == 1:
            array[i] = 0
else:
    for i in range(n):
        if array[i] == 0:
            array[i] = 1
print(array)