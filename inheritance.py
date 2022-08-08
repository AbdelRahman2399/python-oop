class Man:
    def __init__(self):
        self.talk1="I am a man"
    def talk(self):
        print(f'{self.talk1}')

class Engineer(Man):
    def __init__(self):
        Man.__init__(self)
        self.talk2="I am an engineer"
    def talkk(self):
        print(f'{self.talk1} and {self.talk2}')


bido= Engineer()
bido.talkk()
