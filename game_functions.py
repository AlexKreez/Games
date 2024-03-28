import copy
import threading
import time
import random

from pynput import keyboard

countWave = 0

target = 0

EffectOn = False

can_buy = False

entrance = False

category = ""

filtered = []

back = False

EffectList = [{"name": "яд", "damage": 1, "time": 10}, {"name": "яд", "damage": 2, "time": 5},
              {"name": "огонь", "damage": 5, "time": 6}, {"name": "лёд", "damage": 7, "time": 7},
              {"name": "тьма", "damage": 13, "time": 8}, {"name": "пустота", "damage": 18, "time": 9},
              {"name": "свет", "damage": 25, "time": 10},
              {"name": "пламя", "damage": 30, "time": 10}, {"name": "сила война", "damage": 40, "time": 10}]


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


class Skill():
    def __init__(self, name, value, cd, effect, type, manacoast):
        self.name = name
        self.cd = cd
        self.value = value
        self.effect = effect
        self.type = type
        self.manacoast = manacoast


skills = [Skill("Fireblast", 50, 10, EffectList[2], "damage_spell", 40),
          Skill("Похищение жизни", 50, 10, EffectList[2], "damage_spell", 30),
          Skill("Берсерк", 50, 10, EffectList[2], "power_spell", 50),
          Skill("хил", 50, 10, [], "heal_spell", 20)]

skils_type = {"damage_spell", "damage_spell", "power_spell", "heal_spell"}

orc = {"name": "Орк варлок", "class": "orc", "attack": 20, "defense": 5, "hp": 400, "hp_max": 400, "skills": [],
       "lvl": 1, "lives": 1, "cost": 25, "Мечи": {}, "mana": 100}

orcmage = {"name": "Орк маг", "class": "orc", "attack": 10, "defense": 5, "hp": 400, "hp_max": 400, "skills": [],
           "lvl": 1, "lives": 1, "cost": 35, "Мечи": {}, "mana": 150}

orcwarrior = {"name": "Орк воин", "class": "orc", "attack": 40, "defense": 10, "hp": 400, "hp_max": 400, "skills": [],
              "lvl": 1, "lives": 1, "cost": 40, "Мечи": {}, "mana": 50}

orchealer = {"name": "Орк жрец", "class": "orc", "attack": 10, "defense": 5, "hp": 200, "hp_max": 200, "skills": [],
             "lvl": 1, "lives": 1, "cost": 15, "Мечи": {}, "mana": 100}

swordsman = {"name": "Мечник", "class": "human", "attack": 50, "defense": 10, "hp": 300, "hp_max": 300, "skills": [],
             "lvl": 1, "exp": 0, "magicResist": 25, "lives": 3, "gold": 10000, "Мечи": {}, "Щиты": {}, "Шлема": {},
             "Кираса": {}, "Поножи": {}, "Наручи": {}}

priest = {"name": "Жрец", "class": "cleric", "attack": 5, "defense": 5, "hp": 500, "hp_max": 500, "skills": [],
          "lvl": 1, "lives": 1, "Мечи": {}}

# Доделать механику скиллов
# Сделать механику блока атак щитом
# Перенести на pygame

mage = {"name": "Маг", "class": "human", "attack": 10, "defense": 5, "hp": 500, "hp_max": 500, "skills": {}, "lvl": 1,
        "lives": 1, "Мечи": []}

swordsman["Мечи"] = Item("Стальной меч", 0, 0, EffectList[0], "Меч", 0, 0)
swordsman["Щиты"] = Item("Деревянный меч", 0, 0, [], "Меч", 0, 3)
swordsman["Шлема"] = Item("Шлем новичка", 0, 0, [], "Меч", 1, 0)
swordsman["Кираса"] = Item("Стальной Кираса", 0, 0, [], "Меч", 1, 0)
swordsman["Поножи"] = Item("Стальные Поножи", 0, 0, [], "Меч", 1, 0)
swordsman["Наручи"] = Item("Кожанные наручи", 0, 0, [], "Меч", 1, 0)

orc["Мечи"] = Item("Стальной меч", 0, 0, [], "Меч", 0, 0)
orcwarrior["Мечи"] = Item("Стальной меч", 0, 0, [], "Меч", 0, 0)
orchealer["Мечи"] = Item("Стальной меч", 0, 0, [], "Меч", 0, 0)
orcmage["Мечи"] = Item("Стальной меч", 0, 0, [], "Меч", 0, 0)
priest["Мечи"] = Item("Стальной меч", 0, 0, [], "Меч", 0, 0)
mage["Мечи"] = Item("Стальной меч", 0, 0, [], "Меч", 0, 0)

orchealer["skills"].append(skills[3])
priest["skills"].append(skills[3])
orc["skills"].append(skills[0])
table_lvls = {"2": 200, "3": 400, "4": 600, "5": 800, "6": 1000, "7": 1300, "8": 1600, "9": 1900, "10": 2500}

