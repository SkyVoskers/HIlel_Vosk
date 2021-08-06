print("Укажите натуральное число и я скажу есть ли в нём повторяющиеся символы : ")
number = int(input())
try:
    chek_number=int(number)
    i=0
    k=0
    while(i<len(number) and k==0 ):
        current_character= number[i]
        for j in range (i+1, len(number)):
            current_character_2=number[j]

            if (current_character == current_character_2):
                k+=1
        i+=1
    if (k>0):
            print("Ваше число", number, "имеет повторяющиеся символы")
    else:
        print("Ваше число", number, " НЕ имеет повторяющиеся символы")

except:
    print("Ваше число", number, "не является натуральным числом или ВООБЩЕ числом")



