class RelicSet:
    """
    Class for the relic set bonus.
    (2p and 4p bonuses of the same set are given different instances)

    Args:
        set_id : ID of the set
        set_name : Name of the Set
        num_piece: Type of effect (2 or 4)
        desc: Set effect description
        properties: Set effect stat bonuses.
    """
    def __init__(self, set_id, set_name, num_piece, desc, properties):
        self.id = set_id
        self.name = set_name
        self.num_piece = num_piece
        self.desc = desc
        self.properties = properties
