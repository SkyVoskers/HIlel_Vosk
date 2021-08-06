print("Input number from 3 to 9, to print a Pyramid: ")
pyramid_high = input()
try:
    int_pyramid_high = int(pyramid_high)
    if ( int_pyramid_high<3 or int_pyramid_high>9):
        print("Sorry, you are out of range")
    else:
        for i in range(1, int_pyramid_high + 1):
            result_pyramid = ""
            for j in range(1, i):
                result_pyramid += str(j)
            for k in range(i, 0, -1):
                result_pyramid += str(k)
            print(result_pyramid)


except:
    print("Sorry, you have inputted not a number or wrong number")