class LightCone:
    """
    Class for the character lightcone

    Args:
        lightcone_id : ID for the lightcone
        name : Name of the lightcone
        rarity: Rarity of the lightcone
        superimposition: Superimposition level of the lightcone
        level : Lightcone level
        promotion : Ascension level
        path : Path of the lightcone
        attributes : Flat stats from the lightcone (HP, ATK, DEF)
        properties : Other attributes from the lightcone passive
    """
    def __init__(self, lightcone_id, name, rarity, superimposition, level, promotion, path, attributes, properties):
        self.id = lightcone_id
        self.name = name
        self.rarity = rarity
        self.superimposition = superimposition
        self.level = level
        self.promotion = promotion
        self.path = path
        self.attributes = attributes
        self.properties = properties

    def getAttributes(self):
        """
        Return a dict of lightcone base attributes
        """
        keys = []
        values = []
        for stat in self.attributes:
            keys.append(stat['name'])
            values.append(stat['value'])
        return dict(zip(keys, values))
