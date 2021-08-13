text_dict=("Get to the point, as in To make a long story short, they got married"
      " and moved to Omaha. Although the idea of abbreviating a long-winded "
      "account is ancient, this precise phrase dates only from the 1800s. "
      "Henry David Thoreau played on it in a letter of 1857: ' Not that the "
      "story need be long, but it will take a long time to make it short. '")
symbols_dict=[",",".",":"]
text_list=list(text_dict.split()) #Хранятся слова по отдельности
for i in range(len(text_list)):
    for j in symbols_dict:
        if j in text_list[i]:
            text_list[i] = text_list[i].replace(j, '')
    #if symbols_dict in text_list[i]:

print(text_list)
counter_list=list() #количество повторений каждого слова через count, каждый Соунт будет добавляться в список коунтер
words_list=list()
for i in range(len(text_list)):
    if text_list[i] not in words_list:
        counter_list.append(text_list.count(text_list[i]))
        words_list.append(text_list[i])
union_list = {i: j for i, j in zip(words_list, counter_list)}
#union_list=dict(zip(words_list,counter_list))
print(union_list)

