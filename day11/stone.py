import math
class Stone:
    def __init__(self, val, generation, library):
        self.val = int(val)
        self.generation = generation
        self.library = library

    def blink(self):
        if self.val == 0:
            return [Stone(1, self.generation - 1, self.library)]

        if self._is_even_digits():
            return self._halfsies()

        return [Stone(self.val * 2024, self.generation - 1, self.library)]

    # def _is_even_digits(self):
    #     # log10 is odd for even digits (ie. log10(999) is 2.999 and log10(1111) is 3.01)
    #     return divmod(math.floor(math.log10(self.val)), 2)[1] == 1

    def _is_even_digits(self):
        return divmod(len(str(self.val)),2)[1] == 0

    def _halfsies(self):
        pow10 = math.ceil(math.ceil(math.log10(self.val)) / 2)
        parts = divmod(self.val, math.pow(10,pow10))
        return [Stone(int(parts[0]), self.generation - 1, self.library), Stone(int(parts[1]), self.generation - 1, self.library)]

    # def _halfsies(self):
    #     s = str(self.val)
    #     h = int(len(s) / 2)
    #     return [Stone(int(s[0:h]), self.generation - 1, self.library), Stone(int(s[h:]), self.generation - 1, self.library)]


    def score(self):
        # If we've already calculated a score for this value at this generation, then we can just return the cached value
        coords = (self.val, self.generation)
        if (coords in self.library):
            return self.library[coords]

        # Base case: If we have no more generations, then we return 1 for myself, a single stone
        if(self.generation == 0):
            self.library[coords] = 1
            return 1

        # Otherwise, blink to reveal the next generation of stones and sum their scores
        substones = self.blink()
        val = sum([stone.score() for stone in substones])
        self.library[coords] = val
        return val

        