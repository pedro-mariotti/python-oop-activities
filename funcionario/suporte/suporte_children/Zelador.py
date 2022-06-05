from ..Suporte import Suporte

class Zelador(Suporte):
  def __init__(self, data):
    try:
      self.__totalQuartoResponsaveis = data["totalQuartoResponsaveis"]
      super().__init__(data)
    except:
      print("Dados incorretos de Zelador, favor preencher corretamente a ficha de inscrição")
    else:
      print("Dados cadastrados com sucesso!")
  def getTotalQuarto(self):
    return self.__totalQuartoResponsaveis
  def setTotalQuarto(self, novoTotal):
    self.__totalQuartoResponsaveis = novoTotal