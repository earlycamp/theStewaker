for i in range(1,101):
    if i % 5 == 0 and i % 3 == 0:
        print("Marco Polo")
    elif i % 3 == 0:
        print("Marco")
    elif i % 5 == 0:
        print("Polo")
    
    else:
        print(i)