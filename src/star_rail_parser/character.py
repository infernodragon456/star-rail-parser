from star_rail_parser import SkillTree, LightCone, Relic, RelicSet, Stat, Ability


class Character:
    """
    Class for an individual character in the user's showcase.

    char_id : ID of the character
    name : Name of the character
    rarity : Rarity of the character (4star or 5star)
    rank : Eidolon level of the character
    level : Level of the character
    promotion : Ascension level of the character
    path : Path of the character
    element : Element of the character
    abilities : A list of 'ability' dicts
    skill_tree : A list of 'node' dicts with a parent key
    light_cone : A dict providing info about the lightcone
    relics : A list of dicts providing relic info
    relic_set_bonuses : A list of dicts providing relic set bonus info
    base_stats : A list of dicts providing base stat details (HP, ATK, DEF, Crate, CDmg)
    added_stats :  A list of dicts providing added stat details (HP, ATK, DEF, Crate, CDmg)
    stat_bonuses : A list of dicts providing all the stat bonuses on the character from relics, relic sets, traces, lightcone, etc

    """
    def __init__(self, char_id, name, rarity, rank, level, promotion, path, element, abilities, skill_tree, light_cone,
                 relics, relic_set_bonuses, base_stats, added_stats, stat_bonuses):
        self.id = char_id
        self.name = name
        self.rarity = rarity
        self.eidolon = rank
        self.level = level
        self.promotion = promotion
        self.path = path
        self.element = element
        self.abilities = []

        """
        skill_tree[:5] contains node information about Basic ATK, Skill, Talent, Technique and Ultimate
        Omitted as these are unlocked by default, and are already covered in self.abilities
        """
        self.skill_tree = SkillTree(skill_tree[5:])

        self.light_cone = LightCone(light_cone['id'], light_cone['name'], light_cone['rarity'], light_cone['rank'],
                                    light_cone['level'], light_cone['promotion'], light_cone['path']['name'],
                                    light_cone['attributes'], light_cone['properties'])

        self.relics = [Relic(relic['id'], relic['name'], relic['type'], relic['set_id'], relic['set_name'],
                             relic['rarity'], relic['level'], relic['main_affix'], relic['sub_affix'])
                       for relic in relics]

        self.relic_set_bonuses = [RelicSet(relic_set['id'], relic_set['name'], relic_set['num'], relic_set['desc'],
                                           relic_set['properties']) for relic_set in relic_set_bonuses]

        self.base_stats = [Stat(stat['name'], stat['value'], stat['percent']) for stat in base_stats]

        self.added_stats = [Stat(stat['name'], stat['value'], stat['percent']) for stat in added_stats]

        self.stat_bonuses = [Stat(stat['type'], stat['value'], stat['percent']) for stat in stat_bonuses]

        for ability in abilities:
            """
            Used to omit empty skills returned from the mihomo API
            """
            if ability['level'] != 0:
                abilityObj = Ability(ability['id'], ability['name'], ability['level'], ability['max_level'],
                                     ability['element'], ability['type_text'], ability['effect_text'],
                                     ability['simple_desc'], ability['desc'])
                self.abilities.append(abilityObj)

    def getCharData(self):
        """
        Return a dict of basic character information

        """

        keys = ['name', 'rarity', 'eidolon', 'level', 'promotion', 'path', 'element']
        values = [self.name, self.rarity, self.eidolon, self.level, self.promotion, self.path, self.element]
        return dict(zip(keys, values))

    def getBaseStats(self):
        """
        Return a dict of character base stats
        """

        stats_dict = {}

        for stat in self.base_stats:
            stats_dict[stat.type] = stat.value

        return stats_dict

    def getAddedStats(self):
        """
        Return a dict of character added stats
        """

        stats_dict = {}

        for stat in self.added_stats:
            stats_dict[stat.type] = stat.value

        return stats_dict

    def getStatBonuses(self):
        """
        Return a dict of all stat bonuses on the character from traces, relics, relic sets, lightcone, etc

        """
        stats_dict = {}

        for stat in self.stat_bonuses:
            stats_dict[stat.type] = stat.value

        return stats_dict
