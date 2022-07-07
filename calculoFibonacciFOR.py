#Rafael Richard Alves de Godoy - Vida Nova Tec
#Exercicio 02 calculo Fibonacci com FOR - Python

print("\nBem vindo ao programa de calculo de fibonacci!")
quantidade = 1

while(quantidade != 0): #Repeticao ate o usuario digitar 0 

    #pede pro usuario digitar um numero para calcular fibonacci

    quantidade = int(input("\nDigite a quantidade que deseje calcular ou 0 (zero) para finalizar:  ")) 
    #atribuindo valores inicias para variaveis
    num1 = 0
    num2 = 1
    aux = 0
    contador = 0
   
    print("Sequencia fibonacci")
    print(aux, end = " ")
    
    #for para calcular o fibonacci

    for i in range (quantidade - 1):  
       
        num1 = num2
        num2 = aux
        aux = num1 + num2
           
        print(aux, end = " ")