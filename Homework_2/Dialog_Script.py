import random
print("Hello my friend, what`s your name?")
name=input()
while(True):
    print(name + " ,do you wanna play? (put `y` or `n`)")
    ans_play=input()

    if(ans_play=="y"):
        print("OK, lets play `21`,your pull first:")
    elif (ans_play=="n"):
        print("OK, good bye,"+name)
        break
        score_player =0
        score_bot =0
        while(True):
            print("Your score:", score_player,"Push `y` for getting more cards or `n` for stop:")
            ans_y=input()
            if(ans_y=="y"):
                score_player+=random.randint(1,11)
                if(score_player>21):
                    print("Your nubmer is too high ",score_player,". Sorry you are looser")
                    break
            if (ans_y == "n"):
                score_bot=random.randint(18,21)
                if(score_player<score_bot):
                    print("player score: ",score_player,". bot score: ",score_bot,"."+"Who are the best PLAYER???!!! SURELY NOT YOU!!!")
                    break
                elif (score_player > score_bot):
                    print(
                        "player score: " , score_player, ". bot score: ",score_bot, "." + "You are the greates player i have ever seen!!!!")
                    break
                elif (score_player == score_bot):
                    print(
                        "player score: " , score_player , ". bot score: ", score_bot, "." + "It`s draw, bro, sometimes it happens")
                    break