import random
def Simple_Numbers_Generator (number_1,number_2):
    #arr=list()
    for i in range (number_1,number_2+1):
        k=0 # chislo deliteley
        for j in range(1, i+1):
            if i % j == 0:
                k += 1
        if k == 2:
            yield i

number_1=int(input("Введи ЛЕВУЮ границу чисел: "))
number_2=int(input("Введи ПРАВУЮ границу чисел: "))
# if (number_2 - number_1>0):
#     print(Simple_Numbers_Generator(number_1,number_2))
for i in Simple_Numbers_Generator(number_1, number_2):
    print(i, end=' ')