import os
import time

clientes = []

def limpar_terminal():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')

def cadastra_cliente(cliente):
  clientes.append(cliente)

def listar_clientes():
  limpar_terminal()
  index = 0
  for cliente in clientes:
    print(f'=== Cliente {index} ===')
    print(f'Nome: {cliente["nome"]}')
    print(f'Saldo: {cliente["saldo"]}\n')
    index += 1

def depositar(value, conta):
  limpar_terminal()
  clientes[conta]['saldo'] += value
  print(f'{value} depositado na conta de {clientes[conta]['nome']}')
  time.sleep(2)
  limpar_terminal()

def sacar(value, conta):
  limpar_terminal()
  saldo = clientes[conta]['saldo']
  if value > saldo:
    print('Saldo insuficiente.')
  else:
    clientes[conta]['saldo'] -= value
    print(f'Saque de {value} realizado da conta de {clientes[conta]['nome']}')
  time.sleep(2)
  limpar_terminal()

if __name__ == '__main__':
  limpar_terminal()
  option = 0

  while (option != 5):
    if (option == 0):
      print('===== Sistema bancário =====')
      print('1 - Cadastrar novo cliente')
      print('2 - Listar todos os clientes cadastrados')
      print('3 - Depositar dinheiro em um cliente')
      print('4 - Sacar dinheiro de um cliente')
      print('5 - Sair do programa')
      option = int(input('Selecione uma opção: '))

    if (option == 1):
      limpar_terminal()
      nome = input('Insira o nome do cliente: ')
      saldo_inicial = float(input(f'Insira o saldo inicial da conta de {nome}: '))
      cadastra_cliente({'nome': nome, 'saldo': saldo_inicial})
      limpar_terminal()
      print(f'{nome} Cadastrado com sucesso!')
      time.sleep(2)
      limpar_terminal()
      option = 0
    
    if (option == 2):
      limpar_terminal()
      listar_clientes()
      input('Pressione "Enter" para continuar...')
      limpar_terminal()
      option = 0
    
    if (option == 3):
      limpar_terminal()
      conta = int(input('Informe a conta de depósito: '))
      value = float(input('Informe o valor a ser depositado: '))
      depositar(value, conta)
      option = 0

    if (option == 4):
      limpar_terminal()
      conta = int(input('Informe a conta de saque: '))
      value = float(input('Informe o valor a ser sacado: '))
      sacar(value, conta)
      option = 0

    if (option == 5):
      print('Saindo...')
      time.sleep(1)
      limpar_terminal()
      break

    if (option > 5):
      limpar_terminal()
      print('Opção inválida.')
      time.sleep(2)
      limpar_terminal()
      option = 0
      