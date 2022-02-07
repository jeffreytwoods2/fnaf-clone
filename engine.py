from threading import currentThread


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