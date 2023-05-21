# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X

# 5
# 1 2 3 4 5
# 6
# -> 5

n = int(input('Введите кол-во элементов в массиве: '))
x = int(input('Введите число Х для проверки: '))
list_1 = []
list_2 = []
gap = 0
index = 0


for i in range(1, n+1):
    list_1.append(i)

for i in range(len(list_1)):
    gap = list_1[i] - x
    if gap < 0:
        gap = gap * -1
    list_2.append(gap)

min_value = list_2[0]
for i in range(1, len(list_2)):
    if list_2[i] <= min_value:
        min_value = list_2[i]
        index = i

print(n)
print(*list_1)
print(x)
print(f'-> {list_1[index]}')
