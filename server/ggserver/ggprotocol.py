
from twisted.internet.protocol import Protocol
import cPickle
import ggcommon.eventos

class GenteGuadaProtocol(Protocol):
  """
  Procedimiento a seguir con las conexiones de los clientes
  """

  def connectionMade(self):
    """
    Metodo que se ejecuta cuando se recibe una conexion por parte de un
    cliente nuevo. Dicha conexion, se inserta en la coleccion conexiones 
    de nuestra factoria
    """
    print "conexion"
    for clients in self.factory.clients:
      clients.transport.write("Nuevo cliente conectado\n")
    self.factory.clients.append(self)

  def dataReceived(self, data):
    """
    Metodo que se ejecuta cuando un cliente ya registrado envia datos al 
    servidor.

    Parametros:

      data => datos enviados al servidor
    """
    print data
    event = ggcommon.eventos.Event()
    miEventoSerializado = cPickle.dumps(event)
    for clients in self.factory.clients:
      clients.transport.write(miEventoSerializado)

  def connectionLost(self, reason):
    """
    Metodo que se ejecuta cuando un cliente cierra la conexion con el servidor,
    al cerrar la comunicacion le sacamos de la lista de clientes activos

    Parametros:
    
      reason => razon de perdida de conumicacion
    """
    print reason.value
    self.factory.clients.remove(self)
    for clients in self.factory.clients:
      clients.transport.write("Cliente desconectado\n")

