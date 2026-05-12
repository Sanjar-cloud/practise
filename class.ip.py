# CLASS deep diving
# 1-ENCAPSULATION
# 2-INHERITENCE
# 3-POLIMORPHISM

print("===== INHERITENCE =====")
# PARENT > CHILD

class Animal:  # Parent
    description = "The class creates animals"

    def __init__(self, voice):
        self.status = "then animal alive"
        self.voice = voice

    def make_voice(self):
        print(f"the animal can make voice: {self.voice}")


class Dog(Animal):  # Child
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"{self.name} says: {self.sound} {self.sound}")

    def protect(self):
        print("Yes, I can protect you!")

class cat(Animal):  # Child
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"{self.name} says: {self.sound} {self.sound}")

    def play(self):
        pass

class fish(Animal):  # Child
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"{self.name} says: {self.sound} {self.sound}")

    def swim(self):
        print("Yes, i can swim")

# dog  = Dog("Rex", "wow", True)
cat  = cat("Tom", "myeow", True)
fish = fish("Nemo", "ZzZ", False)


cat.introduce()
fish.introduce()
print("----")

# dog.make_voice()
fish.make_voice()
cat.make_voice()

print(Animal.description)
print(Dog.description)

print(fish.voice, cat.voice)
print("cat.status:", cat.status)
print("fish.status:", fish.status)
