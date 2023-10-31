# FILEPATH: /Users/trysh/project/vscode/aigame/aigame.py
import random

# 主角类
class Hero:
    def __init__(self, name, hp, attack, defense, gold):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.gold = gold
        self.experience = 0  # 新增：经验值
        self.level = 1  # 新增：等级

    # 新增：获得经验
    def gain_experience(self, amount):
        self.experience += amount
        print(f"{self.name}获得了{amount}点经验。")
        if self.experience >= self.level * 100:
            self.level_up()

    # 新增：升级
    def level_up(self):
        self.experience -= self.level * 100
        self.level += 1
        self.hp += 10
        self.attack += 2
        self.defense += 2
        print(f"{self.name}升级了！现在是{self.level}级。")

# 敌人类
class Enemy:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense

    def attack_hero(self, hero):
        damage = self.attack - hero.defense
        if damage > 0:
            hero.hp -= damage
            print(f"{self.name}对{hero.name}造成了{damage}点伤害。")
        else:
            print(f"{self.name}的攻击被{hero.name}防御了。")

    def defend(self):
        self.defense *= 2
        print(f"{self.name}进入了防御状态。")

    def resume_defense(self):
        self.defense //= 2
        print(f"{self.name}结束了防御状态。")

# 战斗类
class Battle:
    def start(self):
        print(f"{self.hero.name}遭遇了{self.enemy.name}！")
        while self.hero.hp > 0 and self.enemy.hp > 0:
            action = input("请选择行动（attack/defend）：")
            if action == "attack":
                self.hero.attack_enemy(self.enemy)
                if self.enemy.hp <= 0:
                    print(f"{self.hero.name}战胜了{self.enemy.name}！")
                    self.hero.gold += random.randint(1, 10) * 10
                    print(f"{self.hero.name}获得了{self.hero.gold}金币。")
                    self.hero.gain_experience(50)  # 新增：获得经验
                    break
                self.enemy.attack_hero(self.hero)
                if self.hero.hp <= 0:
                    print(f"{self.hero.name}被{self.enemy.name}击败了！")
                    break
            elif action == "defend":
                self.hero.defend()
                self.enemy.attack_hero(self.hero)
                if self.hero.hp <= 0:
                    print(f"{self.hero.name}被{self.enemy.name}击败了！")
                    break
                self.hero.resume_defense()
            else:
                print("无效的行动。")

# 地图类
class Map:
    def __init__(self, size, terrain):
        self.size = size
        self.terrain = terrain
        self.shop = Shop()

    def move(self, direction):
        if direction == "up":
            print("向上移动了一格。")
        elif direction == "down":
            print("向下移动了一格。")
        elif direction == "left":
            print("向左移动了一格。")
        elif direction == "right":
            print("向右移动了一格。")
        elif direction == "shop":
            self.shop.visit()
        else:
            print("无效的移动方向。")

    def trigger_event(self, event):
        if event == "monster":
            print("遇到了一只怪物！")
            enemy = Enemy("魔王", 100, 20, 10)
            battle = Battle(hero, enemy)
            battle.start()
        elif event == "treasure":
            print("发现了一处宝藏！")
            reward = random.randint(1, 10) * 10
            hero.gold += reward
            print(f"{hero.name}获得了{reward}金币。")
        else:
            print("无效的事件。")

# 商店类
class Shop:
    def __init__(self):
        self.items = [
            Item("药水", "恢复20点生命值", 50, 20),
            Item("护盾", "提升10点防御力", 100, 10)
        ]

    def visit(self):
        print("欢迎光临！以下是本店的商品：")
        for i, item in enumerate(self.items):
            print(f"{i+1}. {item.name} - {item.description} - {item.price}金币")
        choice = input("请选择要购买的商品编号（输入0退出）：")
        if choice.isdigit():
            choice = int(choice)
            if choice > 0 and choice <= len(self.items):
                item = self.items[choice-1]
                hero.buy_item(item)
            elif choice == 0:
                print("欢迎下次光临！")
            else:
                print("无效的商品编号。")
        else:
            print("无效的输入。")

# 物品类
class Item:
    def __init__(self, name, description, price, effect):
        self.name = name
        self.description = description
        self.price = price
        self.effect = effect

# 事件类
class Event:
    def __init__(self, condition, reward):
        self.condition = condition
        self.reward = reward

    def trigger(self):
        if self.condition:
            print("事件触发！")
            print(f"获得了{self.reward}的奖励。")
        else:
            print("事件未触发。")

# 游戏类
class Game:
    def __init__(self):
        self.hero = Hero("勇士", 100, 20, 10, 0)
        self.map = Map((10, 10), "平原")
        self.event = Event(True, 100)

    def start(self):
        print("游戏开始！")
        while self.hero.hp > 0:
            direction = input("请输入移动方向（up/down/left/right/shop）：")
            self.map.move(direction)
            event = input("是否触发事件（y/n）：")
            if event == "y":
                event_type = input("请选择事件类型（monster/treasure）：")
                self.map.trigger_event(event_type)
            self.event.trigger()
        print("游戏结束！")

game = Game()
game.start()