type_items = ["Мечи", "Щиты", "Шлема", "Кираса", "Поножи", "Наручи"]

enemies = [[copy.deepcopy(orc)], [copy.deepcopy(orc), copy.deepcopy(orcwarrior)],
           [copy.deepcopy(orc), copy.deepcopy(orcmage), copy.deepcopy(orcwarrior)],
           [copy.deepcopy(orc), copy.deepcopy(orchealer), copy.deepcopy(orcmage), copy.deepcopy(orcwarrior)]]


def Buy(type):
    global filtered
    filtered = list(filter(lambda x: x.type == type, items))
    print("               ", type, "      ")
    for index, item in enumerate(filtered):
        print(index + 1, ".", item.ShowInfo())


def generateEnemies():
    array = [copy.deepcopy(orc), copy.deepcopy(orchealer), copy.deepcopy(orcmage), copy.deepcopy(orcwarrior)]
    wave = []
    for i in range(0, len(enemies) + 1):
        monster = random.choice(array)
        wave.append(monster)
    enemies.append(wave)


def addSkill(unit, skill):
    unit["skills"].append(skills[unit["lvl"] - 1])
    print(str(unit["name"]),
          "получил скилл" + str(unit["skills"][unit["lvl"] - 1]) + " dmg " + str(skills[unit["lvl"] - 1].value))


def targetChange():
    global target
    wave = enemies[countWave]
    if len(wave) >= target + 1:
        return wave[target]
    else:
        print("Начать следующую волну?" + "\n" + "   нажимте SPACE   ")
        return False


def lvlUp(unit):
    exp = unit["exp"]
    for lvl in table_lvls:
        if exp >= table_lvls[lvl]:
            unit["lvl"] = int(lvl)
            print("LVLUP!", unit["lvl"])
            unit["attack"] = unit["attack"] + 10
            unit["defense"] = unit["defense"] + 5
            unit["hp_max"] = unit["hp_max"] + 100
            unit["hp"] = unit["hp_max"]
            if unit["lvl"] == 2:
                swordsman["skills"].append("bladefury")
            if unit["lvl"] == 8:
                addSkill(swordsman, "bladerain")
            if unit["lvl"] == 10:
                addSkill(swordsman, "321")


def attack(attacker, defender):
    global EffectOn
    if not defender:
        return False

    if defender["hp"] <= 0 and attacker["name"] == "Мечник":
        attacker["exp"] = attacker["exp"] + defender["lvl"] * 100
        attacker["gold"] += defender["cost"]
        print("you have killed", defender["name"])
        lvlUp(attacker)

    if defender["hp"] <= 0:
        if attacker["name"] == "Мечник" or attacker["name"] == "Маг" or attacker["name"] == "Жрец":
            global target
            target += 1
            print('у вас нет цели')
            EffectOn = False
            return False
        else:
            print('вы погибли')
            print("Нажмите ESC что бы выйти")
            return False
    if attacker["hp"] <= 0:
        return False
    else:
        defender["hp"] = defender["hp"] - (attacker["attack"] - defender["defense"] + attacker["Мечи"].damage)
        print(swordsman)
    if attacker["name"] == "Мечник" or attacker["name"] == "Маг" or attacker["name"] == "Жрец":
        print("ВЫ наносите урон ", (attacker["attack"] - defender["defense"] + attacker["Мечи"].damage),
              defender["name"], "от атаки", "\n", defender["hp"], "hp от", defender["hp_max"], "hp",
              emoji.emojize(':man:'))
        if swordsman["Мечи"].effect != 0 and EffectOn == False:
            AutoEffect(attacker, defender)
            EffectOn = True

    else:
        print(attacker["name"], "наносит вам урон ", (attacker["attack"] - defender["defense"]), "от атаки", "\n",
              defender["hp"], "hp от", defender["hp_max"], "hp")


def SkillBladefury():
    if swordsman["lvl"] >= 2:
        for i in range(0, len(enemies[countWave])):
            if enemies[countWave][i]["hp"] > 0:
                attack(swordsman, enemies[countWave][i])
    else:
        print("Вашего уровня недостаточно что бы использовать этот скилл")


def Effect(attacker, defender):
    defender["hp"] = defender["hp"] - attacker["Мечи"].effect["damage"]
    print("урона от", attacker["Мечи"].effect["name"], attacker["Мечи"].effect["damage"], "|", defender["hp"], "|")


def clock(interval, attacker, defender, wave):
    while True:
        attack(attacker, defender)
        skillTrigger(attacker, defender, wave)
        time.sleep(interval)


def clockEffect(interval, attacker, defender):
    while True:
        Effect(attacker, defender)
        time.sleep(interval)
        if defender["hp"] <= 0:
            break


