import time
import random
from sys import exit
from textwrap import dedent

# I'm going to use global vars b/c this isn't going to prod, ever.
deathArt = open("death_art.txt")
time = ['2am', '2:30am', '3am', '3:30am', '4am', '4:30am', '5am', '5:30am', '6am']
timeIndex = 0

def wait(pause):
    time.sleep(pause)

class Death(object):

    def start(self):
        print(deathArt.read())
        deathArt.close()
        print("\nYou died.")
        exit(1)

# Midnight is the opening scene, not requiring action from the player. It set the scene and explains how to play
class Midnight(object):

    def start(self):
        print("*phone rings*")
        wait(0.75)
        print(dedent("""
            Hey there, welcome to your first night on the job!
            Our pizzeria provides the best in animatronic entertainment
            for the children of our community.
        """))
        wait(1)
        print(dedent("""
            Fredbear, our lead animatronic, is equipped with quite the advanced AI.
            When the pizzeria closes, he shows himself off stage and stores himself in the backroom.
        """))
        wait(1)
        print(dedent("""
            I'll let you in on another secret: his eyes are cameras, equipped with face-recognition technology.
            We've teamed up with state law enforcement to help identify predators who may be attending 
            childrens' parties illegally.
        """))
        wait(1.5)
        print(dedent("""
            Unfortunately, we haven't worked out every kink, and Fredbear still doesn't have a proper night
            mode. When the pizza place is closed, he believes that he's in the wrong room and heads out 
            to find the nearest human...which would be you during the night shift.
        """))
        wait(1.5)
        print(dedent("""
            He also seems to act more aggressive toward adults at night, which is why we needed a night guard
            ...so he doesn't escape and cause any harm in town. If you seem him appear in the hallway, flash your
            light in his eyes; that seems to reset his circuits and send him back to the storage room.
        """))
        wait(1.5)
        print(dedent("""
            If it doesn't quite work for some reason, I've provided you with a spare animatronic mask. Put it over
            your face, and Fredbear will assume that you're just another robobt and leave the room.
        """))
        wait(1)
        # Print out the instructions of what actions to type
        # shine = shine flashlight in Fredbear's eyes
        # check = check the storage room camera for Fredbear. There's a 50/50 chance he'll be there
            # If he's there, time increments by 1 and HallwayEmpty is sent again.
            # If he's gone, a "3-sided die" is rolled and a random Fredbear scene is sent

# This is the scene where the player may begin to play. Checking the camera here is explained in Midnight class.
# Shining the flashlight won't do anything.
class HallwayEmpty(object):
    def start(self):
        exit(1)

# Descriptive text about Fredbear appearing at end of hallway. 'Shine' action will flip a coin; heads = Fredbear goes back and hour is incremented by 1.
# Tails = either FredbearNear or FredbearAtDesk is sent.
class FredbearFar(object):
    def start(self):
        exit(1)

# Fredbear is near the office. Same mechanics for 'shine' action as FredbearFar, except 'tails' sends FredbearAtDesk.
class FredbearNear(object):
    def start(self):
        exit(1)

# This scene is the only one where the player can die. A 4-second countdown is set, and if the player doesn't put on the mask in time, the Death scene is sent.
# If player sends mask action in time:
    # - a message explains that Fredbear has returned to the storage room
    # - timeIndex is incremented by 1
    # - HallwayEmpty is sent
class FredbearAtDesk(object):
    def start(self):
        exit(1)

# When timeArray = 8, this scene is sent, player wins, game is exited
class SixAm(object):
    def start(self):
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('six-am')

        while timeIndex < 8:
            next_scene_name = current_scene.start()
            current_scene = self.scene_map.next_scene(next_scene_name)

        last_scene.start()

class Map(object):
    scenes = {
        # 'midnight': Midnight(),
        # 'hallway_empty': HallwayEmpty(),
        # 'fredbear_far': FredbearFar(),
        # 'fredbear_near': FredbearNear(),
        # 'fredbear_at_desk': FredbearAtDesk(),
        'death': Death(),
        # 'six-am': SixAm(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        get_next_scene = Map.scenes.get(scene_name)
        return get_next_scene

    def opening_scene(self):
        return self.next_scene(self.start_scene)

start_scene = Map('death')
start_engine = Engine(start_scene)
start_engine.play()