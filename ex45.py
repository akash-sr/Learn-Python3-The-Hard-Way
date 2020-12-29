# The GAME
from sys import exit
from random import randint
from os import system, name
import time

def clear():
    if name == 'nt':
        # this is for windows
        system('cls')
    else:
        # this is for unix OS
        system('clear')  # Works only for linux

# Pokemon parent
class Pokemon(object):
    def attack(self):
        print(f"{type(self).__name__} uses {self.attacks[randint(0,1)]} !!!")
    def fainted(self):
        print(f"{type(self).__name__} has fainted...")
# Pokemons
class Onix(Pokemon):
    attacks = []
    type = None
    used = False
    def __init__(self):
        self.attacks.append("rock slide")
        self.attacks.append("whip")
        self.type = "rock"


class Macho(Pokemon):
    attacks = []
    type = None
    used = False
    def __init__(self):
        self.attacks.append("knock out")
        self.attacks.append("body smash")
        self.type = "rock"

class Blastoise(Pokemon):
    attacks = []
    type = None
    used = False
    def __init__(self):
        self.attacks.append("water blast")
        self.attacks.append("smash")
        self.type = "water"

class Infernape(Pokemon):
    attacks = []
    type = None
    used = False
    def __init__(self):
        self.attacks.append("fire blast")
        self.attacks.append("combat")
        self.type = "fire"

class Pikachu(Pokemon):
    attacks = []
    type = None
    used = False
    def __init__(self):
        self.attacks.append("giga shock")
        self.attacks.append("electric takle")
        self.type = "electric"

class Voltrob(Pokemon):
    attacks = []
    type = None
    used = False
    def __init__(self):
        self.attacks.append("giga shock")
        self.attacks.append("discharge")
        self.type = "electric"

# Role parent
class Role(object):
    def __init__(self):
        pass
    def lineup(self):
        pass
# Roles
class GymLeader(Role):
    pokemons=[]
    def __init__(self):
        self.pokemons.append(Pikachu())
        self.pokemons.append(Voltrob())
class Challenger(Role):
    pokemons=[]
    def __init__(self):
        self.pokemons.append(Onix())
        self.pokemons.append(Blastoise())
        self.pokemons.append(Macho())
        self.pokemons.append(Infernape())
# Scene parent
class Scene(object):
    def enter(self,gym_leader,player):
        exit(1)
# Scenes
class Victory(Scene):
    def enter(self,gym_leader,player):
        time.sleep(2)
        clear()
        print("Congratulations!! You've won the Electra Badge")
        print("""
                            /
                          ///
                        ////
                      //////////
                          ////
                         ///
                         /
        """)
        exit(1)
class Defeat(Scene):
    def enter(self,gym_leader,player):
        print("Better luck next time...")
        exit(1)

class First(Scene):
    def enter(self,gym_leader, player):
        print("First Battle!")
        self.gp = gym_leader.pokemons[0]
        self.gp.used = True
        print(f"GymLeader Ash chooses {type(self.gp).__name__}")
        self.p = int(input("Choose your Pokemon > "))
        if self.p < 4:
            self.mp = player.pokemons[self.p]
            self.mp.used = True
        else:
            print("Heh, Nice try! You LOST!")
            exit(1)
        print(f"You choose {type(self.mp).__name__}")
        print("\n")
        if self.mp.type != "rock":
            self.mp.attack()
            self.gp.attack()
            self.mp.fainted()
            print("You Loose!")
            return "defeat"
        else:
            self.gp.attack()
            self.mp.attack()
            self.gp.fainted()
            print("That's good, you move to the next round...")
            return "finale"
class Finale(Scene):
    def enter(self,gym_leader,player):
        print("Final Battle!")
        self.gp = gym_leader.pokemons[1]
        print(f"GymLeader Ash chooses {type(self.gp).__name__}")
        self.p = int(input("Choose your Pokemon > "))
        if self.p < 4:
            self.mp = player.pokemons[self.p]
        else:
            print("INVALID")
            return "finale"
        if self.mp.used == True:
            print(f"{type(self.mp).__name__} has low HP...")
            return "defeat"
        print(f"You choose {type(self.mp).__name__}")
        print("\n")
        if self.mp.type != "rock":
            self.mp.attack()
            self.gp.attack()
            self.mp.fainted()
            print("All you're pokemons have fainted...")
            return "defeat"
        else:
            self.gp.attack()
            self.mp.attack()
            self.gp.fainted()
            print("You've defeated the GymLeader!!!")
            return "victory"
class Welcome(Scene):
    def enter(self,gym_leader,player):
        print("Welcome to the Electro Gym of the Univer region!")
        print("\n")
        print("Your Pokemons:")
        for i in range(len(player.pokemons)):
            print(f"{type(player.pokemons[i]).__name__} {i}")
        print("\n")
        print("Gym Leader's Pokemons:")
        for i in range(len(gym_leader.pokemons)):
            print(f"{type(gym_leader.pokemons[i]).__name__} {i}")
        return "first"
# Map
class Map(object):
    scenes = {
    "victory":Victory(),
    "finale":Finale(),
    "first":First(),
    "defeat":Defeat(),
    "welcome": Welcome()
    }
    def __init__(self,start_scene):
        self.start_scene = start_scene
    def next_scene(self,scene_name):
        val = Map.scenes.get(scene_name)
        return val
    def opening_scene(self):
        return self.next_scene(self.start_scene)
# Engine
class Engine(object):
    def __init__(self,scene_map):
        self.scene_map=scene_map
    def play(self):
        Ash = GymLeader()
        Reacher = Challenger()
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene("victory")
        while current_scene != last_scene:
            next_scene_name = current_scene.enter(Ash,Reacher)
            current_scene = self.scene_map.next_scene(next_scene_name)
        current_scene.enter(Ash,Reacher)
clear()
the_map = Map("welcome")
the_game = Engine(the_map)
the_game.play()
