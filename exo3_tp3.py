####Q1###
def InitialiserTab(n):
    tab = [0] * n
    return tab
###2###
import random

def InitialiserTabAlea(n):
    tab = []
    for i in range(n):
        tab.append(random.randint(0, 99))
    return tab