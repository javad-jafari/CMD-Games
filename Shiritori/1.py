class Shiritori:
    def __init__(self):
        self.words = list()
        self.game_over = False

    def paly(self,name):
        if len(self.words)==0:
            self.words.append(name)

        elif len(self.words) > 0:
            if name[0] == self.words[-1][-1] and name not in self.words :
                self.words.append(name)

            else:
                self.game_over = True
                return "game over"
        return self.words

    def restart(self):
        self.words.clear()
        self.game_over = False
        return "game restarted"