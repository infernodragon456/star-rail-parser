class Stat:
    """
    Class for relic stats (main stat and sub stats), and character stats

    Args:
        stat_type: Type of the stat (Flat HP, HP%, Crate, etc.)
        value: Value of the stat
        isPercent: Bool for whether the value is a percentage
        count (optional) : The number of rolls on the sub stat. Only valid for sub stats.
                           By default, it's 1 for every sub stat.
        step (optional)  : Frankly, no idea what this actually is. Only valid for sub stats
    """
    def __init__(self, stat_type, value, isPercent, count=None, step=None):
        self.type = stat_type
        self.value = value
        self.isPercent = isPercent
        self.count = count
        self.step = step
