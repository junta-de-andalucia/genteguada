import dMVC.model
import GG.isoview.isoview_hud

class GGSession(dMVC.model.Model):
  """ GGSession class.
  Includes room and player objects, and some procedures to manage data.
  """
    
  def __init__(self, player):
    """ Initializes session attributes.
    player: session user.
    """
    dMVC.model.Model.__init__(self)
    self.__player = player
      
  def getPlayer(self):
    """ Returns the active player.
    """
    return self.__player
    
  @dMVC.model.localMethod
  def defaultView(self, screen):
    """ Esto deberia ser IsoViewSession.
    screen: screen handler.
    """
    return GG.isoview.isoview_hud.IsoViewHud(self, screen)

  def logout(self):
    """
    """
    #lanzar evento removePlayer a la habitacion
    pass

