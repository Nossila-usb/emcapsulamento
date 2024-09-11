from classe import *

if __name__ == '__main__':
    nome = input('Informe o nome: ')
    idade = int(input('Informe a idade: '))
    email = input('Informe o e-mail: ')

    # instacia da classe
    usuario = Pessoa(nome, idade, email)

    # saida de dados 
    print(f'Nome: {usuario.nome}.') 
    print(f'Idade: {usuario.idade}.')
    print(f'email: {usuario.email}.')
       
    
    