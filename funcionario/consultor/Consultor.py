from ..Funcionario import Funcionario

class Consultor(Funcionario):
  def __init__(self, data):
    try:
      self.__especialidade = data["especialidade"]
      super().__init__(data["nome"], data["idade"], data["sexo"], data["id"])
    except:
      print("Dados incorretos de Consultor, favor preencher corretamente a ficha de inscrição")
    else:
      print("Dados cadastrados com sucesso!")

  def getEspecialidade(self):
    return self.__especialidade
  def alterarEspecialidade(self, novaEspecialidade):
    self.__especialidade = novaEspecialidade