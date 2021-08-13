import random
size=(int(input("Input the size of list:")))
numbers= [random.randint(1,100) for j in range(size)]
print(numbers)
set_list=set(numbers)
print(set_list)
print("amount of different  numbers: ",len(set_list))