def SkillFireblast(caster, target):
    if caster["skills"]:
        target["hp"] -= (skills[0].value - (skills[0].value * target["magicResist"] / 100))
        caster["mana"] -= skills[0].manacoast
        print(target["hp"])


def clockOrcManaregen(interval):
    while True:
        if orc["mana"] < 100:
            orc["mana"] += 2
            print("123456")
        time.sleep(interval)


def OrcManaregen(gainer):
    t = threading.Thread(target=clockOrcManaregen, args=(3, gainer))
    t.daemon = True
    t.start()


def autoAttack(attacker, defender, wave):
    t = threading.Thread(target=clock, args=(3, attacker, defender, wave))
    t.daemon = True
    t.start()


def waves():
    wave = enemies[countWave]
    for index, enemy in enumerate(wave):
        autoAttack(enemy, swordsman, wave)


def rebirth(unit1, unit2, unit3, unit4, unit5, unit6, unit7):
    unit1["hp"] = unit1["hp_max"]
    unit2["hp"] = unit2["hp_max"]
    unit3["hp"] = unit3["hp_max"]
    unit4["hp"] = unit4["hp_max"]
    unit5["hp"] = unit5["hp_max"]
    unit6["hp"] = unit6["hp_max"]
    unit7["hp"] = unit7["hp_max"]


def skillTrigger(attacker, defender, wave):
    # условие дальности
    for enemy in wave:
        print(enemy)
        if enemy["hp"] <= 0.8 * enemy["hp_max"] and len(attacker["skills"]) > 0 and (
                attacker["name"] == "Орк жрец" or attacker["name"] == "Жрец"):
            enemy["hp"] += attacker["skills"][0].value
            print(enemy["name"], "исцелён на", attacker["skills"][0].value)


def AutoEffect(attacker, defender):
    t = threading.Thread(target=clockEffect, args=(attacker["Мечи"].effect["time"], attacker, defender))
    t.daemon = True
    t.start()


def on_press(key):
    try:
        if key == keyboard.Key.esc:
            print('Вы вышли из игры')
    except AttributeError:
        print('special key {0} pressed'.format(
            key))


print(
    "esc- выйти| a- атаковать| u- инвентарь| b- автоатака волны по мечнику| g- узнать количество золота| i- магазин| l-узнать скиллы| q-BlaadeFury|||")


def category_choose(num_type):
    global entrance, category
    type = type_items[num_type]
    Buy(type)


def item_choose(num_item):
    global filtered, entrance
    item = filtered[num_item - 1]
    swordsman[category] = item
    if swordsman["gold"] >= item.cost:
        swordsman["gold"] = swordsman["gold"] - item.cost
        print("Вы купили", item.name)
        entrance = False
    else:
        print("У вас не хватает денег")
        entrance = True


def on_release(key):
    global countWave, target, buy1, can_buy, entrance, category, category, back
    if key == keyboard.Key.esc:
        return False
    if key == keyboard.Key.space:
        rebirth(orc, orcmage, orcwarrior, swordsman, priest, mage, orchealer)
        countWave += 1
        if len(enemies) < countWave + 1:
            generateEnemies()
        print("ВОЛНА" + str(countWave + 1))
        target = 0
    else:
        if key.char == 'a':
            # print(enemies,"\n", target,"\n", countWave)
            attack(swordsman, defender=targetChange())
        if key.char == 'u':
            print('       ИНВЕНТАРЬ    ', "\n",
                  swordsman["Мечи"].name, "| Урон", swordsman["Мечи"].damage, "\n",
                  swordsman["Шлема"].name, "| Защита", swordsman["Шлема"].defense, "\n",
                  swordsman["Щиты"].name, "| Прочность", swordsman["Щиты"].hp, "\n",
                  swordsman["Кираса"].name, "| Защита", swordsman["Кираса"].defense, "\n",
                  swordsman["Поножи"].name, "| Защита", swordsman["Поножи"].defense, "\n",
                  swordsman["Наручи"].name, "| Защита", swordsman["Наручи"].defense)
        if key.char == 'b':
            waves()
        if key.char == 'g':
            print("золото:" + str(swordsman["gold"]))
        if key.char == 'i':
            print("         МАГАЗИН      ")
            print("1.Мечи", "\n",
                  "2.Щиты", "\n",
                  "3.Шлема", "\n",
                  "4.Кираса", "\n",
                  "5.Поножи", "\n",
                  "6.Наручи", "\n")
            can_buy = True
        if can_buy == True and key.char.isdigit() and entrance == False and int(key.char) > 0:
            num_type = int(key.char) - 1
            category_choose(num_type)
            key.char = ''
            entrance = True
        if entrance == True and key.char.isdigit():
            num_item = int(key.char)
            item_choose(num_item)
            can_buy = False

        if key.char == 'l':
            print(swordsman["skills"])
        if key.char == 'q':
            SkillBladefury()
        if key.char == 'm':
            SkillFireblast(orc, swordsman)


with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
