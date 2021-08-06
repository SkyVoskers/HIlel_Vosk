print("Укажите натуральное число и я скажу есть ли в нём повторяющиеся символы рядом: ")
number=input()
try:
    chek_number=int(number)
    k=0
    for i in range(len(number)-1):
        current_number=number[i]
        next_number=number[i+1]
        if(current_number==next_number):
            k+=1
            break
    if(k>0):
        print("Ваше число", number, "имеет повторяющиеся символы Рядом")
    else:
        print("Ваше число", number, "НЕ имеет повторяющиеся символы Рядом")

except:
    print("Ваше число", number, "не является натуральным числом или ВООБЩЕ числом")