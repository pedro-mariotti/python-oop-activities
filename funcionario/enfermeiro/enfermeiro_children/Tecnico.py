from ..Enfermeiro import Enfermeiro

class Tecnico(Enfermeiro):
  def __init__(self, data):
    self.__especialidadeEnf = data["especialidadeEnf"]
    super().__init__(data)

  def __getEspecialidadeEnf(self) -> str:
    return self.__especialidadeEnf