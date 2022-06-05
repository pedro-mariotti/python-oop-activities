from ..Titular import Titular
from typing import List
import datetime

class Cirurgiao(Titular):
  def __init__(self, data: dict):
    try:
      self.__inicioDeCarreira = data["inicioDeCarreira"] #data de início do profissional na área de atuação
      self.__equipeCirurgica = data["equipeCirurgica"]
      super().__init__(data)
    except:
      print("Dados incorretos de Residente, favor preencher corretamente a ficha de inscrição")
    else:
      print("Dados cadastrados com sucesso!")

  def getInicioDeCarreira(self) -> datetime:
    return self.__inicioDeCarreira
  def getEquipeCirurgica(self) -> List[Titular]:
    try:
      return self.__equipeCirurgica
    except:
      raise Exception("Dados não são listas de Médicos titulares, favor preencher corretamente")
      return []

  def addMembroEquipe(self, membro: Titular):
    try:
      self.__equipeCirurgica.append(membro)
    except:
      print("Favor inserir dados corretamente")
    #else:
      #print("Membro cadastrado com sucesso")

  def removeMembroEquipe(self, membro: Titular):
    try:
      self.__equipeCirurgica.remove(membro)
    except:
      print("Médico não encontrado, favor colocar cadastro válido")
    else:
      print("Membro removido com sucesso")
  
  def reCadastroTitular(self, data: dict):
    try:
      # utiliza o método da superclasse para cadastrar dados gerais, para depois cadastrar dados especificos
      self.__inicioDeCarreira = data["inicioDeCarreira"]
      self.__equipeMedica = data["equipeMedica"]
      super().cadastroTitular(data)
    except:
      print("Dados de cadastro de Cirurgião incompletos, favor preenchê-los integralmente")
    else:
      print("Dados recadastrados com sucesso!")