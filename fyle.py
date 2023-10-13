"""
Create a game using the classes you defined. For this, you will need to:
- Create a new `file.py`
- Import the classes you defined earlier
- Define functions to create the workflow of the game: i.e. functions to create teams
(maybe you can create random teams with your classmates' names), run the game, etc.

"""
from vikingsClasses import Soldier, Viking, Saxon, War

soldado = input("Chose your team. Type VIKING or SAXON")
while soldado.upper() != "VIKING" and soldado.upper() != "SAXON":
    soldado = input("Wrong team, choose again. Type VIKING or SAXON")

if soldado.upper() == "VIKING":
    name = input("Please, name your soldier, good luck: ")

strength = input("Choose your strength wisely from 1-100:")


    
    
    
    
    
    