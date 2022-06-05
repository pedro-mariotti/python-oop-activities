from ..Medico import Medico
import datetime

class Interno(Medico):
  def __init__(self, data: dict):
    try:
      if data["tempoDeInternato"] >= datetime.datetime.now():
        self.__tempoDeInternato = data["tempoDeInternato"] - datetime.datetime.now()
      else:
        raise Exception("Favor fornecer uma data válida")
      self.__supervisor = data["supervisor"]
      self.__rotacao = data["rotacao"]
      super().__init__(data)
    except :
      print("Dados incorretos de Interno, favor preencher corretamente a ficha de inscrição")
    else:
      print("Dados cadastrados com sucesso!")

  def getTempoDeInternato(self) -> datetime:
    return self.__tempoDeInternato
  def getSupervisor(self):
    return self.__supervisor
  def getRotacao(self):
    return self.__rotacao

  def setTempoDeInternato(self, tempoInternato):
    if tempoInternato >= datetime.datetime.now():
      self.__tempoDeInternato = tempoInternato - datetime.datetime.now()
    else:
      raise Exception("Favor fornecer uma data válida")