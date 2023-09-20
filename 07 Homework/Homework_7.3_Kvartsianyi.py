import statistics

import random


def average(lst):
    return sum(lst) / len(lst)


def median(lst):
    return statistics.median(lst)


k = 10

data = []

for i in range(k):
    data.append(random.randint(1, k))

print("Вихідні дані: ", data)

print("Середнє значення масиву: ", average(data))

print("Медіана масиву: ", median(data))
