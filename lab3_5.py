year = input("Ange år: ")
if(int(year) % 4 == 0):
    if(int(year) % 100 == 0):
        if(int(year) % 400 == 0):
            print(year + " är ett skottår")
        else:
            print(year + " är inte ett skottår")
    else:
        print(year + " är ett skottår")
else:
    print(year + " är inte ett skottår")