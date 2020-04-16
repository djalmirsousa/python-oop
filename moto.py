import veiculo

class Moto(veiculo.Veiculo):
    def __init__(self, cor, tipo_combustivel, potencia, qtd_passageiros)
        super.__init__(cor, tipo_combustivel, potencia)
        self.qtd_passageiros = qtd_passageiros
        self._libras = 30

    def pintar(self, cor):
        return self.__cor = cor
