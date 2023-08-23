# autor: Michel
# data: 23/08/2023

# 2.	- Escreva uma classe Automovel que herda todas as informações da classe anterior.
#     - Acrescente os atributos capacidade de passageiros e o número de portas, além dos métodos getters e setters. 

from veiculo import Veiculo

class Automovel(Veiculo):
    def __init__(self, cor, tipo, ano_fabricacao, modelo, placa, valor, capacidadePassageiros, numeroPortas):
        super().__init__(cor, tipo, ano_fabricacao, modelo, placa, valor)
        self._capacidadePassageiros = capacidadePassageiros
        self._numeroPortas = numeroPortas

    def calculaIPVA(self):
        if 2023 - self.ano_fabricacao < 15:
            self.IPVA = self._valor * 0.02
            return self.IPVA

        return 'Isento de IPVA'


    # getters
    @property
    def capacidadePassageiros(self):
        return self._capacidadePassageiros

    @property
    def numeroPortas(self):
        return self._numeroPortas

    #setters
    @capacidadePassageiros.setter
    def capacidadePassageiros(self, newCapacidadePassageiros):
        self._capacidadePassageiros = newCapacidadePassageiros

    @numeroPortas.setter
    def numeroPortas(self, newNumeroPortas):
        self._numeroPortas = newNumeroPortas