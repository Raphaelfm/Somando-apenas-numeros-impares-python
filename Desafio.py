#Desafio 10: Faça um programa em Python que você solicite ao usuário um número positivo entre 1 e 100.
#Caso o usuário digite um número fora dessa faixa de valores solicitar novamente o um novo número até
#que o número esteja nesta faixa (1-100). Após a validação do número calcule a soma apenas dos números 
#ímpares maiores que o número escolhido pelo usuário até o número 100.

import time
soma = 0
n = int(input('Digite um número positivo entre 1 e 100: '))
while ((n > 100) or (n < 1)):
    print('Você deve digitar um número entre 1 e 100. ')
    n = int(input('Digite um número entre 1 e 100: '))

print('O número digitado pelo usuário foi: ' + str(n))
    
while n < 100:
    n = (n + 1)
    if (n%2 == 1):
        print(n)
        time.sleep(0.1) 
        soma = (n + soma)
                
print('A soma dos numeros impares posteriores é: ' + str(soma))
