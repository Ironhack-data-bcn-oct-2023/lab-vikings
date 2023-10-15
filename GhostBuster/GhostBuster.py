# %%
import random as rd

names = ["aída", "Amir", "ana","bego","claudia","Edward", "Emma", "Esther", "Leon", "Junior", "Lucia", "Maira", "Marc", "Marco", "Marta", "Miquel", "Noemi", "Patricia", "Pati", "Ricardo", "Sara", "Uri", "Victor", "Xavier"]

rd.shuffle(names)

division_team = int(len(names) / 2)

team_hunter = names[:division_team]

team_ghost = names[division_team:]


class Soldier:
    
    def __init__(self, health, strength):
        
        self.health = health
        self.strength = strength
        
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health -= damage
        

 ## TEAM 1 ##

class Hunters(Soldier):
    
    def __init__(self, name_team1, health, strength):
        
        super().__init__(health, strength)
        self.name_team1 = name_team1
        
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return "{} has received {} points of damage".format(self.name_team1, damage)
        else: 
            return "{} has died in act of combat".format(self.name_team1)
        
    def battleCry(self):
        return "For Glory and Victory!"
    
    
class Ghosts(Soldier):
    
    def __init__(self, name_team2, health, strength):
        
        super().__init__(health, strength)
        self.name_team2 = name_team2
    
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return "{} has received {} points of damage".format(self.name_team2, damage)
        else:
            return "{} has died in combat".format(self.name_team2)
    
    def battleCry(self):
        return "No Mercy, No Regrets!"
    
    
        
class GhostBusters(Soldier):
    
    def __init__(self, team_hunter, team_ghost):
        self.hunting_squad = team_hunter
        self.ghost_squad = team_ghost

    def hunterAttack(self):
        if not self.ghost_squad:
            return "There are no ghosts left to attack."
        
        random_hunter = rd.choice(self.hunting_squad)
        random_ghost = rd.choice(self.ghost_squad)
        
        damage = random_hunter.attack()
        result = random_ghost.receiveDamage(damage)
        
        if random_ghost.health <= 0:
            self.ghost_squad.remove(random_ghost)
        
        return result

    def ghostAttack(self):
        if not self.hunting_squad:
            return "There are no hunters left to possess."
        
        random_ghost = rd.choice(self.ghost_squad)
        random_hunter = rd.choice(self.hunting_squad)
        
        damage = random_ghost.attack()
        result = random_hunter.receiveDamage(damage)
        
        if random_hunter.health <= 0:
            self.hunting_squad.remove(random_hunter)
        
        return result

    def showStatus(self):
        
        if not self.ghost_squad:
            return "Hunters have won the hunting of the century"
        
        elif not self.hunting_squad:
            return "Ghosts have possessed the bodies of hunters"
        
        else:
            return "Hunters and Ghosts are still in the thick of battle!!"

        



