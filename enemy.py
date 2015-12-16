class Enemy:
    def __init__(self, name="Bron", title="Dragonslayer", health=100, mana=100, damage=20):
        self._name = name
        self._title = title
        self._health = health
        self._mana = mana
        self._damage = damage

    def __str__(self):
        message = "Your Enemy is {} the {} and you have: {} health, {} mana."
        return message.format(self._name, self._title, self._health, self._mana)

    def __repr__(self):
        return self.__str__()

    def known_as(self):
        return "{} the {}".format(self._name, self._title)

    def get_health(self):
        return self._health

    def get_mana(self):
        return self._mana

    def is_alive(self):
        return self.get_health() > 0

    def can_cast(self):
        return self.can_cast > 0

    def take_damage(self, damage_points):
        if self.get_health() <= damage_points:
            self._health = 0
        else:
            self._health = self._health - damage_points

    def take_healing(self, healing_points):
        if self.is_alive():
            if self.get_health() + healing_points >= 100:
                self._health = 100
            else:
                self._health = self.get_health() + healing_points
            return True
        else:
            return False

    def take_mana(self, mana_points):
        if self.get_mana() + mana_points <= 0:
            return False
        elif 0 < self.get_mana() + mana_points and self.get_mana() + mana_points <= 100:
            self._mana = self.get_mana() + mana_points
            return True
        else:
            self._mana = 100
            return True

    def equip(self, weapon):
        self.weapon = weapon

    def learn(self, spell):
        self.spell = spell

# golqm problem!!!!!!!
# tuk ne trqbva da podavam obekt a string 

    def attack(self, atack_with):
        if atack_with == 'weapon':
            return self._damage + weapon.get_damage()
        elif atack_with == 'spell':
            self._mana -= spell.get_mana()
            return self._damage + spell.get_damage()
        else:
            raise Exception("Incorect weapon")
