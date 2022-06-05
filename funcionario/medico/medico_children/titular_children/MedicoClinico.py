from ..Titular import Titular

class MedicoClinico(Titular):
  def __init__(self, data: dict):
    try:
      super().__init__(data)
      self.__endereco = data["enderecoClinica"]
    except:
      print("Dados incorretos de Médigo Geral, favor preencher corretamente a ficha de inscrição")
    else:
      print("Dados cadastrados com sucesso!")
  def getEndereco(self):
    return self.__endereco
  def reCadastroTitular(self, data: dict):
    try:
      # utiliza o método da superclasse para cadastrar dados gerais, para depois cadastrar dados especificos
      super().cadastroTitular(data)
      self.__endereco = data["newEndereco"]
    except:
      print("Dados de cadastro de Médico Geral incompletos, favor preenchê-los integralmente")
    else:
      print("Dados cadastrados com sucesso!")