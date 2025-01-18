#importing required libraries
import time

#we created our class
class machine:
    def __init__(self):
        #we created a variabla named loop and we set it True, so we it will work until we want to stop it 
        self.loop = True

    def program(self):
        secim = self.choice()

        if secim == "1":
            self.topla()
        if secim == "2":
            self.cikart()
        if secim == "3":
            self.bolme()
        if secim == "4":
            self.carpma()
        if secim == "5":
            self.exit()

#we created a method to take an input from our user
    def choice(self):
        choice = input("1-topla\n2-cikart\n3-bolme\n4-carp\n5-exit")
        return choice

#our mathematical methods
    def topla(self):
        a = int(input("give me the first number"))
        b = int(input("give me the second number"))

        print(a + b)


    def cikart(self):
        a = int(input("give me the first number"))
        b = int(input("give me the second number"))

        print(a - b)

    def bolme(self):
        a = int(input("give me the first number"))
        b = int(input("give me the second number"))

        print(a / b)

    def carpma(self):
        a = int(input("give me the first number"))
        b = int(input("give me the second number"))

        print(a * b)

#user want to quit from application we set the loop variable False and our while loop stopped
    def exit(self):
        print("quitting")
        time.sleep(1)
        self.loop = False
        exit()


system = machine()
#we created a while loop it will work until we want to stop it
while system.loop:
    system.program()

