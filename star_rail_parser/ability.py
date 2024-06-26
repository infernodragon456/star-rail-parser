class Ability:
    """
    Class for Character skill/ability (Basic ATK, Skill, Ultimate, Talent, Enhanced Abilities)

    Args:
        skill_id : ID of the ability
        name : Name of the ability
        lvl : Current level of the ability
        max_lvl : Max possible level for the ability with eidolons
        element : Element type of the ability
        ability_type : Type of the ability (Basic ATK, Skill, Ultimate, etc.)
        effect : Damage type of the ability (Single attack, Blast attack, AOE)
        small_desc : Simple description of the ability without any stats
        desc : Full description of the ability with stats
    """
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
        """
        Return a dict of the basic ability details

        """
        keys = ['name', 'lvl', 'max_lvl', 'type', 'effect', 'small_desc']
        values = [self.name, self.lvl, self.max_lvl, self.type, self.effect, self.small_desc]
        return dict(zip(keys, values))
