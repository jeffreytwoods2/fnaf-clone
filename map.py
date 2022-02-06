class Map(object):
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