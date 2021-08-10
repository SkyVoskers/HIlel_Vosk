import random
# size=int(input("Введите размер списка:"))
# arr = [random.randint(1,100) for j in range(size)]
# print(arr)
# rmv_index=int(input("Введите индекс элемента, который хотите удалить: "))
# a=arr.pop(rmv_index-1)
# print(arr)
############################################################3##
# def remover (index=int(),array=list()):
#     for k in range(index,len(array)):
#         array[k] = array[k + 1]
#         array.pop()
#     return False
#
# size=int(input("Введите размер списка:"))
# arr = [random.randint(1,100) for j in range(size)]
# tmp=True
# while (tmp):
#     rmv_index=int(input("Введите индекс элемента для удаления:"))
#     if(rmv_index<=size):
#         tmp=remover(rmv_index,arr)
#         print(arr)
######################################################################

size=int(input("Введите размер списка:"))
arr = [random.randint(1,100) for j in range(size)]
print(arr)
print(arr[2])
print(arr[len(arr)-1])
rmv_index=int(input("Введите индекс элемента, который хотите удалить: "))

for i in range (len(arr)):
    if(arr[i]==arr[rmv_index]):
        arr[rmv_index]=arr[len(arr)-1]
        arr.pop()
        print(arr)
print(arr)
