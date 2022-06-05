from ..Atendente import Atendente

class Recepcionista(Atendente):
  def __init__(self, data: dict):
    try:
      self.__telefoneBancada = data["telefoneBancada"]
      super().__init__(data)
    except:
      print("Dados incorretos de Recepcionista, favor preencher corretamente a ficha de inscrição")
    else:
      print("Dados cadastrados com sucesso!")

  def setTelefone(self, telefoneBancada):
    self.__telefoneBancada = telefoneBancada

  def getTelefone(self):
    return self.__telefoneBancada