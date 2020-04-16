import veiculo

class Carro(veiculo.Veiculo):
    def __init__(self, cor, tipo_combustivel, potencia, qtd_portas)
        super.__init__(cor, tipo_combustivel, potencia)
        self.qtd_portas = qtd_portas

    def abastecer(self, litros):
        print('Método abastecer chamado a partir da class Carro.')
        self._qtd_combustivel += litros

    def pintar(self, cor):
        return self.__cor = cor
