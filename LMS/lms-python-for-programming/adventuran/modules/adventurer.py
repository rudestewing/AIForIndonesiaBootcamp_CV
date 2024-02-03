from typing import List
from modules.mission import Mission
from modules.rank import Rank
from modules.exceptions import MissionRankNotCompatible

class Adventurer:
  def __init__(self, name) -> None:
    self.name = name
    self.exp = 0
    self.missions: List[Mission] = []
    self.rank: Rank = None

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

  def upgradeRank(self):
    if(self.exp > self.rank.maximumExp):
      self.rank = self.rank.nextRank
