n, t = map(int, input().split())
floors = list(map(int, input().split()))
number = int(input())

if n < 2:
    print("Введите не меньше 2 сотрудников")
elif t > 100:
    print("Введите количество минут до 100")
elif len(floors) != n:
    print("Количество этажей не соответствует количеству сотрудников")
elif any(abs(f) > 100 for f in floors):
    print("Число по абсолютной величине больше 100")
elif any(floors[i] <= floors[i - 1] for i in range(1, n)):
    print("Этажи идут не в порядке возрастания")
else:
    liv_index = number - 1  # индекс уходящего коллеги
    liv_floor = floors[liv_index]  # этаж уходящего коллеги
    remaining_floors = floors[:liv_index] + floors[liv_index+1:]  # оставшиеся этажи
    stairs = 0  # лестничные пролеты
    movemant = liv_floor  # перемещение
    for floor in remaining_floors:
        stairs += abs(floor - movemant)
        movemant = floor
    print(stairs)
