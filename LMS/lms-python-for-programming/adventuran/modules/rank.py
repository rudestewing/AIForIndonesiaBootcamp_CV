class RankName:
  NOVICE = 'novice'
  WARRIOR = 'warrior'
  MASTER = 'master'
  LEGEND = 'legend'
  MYTH = 'myth'

class Rank:
  def __init__(self) -> None:
    self.grade = 0
    self.name = 'rank'
    self.maximumExp: int
    self.nextRank: Rank

class RankNovice(Rank):
  def __init__(self) -> None:
    self.grade = 1
    self.name = 'Novice'
    self.maximumExp = 100
    self.nextRank = RankWarrior()

class RankWarrior(Rank):
  def __init__(self) -> None:
    self.grade = 2
    self.name = 'Warrior'
    self.maximumExp = 200
    self.nextRank = RankMaster()

class RankMaster(Rank):
  def __init__(self) -> None:
    self.grade = 3
    self.name = 'Master'
    self.maximumExp = 300
    self.nextRank = RankLegend()

class RankLegend(Rank):
  def __init__(self) -> None:
    self.grade = 4
    self.name = 'Legend'
    self.maximumExp = 400
    self.nextRank = RankMyth()

class RankMyth(Rank):
  def __init__(self) -> None:
    self.grade = 5
    self.name = 'Myth'
    self.maximumExp = 500
    self.nextRank = None
