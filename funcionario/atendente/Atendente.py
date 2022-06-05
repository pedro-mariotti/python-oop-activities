from ..Funcionario import Funcionario

class Atendente(Funcionario):
  def __init__(self, data: dict):
    try:
      self.__setor = data["setor"]
      self.__cargaHoraria = data["cargaHoraria"]
      super().__init__(data["nome"], data["idade"], data["sexo"], data["id"])
    except:
      print("Dados incorretos de Atendente, favor preencher corretamente a ficha de inscrição")
    else:
      print("Dados cadastrados com sucesso!")
  
  def getSetor(self) -> str:
    return self.__setor
  def getCargaHoraria(self) -> str:
    return self.__cargaHoraria
  
  
  def setSetor(self, setor):
    self.__setor = setor
  def setCargaHoraria(self, cargaHoraria: float):
    self.__cargaHoraria = cargaHoraria