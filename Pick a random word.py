import random


def random_word():
    print(random.choice(open("sowpods.txt").read().split()))


random_word()
