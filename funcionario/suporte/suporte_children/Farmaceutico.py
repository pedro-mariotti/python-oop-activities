from ..Suporte import Suporte

class Farmaceutico(Suporte):
  def __init__(self, data):
    try:
      self.__totalMedEntregues = data["totalMedEntregues"]
      self.__estoqueMeds = data["estoqueMeds"]
      super().__init__(data)
    except:
      print("Dados incorretos de Farmaceutico, favor preencher corretamente a ficha de inscrição")
    else:
      print("Dados cadastrados com sucesso!")
  def getEstoque(self):
    return self.__estoqueMeds
  def getTotalMedEntregues(self):
    return self.__totalMedEntregues
  def addEntregas(self):## aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    self.__totalMedEntregues = self.__totalMedEntregues + 1
  def removeEntrega(self, casoRemovido):
    self.__totalMedEntregues = self.__totalMedEntregues - 1