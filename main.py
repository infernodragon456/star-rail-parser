from star_rail_parser import Trailblazer

obj = Trailblazer('807842788')


charList = obj.getCharacters()
print(charList[1].relics[4].sub_stats[3].__dict__)




