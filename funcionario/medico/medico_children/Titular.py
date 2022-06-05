from ..Medico import Medico

class Titular(Medico):
  def __init__(self, data: dict):
    try:
      if (type(data["crm"]) and type(data["areaAtuacao"])) is str:
        self.__crm = data["crm"]
        self.__areaAtuacao = data["areaAtuacao"]
        super().__init__(data)
      else:
        raise Exception("dados enviados estão com tipos incorretos")
    except:
      print("Dados incorretos de Médico Titular, favor preencher corretamente a ficha de inscrição")
    else:
      print("Dados cadastrados com sucesso!")

  def getCrm(self) -> str:
    return self.__crm
  def getAreaAtuacao(self) -> str:
    return self.__areaAtuacao

  def reCadastroTitular(self, data: dict):
    self.__crm = data["crm"]
    self.__areaAtuacao = data["areaAtuacao"]

  def setEspecialidade(self, especialidade):
    self.__especialidade = especialidade
  def setAreaAtuacao(self, areaAtuacao):
    self.__areaAtuacao