def introduction():
    print("Hello, human, my name is Alexa")
    print("I was created in 2021!")


def your_name():
    print("What's your name?")
    name = input()
    print("Welcome on board, " + name + ".")


def your_age():
    print('Let me show of guessing your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
    print("Your age is " + str(age) + ", you're getting old...")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print("Let's test your programming knowledge.")
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times.")
    print("2. To decompose a program into several small subroutines.")
    print("3. To determine the execution time of a program.")
    print("4. To interrupt the execution of a program.")
    anwser = int(input())
    while anwser != 2:
        print("Wrong! try again.")
        anwser = int(input())
    print("You're right!")


def end():
    print('Great work!')


introduction()
your_name()
your_age()
count()
test()
end()
