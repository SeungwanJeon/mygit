class Animal:
    def __init__(self, name):
        self.name=name
    def speak(self):
        return 'unknown'

class Dog(Animal):
    def speak(self):
        return '멍멍'

class Cat(Animal):
    def speak(self):
        return '야옹'

animalList=[Dog('dog1'),Dog('dog2'),Cat('cat1')]

for a in animalList:
    print(a.name + ': ' + a.speak())
