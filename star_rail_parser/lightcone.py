class LightCone:
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
        keys = []
        values = []
        for stat in self.attributes:
            keys.append(stat['name'])
            values.append(stat['value'])
        return dict(zip(keys, values))
