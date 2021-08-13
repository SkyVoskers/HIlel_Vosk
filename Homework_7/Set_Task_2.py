import random
size_1=(int(input("Input the size of list_1:")))
numbers_1= [random.randint(1,100) for j in range(size_1)]
size_2=(int(input("Input the size of list:")))
numbers_2= [random.randint(1,100) for j in range(size_2)]
my_set=set(numbers_1+numbers_2)
print("Amount of elements in 2 lists: ",len(my_set))
