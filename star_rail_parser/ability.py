class Ability:
    def __init__(self, skill_id, name, lvl, max_lvl, element, ability_type, effect, small_desc, desc):
        self.id = skill_id
        self.name = name
        self.lvl = lvl
        self.max_lvl = max_lvl
        self.element = element
        self.type = ability_type
        self.effect = effect
        self.small_desc = small_desc
        self.desc = desc

    def getAbilityData(self):
        keys = ['name', 'lvl', 'max_lvl', 'type', 'effect', 'small_desc']
        values = [self.name, self.lvl, self.max_lvl, self.type, self.effect, self.small_desc]
        return dict(zip(keys, values))
