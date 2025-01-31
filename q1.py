def maioridade(idade):
  if (idade >= 18):
    print('É maior de idade.')
  else:
    print('Não é maior de idade.')


if __name__ == '__main__':
  idade = int(input('Informe a idade: '))
  maioridade(idade)
