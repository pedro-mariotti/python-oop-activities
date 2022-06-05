from ..Funcionario import Funcionario

class Medico(Funcionario):
  def __init__(self, data: dict):
    try:
      self.__emAtendimento = data["emAtendimento"]
      self.__especialidade = data["especialidade"]
      super().__init__(data["nome"], data["idade"], data["sexo"], data["id"])
    except:
      print("Dados incorretos de Médico, favor preencher corretamente a ficha de inscrição")
    else:
      print("Dados cadastrados com sucesso!")

    
  def getEmAtendimento(self) -> bool:
    return self.__emAtendimento
  def getEspecialidade(self) -> str:
    return self.__especialidade

  def setEmAtendimento(self, atendendo: bool):
    self.__emAtendimento = atendendo
  def setEspecialidade(self, especialidade):
    self.__especialidade = especialidade