while(True):
    print("Input year to check whether the year in 1900-1000000 range, and whether it leap or not: ")
    year=int(input())
    if (1900<=year<=1000000):
        print("Success!!!! Input year", year ,"in 1900-1000000 range")
        if(year % 4 == 0):
            print("Input year", year, "is leap")
        else:
            print("Input year", year, "is not leap")
    else:
        print("Sorry, ",year," is not in 1900-1000000 range")

