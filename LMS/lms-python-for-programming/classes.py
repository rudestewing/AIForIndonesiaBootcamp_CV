from typing import List

class MissionRankNotCompatible(Exception):
  pass

class Rank:
  def __init__(self, grade, name) -> None:
    self.grade = grade
    self.name = name

class Reward:
  def __init__(self, exp=0, gold=0) -> None:
    self.exp = exp
    self.gold = gold

class Mission:
  def __init__(self, name, rank: Rank, reward: Reward) -> None:
    self.name = name
    self.rank = rank
    self.reward = reward

class Adventurer:
  def __init__(self, name) -> None:
    self.name = name
    self.exp = 0
    self.missions: List[Mission] = []
    self.rank = None

  def takeMission(self, mission: Mission):
    try:
      if mission.rank.grade > self.rank.grade:
        raise MissionRankNotCompatible
      self.missions.append(mission)
    except MissionRankNotCompatible:
      print('Mission rank not compatible with adventurer rank')

  def getCurrentMissions(self):
    return self.missions

  def completeMission(self, missionIndex: int):
    if 0 <= missionIndex < len(self.missions):
      completed_mission = self.missions.pop(missionIndex)
      self.exp += completed_mission.reward.exp
    else:
      print('Invalid mission index')

  def joinRank(self, rank: Rank):
    self.rank = rank

ranks = {
  'novice': Rank(1, 'novice'),
  'warrior': Rank(2, 'warrior'),
  'master': Rank(3, 'master'),
  'legend': Rank(4, 'legend'),
  'myth': Rank(5, 'myth'),
}

missions = [
  Mission("Hunt's Rathalos", ranks['master'], Reward(30, 100)),
  Mission("Collect Blue Berry", ranks['novice'], Reward(10, 20)),
]

rudestewing = Adventurer('rudestewing')
rudestewing.joinRank(ranks['novice'])

rudestewing.takeMission(missions[0])
print(rudestewing.getCurrentMissions())

rudestewing.completeMission(0)
print(rudestewing.exp)
