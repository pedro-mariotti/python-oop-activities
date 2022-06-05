from ..Suporte import Suporte

class Entregador(Suporte):
  def __init__(self, data):
    try:
      self.__totalEntregas = data["totalEntregas"]
      super().__init__(data)
    except:
      print("Dados incorretos de Entregador, favor preencher corretamente a ficha de inscrição")
    else:
      print("Dados cadastrados com sucesso!")
  def getTotalEntregas(self):
    return self.__totalEntregas
  def addEntregas(self):
    self.__totalEntregas = self.__totalEntregas + 5# entregador entrega 5 pedidos por vez
  def removeEntrega(self, casoRemovido):
    self.__totalEntregas = self.__totalEntregas - 5