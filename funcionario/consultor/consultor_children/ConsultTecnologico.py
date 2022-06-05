from ..Consultor import Consultor

class ConsultTecnologico(Consultor):
  def __init__(self, data):
    try:
      self.__tecnologiaResponsavel = data["tecnologiasResponsaveis"]
      self.__setorResponsavel = data["setor"]
      super().__init__(data)
    except:
      print("Dados incorretos de Consultor Tecnológico, favor preencher corretamente a ficha de inscrição")
    else:
      print("Dados cadastrados com sucesso!")
  def getTecnologias(self) -> list:
    return self.__tecnologiaResponsavel
  def getSetor(self):
    return self.__setorResponsavel
  def mudaSetor(self, __setorResponsavel):
    return self.__setorResponsavel
  def addTecnologia(self, tecnologiaNova):
    self.__tecnologiaResponsavel.append(tecnologiaNova)
  def removeTecnologia(self, tecnologiaRemovida):
    self.__tecnologiaResponsavel.remove(tecnologiaRemovida)