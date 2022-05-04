import random

def lotto():
    number = set()
    while len(number) <  6:
        number.add(random.randint(1, 45))
    number = list(number)
    number.sort()

    for i in number:
        print(i, end=" ")
    print()

def run():
    times = int(input("시행 횟수 : "))
    for i in range(times):
        lotto();


run()