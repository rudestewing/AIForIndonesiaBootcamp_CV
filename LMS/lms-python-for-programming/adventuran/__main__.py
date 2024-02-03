from modules.rank import Rank, RankName, RankNovice, RankWarrior, RankMaster, RankLegend, RankMyth
from modules.mission import Mission
from modules.reward import Reward
from modules.adventurer import Adventurer

data_missions = [
  Mission("Hunt's Rathalos", RankMaster(), Reward(30, 100)),
  Mission("Collect Blue Berry", RankNovice(), Reward(10, 20)),
]

rudestewing = Adventurer('rudestewing')
rudestewing.joinRank(RankNovice())

rudestewing.takeMission(data_missions[1])
print(rudestewing.getCurrentMissions())

rudestewing.completeMission(0)
rudestewing.upgradeRank()
