class Stoneline:
    def __init__(self, stones):
        self.library = {}

    def blink(self, max_generation, current_generation):
        new_stones = [blinked_stone for stone in self.stones for blinked_stone in stone.blink()]

    def _get_library_value(self, value, generation):
        if value not in self.library:
            return None
        
        generations = self.library[value]
        if (len(generations) < generation):
            generations.extend([-1 for i in range(len(generations, generation))])

        generations[generation] = ???
        