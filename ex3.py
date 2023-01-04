try:
    number = int(input("Enter a number: ")) #use try except
    print(number)
except ZeroDivisionError:
    print("Divided y zero")
except ValueError:
    print("invalid input")    