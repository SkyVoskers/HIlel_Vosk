dict_words=dict()
text=("Get to the point, as in To make a long story short, they got married"
      " and moved to Omaha. Although the idea of abbreviating a long-winded "
      "account is ancient, this precise phrase dates only from the 1800s. "
      "Henry David Thoreau played on it in a letter of 1857: ' Not that the "
      "story need be long, but it will take a long time to make it short. '")
text:list=text.split()
symbols_dict=[",",".",":"]
for i in range(len(text)):
    for j in symbols_dict:
        if j in text[i]:
            text[i] = text[i].replace(j, '')
print(text)
for i in text:
    key=text.count(i)
    if dict_words.get(key)==None:
        dict_words[key]=list()
    if key>1 and dict_words[key].count(i)==1:
        continue
    dict_words[key].append(i)
print(dict_words)
count=0
tmp=False
for i in dict_words.keys():
    if i>count:
        count=i

print(dict_words[count])
for i in text[::-1]:
    for element in dict_words[count]:
        if i==element:
            print("The most common words:'",i,"'in using:",count)
            tmp=True
            break
    if tmp==True:
        break

