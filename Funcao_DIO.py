### função -> é um bloco de código que realiza uma ação específica
### Na função podemos passar parâmetros, que são valores que a função pode receber para realizar sua ação. Além disso, uma função pode retornar um valor, que é o resultado da ação realizada.
### Exemplo da DIO

def injetarPao ():
    print("Preparando para injetar o pão...")
    print("Finalizado")
def torrar ():
    print("Torrando o pão...")
    injetarPao()


torrar()

print("---------------------------------------------------")
# Não se deve começar o nome de uma função com números, nem com caracteres especiais, nem com espaços. O nome da função deve ser descritivo, para que seja fácil entender o que ela faz. Além disso, é uma boa prática utilizar letras minúsculas e separar as palavras com underscores (_)

# Dica, nomear as funções com verbos, pois elas realizam ações. Exemplo: calcular_media(), enviar_email(), etc.
# Fazer uma função para cada ação específica, para que o código fique mais organizado e fácil de entender. Evitar funções muito longas, pois elas podem se tornar difíceis de entender e manter.

# Existe também uma função chamada pai, que é uma função que chama outras funções dentro dela. Isso é útil para organizar o código e evitar repetição de código.

def getData():
    print("Pegando dados do usuário...")

def checkValues():
    print("Validando dados")

def sendToDatabase():
    print("Cadastrando dados")

def main():
    getData()
    checkValues()
    sendToDatabase()

main()

print("---------------------------------------------------")


# Começando funções com parâmetros, que são valores que a função pode receber para realizar sua ação. Além disso, uma função pode retornar um valor, que é o resultado da ação realizada.

#Função com parâmetros
#no exemplo da torradeira, vamos falar do pão kkk
#O pão é um parâmetro, pois ele se comporta como uma variável.

def torrar ():
    print("Torrada feita")

torrar()

#Nesse caso, é uma função direta, sem parâmetros.

#Para adicionar um parâmetro na função fazemos a seguinte forma.

def torrar (pao): # Nesse caso o parâmetro que se pede é o tipo do pão ele se torna uma variável.
    print("torrada feita com ", pao)
#então quando eu for chamar essa função, eu preciso colocar a variável que eu quero dentro dos parenteses da função.
#Ex.:
torrar ("pão de forma")

#ele vai considerar o que eu colocar dentro do parenteses como o resultado daquela função. Tanto que eu posso mudar o meu print para:


#o resultado desse print vai ser "Torrada feita com pão de forma

torrar ("Pão de Forma")
torrar ("Pão Integral")
torrar ("Pão Australiano")

#cada função dessa terá respectivamente os seguintes resultados.

#Torrada feita com Pão de Forma
#Torrada feita com Pão Integral
#Torrada feita com Pão Australiano

#IMPORTANTE!!! As variáveis criadas dentro da função, só existem na função, porém se eu usar uma variável



Q#uando há multiplos parâmetros. Temos que também declarar na mesma ordem.
#Ex.:
def torrar (pao, nome):
    print("Torrada feita com ", pao, "para o usuário ", nome)
#quando eu for chamar essa função eu preciso chamar

torrar ("Pão de forma", "Victor")




#exemplo de exemplo real.

def createStringConnection (databaseName):
    print("connect:DBCONNECT;user=Victor;pass=1234;initial_database= ", databaseName)


createStringConnection ("db_products")