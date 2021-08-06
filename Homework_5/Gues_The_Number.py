import random
print("Привет, я загадал число от 1 до 100, твоя задача угадывать,"
      " а я буду подсказывать куда тебе двигаться в большую или меньшую сторону, удачи =):")
bool_value=True
answer_number=random.randint(1,100)
tries=1
while(bool_value==True):
    try:
        number=input()
        int_number=int(number)
        if(int_number<answer_number):
            print("Попробуй ввести число БОЛЬШЕ:")
        elif(int_number>answer_number):
            print("Попробуй ввести число МЕНЬШЕ:")
        elif(int_number==answer_number):
            print("Поздравлю, друг, ты угадал это число"+" '",answer_number,"'"+". Твоё количество попыток перед правильным ответом:",tries)
            bool_value=False
        tries += 1

    except:
        tries += 1
        print("Не знаю что ты ввёл, но за попытку посчитаю, играем дальше:")



