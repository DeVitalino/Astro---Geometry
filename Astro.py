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
        
        area_triangulo = base_triangulo = altura_triangulo = None
        valores = input('Digite a base e a altura do triângulo separadas por espaço (ou digite "?" para o valor desconhecido): ').split()
        
        if '?' in valores:
            if valores[0] == '?':
                altura_triangulo = float(valores[1])
                area_triangulo = float(input('Digite o valor da Área (A): '))
                base_triangulo = (2 * area_triangulo) / altura_triangulo
            elif valores[1] == '?':
                base_triangulo = float(valores[0])
                area_triangulo = float(input('Digite o valor da Área (A): '))
                altura_triangulo = (2 * area_triangulo) / base_triangulo
        else:
            base_triangulo, altura_triangulo = map(float, valores)
            area_triangulo = (base_triangulo * altura_triangulo) / 2
        
        time.sleep(1.5)
        print(f'O valor da Área do Triângulo é A = {area_triangulo:.2f}.')
    
    elif forma in {'círculo', 'circulo'}:
        print('Ótimo! Para calcular a área do Círculo, usamos a fórmula A = π × r². \n')
        
        raio = input('Digite o valor do Raio (r) ou "?" se não souber: ').strip()
        
        if raio == '?':
            area_circulo = float(input('Digite o valor da Área (A): '))
            raio = (area_circulo / math.pi) ** 0.5
        else:
            raio = float(raio)
            area_circulo = math.pi * (raio ** 2)
        
        time.sleep(1.5)
        print(f'O valor da Área do Círculo é A = {area_circulo:.2f}.')
    
    elif forma in {'quadrado'}:
        print('Vamos lá! Para calcular a área do Quadrado, usamos a fórmula A = L². \n')
        
        lado = input('Digite o valor do Lado (L) ou "?" se não souber: ').strip()
        
        if lado == '?':
            area_quadrado = float(input('Digite o valor da Área (A): '))
            lado = area_quadrado ** 0.5
        else:
            lado = float(lado)
            area_quadrado = lado * lado
        
        time.sleep(1.5)
        print(f'O valor da Área do Quadrado é A = {area_quadrado:.2f}.')
    
    elif forma in {'retângulo', 'retangulo'}:
        print('Ótimo! Para calcular a área do Retângulo, usamos a fórmula A = base × altura. \n')
        
        area_retangulo = base_retangulo = altura_retangulo = None
        valores = input('Digite a base e a altura do retângulo separadas por espaço (ou digite "?" para o valor desconhecido): ').split()
        
        if '?' in valores:
            if valores[0] == '?':
                altura_retangulo = float(valores[1])
                area_retangulo = float(input('Digite o valor da Área (A): '))
                base_retangulo = area_retangulo / altura_retangulo
            elif valores[1] == '?':
                base_retangulo = float(valores[0])
                area_retangulo = float(input('Digite o valor da Área (A): '))
                altura_retangulo = area_retangulo / base_retangulo
        else:
            base_retangulo, altura_retangulo = map(float, valores)
            area_retangulo = base_retangulo * altura_retangulo
        
        time.sleep(1.5)
        print(f'O valor da Área do Retângulo é A = {area_retangulo:.2f}.')
    
    else:
        print('Ops! Ainda não suportamos essa forma geométrica. Tente novamente.')
    
    continuar = input('Deseja calcular outra forma geométrica? (sim/não) ').strip().lower()
    if continuar != 'sim':
        print('Obrigado por usar o Astro! Até mais!')
        break
