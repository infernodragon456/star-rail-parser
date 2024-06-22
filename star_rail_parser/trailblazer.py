import requests

url = 'http://api.mihomo.me/sr_info_parsed/'
params = {'lang': 'en'}


class Trailblazer:
    def __init__(self, uid: str):
        response = requests.get(f'{url}{uid}', params)
        data = response.json()
        self.data = data
        self.player_data = data['player']
        self.character_data = data['characters']

    def show(self):
        print(self.player_data)

    def getBasicData(self):
        keys = ['uid', 'nickname', 'level', 'world_level', 'friend_count', 'signature', 'avatar']
        values = list(map(self.player_data.get, keys))
        return dict(zip(keys, values))

    def getOtherData(self):
        return self.player_data['space_info']



class Character:
    def __init__(self):