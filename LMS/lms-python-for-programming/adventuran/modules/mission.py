from modules.rank import Rank
from modules.reward import Reward

class Mission:
  def __init__(self, name, rank: Rank, reward: Reward) -> None:
    self.name = name
    self.rank = rank
    self.reward = reward
