from ..Titular import Titular

class Residente(Titular):
  def __init__(self, data: dict):
    try:
      super().__init__(data)
    except:
      print("Dados incorretos de Residente, favor preencher corretamente a ficha de inscrição")
    else:
      print("Dados cadastrados com sucesso!")

  def reCadastroTitular(self, data: dict):
    try:
      # utiliza o método da superclasse para cadastrar dados gerais, para depois cadastrar dados especificos
      super().cadastroTitular(data)
    except:
      print("Dados de cadastro de Residente incompletos, favor preenchê-los integralmente")
    else:
      print("Dados cadastrados com sucesso!")