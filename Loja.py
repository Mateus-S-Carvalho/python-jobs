"""requisitos = []

while True:
    controle = input("Deseja adicionar um pedido? (s/n): ")
    if controle == 's':
        pedidos = int(input("Digite os pedidos separados por vírgula: "))
        requisitos.append(pedidos)
    else:
        break
    

soma = sum(requisitos)

print("Pedidos recebidos:", requisitos)
print("Total de pedidos:", soma)"""




"""VARIAVEIS
listaProdutos = []
listaQuantidade = []
listaValor = []


while True:
    entrada = input("Deseja adicionar outro produto? (s/n): ")
    if entrada == 's':
        produto = input("Digite o nome do produto: ")
        listaProdutos.append(produto)
        quantidadeProduto = int(input('Quantidade de produtos: '))
        listaQuantidade.append(quantidadeProduto)
        valorProduto = float(input('Valor do produto: '))
        listaValor.append(valorProduto)
    else:
        break

quantidadeVendida = sum(listaValor)


print("Produtos vendidos:", listaProdutos)
print("Quantidade de produtos vendidos:", listaQuantidade)
print("Valor total dos produtos vendidos: R$", quantidadeVendida)"""


"""VARIAVEL"""

produtoss = [
    {'nomeProduto': 'banana',
    'quantidadeProduto':1,
    'valorProduto':10},
    {'nomeProduto': 'maça',
    'quantidadeProduto':3,
    'valorProduto':2},  
]
valores = []
nomes = []
Produtos = [] 




"""FUNÇÃO"""

def adicionarProduto (nomeProduto,quantidadeProduto,valorProduto):
    informacaoProduto = {
        'nomeProduto': nomeProduto,
        'quantidadeProduto':quantidadeProduto,
        'valorProduto':valorProduto
    }
    return informacaoProduto

"""ADICIONAR INTENS"""

while True:
    entrada = input('Deseja adicionar um produto? (s/n)').lower()
    if entrada == 's':
        nomeProduto = input('Nome do produto: ')

        while True:
            try:
                quantidadeProduto = int(input('Quantida de produto: '))
                break
            except:
                print('Parece que não digitou um numero, por favor tente novamente: ')
        
        while True:
            try:
                valorProduto = float(input('Valor do produto: '))
                break
            except:
                print('Parece que você não digitou um valor, tente novamente: ')
        
        produtoCriado = adicionarProduto(nomeProduto, quantidadeProduto, valorProduto)
        produtos.append(produtoCriado)
    elif entrada == 'n':
        break
    else:
        print('Parece que não digitou as letras corretas, por favor digite "s" para adicionar ou "n" para parar.')




for itens in produtos:
    valor = itens['valorProduto'] * itens['quantidadeProduto']
    valores.append(valor)

"""SOMA DO TOTAL DE VENDAS"""
vendaTotal = sum(valores)

print(valores)
print(vendaTotal)

"""print(produtos)"""