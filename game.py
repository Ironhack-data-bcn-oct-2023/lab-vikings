import random
from vikingsClasses import War, Viking, Saxon


# Function to create teams
def create_teams(num_vikings, num_saxons):
    viking_team = []
    saxon_team = []

    # Create Viking team
    for _ in range(num_vikings):
        health = random.randint(50, 100) #health between 50 and 100
        strength = random.randint(20, 40) #strenght between 20 and 40
        viking_name = random.choice(viking_names)
        viking = Viking(viking_name, health, strength)
        viking_names.remove(viking_name)  # Remove the selected name from the list
        viking_team.append(viking)

    # Create Saxon team
    for _ in range(num_saxons):
        health = random.randint(30, 60) #health between 30 and 60
        strength = random.randint(5, 15) #strenght between 5 and 15
        saxon = Saxon(health, strength)
        saxon_team.append(saxon)

    return viking_team, saxon_team

# Function to run the game
def run_game(num_vikings, num_saxons):
    # Create teams
    viking_team, saxon_team = create_teams(num_vikings, num_saxons)

    # Create a War instance
    war = War()

    # Add Vikings and Saxons to the war
    for viking in viking_team:
        war.addViking(viking)

    for saxon in saxon_team:
        war.addSaxon(saxon)

    # Main game loop
    while war.vikingArmy and war.saxonArmy: #Loop doesn't stop if theres army in each list
        # Randomly choose an attacker
        attacker = random.choice(["Viking", "Saxon"])

        if attacker == "Viking":
            result = war.vikingAttack()
            
        else:
            result = war.saxonAttack()

        print(result)

    # Determine the outcome
    outcome = war.showStatus()
    print(outcome)

# Entry point of the game
viking_names = ["Javier", "Ricardo", "Edu", "Marco", "Marc", "Noe", "Ana", "Mira", "Martina", "Marta", "Lucia", "Claudia", "Ester", "Felix", "Pati", "Pere", "Amir", "Patricia", "Emma", "Vicotr", "Miquel", "León", "Junior", "Bego", "Fer","Sandra", "Uri"]
if __name__ == "__main__":
    num_vikings = 10 # Adjust the number of Vikings
    num_saxons = 30   # Adjust the number of Saxons
    run_game(num_vikings, num_saxons)
