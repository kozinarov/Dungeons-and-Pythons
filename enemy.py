class Enemy:
    def __init__(self, name="Bron", title="Dragonslayer", health=100, mana=100, damage=20):
        self._name = name
        self._title = title
        self._health = health
        self._max_health = health
        self._mana = mana
        self._damage = damage
        self._weapon_equipped = None
        self._spell_learned = None

    def __str__(self):
        message = "Your Enemy is {} the {} and have: {} health, {} mana."
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
        return self._spell_learned and self._mana >= self._spell_learned.get_mana_cost()

    def take_damage(self, damage_points):
        if self.get_health() <= damage_points:
            self._health = 0
        else:
            self._health -= damage_points

    def take_healing(self, healing_points):
        if self.is_alive():
            if self.get_health() + healing_points >= self._max_health:
                self._health = self._max_health
            else:
                self._health += self.get_health()
            return True
        else:
            return False

    def take_mana(self, mana_points):
        if self._mana + mana_points > self._max_mana:
            self._mana = self._max_mana
        else:
            self._mana += mana_points

    def equip(self, weapon):
        self._weapon_equipped = weapon

    def learn(self, spell):
        self._spell_learned = spell

    def attack(self, ws="weapon"):
        if ws == "weapon":
            if self._weapon_equipped is None:
                print("No weapon equiped")
                return 0
            return self._weapon_equipped.get_damage()
        if ws == "spell":
            if self._spell_learned is None:
                print("No spell learned")
                return 0
            if self.can_cast():
                self._mana -= self._spell_learned.get_mana_cost()
                return self._spell_learned.get_damage()
            return 0
