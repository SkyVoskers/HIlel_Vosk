import random
def sumchek (arr,number):
    for i in range(len(arr)):
        for g in range(i+1,len(arr)):
            if arr[i]+arr[g] == number:
                return True

    return False
#########################################################################################################################
#  FIRST TEST (1)
size_1=(int(input("Input the size of list:")))
array_1 = [random.randint(1,100) for j in range(size_1)]
print(array_1)
nubmer_1 = (int(input("Input the number, to check whether at least 2 elements the sum of your number:")))
print(sumchek(array_1, nubmer_1))
#########################################################################################################################
#  Second TEST (2)
size_2 = (int(input("SECOND TEST: Input the size of list:")))
array_2 = [random.randint(1,100) for j in range(size_2)]
print(array_2)
nubmer_2=(int(input("SECOND TEST: Input the number, to check whether at least 2 elements the sum of your number:")))
print(sumchek(array_2, nubmer_2))

