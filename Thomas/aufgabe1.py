print("Wie heisst du?")
name = input()
print("Hallo", name)

print("Welche zwei Zahlen willst du addieren?")
print("Bitte gebe deine erste Zahl ein?")
zahl1 = int(input())
print("Bitte gebe deine zweite Zahl ein?")
zahl2 = int(input())
summe = zahl1 + zahl2
print("Deine Zahl ist", summe)

password_correct = "Ruag2021$"
print("Bitte gib dein Passwort ein.")
password = input()
if password == password_correct:
    print("Dein Passwort ist correct")
else:
    print("Dein Passwort ist incorrect")

print("Welcher Operator willst du brauchen? +,-,*,/")
operator = str(input())
print("Bitte gebe deine erste Zahl ein?")
zahl1 = int(input())
print("Bitte gebe deine zweite Zahl ein?")
zahl2 = int(input())

if operator == "+":
    sum1 = zahl1 + zahl2
    print(sum1)
elif operator == "-":
    sum2 = zahl1 - zahl2
    print(sum2)
elif operator == "*":
    sum3 = zahl1 * zahl2
    print(sum3)
else:
    sum4 = zahl1 / zahl2
    print(sum4) 

num = range(101)
for x in num:
    print(x)

import random

def guess_num():
    number = random.randint(0,100)
    
    while True:
        guess = input("Rate eine Zahl zwischen 0 und 100. (X ist zum beenden)")

        if guess.lower() == "x":
            print("GAME OVER")
            break

        try:
            guess = int(guess)
        except ValueError:
            print("BITTE GIB EINE ZAHL EIN - NICHTS ANDERES")
            continue

        if guess < number:
            print("Zahl ist grösser als:")
        elif guess > number:
            print("Zahl ist kleiner als:")
        else:
            print("Gut gemacht. Du hast es erraten.")
            play_again = input("Willst du nochmals spielen? antworte mit Ja oder Nein ")
            if play_again == "Ja":
                number = random.randint(0, 100)
                continue
            else:
                break

guess_num()



import turtle

fenster = turtle.Screen()
stift = turtle.Turtle()
fenster.setup(1000, 400)

stift.fd(100)
stift.rt(90)
stift.fd(100)
stift.rt(90)
stift.fd(100)
stift.rt(90)
stift.fd(100)
stift.rt(90)

stift.penup()
stift.fd(200)
stift.pendown()

stift.fd(100)
stift.rt(90)
stift.fd(100)
stift.rt(90)
stift.fd(100)
stift.rt(90)
stift.fd(100)

len1 = 100
rad1 = 25

turtle.penup()
turtle.goto(-len1/2, -len1/2)
turtle.pendown()

turtle.right(90)
turtle.forward(rad1)

turtle.circle(rad1, 90)

turtle.forward(len1 - 2 * rad1)

turtle.circle(rad1, 90)

turtle.forward(len1 - 2 * rad1)

turtle.circle(rad1, 90)

turtle.forward(len1 - 2 * rad1)

turtle.circle(rad1, 90)

turtle.forward(len1 - 2 * rad1)

turtle.circle(rad1, 90)

turtle.forward(rad1)
turtle.right()

input()


stift.fd(100)
stift.rt(120)
stift.fd(50)
stift.rt(60)
stift.fd(100)
stift.rt(120)
stift.fd(50)
stift.rt(60)


turtle.write("Thomas")
input()
12
import random
import string

def password_generator(len):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(len))
    return password

def main():
    len = int(input("Wie lang soll das Passwort sein?"))
    password = password_generator(len)
    print("Dein neues Passwort", password)

if __name__ == "__main__":
    main()


def berechne_quersumme(num):
    quersum = sum(int(digit) for digit in str(num))
    return quersum

def main():
    num = int(input("Geben Sie eine Zahl ein: "))
    quersum = berechne_quersumme(num)
    print("Die Quersumme der Zahl", num, "ist", quersum)

main()

def rechteck_zeichnen(breite, höhe):
    for i in range(höhe):
        for j in range(breite):
            print("*", end="")
        print()


print("Deine breite")
breite = int(input())
print("Deine höhe")
höhe = int(input())

rechteck_zeichnen(breite, höhe)


from turtle import *
import turtle as tur

tur = tur.Turtle()

tur.penup ()
tur.left (90)
tur.fd (200)
tur.pendown ()
tur.right (90)
 

tur.fillcolor ("red")
tur.begin_fill ()
tur.circle (10,180)
tur.circle (25,110)
tur.left (50)
tur.circle (60,45)
tur.circle (20,170)
tur.right (24)
tur.fd (30)
tur.left (10)
tur.circle (30,110)
tur.fd (20)
tur.left (40)
tur.circle (90,70)
tur.circle (30,150)
tur.right (30)
tur.fd (15)
tur.circle (80,90)
tur.left (15)
tur.fd (45)
tur.right (165)
tur.fd (20)
tur.left (155)
tur.circle (150,80)
tur.left (50)
tur.circle (150,90)
tur.end_fill ()
 

tur.left (150)
tur.circle (-90,70)
tur.left (20)
tur.circle (75,105)
tur.setheading (60)
tur.circle (80,98)
tur.circle (-90,40)

tur.left (180)
tur.circle (90,40)
tur.circle (-80,98)
tur.setheading (-83)

tur.fd (30)
tur.left (90)
tur.fd (25)
tur.left (45)
tur.fillcolor ("dark green")
tur.begin_fill ()
tur.circle (-80,90)
tur.right (90)
tur.circle (-80,90)
tur.end_fill ()
tur.right (135)
tur.fd (60)
tur.left (180)
tur.fd (85)
tur.left (90)
tur.fd (80)
 
tur.right (90)
tur.right (45)
tur.fillcolor ("dark green")
tur.begin_fill ()
tur.circle (80,90)
tur.left (90)
tur.circle (80,90)
tur.end_fill ()
tur.left (135)
tur.fd (60)
tur.left (180)
tur.fd (60)
tur.right (90)
tur.circle (200,60)

input()

tur.rt(45)
tur.fd(100)


import turtle
f = turtle.Screen()
s = turtle.Turtle()
f.setup(1000, 400)

s.lt(45)
s.fd(89)
s.lt(225)
s.fd(33)
s.rt(90)
s.fd(33)
s.lt(90)
s.fd(33)
s.rt(45)
s.fd(40)
s.rt(135)
s.fd(33)
s.rt(180)
s.fd(33)
s.rt(270)
s.fd(60)
s.rt(270)
s.fd(30)
s.rt(270)
s.fd(30)


input()
