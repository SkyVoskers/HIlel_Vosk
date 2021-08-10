import random
#size=int(input("Введите размер списков:"))
#arr_1=[random.randint(1,100) for j in range(size)]
#arr_2=[random.randint(1,100) for j in range(size)]
arr_1=[1,2,3,4,5,6]
print("Список 1:",arr_1)
arr_2=[1,2,3,4,5,7]
print("Список 2:",arr_2)
uniq_list=[x for x in arr_1 + arr_2 if x not in arr_1 or x not in arr_2]
print("Cписок уникальных элементов с 1 и 2 списка:",uniq_list, "\nКоличество уникальных элементов в списке:",len(uniq_list))
if not uniq_list:
    print("Списки одинаковые 1 и 2 одинаковые")
else:
    print("Списки одинаковые 1 и 2 НЕ одинаковые")
