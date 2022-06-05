from ..Consultor import Consultor

class ConsultJuridico(Consultor):
  def __init__(self, data):
    try:
      self.__casosResponsaveis = data["casos"]
      super().__init__(data)
    except:
      print("Dados incorretos de Consultor Jurídico, favor preencher corretamente a ficha de inscrição")
    else:
      print("Dados cadastrados com sucesso!")
  def getCasos(self):
    return self.__casosResponsaveis
  def addCaso(self, casoNovo):
    self.__casosResponsaveis.append(casoNovo)
  def removeCaso(self, casoRemovido):
    self.__casosResponsaveis.remove(casoRemovido)