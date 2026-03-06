'''Este programa simples verifica se um cupom de desconto é válido e, caso seja, 
aplica um desconto de 10% ao preço do produto. 
O programa solicita ao usuário que insira um cupom de desconto e, em seguida, 
verifica se o cupom corresponde a "DESCONTO10". Se for válido, o programa informa que o cupom foi aplicado;
 caso contrário, exibe o preço original do produto.'''

# Recebe o cupom de desconto
cupom = str(input('Digite o cupom de desconto: '))

# preço do produto
preco = 100

#Verifica se o cupom é válido e aplica o desconto
if cupom == 'DESCONTO10':
    print('Cupom de 10% aplicado!')

else:
    print(preco)