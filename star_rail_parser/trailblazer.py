import requests

url = 'http://api.mihomo.me/sr_info_parsed/'
params = {'lang': 'en'}


class Trailblazer:
    def __init__(self, uid: str):
        self.character_data = []
        response = requests.get(f'{url}{uid}', params)
        data = response.json()
        self.player_data = data['player']

        for char in data['characters']:
            charObj = Character(char['id'], char['name'], char['rarity'], char['rank'], char['level'],
                                char['promotion'], char['path']['name'], char['element']['name'], char['skills'],
                                char['skill_trees'], char['light_cone'], char['relics'], char['relic_sets'],
                                char['attributes'])
            self.character_data.append(charObj)

    def show(self):
        print(self.player_data)

    def getBasicData(self):
        keys = ['uid', 'nickname', 'level', 'world_level', 'friend_count', 'signature', 'avatar']
        values = list(map(self.player_data.get, keys))
        return dict(zip(keys, values))

    def getOtherData(self):
        return self.player_data['space_info']

    def getCharacters(self):
        return self.character_data


class Character:
    def __init__(self, char_id, name, rarity, rank, level, promotion, path, element, abilities, skill_tree, light_cone,
                 relics, relic_set_bonuses, stats):
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
        self.light_cone = light_cone
        self.relics = relics
        self.relic_set_bonuses = relic_set_bonuses
        self.stats = stats

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


class Ability:
    def __init__(self, skill_id, name, lvl, max_lvl, element, type, effect, small_desc, desc):
        self.id = skill_id
        self.name = name
        self.lvl = lvl
        self.max_lvl = max_lvl
        self.element = element
        self.type = type
        self.effect = effect
        self.small_desc = small_desc
        self.desc = desc

    def getAbilityData(self):
        keys = ['name', 'lvl', 'max_lvl', 'type', 'effect', 'small_desc']
        values = [self.name, self.lvl, self.max_lvl, self.type, self.effect, self.small_desc]
        return dict(zip(keys, values))


class SkillTree:

    def __init__(self, skill_tree_nodes):
        self.nodes = []
        for node in skill_tree_nodes:
            skill_tree_node = SkillTreeNode(node['id'], bool(node['level']), node['parent'])
            self.nodes.append(skill_tree_node)

    def getTree(self):
        tree = []
        roots = list(filter(lambda x: x.parent_node is None, self.nodes))
        for root in roots:
            branch = self.getBranch(root=root, nodes=self.nodes)
            tree.append(branch)
        return tree

    @staticmethod
    def getBranch(root, nodes):
        branch = [root]
        it = root

        while True:
            childList = [node for node in nodes if node.parent_node == it.id]
            if len(childList) == 0:
                break
            elif len(childList) == 1:
                it = childList[0]
                branch.append(it)
            else:
                branch_list = []
                for child in childList:
                    child_branch = SkillTree.getBranch(child, nodes)
                    branch_list.append(child_branch)

                branch.append(branch_list)
                break

        return branch


class SkillTreeNode:
    def __init__(self, node_id, activated, parent_node_id):
        self.id = node_id
        self.activated = activated
        self.parent_node = parent_node_id
