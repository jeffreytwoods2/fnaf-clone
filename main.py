from time import sleep
from random import randint
from sys import exit
from textwrap import dedent

clock = ['2 AM', '2:30 AM', '3 AM', '3:30 AM', '4 AM', '4:30 AM', '5 AM', '5:30 AM', '6 AM']
timeIndex = 0

class Death():

    def start(self):
        with open("death_art.txt", "r") as ded:
            print(ded.read())
        sleep(0.5)
        print("You died.")
        exit(1)

class Midnight():

    def start(self):
        print(dedent("""
            *phone rings*

            Hey there, welcome to your first night on the job!
            Our pizzeria provides the best in animatronic entertainment
            for the children of our community.

            Fredbear, our lead animatronic, is equipped with quite the advanced AI.
            When the pizzeria closes, he shows himself off stage and stores himself in the backroom.

            I'll let you in on another secret: his eyes are cameras, equipped with face-recognition technology.
            We've teamed up with state law enforcement to help identify predators who may be attending 
            childrens' parties illegally.

            Unfortunately, we haven't worked out every kink, and Fredbear still doesn't have a proper night
            mode. When the pizza place is closed, he believes that he's in the wrong room and heads out 
            to find the nearest human...which would be you during the night shift.

            He also seems to act more aggressive toward adults at night, which is why we needed a night guard
            ...so he doesn't escape and cause any harm in town. If you see him appear in the hallway, flash your
            light in his eyes; that seems to reset his circuits and send him back to the storage room.

            If it doesn't quite work for some reason and Fredbear is upon you, I've provided you with a spare animatronic mask. Put it over
            your face, and Fredbear will assume that you're just another robobt and leave the room.

            Type 'mask' (no quotes) to quickly put on your mask.
            Type 'check' to check the security camera in the storage room.
            Type 'shine' to shine your flashlight in Fredbear's eyes.
            Type 'time' to check the time of night.
        """))
    
        while True:
            ready = input("\nType 'y' when you're ready to begin the shift:\n>")

            if ready == "y":
                return "hallway_empty"

            elif ready == "mask":
                print("Um, ok, you randomly raise your mask.")

            elif ready == "check":
                print("Fredbear is there in storage, where he should be...and he's looking directly into the camera...")
            
            elif ready == "shine":
                print("You shine your light on the empty hallway.")

            elif ready == "time":
                print(f"The time is currently {clock[timeIndex]}")

            else:
                print("You mistyped something, Fredbear runs up and kills you immediately.")
                exit(1)

class HallwayEmpty():
    def start(self):
        print("The hallway is empty. Might be a good idea to check the camera.")

        while True:
            action = input("mask, shine, check, time:\n>")

            if action == "mask":
                print("Good precaution. You raise your mask for a sec.")
            elif action == "shine":
                print("You flash your light down the hallway. Still empty.")
            elif action == "check":
                coinToss = randint(0, 1)

                if coinToss:
                    print("...")
                    sleep(0.5)
                    print("...Fredbear is gone.")
                    sleep(1.5)

                    rollDie = randint(0, 2)
                    fredSceneArray = [
                        "fredbear_far",
                        "fredbear_near",
                        "fredbear_at_desk"
                    ]
                    return fredSceneArray[rollDie]
                else:
                    print("Phew, Fredbear is still in storage...can he see me through the camera...?\n")
                    global timeIndex 
                    timeIndex += 1
                    return "hallway_empty"
            elif action == "time":
                print(f"The time is currently {clock[timeIndex]}")
            else:
                print("Typo? I didn't quite catch that.")
                    
class FredbearFar():
    def start(self):
        print("You lower the camera and catch something at the end of the hall.\n\nIt's Fredbear.")
        while True:
            action = input("mask, shine, check, time:\n>")

            if action == "mask":
                print("You raise your mask, but I'm not sure if it makes a difference from here.")
            elif action == "shine":
                print("You flash your light down the hallway.")
                coinToss = randint(0, 1)
                if coinToss:
                    print("Thank god, it worked. Fredbear resets and returns to storage.")
                    global timeIndex
                    timeIndex += 1
                    return "hallway_empty"
                else:
                    print("The light didn't seem to work...")
                    fredbearMovement = randint (0, 1)
                    fredSceneArray = [
                        "fredbear_near",
                        "fredbear_at_desk"
                    ]
                    return fredSceneArray[fredbearMovement]
            elif action == "check":
                print("You check the camera for no good reason, and Fredbear advances.\n")
                fredbearMovement = randint (0, 1)
                fredSceneArray = [
                    "fredbear_near",
                    "fredbear_at_desk"
                ]
                return fredSceneArray[fredbearMovement]
            elif action == "time":
                print(f"The time is currently {clock[timeIndex]}")
            else:
                print("Typo? I didn't quite catch that.")

class FredbearNear():
    def start(self):
        print("Dear lord...Fredbear is standing just outside the office.")
        while True:
            action = input("mask, shine, check, time:\n>")

            if action == "mask":
                print("You raise your mask, but Fredbear is still too far away to examine it.")
            elif action == "shine":
                print("You flash your light directly at Fredbear.")
                coinToss = randint(0, 1)
                if coinToss:
                    print("Thank god, it worked. Fredbear resets and returns to storage.")
                    global timeIndex
                    timeIndex += 1
                    return "hallway_empty"
                else:
                    print("You flash the light, but Fredbear doesn't care.")
                    sleep(1)
                    return "fredbear_at_desk"
            elif action == "check":
                print("You check the camera at an awful time. The storage room is obviously empty.\n")
                sleep(1)
                return "fredbear_at_desk"
            elif action == "time":
                print(f"The time is currently {clock[timeIndex]}")
            else:
                print("Typo? I didn't quite catch that.")

class FredbearAtDesk():
    def start(self):
        print("FREDBEAR IS AT YOUR DESK. LIFT YOUR MASK NOW.")

        action = input("mask, mask, mask\n>")

        if action == "mask":
            print("You raise your mask in the nick of time. Fredbear returns to storage.")
            global timeIndex
            timeIndex += 1
            return "hallway_empty"
        else:
            print("Wrong move.")
            sleep(1)
            return "death"
        
class SixAm():
    def start(self):
        print("It's 6 AM! The sun comes out, and Fredbear heads for the stage.")
        exit(1)

class Engine():
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('six-am')

        while timeIndex < 8:
            next_scene_name = current_scene.start()
            current_scene = self.scene_map.next_scene(next_scene_name)

        last_scene.start()

class Map():
    scenes = {
        'midnight': Midnight(),
        'hallway_empty': HallwayEmpty(),
        'fredbear_far': FredbearFar(),
        'fredbear_near': FredbearNear(),
        'fredbear_at_desk': FredbearAtDesk(),
        'death': Death(),
        'six-am': SixAm(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        get_next_scene = Map.scenes.get(scene_name)
        return get_next_scene

    def opening_scene(self):
        return self.next_scene(self.start_scene)

first_scene = Map('midnight')
start_engine = Engine(first_scene)
start_engine.play()