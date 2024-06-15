try:
    numero1 = 10
    numero2 = 2
    resultado = numero1 / numero2
    print(f'O resultado é: {resultado}')
except ZeroDivisionError:
        print('Divisao realizada com sucesso')
else: 
        print('Divisao realizada com sucesso')
finally:
        print('Fim de divisão')

