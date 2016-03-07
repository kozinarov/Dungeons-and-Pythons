from enemy import Enemy
from hero import Hero
from spell import Spell
from weapon import Weapon
from fight import Fight

import random


class Dungeon:

    def __init__(self, filename):
        self._filename = filename
        self._map = []
        self.read_file()
        self.hero = None

    def read_file(self):
        with open(self._filename, 'r') as data:
            self._map = [list(line) for line in data]

    def print_map(self):
        for row in self._map:
            print(''.join(row))

    def spawn(self, hero):
        for r in range(len(self._map)):
            for c in range(len(self._map[r])):
                if self._map[r][c] == 'S':
                    self._map[r][c] = 'H'
                    self.hero = hero
                    return True
        return False

    def in_map(self, row, col):
        return row < len(self._map) and row >= 0 and col < len(self._map[row]) and col >= 0

    def symbol_in_map(self, row, col):
        if self.in_map(row, col):
            return self._map[row][col]
        return False

    def change_symbol_in_map(self, symbol, row, col):
        self._map[row][col] = symbol

    def get_hero_coord(self):
        for r in range(len(self._map)):
            for c in range(len(self._map[r])):
                if self._map[r][c] == 'H':
                    return [r, c]

    def pick_treasure(self, treasures):
        return random.choice(treasures)

    def _get_treasury(self):
        treasuries = {0: "mana potion",
                      1: "health potion",
                      2: "weapon",
                      3: "spell"}
        treasury = random.randrange(0, 4)
        treasuries[treasury]

    def next_step(self, row, col):
        if self.in_map(row, col):
            if self.symbol_in_map(row, col) is 'G':
                print("Congrats you are goint to the next level")
                return True
            elif self.symbol_in_map(row, col) is '#':
                print("Cannot move in this direction because of obstacle")
                return False
            elif self.symbol_in_map(row, col) is 'E':
                enemy = Enemy()
                battle = Fight(self.hero, enemy)
                battle.start_fight()
                return True
            elif self.symbol_in_map(row, col) is 'T':
                print("You found a treasury")
                s = Spell()
                self.hero.learn_spell(s)
                return True
            else:
                return True
        else:
            print("Out of map")
            return False

    def move_hero(self, direction):
        if direction == 'up':
            coord = self.get_hero_coord()
            if self.next_step(coord[0] - 1, coord[1]):
                self.change_symbol_in_map('.', coord[0], coord[1])
                self.change_symbol_in_map('H', coord[0] - 1, coord[1])

        if direction == 'down':
            coord = self.get_hero_coord()
            if self.next_step(coord[0] + 1, coord[1]):
                self.change_symbol_in_map('.', coord[0], coord[1])
                self.change_symbol_in_map('H', coord[0] + 1, coord[1])

        if direction == 'left':
            coord = self.get_hero_coord()
            if self.next_step(coord[0], coord[1] - 1):
                self.change_symbol_in_map('.', coord[0], coord[1])
                self.change_symbol_in_map('H', coord[0], coord[1] - 1)

        if direction == 'right':
            coord = self.get_hero_coord()
            if self.next_step(coord[0], coord[1] + 1):
                self.change_symbol_in_map('.', coord[0], coord[1])
                self.change_symbol_in_map('H', coord[0], coord[1] + 1)
        return True
