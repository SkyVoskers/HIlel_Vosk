import random
size=int(input("Введите размер списка:"))
arr = [random.randint(1,100) for j in range(size)]
print(arr)
elem_value=int(input("Введите значение элемента:"))
insert_index=int(input("Введите индекс который хотите присвоить элементу : "))-1
if (insert_index>size or insert_index<1):
    print("Ошибка, ваш индекс неправильный, пока")
for i in range (insert_index,len(arr)-1):
    arr[i]=arr[i+1]
arr.pop()
print(arr)