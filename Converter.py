import sys

def decimaltobinary(a):
    liste = []
    while a // 2 != 0:
        if a % 2 == 0:
            liste.append(0)
        else:
            liste.append(1)
        a = a // 2
    liste.append(1)
    liste.reverse()
    return liste


# decimaltobinary(int(input("Enter a number :")))

def binarytodecimal(a):
    liste = []
    counter = 1
    decimal = 0
    exponent = 0
    index = 0
    for i in a:
        liste.append(i)
    liste.reverse()
    while counter <= len(liste):
        decimal += int(liste[index]) * (2 ** exponent)
        exponent = exponent + 1
        counter = counter + 1
        index = index + 1

    return decimal


# binarytodecimal(input("Enter a number :"))


def decimaltooctal(a):
    liste = []
    while a // 8 != 0:
        if a % 8 == 0:
            liste.append(a % 8)
        else:
            liste.append(a % 8)
        a = a // 8
    liste.append(a)
    liste.reverse()
    return liste


# decimaltooctal(int(input("Enter a number :")))


def octaltodecimal(a):
    liste = []
    counter = 1
    decimal = 0
    exponent = 0
    index = 0
    for i in a:
        if int(i) >= 8:
            print("Octal number cannot have any digit bigger than 7")
            sys.exit()
        else:
            liste.append(i)
    liste.reverse()
    while counter <= len(liste):
        decimal += int(liste[index]) * (8 ** exponent)
        exponent = exponent + 1
        counter = counter + 1
        index = index + 1

    return decimal


# octaltodecimal(input("Enter a number :"))


def decimaltohex(a):
    liste = []
    while a // 16 != 0:
        if a % 16 == 0:
            liste.append(a % 16)
        else:
            liste.append(a % 16)
        a = a // 16
    liste.append(a)
    liste = ['A' if i == 10 else i for i in liste]
    liste = ['B' if i == 11 else i for i in liste]
    liste = ['C' if i == 12 else i for i in liste]
    liste = ['D' if i == 13 else i for i in liste]
    liste = ['E' if i == 14 else i for i in liste]
    liste = ['F' if i == 15 else i for i in liste]
    liste.reverse()
    return liste


# decimaltohex(int(input("Enter a number :")))

def hextodecimal(a):
    liste = []
    counter = 1
    decimal = 0
    exponent = 0
    index = 0
    for i in a:
        liste.append(i)
    liste = [10 if i == 'A' else i for i in liste]
    liste = [11 if i == 'B' else i for i in liste]
    liste = [12 if i == 'C' else i for i in liste]
    liste = [13 if i == 'D' else i for i in liste]
    liste = [14 if i == 'E' else i for i in liste]
    liste = [15 if i == 'F' else i for i in liste]
    liste.reverse()
    while counter <= len(liste):
        decimal += int(liste[index]) * (16 ** exponent)
        exponent = exponent + 1
        counter = counter + 1
        index = index + 1

    return decimal


# hextodecimal(input("Enter a number :"))

print("*********************************************\n"
      "Welcome to Convertor\n"
      "*********************************************\n"
      "OPERATIONS :\n"
      "0-Decimal to Binary\n"
      "1-Binary to Decimal\n"
      "2-Decimal to Octal\n"
      "3-Octal to Decimal\n"
      "4-Decimal to Hexadecimal\n"
      "5-Hexadecimal to Decimal\n"
      "6-Octal to Hexadecimal\n"
      "7-Hexadecimal to Octal\n"
      "8-Octal to Binary\n"
      "9-Hexadecimal to Binary\n"
      "10-Binary to Hexadecimal\n"
      "11-Binary to Octal\n"
      "Press 'q' to exit\n"
      "*********************************************")

while True:
    op = str(input("\n*********************************************"
                   "\nPlease select an operation:\n"))
    if op == "0":
        for i in decimaltobinary(int(input("Enter a Decimal number :\n"))):
            print(i, end="")
    elif op == "1":
        print(binarytodecimal(input("Enter a Decimal number :\n")))
    elif op == "2":
        for i in decimaltooctal(int(input("Enter a Decimal number :\n"))):
            print(i,end="")
    elif op == "3":
        print(octaltodecimal(input("Enter a Octal number :\n")))
    elif op == "4":
        for i in decimaltohex(int(input("Enter a Decimal number :\n"))):
            print(i,end="")
    elif op == "5":
        print(hextodecimal(input("Enter a Hexadecimal number :\n")))
    elif op == "6":
        for i in decimaltohex(octaltodecimal(input("Enter a number :\n"))):
            print(i,end="")
    elif op == "7":
        for i in decimaltooctal(hextodecimal(input("Enter a number :\n"))):
            print(i,end="")
    elif op == "8":
        for i in decimaltobinary(octaltodecimal(input("Enter a number :\n"))):
            print(i,end="")
    elif op == "9":
        for i in decimaltobinary(hextodecimal(input("Enter a number :\n"))):
            print(i,end="")
    elif op == "10":
        for i in decimaltohex(binarytodecimal(input("Enter a number :\n"))):
            print(i,end="")
    elif op == "11":
        for i in decimaltooctal(binarytodecimal(input("Enter a number :\n"))):
            print(i,end="")
    elif op == "12":
        print("Have a nice Day!\n")
        sys.exit()
