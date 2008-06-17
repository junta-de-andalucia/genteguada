import ggmodel
import GG.utils
import inventory_item
import GG.isoview.isoview_item
import dMVC.model

class GGRoomItem(inventory_item.GGInventoryItem):
  """GGRoomItem class.
  Defines item attributes and methods.
  """
  
  def __init__(self, spriteName, position, offset):
    """ Class constructor.
    sprite: image name.
    position: position on screen for the item.
    offset: offset for that position.
    """
    inventory_item.GGInventoryItem.__init__(self, spriteName)
    self.offset = offset
    self.__position = position
    self.__room = None
    self.__upperItem = None
    self.__lowerItem = None
    
  def variablesToSerialize(self):
    """ Sets some vars to be used as locals.
    """
    parentVars = GG.model.inventory_item.GGInventoryItem.variablesToSerialize(self)
    return parentVars + ['offset']
  
  # self.__position
  
  def getPosition(self):
    """ Returns the item position.
    """
    return self.__position

  def setPosition(self, pos):
    """ Sets a new position for the item.
    pos: new position.
    """
    if not self.__position == pos:
      old = self.__position
      self.__position = pos
      self.triggerEvent('position', position=pos, oldPosition=old)

  def setStartPosition(self, pos):
    """ Sets a new start position for the item.
    pos: new position.
    """
    if self.__position != pos:
      self.__position = pos
      if pos != None:
        self.triggerEvent('startPosition', position=pos)

  # self.__room
    
  def getRoom(self):
    """ Returns the room where the player is.
    """
    return self.__room
  
  def clearRoom(self):
    """ Sets the item's room as none.    
    """
    if self.__room == None:
      raise Exception("Error en limpieza de room")
    self.__setRoom(None)
    
  def setRoom(self, room):
    """ Sets a new room for the player.
    room: new room.
    """
    if self.__room != None:
      raise Exception("Error: el item ya tiene un room")
    if room == None:
      raise Exception("Error: habitacion = None")
    self.__setRoom(room)
      
  def __setRoom(self, room):
    """ Private method. Sets the item's room with a new value and triggers an event.
    room: new room.
    """
    self.__room = room
    self.triggerEvent('room', room=room)

  # self.__upperItem
  
  def getUpperItem(self):
    return self.__upperItem

  def setUpperItem(self, item):
    if not self.__upperItem.checkSimilarity(item):
      self.__upperItem = item
      self.triggerEvent('lowerItem', item=item)
      
  # self.__lowerItem
  
  def getLowerItem(self):
    return self.__lowerItem

  def setLowerItem(self, item):
    if not self.__lowerItem.checkSimilarity(item):
      self.__lowerItem = item
      self.triggerEvent('lowerItem', item=item)
  
  @dMVC.model.localMethod 
  def defaultView(self, screen, room, parent):
    """ Creates an isometric view object for the item.
    screen: screen handler.
    parent: isoview hud handler.
    """
    return GG.isoview.isoview_item.IsoViewItem(self, screen, room, parent)
  
  def checkSimilarity(self, item):
    if inventory_item.GGInventoryItem.checkSimilarity(self, item):
      if item.offset == self.offset:
        return True
    return False   
  
  """
  def inventoryOnly(self):
    return False
  """
  
  def clickedBy(self, clicker):
    """ Triggers an avent when the item receives a click by a player.
    clicker: player who clicks.
    """
    clicker.setHeading(GG.utils.getNextDirection(clicker.getPosition(), self.__position))
    
  def tick(self, now):
    """ Call for an update on item.
    Not used at the moment.
    """
    pass
  
  def abandonRoom(self):
    """ Tells a room to remove this item from it.
    """
    self.__room.removeItem(self)
