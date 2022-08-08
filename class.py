class Turtles:

    def __init__(self, name, color, weapon):
        self.name = name
        self.color = color
        self.weapon = weapon


raphaelo = Turtles('raphaelo', 'red', 'sai')
print(f'{raphaelo.name} is {raphaelo.color} and uses {raphaelo.weapon}')
donatello = Turtles('donatello', 'purple', 'staff')
print(f'{donatello.name} is {donatello.color} and uses {donatello.weapon}')