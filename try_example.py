while True:
    try: 
        num = int( input("Enter an integer: ") )
        print(num)
        break
    except ValueError:
        print("Try again.")

