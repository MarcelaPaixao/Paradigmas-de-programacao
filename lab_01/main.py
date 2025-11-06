import random


def f1():
    num = int(input())

    for i in range(1,num+1):
        if(i%2 == 0):
            print(f"{i}")

def f2():
    str = input()
    count = 0

    for c in str:
        if(c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'):
            count += 1

    print(f"Qtd de vogais: {count}")

def f3():
    numbers = []
    for i in range(5):
        numbers.append(int(input()))
    
    for i in range(1, len(numbers)):
        num = numbers[i]
        j = i - 1

        while j >= 0 and num < numbers[j]:
            numbers[j + 1] = numbers[j]
            j -= 1
            
        numbers[j + 1] = num

    print(numbers)

def f4():
    num = input()
    sum = 0

    for c in num:
        n = int(c)
        sum += n

    print(sum)


def f5():
    num = int(input())

    print(f"--- Tabuada de {num} ---") 
    for i in range(1, 11):
        result = num * i
        print(f"        {num} x {i} = {result}")

def f6():
    min = max = 0
    for i in range(10):
        num = int(input())
        if(num < min): min = num
        if(num > max): max = num
        
def f7():
    n = int(input())
    print('Contagem regressiva:')
    for i in range(n, -1, -1):
        print(i)
    print('FIM!')

def f8():
    c = float(input())

    k = c + 273
    f = (c * (9/5)) + 32

    print(f'Celcius: {c}°C')
    print(f'Kelvin: {k}K')
    print(f'Fahrenheint: {f}°F')

def f9():
    mat = []

    for i in range(3):
        row = []
        for j in range(3):
            row.append(int(input()))
        mat.append(row)
    
    print(mat)

def f10():
    a = int(input())
    b = int(input())
    
    for i in range(a, b+1):
        primo = True
        for j in range(2, i):
            if (i != j and i%j == 0):
                primo = False
                break
        if(primo):
            print(i)

def f11():
    print('FAZER')################################

def f12():
    n = int(input())
    fat = 1

    for i in range(n,1,-1):
        fat *= i
    print(f'{n}! = {fat}')

def f13():
    pal = input()
    eh_palindromo = True
    size = len(pal) - 1

    for i in range(int(size/2) + 1):
        if pal[i] != pal[size - i]:
            eh_palindromo = False

    print(f'A palvra é palindromo? {eh_palindromo}')


def f14():
    mat = []
    n = int(input())

    for i in range(n):
        row = []
        for j in range(n):
            if(i == j): row.append(1)
            else: row.append(0)
        mat.append(row)
    
    print(mat)

def f15():
    notas = [int(i) for i in input().split()]
    pesos = [int(i) for i in input().split()]
    media = 0

    for i in range(len(notas)):
        media += notas[i] * pesos[i]
    
    soma_pesos = 0
    for p in pesos: soma_pesos += p
    
    media = media/soma_pesos
    print(media)

def f16():
    n = random.randint(1, 100)
    count = 0

    print('Tente adivinhar o número: ')
    while 1:
        guess = int(input())
        count += 1

        if guess == n: 
            print('PARABÉNS, você venceu!') 
            break
        if(guess < n): print('O número é MAIOR que esse!')
        if(guess > n): print('O número é MENOR que esse!')
        print('\nTente novamente: ')

    print(f'Qtd de tentativas: {count}')
    
f13()