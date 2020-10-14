import sqlite3


def guest_number():
    t,g=random.randint(1,10),0
    g=int(input("Guess a number that's between 1 and 10: "))
    while t!=g:g=int(input("Guess again! "))
    print("That's right!")

# Guess the number: example taken from http://www.rosettacode.org/
if __name__ == '__main__':
    guest_number()