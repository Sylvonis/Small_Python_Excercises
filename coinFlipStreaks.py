# Coin Flip Streaks
# For this exercise, we’ll try doing an experiment. If you flip a coin
# 100 times and write down an “H” for each heads and “T” for each tails,
# you’ll create a list that looks like “T T T T H H H H T T.” If you ask a
# human to make up 100 random coin flips, you’ll probably end up with
# alternating head-tail results like “H T H T H H T H T T,” which looks
# random (to humans), but isn’t mathematically random. A human will almost
# never write down a streak of six heads or six tails in a row, even though
# it is highly likely to happen in truly random coin flips. Humans are
# predictably bad at being random.
#
# Write a program to find out how often a streak of six heads or a streak
# of six tails comes up in a randomly generated list of heads and tails.
# Your program breaks up the experiment into two parts: the first part
# generates a list of randomly selected 'heads' and 'tails' values, and
# the second part checks if there is a streak in it. Put all of this code
# in a loop that repeats the experiment 10,000 times so we can find out
# what percentage of the coin flips contains a streak of six heads or
# tails in a row. As a hint, the function call random.randint(0, 1) will
# return a 0 value 50% of the time and a 1 value the other 50% of the time.
#
# You can start with the following template:
#
# import random
# numberOfStreaks = 0
# for experimentNumber in range(10000):
#     # Code that creates a list of 100 'heads' or 'tails' values.
#
#     # Code that checks if there is a streak of 6 heads or tails in a row.
# print('Chance of streak: %s%%' % (numberOfStreaks / 100))

import random

numberOfStreaks = 0


def toss():
    i = random.randint(0, 1)
    if i == 0:
        return 'H'
    else:
        return 'T'


lista = []
streak = 0
for experimentNumber in range(10000):

    for i in range(100):
        lista.append(toss())
    for position in range(100):
        if lista[position] == lista[position - 1]:
            streak += 1
            if streak == 6:
                numberOfStreaks += 1
                streak = 0
        else:
            streak = 0
    lista = []
    print('Chance of streak: %s%%' % (numberOfStreaks / 100))  # the chance will rise according as the numbers rise

    # Code that creates a list of 100 'heads' or 'tails' values.

    # Code that checks if there is a streak of 6 heads or tails in a row.
