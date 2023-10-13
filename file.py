from vikingsClasses import Soldier
from vikingsClasses import Viking
from vikingsClasses import Saxon
from vikingsClasses import War

import random as rn

'''
def new_viking_team(n_vikings):
    vikings=[]  
    for i in range(n_vikings):
        vikings.append(Viking('viking'+i, rn.randint(1,100), rn.randint(1,100)))
    return vikings

def new_saxon_team(n_saxons):
    saxons=[]
    for i in range(n_saxons):
        saxons.append(Saxon(rn.randint(1,100),rn.randint(1,100)))
    return saxons
'''

def war(n_vikings, n_saxons, days_of_battles=1000000000):
    days=0
    guerra=War() 
    for i in range(n_vikings):
        viking_sold = Viking('viking', rn.randint(1,50), rn.randint(1,50))
        guerra.addViking(viking_sold)        
    for i in range(n_saxons):
        saxon_soldier = Saxon(rn.randint(1,50),rn.randint(1,50))
        guerra.addSaxon(saxon_soldier)

    while days < days_of_battles and guerra.saxonArmy and guerra.vikingArmy:
        coin=rn.randint(0,1)
        if coin:
            guerra.vikingAttack()
        else:
            guerra.saxonAttack()
        days+= 1
    
    return guerra.showStatus()


war(10,10)

