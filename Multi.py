#Mathamatical multitool
#Made by Lucas Brattinga and in collaboration with Cameron Lewis

import os

def Main():
    print("")
    print(" ~~~~~~~~~~~~~~~~~~~~~~~~ ")
    print("   M th m ti  l Multitool ")
    print("    X  X X  .X            ")
    print("    X  X X  .X            ")
    print("    .  X .  ..            ")
    print("    .  X .  ..            ")
    print("    .  X .  ..            ")
    print("    .  . .  ..            ")
    print("                          ")
    print("  Mathematical Multitool  ")
    print("    By: Lucas Brattinga   ")
    print(" ~~~~~~~~~~~~~~~~~~~~~~~~ ")
Main()

class MainMenu():
    def MMenu():
        print("       [Main Menu]")
        menu = {}
        menu["[1]"] = ("Unit Convirter")
        menu["[2]"] = ("Calculator")
        menu["[3]"] = ("Area of Shapes")
        menu["[4]"] = ("Meal Price")
        menu["[5]"] = ("Help")
        menu["[6]"] = ("Credits")
        menu["[7]"] = ("Exit")

        choice = menu.keys()
        for row in choice:
            print (row, menu[row])
    MMenu()

    selection = input("Choose an option: ")

    if selection == "1":
        multi = 1

        os.system('cls')
    elif selection == "2":
        multi = 2

        os.system('cls')
    elif selection == "3":
        multi = 3

        os.system('cls')
    elif selection == "4":
        multi = 4

        os.system('cls')
    elif selection == "5":
        multi = 5

        os.system('cls')
    elif selection == '6':
        multi = 6
        os.system('cls')

    else:
            print("[!]Error unknown input")
            os.system('cls')


MainMenu()

if MainMenu.multi == 1:
    Main()
    print("[Unit Convirter]")


elif MainMenu.multi == 2:
    Main()
    print("     [Basic Calculator] ")
        #Basic Calculator V1
    def CalculatorScript():

        menu = {}
        menu["[1]"] = ("Addition")
        menu["[2]"] = ("Subtraction")
        menu["[3]"] = ("Multiplication")
        menu["[4]"] = ("Division")
        menu["[5]"] = ("Back")

        choice = menu.keys()
        for row in choice:
                print (row, menu[row])

        class Topporator:
            def add(x,y):
                return x + y

            def subtract(x,y):
                return x - y

            def multi(x,y):
                return x * y

            def subtr(x,y):
                return x / y

        opporation = input("Choose an option: ")

        if opporation == '1':
            Value1 = input("Number1: ")
            Value2 = input("Number2: ")
            print (Topporator.add(float(Value1),float(Value2)))

        elif opporation == '2':
            Value1 = input("Number1: ")
            Value2 = input("Number2: ")
            print (Topporator.subtract(float(Value1),float(Value2)))

        elif opporation == '3':
            Value1 = input("Number1: ")
            Value2 = input("Number2: ")
            print (Topporator.multi(float(Value1),float(Value2)))

        elif opporation == '4':
            Value1 = input("Number1: ")
            Value2 = input("Number2: ")
            print (Topporator.subtr(float(Value1),float(Value2)))

        elif opporation == '5':
                os.system('cls')
                Main()
                MainMenu.MMenu()
                MainMenu()
                #working back button^
        else:
            print ("")
            print ("[!]Error")
            print ("")
            input()
            os.system('cls')
            Main()
            print("     [Basic Calculator] ")
            CalculatorScript()
    CalculatorScript()

elif MainMenu.multi == 3:
    Main()
    print(" [Area of Shapes]")

elif MainMenu.multi == 4:
    Main()
    print("[Meal Price]")

elif MainMenu.multi == 5:
    print("                        ~~~~~[Help]~~~~~")
    helptxt = open("Help.txt")
    print(helptxt.read())
    input()

elif MainMenu.multi == 6:
    print("[Credits]")
    credits_txt = open("Credits.txt")
    print(credits_txt.read())
