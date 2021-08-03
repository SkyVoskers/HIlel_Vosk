while(True):
    print("Input year to check whether it LEAP or NOT in Gregorian_Calendar : ")
    year=int(input())
    if (year % 400== 0 or year % 4 ==0):
        print("Input year", year, "is leap")
    else:
        print("Input year", year, "is not leap")