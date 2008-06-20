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
    self.container = ocempgui.widgets.VFrame()
    
    self.container.add_child(GG.utils.OcempLabel(model.getMessage() ,140))
    for answer in self.__answers:
      self.container.add_child(GG.utils.OcempLabel(answer ,140))
    self.buttonBar = ocempgui.widgets.HFrame()
    
    i = 1
    for answer in self.__answers:
      button = ocempgui.widgets.ImageButton(GG.genteguada.GenteGuada.getInstance().getDataPath("interface/hud/4.png"))
      button.border = 0
      button.connect_signal(ocempgui.widgets.Constants.SIG_CLICKED, self.actionButton, i)
      i += 1
      self.buttonBar.add_child(button)
    self.buttonBar.border = 0
      
    self.container.set_align(ocempgui.widgets.Constants.ALIGN_LEFT)
    self.container.add_child(self.buttonBar)
    self.container.topleft = [20, 20]
    self.container.border = 0
    self.__isohud.getIsoviewRoom().addTopSprite(self.container)
    self.__isohud.widgetContainer.add_widget(self.container)
    
    
    """
    self.labelQ = GG.utils.OcempLabel("de que color es el caballo blanco de santiago" ,140)
    self.labelWhite = GG.utils.OcempLabel("blanco" ,140)
    self.labelBlue = GG.utils.OcempLabel("azul" ,140)
    self.labelGrey = GG.utils.OcempLabel("gris" ,140)
    self.container.add_child(self.labelQ)
    self.container.add_child(self.labelWhite)
    self.container.add_child(self.labelBlue)
    self.container.add_child(self.labelGrey)
    self.buttonBar = ocempgui.widgets.HFrame()
    
    button1 = ocempgui.widgets.ImageButton(GG.genteguada.GenteGuada.getInstance().getDataPath("interface/hud/4.png"))
    button1.border = 0
    button1.connect_signal(ocempgui.widgets.Constants.SIG_CLICKED, self.actionButton, 1)
    button2 = ocempgui.widgets.ImageButton(GG.genteguada.GenteGuada.getInstance().getDataPath("interface/hud/4.png"))
    button2.border = 0
    button2.connect_signal(ocempgui.widgets.Constants.SIG_CLICKED, self.actionButton, 2)
    button3 = ocempgui.widgets.ImageButton(GG.genteguada.GenteGuada.getInstance().getDataPath("interface/hud/4.png"))
    button3.border = 0
    button3.connect_signal(ocempgui.widgets.Constants.SIG_CLICKED, self.actionButton, 3)
    self.buttonBar.add_child(button1)
    self.buttonBar.add_child(button2)
    self.buttonBar.add_child(button3)
    
    self.container.set_align(ocempgui.widgets.Constants.ALIGN_LEFT)
    self.container.add_child(self.buttonBar)
    self.container.topleft = [20, 20]
    self.__isohud.getIsoviewRoom().addTopSprite(self.container)
    self.__isohud.widgetContainer.add_widget(self.container)
    #self.widgetContainer.add_widget(self.buttonBarActions)
    """
    
  def actionButton(self, option):
    print option
    self.__isohud.widgetContainer.remove_widget(self.container)
    self.__isohud.getIsoviewRoom().removeTopSprite(self.container)
    self.container.destroy()
    
  def __del__(self):
    isoview.IsoView.__del__(self)
    
  def getImg(self):
    return self.container
    #return self.__img
  
  def getScreenPosition(self):
    return self.container.topleft
    #return self.__img.rect.topleft

  def setScreenPosition(self, pos):
    self.container.topleft = pos
  """
  def getStyleMessageChat(self):
    styles = {}
    styles["ballom"] = GG.utils.STYLES["chatBalloon" + GG.utils.CHAT_TYPE[self.getModel().type]]
    styles["entry"] = GG.utils.STYLES["chatEntry" + GG.utils.CHAT_TYPE[self.getModel().type]]
    return styles
  """  
  """
    listStyle = ["White","Red","Green","Blue"]
    color = listStyle[random.randint(0,len(listStyle)-1)]
    styles = {}
    styles["ballom"] = GG.utils.STYLES["chatBalloon"+color]
    styles["entry"] = GG.utils.STYLES["chatEntry"+color]
    return styles
    """
  
  """
  def draw(self):
    hframe = ocempgui.widgets.HFrame()
    hframe.border = 0
    hframe.set_align(ocempgui.widgets.Constants.ALIGN_TOP) 
    imgPath = GG.genteguada.GenteGuada.getInstance().getDataPath(GG.utils.IMAGE_CHAT_MESSAGE)
    image = ocempgui.widgets.ImageLabel(imgPath)
    image.buttom = 0
    hframe.add_child(image)
    string = self.getModel().getHour()+" [" + self.getModel().getSender() + "]: "
    label = GG.utils.OcempLabel(string,300)
    label.set_style(ocempgui.widgets.WidgetStyle(self.style["entry"]))
    hframe.add_child(label)
    label = GG.utils.OcempLabel(self.getModel().getMessage(),300)
    label.set_style(ocempgui.widgets.WidgetStyle(self.style["entry"]))
    hframe.add_child(label)
    return hframe
  """