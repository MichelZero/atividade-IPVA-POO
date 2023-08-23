#
#
# autor: Michel
# data: 23/08/2023

# - Escreva uma classe para armazenar as seguintes informações sobre veículos:
#        cor, tipo, ano de fabricação, modelo, placa, valor do veículo e valor do IPVA.

class Veiculo:
    def __init__(self, cor, tipo, ano_fabricacao, modelo, placa, valor):
        self._cor = cor
        self._tipo = tipo
        self._ano_fabricacao = ano_fabricacao
        self._modelo = modelo
        self._placa = placa
        self._valor = valor
        

    #getters
    @property
    def cor(self):
        return self._cor

    @property
    def tipo(self):
        return self._tipo

    @property
    def ano_fabricacao(self):
        return self._ano_fabricacao
    
    @property
    def modelo(self):
        return self._modelo
    
    @property
    def placa(self):
        return self._placa
    
    @property
    def valor(self):
        return self._valor


    #setters
    @cor.setter
    def cor(self, newCor):
        cores = ['azul', 'verde', 'vermelho']
        if newCor in cores:
            self._cor = newCor
        else:
            print(f"escolha entre as cores: {cores}")
    
    @placa.setter
    def placa(self, newPlaca):
        self._placa = newPlaca
    
    @valor.setter
    def valor(self, newValor):
        self._valor = newValor