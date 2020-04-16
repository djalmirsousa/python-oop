import carro

polo = carro.Carro('vermelho','flex', 3.0, 4)
polo.ligar()
polo.abastecer(50)
print(polo.cor)
print(f'A quantidade de combustível no veículo: {polo.qtd_combustivel} ')


