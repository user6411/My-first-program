while True:
    print('How old are you?')
    
    age = int(input())
    if age < 0:
        print("Error! Please input a valid number")
    
    elif age >= 150:
        print("immortal")
    
    elif age == 100: 
        print("experienced")

    elif age == 0:
        print("baby")
    
    elif age <=12:
        print("kid")

    elif age >=18:
        print("adult")

    elif age > 12 < 18:
        print("teenager")
