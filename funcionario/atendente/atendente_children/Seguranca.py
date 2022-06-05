from ..Atendente import Atendente

class Seguranca(Atendente):
  def __init__(self, data: dict):
    try:
      self.__turno = data["turno"]
      super().__init__(data)
    except:
      print("Dados incorretos de Segurança, favor preencher corretamente a ficha de inscrição")
    else:
      print("Dados cadastrados com sucesso!")

  def setTurno(self, turno: str):
    self.__turno = turno

  def getTurno(self) -> str:
    return self.__turno