from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):
    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)
class Engine(object):
    def __init__(self,scene_map):
        self.scene_map=scene_map
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
        current_scene.enter()

class Death(Scene):
    quips = [
    "You died. You kinda suck at this.",
    "Your Mom would be proud... if she were smarter.",
    "Such a looser",
    "I have a small puppy that's better at this",
    "You're worse than your Dad's jokes"
    ]
    def enter(self):
        print(Death.quips[randint(0,len(self.quips)-1)])
        exit(1)
class CentralRoom(Scene):
    def enter(self):
        print(dedent("""
        LONG ASS DESCRIPTION
        you're running down the central corridor to the aromory when a gothon
        jumps out, red...blah....
        blah...blah...
        """))
        action = input(">")
        if action == "shoot":
            print(dedent("""
            quick on the draw your yank out...
            your lases hits his costume...
            then he eats you.
            """))
            return 'death'
        elif action=="dodge":
            print(dedent("""
            die as the
            gothom stomps your head
            """))
            return 'death'
        elif action=="joke":
            print(dedent("""
            lucky for
            you fool
            you survive and go
            to the armory.
            """))
            return 'armory'
        else:
            print("invalid input")
            return 'central_room'
class Armory(Scene):
    def enter(self):
        print(dedent("""
        you do dive roll..
        there's a keypad...
        code is 3 digits...
        """))
        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        # print(code)
        guess = input("[keypad]>")
        guesses = 0
        while guess!=code and guesses < 10:
            print("bzzzz!")
            guesses+=1
            guess=input("[keypad]>")
        if guess == code:
            print("spot on")
            return 'bridge'
        else:
            print("die")
            return 'death'
class Bridge(Scene):
    def enter(self):
        print("you're at the bridge")
        action = input("> ")
        if action=='boom':
            print("die")
            return "death"
        elif action=='bomb':
            print("escape")
            return 'escape'
        else:
            print("invalid")
            return "bridge"
class EscapeRoom(Scene):
    def enter(self):
        print("Escape Pod")
        good_pod = randint(1,5)
        # print(good_pod)
        guess = input("[pod #]> ")
        if int(guess) != good_pod:
            print("die")
            return "death"
        else:
            print("good Guess")
            return "finished"
class Finished(Scene):
    def enter(self):
        print("You won! Good job")
        return "finished"



class Map(object):
    scenes = {
    "finished": Finished(),
    "death": Death(),
    "bridge": Bridge(),
    "escape": EscapeRoom(),
    "armory": Armory(),
    "central_room": CentralRoom()
    }
    def __init__(self, start_scene):
        self.start_scene = start_scene
    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val
    def opening_scene(self):
        return self.next_scene(self.start_scene)
a_map = Map("central_room")
a_game = Engine(a_map)
a_game.play()
