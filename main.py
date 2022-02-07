import sys
import time
import random
from sys import exit

deathArt = open("death_art.txt")

class Death(object):

    def start(self):
        print(deathArt.read())
        deathArt.close()
        print("\nYou died.")
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('six-am')

        while current_scene != last_scene:
            next_scene_name = current_scene.start()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.start()

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