print("Input at least 2 words and not more than 2 words in order to get them in Vice_Versa: ")

try:
    first_word, second_word, *tmp = input().split()
    new_second_word = second_word[::-1]
    new_second_word = new_second_word.lower()
    new_second_word = new_second_word.replace(new_second_word[0],new_second_word[0].upper())
    new_first_word = first_word[::-1]
    new_first_word = new_first_word.lower()
    new_first_word = new_first_word.replace(new_first_word[0],new_first_word[0].upper())
    print(new_second_word, new_first_word)
except:
    print("You have inputted less than 2 words")
