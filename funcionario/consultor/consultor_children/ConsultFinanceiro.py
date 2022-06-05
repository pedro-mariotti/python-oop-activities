from ..Consultor import Consultor

class ConsultFinanceiro(Consultor):
  def __init__(self, data):
    try:
      self.__setorResponsavel = data["setor"]
      super().__init__(data)
    except:
      print("Dados incorretos de Consultor Financeiro, favor preencher corretamente a ficha de inscrição")
    else:
      print("Dados cadastrados com sucesso!")
  def getSetor(self):
    return self.__setorResponsavel
  def mudaSetor(self, novoSetor):
    self.__setorResponsavel = novoSetor