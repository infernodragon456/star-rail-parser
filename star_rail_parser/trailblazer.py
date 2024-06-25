import requests
from star_rail_parser import Character

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
                                char['attributes'], char['additions'], char['properties'])
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
