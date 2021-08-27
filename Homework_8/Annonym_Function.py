print("Input two numbers and i will raise the first to the exponent of the second ")
print("Also, you have to INPUT AMOUNT of NUMBERS that you would like to work with: ")

amount=int(input("Input amount of numbers in list:"))
number_1=[int(input("Input FIRST number:")) for i in range(amount)]
number_2=[int(input("Input SECOND number:")) for i in range(amount)]
exponent=list(map(lambda x,y=int(2):x**y,number_1,number_2))
print(exponent)
