import abc, interface_veiculo

class Veiculo(interface_veiculo.InterfaceVeiculo, abc.ABC):
    def __init__(self, cor, tipo_combustivel, potencia):
        self.__cor = cor
        self.__tipo_combustivel = tipo_combustivel
        self.__potencia = potencia
        self._qtd_combustivel = 0
        self.__is_ligado = False
        self.__velocidade = 0
        self._libras = 0

    def __del__(self):
        print('O Objeto foi removido da memória.')

    @abc.abstractmethod
    def pintar(self, cor):
        return self.__cor = cor

    @property
    def cor(self):
        return self.__cor

    def abastecer(self, litros):
        self._qtd_combustivel += litros

    def ligar(self):
        print('O Veículo já está ligado' if self.is_ligado else self.is_ligado = True)

    def desligar(self):
         print('O Veículo já está desligado' if not self.is_ligado else self.is_ligado == False)

    def acelerar(self, velocidade = 10):
        if self.__is_ligado:
            self.__velocidade += velocidade
        else:
            print('O Veículo precisa estar ligado para acelerar.')
