class Spell:
    def __init__(self, name="Fireball", damage=30, mana_cost=50, cast_range=2):
        self._name = name
        self._damage = damage
        self._mana_cost = mana_cost
        self._cast_range = cast_range

    def enough_mana(self, mana_available):
        if mana_available < self._mana_cost:
            raise ValueError("Not enough mana")
    
    def get_spell_name(self):
        return self._name

    # tuk v bitkata shte go podam i shte vidi dali ima protivnik v obxvada na magiqta ako ima protivnik shte izvikam cast range funkciqta
    def get_cast_range(self):
        return self._cast_range

    def get_mana_cost(self):
        return self._mana_cost

    def get_damage(self):
        return self._damage

