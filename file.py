from vikingsClasses import War, Viking, Saxon
import random

def createPlayers(arr):
    saxons = []
    vikings = []

    for _ in range(len(arr)//2 + 1):
            saxon = Saxon(200, 5)
            saxons.append(saxon)

    for _ in range(len(arr)):
        random_idx = random.randint(0, len(arr) - 1)
        if arr[random_idx] not in vikings:
            viking = Viking(arr[random_idx], 200, 10)
            vikings.append(viking)

    return [saxons, vikings]


def addPlayers(players):
    
    pass


if __name__ == '__main__':
    names = [
        "Víctor",
        "Ana",
        "Pere",
        "Patty",
        "Sara",
        "Marc",
        "Xavi",
        "Aída",
        "Uri",
        "Ricardo",
        "Lucía",
        "Félix",
        "Esther",
        "Marta",
        "Junior",
        "Martina",
        "Amir",
        "Miki",
        "Noe",
        "Emma",
        "Patricia",
        "Clàudia",
        "Maira",
        "León",
        "Marco",
        "Bego",
        "Fer"
    ]
    war = War()
    players = createPlayers(names)
    addPlayers(players)

