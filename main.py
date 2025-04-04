import random

# Абстрактний клас Visitor
class Visitor:
    def __init__(self, name, race):
        self.name = name
        self.race = race

    def interact(self):
        pass


# Клас Customer (звичайні відвідувачі)
class Customer(Visitor):
    def __init__(self, name, race):
        super().__init__(name, race)

    def interact(self):
        return f"{self.name} (Customer) enjoys the tavern."


# Клас Adventurer (герої з особливими потребами)
class Adventurer(Visitor):
    def __init__(self, name, race, quest):
        super().__init__(name, race)
        self.quest = quest

    def interact(self):
        return f"{self.name} (Adventurer) seeks information about their quest: {self.quest}"


# Клас Troublemaker (проблемні відвідувачі)
class Troublemaker(Visitor):
    def __init__(self, name, race):
        super().__init__(name, race)

    def interact(self):
        return f"{self.name} (Troublemaker) is causing trouble!"


# Клас MenuItem (страви та напої)
class MenuItem:
    def __init__(self, name, type_of_item, magical_property):
        self.name = name
        self.type_of_item = type_of_item
        self.magical_property = magical_property

    def prepare(self):
        return f"Preparing {self.name} ({self.type_of_item}) with magical effect: {self.magical_property}"


# Клас Room (приміщення таверни)
class Room:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def describe(self):
        return f"Room: {self.name}, Capacity: {self.capacity}"


# Клас Event (спеціальні події в таверні)
class Event:
    def __init__(self, name, event_type, date):
        self.name = name
        self.event_type = event_type
        self.date = date

    def organize(self):
        return f"Organizing event: {self.name} ({self.event_type}) on {self.date}"


# Клас QuestBoard (генерація та управління квестами)
class QuestBoard:
    def __init__(self):
        self.quests = []

    def add_quest(self, quest):
        self.quests.append(quest)

    def display_quests(self):
        return "\n".join([f"Quest: {quest}" for quest in self.quests])

    def generate_random_quest(self):
        random_quests = [
            "Defeat the dragon",
            "Find the lost artifact",
            "Rescue the kidnapped prince"
        ]
        return random.choice(random_quests)


# Клас Tavern (основна таверна)
class Tavern:
    def __init__(self):
        self.visitors = []
        self.menu = []
        self.rooms = []
        self.events = []
        self.quest_board = QuestBoard()

    def serve_visitor(self, visitor):
        print(visitor.interact())

    def prepare_item(self, item):
        print(item.prepare())

    def organize_event(self, event):
        print(event.organize())

    def manage_inventory(self, item):
        print(f"Inventory managed: {item.name}")

    def resolve_conflict(self, troublemaker):
        print(f"Resolving conflict with {troublemaker.name}!")

    def display_menu(self):
        print("\nTavern Menu:")
        for item in self.menu:
            print(item.prepare())

    def display_rooms(self):
        print("\nTavern Rooms:")
        for room in self.rooms:
            print(room.describe())

    def add_visitor(self, visitor):
        self.visitors.append(visitor)

    def add_menu_item(self, item):
        self.menu.append(item)

    def add_room(self, room):
        self.rooms.append(room)

    def add_event(self, event):
        self.events.append(event)

    def display_quests(self):
        print("\nQuest Board:")
        print(self.quest_board.display_quests())

    def generate_random_quest(self):
        quest = self.quest_board.generate_random_quest()
        print(f"Generated Quest: {quest}")


# Створення екземплярів та взаємодія
tavern = Tavern()

# Додавання відвідувачів
visitor1 = Customer("Arin", "Human")
visitor2 = Adventurer("Thorn", "Elf", "Find the magical sword")
visitor3 = Troublemaker("Grunt", "Orc")

tavern.add_visitor(visitor1)
tavern.add_visitor(visitor2)
tavern.add_visitor(visitor3)

# Додавання страв
item1 = MenuItem("Elven Wine", "Drink", "Increases magic power for 1 hour")
item2 = MenuItem("Dwarven Stew", "Food", "Restores health")

tavern.add_menu_item(item1)
tavern.add_menu_item(item2)

# Додавання приміщень
room1 = Room("Main Hall", 50)
room2 = Room("Private Room", 10)

tavern.add_room(room1)
tavern.add_room(room2)

# Додавання подій
event1 = Event("Tavern Brawl", "Fight", "2025-04-10")
event2 = Event("Magical Potion Tasting", "Tasting", "2025-04-15")

tavern.add_event(event1)
tavern.add_event(event2)

# Додавання квестів
tavern.quest_board.add_quest("Defeat the dragon")
tavern.quest_board.add_quest("Find the lost artifact")

# Операції з таверною
print("\n=== Serving Visitors ===")
tavern.serve_visitor(visitor1)
tavern.serve_visitor(visitor2)
tavern.serve_visitor(visitor3)

print("\n=== Preparing Menu Items ===")
tavern.prepare_item(item1)
tavern.prepare_item(item2)

print("\n=== Organizing Events ===")
tavern.organize_event(event1)
tavern.organize_event(event2)

print("\n=== Managing Inventory ===")
tavern.manage_inventory(item1)
tavern.manage_inventory(item2)

print("\n=== Resolving Conflicts ===")
tavern.resolve_conflict(visitor3)

# Виведення меню та приміщень
tavern.display_menu()
tavern.display_rooms()

# Виведення квестів
tavern.display_quests()

# Генерація випадкового квесту
tavern.generate_random_quest()