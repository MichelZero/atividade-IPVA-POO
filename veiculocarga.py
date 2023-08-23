# autor: Michel
# data: 23/08/2023

# 3.	Escreva uma classe VeiculoDeCarga que herda todas as informações 
# da classe do item 1. Acrescente atributos como número de eixos e capacidade 
# de carga. Escreva também métodos getters e setters.

from veiculo import Veiculo

class VeiculoDeCarga(Veiculo):
    def __init__(self, cor, tipo, ano_fabricacao, modelo, placa, valor, numeroEixos, capacidadeCarga):
        super().__init__(cor, tipo, ano_fabricacao, modelo, placa, valor)
        self._numeroEixos = numeroEixos
        self._capacidadeCarga = capacidadeCarga

    def calculaIPVA(self):
        if 2023 - self.ano_fabricacao < 15:
            self.IPVA = self._valor * 0.01
            return self.IPVA
        
        return 'Isento de IPVA'

    #getters
    @property
    def numeroEixos(self):
        return self._numeroEixos
    
    @property
    def capacidadeCarga(self):
        return self._capacidadeCarga

    #setters
    @numeroEixos.setter
    def numeroEixos(self, newNumeroEixos):
        self._numeroEixos = newNumeroEixos

    @capacidadeCarga.setter
    def capacidadeCarga(self, newCapacidadeCarga):
        self._capacidadeCarga = newCapacidadeCarga