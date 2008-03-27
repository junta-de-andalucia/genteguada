import math
import os
import sys
import time
import signal
import pygame
import time
    
from pygame.locals import *

from isoview_hud import *
from isoview_room import *
from isoview_item import *
from isoview_player import *

from hud import *
from room import *
from item import *
from player import *

class GG:
  """ Clase GG
  Clase principal del cliente. Maneja la entrada por teclado y ejecuta las \
  operaciones principales.
  """
    
  def __init__(self):
    """ Constructor de la clase.
    """
    pass

  def input(self, events):
    """ Maneja los eventos recibidos por teclado y raton.
    events: evento recibido por los dispositivos de entrada.
    """
    for event in events:
      if event.type == QUIT: 
        sys.exit(0)
      if event.type == KEYDOWN:
        if event.key == K_UP:
          self.player1.moveOne(1)
        if event.key == K_DOWN:
          self.player1.moveOne(2)
        if event.key == K_LEFT:
          self.player1.moveOne(3)
        if event.key == K_RIGHT:
          self.player1.moveOne(4)
        if event.key == K_ESCAPE:
          sys.exit(0)
      if event.type == MOUSEBUTTONDOWN:
        x, y = pygame.mouse.get_pos()
        dest = self.isoviewRoom.findTile([x,y])
        if dest <> [-1, -1]:
          self.room.setPlayerDestination(0, [dest[0], 0, dest[1]])
          
  def start(self):
    """ Inicia el programa. Crea e inicializa subjects y observers y pone en \
    marcha el bucle principal.
    """
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SZ)
    pygame.display.set_caption('GenteGuada 0.01')

    self.room = Room("room1", 0, TILE_STONE)
    self.player1 = Player("player", 0, PLAYER_SPRITE1, CHAR_SZ, (2, 0, 2))
    self.room.insertPlayer(self.player1)

    self.isoviewRoom = IsoViewRoom("<observer Room>")
    self.isoviewRoom.addModel(self.room)
    self.isoViewPlayer = IsoViewPlayer("<observer Player>", screen)
    self.isoViewPlayer.addModel(self.player1)
    self.isoviewRoom.insertPlayer(self.isoViewPlayer)

    #isoViewHud.paintHud()

    while True:
      time.sleep(0.05)
      self.room.tick()
      self.isoviewRoom.draw(screen)
      self.input(pygame.event.get()) 