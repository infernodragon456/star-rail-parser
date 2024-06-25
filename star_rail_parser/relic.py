from star_rail_parser import Stat


class Relic:
    def __init__(self, relic_id, name, relic_type, set_id, set_name, rarity, level, main_stat, sub_stats):
        self.id = relic_id
        self.name = name
        self.type = relic_type
        self.set_id = set_id
        self.set_name = set_name
        self.rarity = rarity
        self.level = level
        self.main_stat = Stat(main_stat['type'], main_stat['value'], main_stat['percent'])
        self.sub_stats = [Stat(sub_stat['type'], sub_stat['value'], sub_stat['percent'], sub_stat['count'],
                               sub_stat['step']) for sub_stat in sub_stats]

    def getRelicStats(self):
        stats_dict = {self.main_stat.type: self.main_stat.value}
        for sub_stat in self.sub_stats:
            if sub_stat.type in stats_dict:
                stats_dict[sub_stat.type] += sub_stat.value
            else:
                stats_dict[sub_stat.type] = sub_stat.value

        return stats_dict
