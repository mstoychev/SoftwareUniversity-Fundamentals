class Zoo:
    __animals = 0

    def __init__(self, name_zoo):
        self.name_zoo = name_zoo
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        result = ""
        if species == "mammal":
            result += f"Mammals in {self.name_zoo}: {', '.join(self.mammals)}\n"
        elif species == "fish":
            result += f"Fishes in {self.name_zoo}: {', '.join(self.fishes)}\n"
        elif species == "bird":
            result += f"Birds in {self.name_zoo}: {', '.join(self.birds)}\n"

        result += f"Total animals: {Zoo.__animals}"
        return result


zoo_name = input()
zoo = Zoo(zoo_name)
n = int(input())
for _ in range(n):
    command = input().split()
    species = command[0]
    name = command[1]
    zoo.add_animal(species, name)

type_specie = input()
print(zoo.get_info(type_specie))
