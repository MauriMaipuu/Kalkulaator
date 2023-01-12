import math

class Calculator: #loome klassi
    def liitmine(self, a, b): #defineerime liitmise
        return a + b

    def lahutamine(self, a, b): #defineerime lahutamise
        return a - b

    def korrutamine(self, a, b): #defineerime korrutamise
        return a * b

    def jagamine(self, a, b): #defineerime jagamise
        return a / b

    def siinus(self, a): #defineerime siinuse
        return math.sin(a)

    def cosiinus(self, a): #defineerime cosiinuse
        return math.cos(a)

    def tangens(self, a): #defineerime tangensi
        return math.tan(a)


#loome kalkulaatori objekti
my_cl = Calculator()

while True:
    #kasutaja peab valima operatsiooni mida teha
    print("1: Liida")
    print("2: Lahuta")
    print("3: Korruta")
    print("4: Jaga")
    print("5: Siinus")
    print("6: Cosiinus")
    print("7: Tangens")
    print("8: Välju")

    ch = int(input("Vali operatsioon: "))

    # teeme kindlaks et kasutaja valis õige funktsiooni
    if ch in (1, 2, 3, 4, 5, 6, 7, 8):

        # kontrollime kas kasutaja tahab väljuda
        if (ch == 8):
            break

        # Kui ei siis palume talt esimest ja teist numbrit
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        if (ch == 1):
            print(a, "+", b, "=", my_cl.liitmine(a, b))
        elif (ch == 2):
            print(a, "-", b, "=", my_cl.lahutamine(a, b))
        elif (ch == 3):
            print(a, "*", b, "=", my_cl.korrutamine(a, b))
        elif (ch == 4):
            print(a, "/", b, "=", my_cl.jagamine(a, b))
        elif (ch == 5):
            print("Siinus", a, "=", my_cl.siinus(a))
        elif (ch == 6):
            print("cosiinus", a, "=", my_cl.cosiinus(a))
        elif (ch == 7):
            print("Tangens", a, "=", my_cl.tangens(a))

    else:
        print("Vale sisestus") #kui on vale siis prindime et vale sisestus