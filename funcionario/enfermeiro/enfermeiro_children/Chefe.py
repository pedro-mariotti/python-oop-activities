from ..Enfermeiro import Enfermeiro

class Chefe(Enfermeiro):
  def __init__(self, data:dict):
    self.__equipe = data["equipe"]
    super().__init__(data)

  def getEquipe(self) -> list:
    return self.__equipe