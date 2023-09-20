import random

# 主角类
class Hero:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense

    def attack_enemy(self, enemy):
        damage = self.attack - enemy.defense
        if damage > 0:
            enemy.hp -= damage
            print(f"{self.name}攻击了{enemy.name}，造成了{damage}点伤害。")
        else:
            print(f"{self.name}攻击了{enemy.name}，但是没有造成伤害。")

    def defend(self):
        self.defense *= 2
        print(f"{self.name}进入了防御状态，防御力翻倍。")

    def resume_defense(self):
        self.defense //= 2
        print(f"{self.name}的防御状态结束，防御力恢复正常。")

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
            print(f"{self.name}攻击了{hero.name}，造成了{damage}点伤害。")
        else:
            print(f"{self.name}攻击了{hero.name}，但是没有造成伤害。")

    def defend(self):
        self.defense *= 2
        print(f"{self.name}进入了防御状态，防御力翻倍。")

    def resume_defense(self):
        self.defense //= 2
        print(f"{self.name}的防御状态结束，防御力恢复正常。")

# 战斗类
class Battle:
    def __init__(self, hero, enemy):
        self.hero = hero
        self.enemy = enemy

    def start(self):
        print(f"{self.hero.name} vs {self.enemy.name}，战斗开始！")
        while self.hero.hp > 0 and self.enemy.hp > 0:
            self.hero.attack_enemy(self.enemy)
            if self.enemy.hp <= 0:
                break
            self.enemy.attack_hero(self.hero)
        if self.hero.hp > 0:
            print(f"{self.hero.name}获得了胜利！")
        else:
            print(f"{self.enemy.name}获得了胜利！")

# 地图类
class Map:
    def __init__(self, size, terrain):
        self.size = size
        self.terrain = terrain

    def move(self, direction):
        if direction == "up":
            print("向上移动了一格。")
        elif direction == "down":
            print("向下移动了一格。")
        elif direction == "left":
            print("向左移动了一格。")
        elif direction == "right":
            print("向右移动了一格。")
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
            hero.hp += reward
            print(f"{hero.name}获得了{reward}点生命值。")
        else:
            print("无效的事件。")

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
        self.hero = Hero("勇士", 100, 20, 10)
        self.map = Map((10, 10), "平原")
        self.event = Event(True, 100)

    def start(self):
        print("游戏开始！")
        while self.hero.hp > 0:
            direction = input("请输入移动方向（up/down/left/right）：")
            self.map.move(direction)
            event = input("是否触发事件（y/n）：")
            if event == "y":
                event_type = input("请选择事件类型（monster/treasure）：")
                self.map.trigger_event(event_type)
            self.event.trigger()
        print("游戏结束！")

game = Game()
game.start()
