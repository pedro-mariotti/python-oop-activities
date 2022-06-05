from ..Funcionario import Funcionario

class Suporte(Funcionario):
  def __init__(self, data):
    try:
      self.__area = data["area"]
      self.__secoesAtendidas = data["secoesAtendidas"]
      super().__init__(data["nome"], data["idade"], data["sexo"], data["id"])
    except:
      print("Dados incorretos de Suporte, favor preencher corretamente a ficha de inscrição")
    else:
      print("Dados cadastrados com sucesso!")

  def getArea(self):
    return self.__area
  def getSecoesAtendidas(self):
    return self.__secoesAtendidas
  def alterarArea(self, novaArea):
    self.__area = novaArea
  def alterarSecoes(self, novaSecao):
    self.__secoesAtendidas.append(novaSecao)