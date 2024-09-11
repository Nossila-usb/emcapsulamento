# classe
class Pessoa:
    def __init__(self, nome, idade, email):
        self.__nome = nome 
        self.__idade = idade 
        self.__email = email

    # metodos get nome
    @property
    def nome(self):
        return self.__nome
    
    # Metodo set nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    # metodos get idade
    @property
    def idade(self):
        return self.__idade
    
    # Metodo set idade
    @idade.setter
    def idade(self, idade):
        self.__idade = idade
    
    # metodos get e-mail
    @property
    def email(self):
        return self.__email
    
    # Metodo set e-mail
    @email.setter
    def email(self, email):
        self.__email = email
    
    
    

    
    

    
      