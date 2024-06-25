from star_rail_parser import SkillTree, LightCone, Relic, RelicSet, Stat, Ability


class Character:
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
            if ability['level'] != 0:
                abilityObj = Ability(ability['id'], ability['name'], ability['level'], ability['max_level'],
                                     ability['element'], ability['type_text'], ability['effect_text'],
                                     ability['simple_desc'], ability['desc'])
                self.abilities.append(abilityObj)

    def getCharData(self):
        keys = ['name', 'rarity', 'eidolon', 'level', 'promotion', 'path', 'element']
        values = [self.name, self.rarity, self.eidolon, self.level, self.promotion, self.path, self.element]
        return dict(zip(keys, values))

    def getBaseStats(self):
        stats_dict = {}

        for stat in self.base_stats:
            stats_dict[stat.type] = stat.value

        return stats_dict

    def getAddedStats(self):
        stats_dict = {}

        for stat in self.added_stats:
            stats_dict[stat.type] = stat.value

        return stats_dict

    def getStatBonuses(self):
        stats_dict = {}

        for stat in self.stat_bonuses:
            stats_dict[stat.type] = stat.value

        return stats_dict
