year = int(input("Year? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"Year {year} is leap.")
        else:
            print(f"Year {year} is not leap.")
    else:
        print(f"Year {year} is leap.")
else:
    print(f"Year {year} is not leap.")
