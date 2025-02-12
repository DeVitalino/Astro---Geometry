import time
import math 

print('Olá, Usuário! Eu sou o Astro e vou te ajudar com o cálculo. \n')

nome = input('Primeiro, gostaria de saber o seu nome: ').strip()

while True:
    confi_nome = input(f'Certo! Seu nome está correto: {nome}? (sim/não) ').strip().lower()

    if confi_nome == 'sim':
        print('Ótimo! Vamos seguir:')
        break  

    elif confi_nome in {'não', 'nao', 'n'}:
        print('Vish! Vamos corrigir...')
        nome = input('Informe o nome correto, por favor: ').strip()

    else:
        print('Ocorreu um erro! Digite apenas sim/não.')

while True:
    forma = input('Qual a forma geométrica que você quer calcular a área? ').strip().lower()

    if forma in {'triângulo', 'triangulo'}:
        print('Joia! Para calcularmos a área do Triângulo, utilizamos a fórmula A = (b × h) / 2. \n')

        valores = input('Digite a base e a altura do triângulo separadas por espaço: ')
        base_triangulo, altura_triangulo = map(float, valores.split())

        print('Estamos calculando...')
        time.sleep(1.5)

        area_triangulo = (base_triangulo * altura_triangulo) / 2
        print(f'O valor da Área do Triângulo é A = {area_triangulo:.2f}.')

    elif forma in {'círculo', 'circulo'}:
        print('Ótimo! Para calcular a área do Círculo, usamos a fórmula A = π × r². \n')

        raio = float(input('Digite o valor do Raio (r): '))

        print('Estamos calculando...')
        time.sleep(1.5)

        area_circulo = math.pi * (raio ** 2)  

        print(f'O valor da Área do Círculo é A = {area_circulo:.2f}.')

    elif forma == 'quadrado':
        print('Vamos lá! Para calcular a área do Quadrado, usamos a fórmula A = L². \n')

        lado = float(input('Digite o valor do Lado (L): '))

        print('Estamos calculando...')
        time.sleep(1.5)

        area_quadrado = lado ** 2  
        print(f'O valor da Área do Quadrado é A = {area_quadrado:.2f}.')

    else:
        print('Ops! Ainda não suportamos essa forma geométrica. Tente novamente.')

    continuar = input('Deseja calcular a área de outra forma geométrica? (sim/não) ').strip().lower()
    
    if continuar not in {'sim', 's'}:
        print('Obrigado por usar o Astro! Até mais!')
        break
