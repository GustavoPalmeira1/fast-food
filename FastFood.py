print('hamburguer:10$')
print('Batata frita:5$')
print('sorvete:2$')
print('Refrigerante:4$')
opcao = int(input('Qual sera a escolha?'))
qtd = int(input('Qual sera a quantidade?'))

if opcao ==1:
    print('O preço sera',10*qtd)

elif opcao == 2:
    print('O preço sera',5*qtd)
elif opcao == 3:
    print('O preço sera',2*qtd)
else:
    print('O preço sera',4*qtd)

input()