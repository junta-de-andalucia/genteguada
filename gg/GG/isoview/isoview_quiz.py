# -*- coding: iso-8859-15 -*-

import ocempgui
import pygame
import random
import GG.utils
import isoview
import animation
import positioned_view

class IsoViewQuiz(positioned_view.PositionedView):
  """ IsoViewQuiz class.
  Defines a chat message view.
  """
  
  def __init__(self, model, screen, isohud):
    """ Class constructor.
    model: chat message model.
    screen: screen handler.
    """
    self.__isohud = isohud
    self.__answers = model.getAnswers()
    
    positioned_view.PositionedView.__init__(self, model, screen)
    self.container = ocempgui.widgets.Box(358,258)
    filePath =  GG.genteguada.GenteGuada.getInstance().getDataPath("interface/backgrounds/trivialWindow.png")
    imgBackground = GG.utils.OcempImageMapTransparent(filePath)
    imgBackground.topleft = 0,0
    self.container.add_child(imgBackground)
    
    label = GG.utils.OcempLabel(model.getMessage() ,250, GG.utils.STYLES["quizLabel"])
    label.set_style(ocempgui.widgets.WidgetStyle(GG.utils.STYLES["quizLabel"]))
    label.topleft = 20, 40
    self.container.add_child(label)
    i = 0
    for answer in self.__answers:
       label = GG.utils.OcempLabel(answer ,250, GG.utils.STYLES["quizLabel"])
       label.set_style(ocempgui.widgets.WidgetStyle(GG.utils.STYLES["quizLabel"]))
       label.topleft = 80, 85 + i *50
       self.container.add_child(label)
       i = i + 1
    
    buttonA = GG.utils.OcempImageButtonTransparent(GG.genteguada.GenteGuada.getInstance().getDataPath("interface/hud/answerA.png"))
    buttonA.topleft = [22,70]
    buttonA.connect_signal(ocempgui.widgets.Constants.SIG_CLICKED, self.actionButton, 1)
    buttonB = GG.utils.OcempImageButtonTransparent(GG.genteguada.GenteGuada.getInstance().getDataPath("interface/hud/answerB.png"))
    buttonB.topleft = [22,120]
    buttonB.connect_signal(ocempgui.widgets.Constants.SIG_CLICKED, self.actionButton, 2)
    buttonC = GG.utils.OcempImageButtonTransparent(GG.genteguada.GenteGuada.getInstance().getDataPath("interface/hud/answerC.png"))
    buttonC.topleft = [22,170]
    buttonC.connect_signal(ocempgui.widgets.Constants.SIG_CLICKED, self.actionButton, 3)
    self.container.add_child(buttonA)
    self.container.add_child(buttonB)
    self.container.add_child(buttonC)
    self.container.topleft = [20, 20]
    self.container.border = 0
    self.container.zOrder = 20000
    self.__isohud.addSprite(self.container)
    self.__isohud.widgetContainer.add_widget(self.container)
    self.__isohud.setActiveQuizWindow(True)
    
  def actionButton(self, option):
    if option == self.getModel().getRightAnswer():
      self.__isohud.getPlayer().triggerEvent('chatAdded', message=GG.model.chat_message.ChatMessage("ˇRespuesta correcta!", \
                'Andatuz', GG.utils.TEXT_COLOR["black"], [2, 0, 2], 2))
      self.__isohud.getPlayer().addPoints(0, self.getModel().question)
      self.getModel().removeRightAnsweredQuestion()
    else:   
      self.__isohud.getPlayer().triggerEvent('chatAdded', message=GG.model.chat_message.ChatMessage("Respuesta incorrecta", \
                'Andatuz', GG.utils.TEXT_COLOR["black"], [2, 0, 2], 2))
    self.__isohud.widgetContainer.remove_widget(self.container)
    self.__isohud.setActiveQuizWindow(False)
    self.container.destroy()
    
  def __del__(self):
    isoview.IsoView.__del__(self)

  def updateZOrder(self):  
    self.label.zOrder = 20000  
    
  def getImg(self):
    return self.container
    
  def getScreenPosition(self):
    return self.container.topleft
    
  def setScreenPosition(self, pos):
    self.container.topleft = pos
  
