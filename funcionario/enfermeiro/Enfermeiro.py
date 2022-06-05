from ..Funcionario import Funcionario

class Enfermeiro(Funcionario):
  def __init__(self, data: dict):
    self.__turno = data["turno"]
    self.__enfermaria = data["enfermaria"]
    self.__coren = data["coren"]
    super().__init__(data["nome"], data["idade"], data["sexo"], data["id"])

  def getTurno(self) -> str:
    return self.__turno
  def getEnfermaria(self) -> str:
    return self.__enfermaria
  def getCoren(self) -> int:
    return self.__coren

  def __setTurno(self, turno):
    self.__turno = turno
  def setEnfermaria(self, enfermaria):
    self.__enfermaria = enfermaria
  def __setCoren(self, coren):
    self.__coren = coren