category = ""

filtered = []
entrance = True


class Item():
    def __init__(self, name, damage, cost, effect, type, defense, hp):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.effect = effect
        self.type = type
        self.defense = defense
        self.hp = hp

    def ShowInfo(self):
        string = self.name + " || "
        if self.damage:
            string += " урон: " + str(self.damage) + " | "
        if self.defense:
            string += " защита: " + str(self.defense) + " | "
        if self.hp:
            string += " прочность: " + str(self.hp) + " | "
        if self.effect:
            string += " эффект: " + str(self.effect["name"]) + " | " + " урон от эффекта: " + str(
                self.effect["damage"]) + " | "
        string += " цена: " + str(self.cost)
        return string


EffectList = [{"name": "яд", "damage": 1, "time": 10}, {"name": "яд", "damage": 2, "time": 5},
              {"name": "огонь", "damage": 5, "time": 6}, {"name": "лёд", "damage": 7, "time": 7},
              {"name": "тьма", "damage": 13, "time": 8}, {"name": "пустота", "damage": 18, "time": 9},
              {"name": "свет", "damage": 25, "time": 10},
              {"name": "пламя", "damage": 30, "time": 10}, {"name": "сила война", "damage": 40, "time": 10}]

items = [Item("Отравленный клинок", 10, 50, EffectList[1], "Мечи", 0, 0),
         Item("Огенный меч", 20, 100, EffectList[2], "Мечи", 0, 0),
         Item("Ледяной меч", 40, 250, EffectList[3], "Мечи", 0, 0),
         Item("Меч демона", 70, 500, EffectList[4], "Мечи", 0, 0),
         Item("Меч бездны", 100, 850, EffectList[5], "Мечи", 0, 0),
         Item("Святой меч", 130, 1000, EffectList[6], "Мечи", 0, 0),
         Item("Всесвергающий", 200, 1500, EffectList[7], "Мечи", 0, 0),
         Item("Экскалибур", 500, 8000, EffectList[8], "Мечи", 0, 0),

         Item("Деревянный Щит", 0, 100, [], "Щиты", 5, 10),
         Item("Стальной Щит", 0, 200, [], "Щиты", 5, 20),
         Item("Щит Рыцаря", 0, 300, [], "Щиты", 5, 30),
         Item("Эбонитовый Щит", 0, 400, [], "Щиты", 5, 40),
         Item("Страж феникса", 0, 500, [], "Щиты", 5, 50),
         Item("Ривердем", 0, 600, [], "Щиты", 5, 60),
         Item("Щит бесконечности", 0, 700, [], "Щиты", 5, 70),
         Item("Монарх", 0, 800, [], "Щиты", 5, 80),

         Item("Шлема_1", 0, 100, [], "Шлема", 5, 0),
         Item("Шлема_2", 0, 200, [], "Шлема", 5, 0),
         Item("Шлема_3", 0, 300, [], "Шлема", 5, 0),
         Item("Шлема_4", 0, 400, [], "Шлема", 5, 0),
         Item("Шлема_5", 0, 500, [], "Шлема", 5, 0),
         Item("Шлема_6", 0, 600, [], "Шлема", 5, 0),
         Item("Шлема_7", 0, 700, [], "Шлема", 5, 0),
         Item("Шлема_8", 0, 800, [], "Шлема", 5, 0),

         Item("Кираса_1", 0, 100, [], "Кираса", 5, 0),
         Item("Кираса_2", 0, 200, [], "Кираса", 5, 0),
         Item("Кираса_3", 0, 300, [], "Кираса", 5, 0),
         Item("Кираса_4", 0, 400, [], "Кираса", 5, 0),
         Item("Кираса_5", 0, 500, [], "Кираса", 5, 0),
         Item("Кираса_6", 0, 600, [], "Кираса", 5, 0),
         Item("Кираса_7", 0, 700, [], "Кираса", 5, 0),
         Item("Кираса_8", 0, 800, [], "Кираса", 5, 0),

         Item("Поножи_1", 0, 100, [], "Поножи", 5, 0),
         Item("Поножи_2", 0, 200, [], "Поножи", 5, 0),
         Item("Поножи_3", 0, 300, [], "Поножи", 5, 0),
         Item("Поножи_4", 0, 400, [], "Поножи", 5, 0),
         Item("Поножи_5", 0, 500, [], "Поножи", 5, 0),
         Item("Поножи_6", 0, 600, [], "Поножи", 5, 0),
         Item("Поножи_7", 0, 700, [], "Поножи", 5, 0),
         Item("Поножи_8", 0, 800, [], "Поножи", 5, 0),

         Item("Наручи_1", 0, 100, [], "Наручи", 5, 0),
         Item("Наручи_2", 0, 200, [], "Наручи", 5, 0),
         Item("Наручи_3", 0, 300, [], "Наручи", 5, 0),
         Item("Наручи_4", 0, 400, [], "Наручи", 5, 0),
         Item("Наручи_5", 0, 500, [], "Наручи", 5, 0),
         Item("Наручи_6", 0, 600, [], "Наручи", 5, 0),
         Item("Наручи_7", 0, 700, [], "Наручи", 5, 0),
         Item("Наручи_8", 0, 800, [], "Наручи", 5, 0)]
type_items = ["Мечи", "Щиты", "Шлема", "Кирасы", "Поножи", "Наручи"]


def Buy(category):
    global filtered
    filtered = list(filter(lambda x: x.category == category, items))
    print("               ", category, "      ")
    for index, item in enumerate(filtered):
        print(index + 1, ".", item.ShowInfo())


def category_choose(num_type):
    global entrance, category
    category = type_items[num_type]
    Buy(category)



category_choose(2)
