print("Укажите натуральное число чтобы вывести все автоморфные числа, что стоят до него: ")
number=input()
try:
    check_number = int(number)
    automorph_number=list()
    for first_number in range(1,check_number):
        sqr = first_number ** 2
        str_first_number=str(first_number)
        str_sqr=str(sqr)
        if(str_sqr.find(str_first_number,len(str_sqr)-len(str_first_number))!=-1):
            print(first_number,"*",first_number,"=",sqr)







except:
    print("Твое число", number, "не является натуральным или вообще не число")

