# -*- coding: iso-8859-15 -*-

import dMVC.model
import ggmodel
import GG.model.teleport
import GG.model.box_heavy
import GG.utils

class GGSession(ggmodel.GGModel):
  """ GGSession class.
  Includes room and player objects, and some procedures to manage data.
  """
    
  def __init__(self, player, system):
    """ Initializes session attributes.
    player: session user.
    """
    ggmodel.GGModel.__init__(self)
    self.__player = player
    self.__system = system
    player.subscribeEvent('chatAdded', self.chatAdded)
    player.getRoom().subscribeEvent('chatAdded', self.chatAdded)
    #player.getRoom().subscribeEvent('quizAdded', self.quizAdded)
    player.subscribeEvent('roomChanged', self.roomChanged)
      
  # self.__player
  
  def getPlayer(self):
    """ Returns the active player.
    """
    return self.__player
   
  def roomChanged(self, event):
    """ Triggers after receiving a change room event.
    event: event info.
    """
    oldRoom = event.getParams()['oldRoom']
    if oldRoom:
      oldRoom.unsubscribeEventMethod(self.chatAdded)
    newRoom = self.__player.getRoom()
    if newRoom: 
      newRoom.subscribeEvent('chatAdded', self.chatAdded)
      #self.__player.subscribeEvent('chatAdded', self.chatAdded)
      #newRoom.subscribeEvent('quizAdded', self.quizAdded)
    
  @dMVC.model.localMethod
  def defaultView(self, screen, fullscreen):
    """ Esto deberia ser IsoViewSession.
    screen: screen handler.
    """
    import GG.isoview.isoview_hud
    return GG.isoview.isoview_hud.IsoViewHud(self, screen, fullscreen)
    
  def chatAdded(self, event):
    """ Triggers after receiving a chat added event.
    event: event info.
    """
    self.triggerEvent('chatAdded', message=event.getParams()['message'])
  
  def quizAdded(self, event):
    """ Triggers after receiving a chat added event.
    event: event info.
    """
    self.triggerEvent('quizAdded', message=event.getParams()['message'])

  def unsubscribeEvents(self):
    self.__player.getRoom().unsubscribeEventObserver(self)
    self.__player.unsubscribeEventObserver(self)

  def logout(self):
    self.__system.logout(self)
    self.__player = None
    self.__system = None
    
  def getRoomLabels(self):
    return self.__system.getRoomLabels()  

  def getRoom(self, roomLabel):
    return self.__system.existsRoom(roomLabel)  
    
  def getObjectsData(self):
    if not self.__player.getAccessMode():
      return None  
    
    self.imagesDict = {}
    
    self.imagesDict["BoxHeavy"] = {"heavy_box.png": [[26, -10], [0, -12]]}
    
    self.imagesDict["Door"] = {}
    self.imagesDict["Door"]["wooden_door.png"] = [[28, 23], [0, 0]]
    self.imagesDict["Door"]["wooden_door_a.png"] = [[24, 37], [0, 0]]
    self.imagesDict["Door"]["wooden_door_b.png"] = [[24, 55], [0, 0]]
    self.imagesDict["Door"]["armored_door_left.png"] = [[17, 15], [0, 0]]
    
    self.imagesDict["DoorWithKey"] = self.imagesDict["Door"]
    
    self.imagesDict["RoomItem"] = {}
    self.imagesDict["RoomItem"]["hedge.png"] = [[55, 13], [0, -26]]
    self.imagesDict["RoomItem"]["fence_up.png"] = [[55, 15], [0, 0]]
    self.imagesDict["RoomItem"]["fence_left.png"] = [[55, 15], [0, 0]]
    self.imagesDict["RoomItem"]["tree.png"] = [[100, 150], [0, -26]]
    self.imagesDict["RoomItem"]["stone_column.png"] = [[13, 15], [0, 0]]
    self.imagesDict["RoomItem"]["wooden_beam.png"] = [[57, 142], [0, 0]]
    self.imagesDict["RoomItem"]["wall_left.png"] = [[55, 0], [0, 0]]
    self.imagesDict["RoomItem"]["wall_up.png"] = [[35, 10], [0, 0]]
    self.imagesDict["RoomItem"]["yard_up.png"] = [[25, 50], [0, 0]]
    self.imagesDict["RoomItem"]["yard_left.png"] = [[45, 50], [0, 0]]
    self.imagesDict["RoomItem"]["yard_lamp_up.png"] = [[25, 50], [0, 0]]
    self.imagesDict["RoomItem"]["yard_lamp_left.png"] = [[45, 50], [0, 0]]
    self.imagesDict["RoomItem"]["yard_corner.png"] = [[55, 45], [0, 0]]
    self.imagesDict["RoomItem"]["warehouseWallUp01.png"] = [[35, 33], [0, 0]]
    self.imagesDict["RoomItem"]["warehouseWallUp02.png"] = [[35, 33], [0, 0]]
    self.imagesDict["RoomItem"]["warehouseWallLeft01.png"] = [[35, 33], [0, 0]]
    self.imagesDict["RoomItem"]["warehouseWallLeft02.png"] = [[35, 33], [0, 0]]
    self.imagesDict["RoomItem"]["warehouseWallCorner.png"] = [[35, 33], [0, 0]]
    self.imagesDict["RoomItem"]["skylineWallUp01.png"] = [[35, 40], [0, 0]]
    self.imagesDict["RoomItem"]["skylineWallUp02.png"] = [[35, 40], [0, 0]]
    self.imagesDict["RoomItem"]["skylineWallUp03.png"] = [[35, 40], [0, 0]]
    self.imagesDict["RoomItem"]["skylineWallUp04.png"] = [[35, 40], [0, 0]]
    self.imagesDict["RoomItem"]["skylineWallLeft01.png"] = [[35, 40], [0, 0]]
    self.imagesDict["RoomItem"]["skylineWallLeft02.png"] = [[35, 40], [0, 0]]
    self.imagesDict["RoomItem"]["skylineCorner.png"] = [[35, 40], [0, 0]]
    
    self.imagesDict["PenguinTalker"] = {}
    self.imagesDict["PenguinTalker"]["andatuz_right.png"] = [[30, 0], [0, 0]]
    self.imagesDict["PenguinTalker"]["andatuz_down.png"] = [[30, 0], [0, 0]]
    self.imagesDict["PenguinTalker"]["andatuz_bottomright.png"] = [[30, 0], [0, 0]]

    self.imagesDict["PenguinTrade"] = self.imagesDict["PenguinTalker"]
    
    self.imagesDict["PenguinQuiz"] = self.imagesDict["PenguinTalker"]
    
    self.imagesDict["GiverNpc"] = {}
    self.imagesDict["GiverNpc"]["gift.png"] = [[15, -30], [0, 0]]
    self.imagesDict["GiverNpc"]["golden_key.png"] = [[15, -30], [0, 0]]
    
    pos = self.__player.getRoom().getNearestEmptyCell(self.__player.getPosition())
    
    self.objectsDict = {
                   "BoxHeavy": {
                            "position": pos,
                            "label": [""],
                            "images": self.imagesDict["BoxHeavy"].keys() 
                            },
                   "Door": {
                            "position": pos,
                            "destinationRoom": [self.__player.getRoom().label],
                            "exitPosition": [0, 0],
                            "label": [""], 
                            "images": self.imagesDict["Door"].keys()                     
                            },
                   "DoorWithKey": {
                            "position": pos,
                            "destinationRoom": [self.__player.getRoom().label],
                            "exitPosition": [0, 0],
                            "label": [""],
                            "key": [""],        
                            "images": self.imagesDict["DoorWithKey"].keys()                     
                            },
                   "GiverNpc": {
                            "position": pos,
                            "label": [""],
                            "images": self.imagesDict["GiverNpc"].keys()     
                            },
                   "PenguinQuiz": {
                            "position": pos,
                            "label": [""],
                            "filePath": [GG.utils.QUESTIONS_PATH],        
                            "images": self.imagesDict["PenguinTalker"].keys()                     
                            },
                   "PenguinTalker": {
                            "position": pos,
                            "label": [""],
                            "message": [""],        
                            "images": self.imagesDict["PenguinTalker"].keys()                     
                            },
                   "PenguinTrade": {
                            "position": pos,
                            "label": [""],
                            "gift": [""],        
                            "images": self.imagesDict["PenguinTrade"].keys()                     
                            },
                   "RoomItem": {
                            "position": pos,
                            "images": self.imagesDict["RoomItem"].keys()                     
                            }
                  }
    return self.objectsDict
    
  def createObject(self, name, data):
    try: 
      posX = int(data["position"][0])    
      posY = int(data["position"][1])
    except ValueError: 
      self.__player.newChatMessage("Valor \"Position\" incorrecto", 1) 
      return
    if name != "RoomItem":
      label = data["label"][0]  
      if label == "":
        self.__player.newChatMessage("Debe introducir un nombre para el objeto.", 1)
        return
    img = data["images"]
    room = self.__player.getRoom()
                  
    roomSz = self.__player.getRoom().size
    if not (0 <= posX <= roomSz[0] and 0 <= posY <= roomSz[1]):
      self.__player.newChatMessage("Las coordenadas del objeto no son correctas.", 1)
      return
                      
    #===============================================
    if name == "BoxHeavy":
      box = GG.model.box_heavy.GGBoxHeavy("furniture/" + img, self.imagesDict[name][img][0], \
                                          self.imagesDict[name][img][1], label)
    #===============================================
    elif name == "Door":
      destinationRoom = self.__system.existsRoom(data["destinationRoom"][0])
      if not room or not destinationRoom:
        self.__player.newChatMessage("No existe esa habitación.", 1)
        return
      try: 
        exPosX = int(data["exitPosition"][0])    
        exPosY = int(data["exitPosition"][1])
      except ValueError: 
        self.__player.newChatMessage("Valor \"exitPosition\" incorrecto", 1) 
        return
    
      roomSz = destinationRoom.size
      if not (0 <= exPosX <= roomSz[0] and 0 <= exPosY <= roomSz[1]):
        self.__player.newChatMessage("Las coordenadas de destino no son correctas.", 1)
        return
    
      box = GG.model.teleport.GGDoor("furniture/" + img, self.imagesDict[name][img][0], 
                                      self.imagesDict[name][img][1], [exPosX, exPosY], destinationRoom, label)
    #===============================================
    elif name == "DoorWithKey":
      destinationRoom = self.__system.existsRoom(data["destinationRoom"][0])
      if not room or not destinationRoom:
        self.__player.newChatMessage("No existe esa habitación.", 1)
        return
      if data["key"][0] == "":
        self.__player.newChatMessage("Debe introducir un nombre para el objeto.", 1)
        return
      try: 
        exPosX = int(data["exitPosition"][0])    
        exPosY = int(data["exitPosition"][2])
      except ValueError: 
        self.__player.newChatMessage("Valor \"exitPosition\" incorrecto", 1) 
        return
    
      roomSz = destinationRoom.size
      if not (0 <= exPosX <= roomSz[0] and 0 <= exPosY <= roomSz[1]):
        self.__player.newChatMessage("Las coordenadas de destino no son correctas.", 1)
        return
    
      box = GG.model.teleport.GGDoorWithKey("furniture/" + img, self.imagesDict[name][img][0], \
                                             self.imagesDict[name][img][1], [exPosX, exPosY], destinationRoom, 
                                             label, data["key"][0])
    #===============================================
    elif name == "GiverNpc":
      box = GG.model.giver_npc.GGGiverNpc("furniture/" + img, self.imagesDict[name][img][0], \
                                          self.imagesDict[name][img][1], "furniture/" + img, label)
    #===============================================
    elif name == "RoomItem":
      box = GG.model.room_item.GGRoomItem("furniture/" + img, self.imagesDict[name][img][0], \
                                          self.imagesDict[name][img][1])
    #===============================================
    elif name == "PenguinTalker":
      if data["message"][0] == "":
        self.__player.newChatMessage("Debe introducir un mensaje.", 1)
        return
      box = GG.model.penguin.GGPenguinTalker("furniture/" + img, self.imagesDict[name][img][0], \
                                             self.imagesDict[name][img][1], label, data["message"][0])
    #===============================================
    elif name == "PenguinTrade":
      room = self.__player.getRoom()
      if data["gift"][0] == "":
        self.__player.newChatMessage("Debe introducir el nombre del objeto regalo recibido.", 1)
        return
      box = GG.model.penguin.GGPenguinTrade("furniture/" + img, self.imagesDict[name][img][0], \
                                            self.imagesDict[name][img][1], label, data["gift"][0])
    #===============================================
    elif name == "PenguinQuiz":
      if data["filePath"][0] == "":
        self.__player.newChatMessage("Debe introducir el nombre del fichero de preguntas.", 1)
        return
      box = GG.model.penguin.GGPenguinQuiz("furniture/" + img, self.imagesDict[name][img][0], \
                                           self.imagesDict[name][img][1], label, data["filePath"][0])
    #===============================================
    room.addItemFromVoid(box, [posX, posY])
    
    