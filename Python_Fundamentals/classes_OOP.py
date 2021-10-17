import sys

class Animal:
    def __init__(self, habitat, diet):
        self.habitat = habitat
        self.diet = diet

    def speak(self):
        print(f'I live in the {self.habitat} and I eat {self.diet}')

animal = Animal('jungle', 'meat')
speak = animal.speak()

class Lion(Animal): # Inheritance from Base Class Animal
    def __init__(self, title, legs):
        super().__init__('mountains', 'vegetables')
        self.title = title
        self.legs = legs

    def roar(self):
        print(f'I am a {self.title} with {self.legs} and I live in the {self.habitat} eating {self.diet}')

lion = Lion('Lion', 4)
speackLion = lion.speak()
roar = lion.roar()

if __name__ == '__main__':
    globals()[sys.argv[1]]

# From Terminal:
# python classes_OOP.py speak
# I live in the jungle and I eat meat
