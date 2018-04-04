class Gamestats():
  """跟踪游戏的统计信息"""
  def __init__(self, ai_settings):
    """初始化统计信息"""
    self.ai_settings = ai_settings
    self.reset_stats()

    #游戏刚启动时属于活动状态
    self.game_active = False

    #在任何情况下都不应该重置最高分
    try:
      fobj = open('high_score.txt')
    except FileNotFoundError:
      self.high_score = 0
    else:
      self.high_score = int(fobj.read())
      fobj.close()


  def reset_stats(self):
    """初始化在游戏运行期间可能变化的统计信息"""
    self.ship_left = self.ai_settings.ship_limit
    self.score = 0
    self.level = 1